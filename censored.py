from pydub import AudioSegment

# load audio files
song = AudioSegment.from_wav("sample/original.wav")
beep = AudioSegment.from_wav("sample/1khz_sin_30sec.wav")

# slice audio
before = song[:4000]
after = song[4200:10000]

censor = beep[:200]

# concatenate
concat = before + censor + after

# generate file
concat.export("output/censored.wav", format="wav")
