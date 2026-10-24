#!/usr/bin/env python3
"""Clean a spoken recording and export a podcast MP3.

    python3 tools/clean_audio.py INPUT OUTPUT.mp3 "Title" [album] [--service]

Steps: remove rumble below 80 Hz; learn the background noise from the quietest
moments (the pauses between words) and subtract it across the recording; a light
second pass for hiss; then even the loudness to the podcast standard (-16 LUFS).
The spoken words themselves are not edited, cut or re-ordered.

--service: settings for full-length Shabbat services (24 kHz mono, 48 kbps), and the
recording is processed in one-minute pieces so long files stay light on memory.
"""
import sys, subprocess, tempfile, os
import numpy as np, soundfile as sf, noisereduce as nr

args = [a for a in sys.argv[1:] if not a.startswith('--')]
service = '--service' in sys.argv
src, out, title = args[0], args[1], args[2]
album = args[3] if len(args) > 3 else ('Shabbat Services 5787' if service else '2 Minutes Podcast')
SR = 24000 if service else 48000

raw = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-i', src, '-ac', '1', '-ar', str(SR), '-af', 'highpass=f=80',
                      '-f', 'f32le', '-'], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32).copy()
del raw

# Noise profile: the quietest 15% of 50 ms frames (pauses, room tone, background)
w = SR // 20
n = len(x) // w
rms = np.sqrt((x[:n * w].reshape(n, w) ** 2).mean(1))
idx = np.where(rms <= np.percentile(rms, 15))[0]
idx = idx[np.linspace(0, len(idx) - 1, min(len(idx), 1200)).astype(int)]  # cap profile at ~60 s
quiet = np.concatenate([x[i * w:(i + 1) * w] for i in idx])

def clean(seg):
    seg = nr.reduce_noise(y=seg, sr=SR, y_noise=quiet, stationary=True, prop_decrease=0.9, n_fft=2048)
    return nr.reduce_noise(y=seg, sr=SR, stationary=False, prop_decrease=0.5, n_fft=2048, time_mask_smooth_ms=60)

chunk, pad = 60 * SR, SR  # one-minute pieces with a one-second overlap, cross-faded
if len(x) <= chunk + pad:
    y = clean(x)
else:
    y = np.zeros_like(x)
    fade = np.linspace(0, 1, pad, dtype=np.float32)
    for start in range(0, len(x), chunk):
        a, b = max(0, start - pad), min(len(x), start + chunk + pad)
        c = clean(x[a:b])[start - a:]
        c = c[:min(len(x), start + chunk + pad) - start]
        if start > 0:                      # fade in over the overlap with the previous piece
            c[:pad] *= fade[:len(c[:pad])]
        if len(c) > chunk:                 # fade out over the overlap with the next piece
            c[chunk:] *= (1 - fade)[:len(c) - chunk]
        y[start:start + len(c)] += c

with tempfile.TemporaryDirectory() as d:
    tmp = os.path.join(d, 'clean.wav')
    sf.write(tmp, y.astype(np.float32), SR)
    enc = ['-ar', '24000', '-b:a', '48k'] if service else ['-ar', '48000', '-q:a', '3']
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', tmp,
                    '-af', f'lowpass=f={11000 if service else 12000},loudnorm=I=-16:TP=-1.5:LRA=11', '-ac', '1', *enc,
                    '-c:a', 'libmp3lame', '-metadata', 'artist=Believers Country',
                    '-metadata', f'album={album}', '-metadata', f'title={title}', out], check=True)
print('cleaned →', out)
