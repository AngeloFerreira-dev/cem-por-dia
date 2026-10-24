# Gera a voz em inglês de cada frase com Kokoro TTS: um mp3 por frase em <tts>/mp3 (build.py empacota por dia).
import sys, os, json, base64, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import build
from kokoro_onnx import Kokoro
import soundfile as sf
TTS = sys.argv[1]  # pasta com kokoro.onnx e voices.bin
OUT = os.path.join(TTS, 'mp3'); os.makedirs(OUT, exist_ok=True)
k = Kokoro(os.path.join(TTS, 'kokoro.onnx'), os.path.join(TTS, 'voices.bin'))
jobs = [(p['id'], p['en']) for d in build() for w in d['waves'] for p in w['phrases']]
# opcional: shard i/n para rodar vários processos em paralelo
if len(sys.argv) > 2:
    i, n = map(int, sys.argv[2].split('/')); jobs = jobs[i::n]
for i, (pid, text) in enumerate(jobs):
    mp3 = f'{OUT}/{pid}.mp3'
    txt = f'{OUT}/{pid}.txt'
    if os.path.exists(mp3) and (not os.path.exists(txt) or open(txt).read() == text): continue
    s, sr = k.create(text, voice='af_heart', speed=0.92, lang='en-us')
    sf.write(f'{OUT}/{pid}.wav', s, sr)
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'{OUT}/{pid}.wav','-af','silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,apad=pad_dur=0.1','-ac','1','-ar','24000','-b:a','32k',mp3], check=True)
    os.remove(f'{OUT}/{pid}.wav')
    open(txt, 'w').write(text)
    print(i, len(jobs), pid, flush=True)
print('DONE', len(jobs))
