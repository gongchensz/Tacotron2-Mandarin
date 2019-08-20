import librosa
import numpy as np
import soundfile

fullpath = '../audios/007064.wav'
sampling_rate = 22050

y, sr = librosa.core.load(fullpath, sampling_rate, mono=True)
print(y, sr)

print('np.mean(y): ' + str(np.mean(y)))
print('np.max(y): ' + str(np.max(y)))
print('np.min(y): ' + str(np.min(y)))

soundfile.write('test.wav', y, sampling_rate)