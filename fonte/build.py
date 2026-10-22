# Monta o app: ../app/index.html (página) + ../app/audio/dNNN.js (vozes de cada dia)
# e ../cem-por-dia.zip (pasta pronta para abrir no Chrome).
# Uso: python3 build.py <pasta com mp3/>
import json, os, sys, base64, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import build, plan
TTS = sys.argv[1] if len(sys.argv) > 1 else None
APP = os.path.join(HERE, '..', 'app'); os.makedirs(os.path.join(APP, 'audio'), exist_ok=True)
days = build()
src = open(os.path.join(HERE, 'site.html')).read()
body = src.replace('/*__DATA__*/null', json.dumps(days, ensure_ascii=False)).replace('/*__PLAN__*/null', json.dumps(plan(), ensure_ascii=False))
missing = 0
for d in days:
    audio = {}
    for w in d['waves']:
        for p in w['phrases']:
            f = TTS and os.path.join(TTS, 'mp3', p['id'] + '.mp3')
            if f and os.path.exists(f):
                audio[p['id']] = 'data:audio/mpeg;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
            else:
                missing += 1
    open(os.path.join(APP, 'audio', 'd%03d.js' % d['n']), 'w').write('CEM_AUDIO(' + json.dumps(audio) + ');\n')
open(os.path.join(APP, 'page.html'), 'w').write(body)  # para publicar como Artifact
skel = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'
open(os.path.join(APP, 'index.html'), 'w').write(skel + body + '</body></html>')
z = os.path.join(HERE, '..', 'cem-por-dia.zip')
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write(os.path.join(APP, 'index.html'), 'cem-por-dia/index.html')
    for d in days:
        n = 'd%03d.js' % d['n']; zf.write(os.path.join(APP, 'audio', n), 'cem-por-dia/audio/' + n)
    zf.writestr('cem-por-dia/LEIA-ME.txt', 'Abra o index.html no Google Chrome (ou Edge) e permita o microfone.\nDeixe a pasta audio ao lado do index.html: as vozes de cada dia ficam nela.\n')
print('ok dias', len(days), 'sem voz', missing, 'zip', os.path.getsize(z))
