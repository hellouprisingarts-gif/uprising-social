# Card template
1080x1350 Instagram/Facebook card. Write a JSON config like example-config.json (photo path relative to this folder: img/<file>.jpg),
then: `python3 tpl.py config.json card.html && node render.js card` (render.js screenshots card.html to card.png at 1080x1350).
Config keys: acc (accent colour), img, bg (background-size/position CSS to crop), filter, shade (gradient CSS), top or bottom (text block position px),
eye (small caps label), h1 (headline, wrap the key phrase in <i>), p (one sentence + one bold stat), credit (photo credit).
