import sys,json
CSS='''*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;position:relative;background:#111;font-family:Inter;-webkit-font-smoothing:antialiased}
.photo{position:absolute;inset:0;background-repeat:no-repeat}
.shade{position:absolute;inset:0}
.logo{position:absolute;left:72px;top:68px;width:190px;opacity:.95}
.block{position:absolute;left:72px;right:72px}
.eye{display:flex;align-items:center;gap:18px;color:var(--acc);font-weight:600;font-size:19px;letter-spacing:3.2px;text-transform:uppercase;line-height:1.5}
.eye:before{content:"";flex:0 0 44px;height:2px;background:var(--acc)}
h1{font-family:Fraunces;font-weight:600;color:#fff;font-size:86px;line-height:1.02;letter-spacing:-1.5px;margin-top:26px}
h1 i{font-style:normal;color:var(--acc)}
p{color:rgba(255,255,255,.86);font-size:28px;line-height:1.45;margin-top:26px;max-width:830px}
p b{color:#fff;font-weight:600}
.foot{position:absolute;left:72px;right:72px;bottom:54px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,.28);padding-top:20px;color:rgba(255,255,255,.75);font-size:17px;letter-spacing:.4px}
.foot .site{font-weight:600;color:#fff;letter-spacing:1.5px}
.foot .cr{font-size:14px;color:rgba(255,255,255,.55)}'''
c=json.load(open(sys.argv[1]))
pos=f"top:{c['top']}px" if 'top' in c else f"bottom:{c['bottom']}px"
html=f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts/f2local.css"><style>{CSS}
:root{{--acc:{c['acc']}}}
.photo{{background-image:url({c['img']});{c['bg']};filter:{c.get('filter','none')}}}
.shade{{background:{c['shade']}}}</style></head><body>
<div class="photo"></div><div class="shade"></div>
<img class="logo" src="img/logo.png">
<div class="block" style="{pos}"><div class="eye">{c['eye']}</div><h1>{c['h1']}</h1><p>{c['p']}</p></div>
<div class="foot"><span class="site">UPRISINGARTS.ORG</span><span class="cr">{c['credit']}</span></div>
</body></html>'''
open(sys.argv[2],'w').write(html)
