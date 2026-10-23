#!/usr/bin/env python3
"""Clean a spoken recording and export a podcast MP3.

    python3 tools/clean_audio.py INPUT OUTPUT.mp3 "Title" [album]

Steps: remove rumble below 80 Hz; learn the background noise from the quietest
moments (the pauses between words) and subtract it across the recording; a light
second pass for hiss; then even the loudness to the podcast standard (-16 LUFS).
The spoken words themselves are not edited, cut or re-ordered.
"""
import sys, subprocess, tempfile, os
import numpy as np, soundfile as sf, noisereduce as nr

src, out, title = sys.argv[1], sys.argv[2], sys.argv[3]
album = sys.argv[4] if len(sys.argv) > 4 else '2 Minutes Podcast'
SR = 48000

raw = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-i', src, '-ac', '1', '-ar', str(SR), '-af', 'highpass=f=80',
                      '-f', 'f32le', '-'], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32).copy()

# Noise profile: the quietest 15% of 50 ms frames (pauses, room tone, background)
w = SR // 20
n = len(x) // w
frames = x[:n * w].reshape(n, w)
rms = np.sqrt((frames ** 2).mean(1))
quiet = frames[rms <= np.percentile(rms, 15)].ravel()

y = nr.reduce_noise(y=x, sr=SR, y_noise=quiet, stationary=True, prop_decrease=0.9, n_fft=2048)
y = nr.reduce_noise(y=y, sr=SR, stationary=False, prop_decrease=0.5, n_fft=2048, time_mask_smooth_ms=60)

with tempfile.TemporaryDirectory() as d:
    tmp = os.path.join(d, 'clean.wav')
    sf.write(tmp, y.astype(np.float32), SR)
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', tmp,
                    '-af', 'lowpass=f=12000,loudnorm=I=-16:TP=-1.5:LRA=11', '-ar', '48000', '-ac', '1',
                    '-c:a', 'libmp3lame', '-q:a', '3', '-metadata', 'artist=Believers Country',
                    '-metadata', f'album={album}', '-metadata', f'title={title}', out], check=True)
print('cleaned →', out)
