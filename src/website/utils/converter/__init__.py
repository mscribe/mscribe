from __future__ import annotations

import re


H1_REGEX = re.compile(r'(^# )([A-Za-z0-9 ]+)', re.MULTILINE)
H1_TAG = r'<h1 class="blogcontent-h1">\2</h1>'

H2_REGEX = re.compile(r'(^## )([A-Za-z0-9 ]+)', re.MULTILINE)
H2_TAG = r'<h2 class="blogcontent-h2">\2</h2>'

H3_REGEX = re.compile(r'(^### )([A-Za-z0-9 ]+)', re.MULTILINE)
H3_TAG = r'<h3 class="blogcontent-h3">\2</h3>'

H4_REGEX = re.compile(r'(^#### )([A-Za-z0-9 ]+)', re.MULTILINE)
H4_TAG = r'<h4 class="blogcontent-h4">\2</h4>'

H5_REGEX = re.compile(r'(^##### )([A-Za-z0-9 ]+)', re.MULTILINE)
H5_TAG = r'<h5 class="blogcontent-h5">\2</h5>'

H6_REGEX = re.compile(r'(^###### )([A-Za-z0-9 ]+)', re.MULTILINE)
H6_TAG = r'<h6 class="blogcontent-h6">\2</h6>'

OL_ITEM_REGEX = re.compile(r'^([0-9]+.\s?)(.+)', re.MULTILINE)
OL_ITEM_TAG = r'<li class="blogcontent-ol-item">\2</li>'

UL_ITEM_REGEX = re.compile(r'^(\*\s?)(.+)', re.MULTILINE)
UL_ITEM_TAG = r'<li class="blogcontent-ul-item">\2</li>'

P_REGEX = re.compile(r'(^[A-Za-z0-9].+)', re.MULTILINE)
P_TAG = r'<p class="blogcontent-p">\1</p>'

STRONG_REGEX = re.compile(r'\*\*(.+)\*\*', re.MULTILINE)
STRONG_TAG = r'<strong class="blogcontent-strong">\1</strong>'

I_REGEX = re.compile(r'\*(.+)\*', re.MULTILINE)
I_TAG = r'<em class="blogcontent-em">\1</em>'

IMG_REGEX = re.compile(r'^\!\[(.+)\]\((.+)\)', re.MULTILINE)
IMG_TAG = r'<img class="blogcontent-img" src="\2" alt="\1"/>'

A_REGEX = re.compile(r'^\[(.+)\]\((.+)\)', re.MULTILINE)
A_TAG = r'<a class="blogcontent-a" href="\2">\1</a>'

HR_REGEX = re.compile(r'^(___)$', re.MULTILINE)
HR_TAG = r'<hr class="blogcontent-hr">'

BR_REGEX = re.compile(r'^\s*$')
BR_TAG = r'<br class="blogcontent-br">'

UL_REGEX = re.compile(r'(?:<li class="blogcontent-ul-item"[^>]*>.*?<\/li>\s*)+')  # noqa
UL_TAG = r'<ul class="blogcontent-ul">\2</ul>'

OL_REGEX = re.compile(r'(?:<li class="blogcontent-ol-item"[^>]*>.*?<\/li>\s*)+')  # noqa
OL_TAG = r'<ol class="blogcontent-ol">\2</ol>'

PRE_REGEX = re.compile(r'```([a-z]+)\n([\s\S]*?)\n```', re.MULTILINE)
PRE_TAG = r'<pre language="\1">\2</pre>'

# TABLE_HEADER = re.compile(r'^|#(.)+?#|', re.MULTILINE)
# TABLE_CELL = re.compile(r'', re.MULTILINE)

# TABLE_REGEX = ''
# TABLE_TAG = ''


class Converter:
    def __new__(cls) -> Converter:
        if not hasattr(cls, 'instance'):
            cls.instance = super(Converter, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self._patterns = [
            (H1_REGEX, H1_TAG),
            (H2_REGEX, H2_TAG),
            (H3_REGEX, H3_TAG),
            (H4_REGEX, H4_TAG),
            (H5_REGEX, H5_TAG),
            (H6_REGEX, H6_TAG),
            (PRE_REGEX, PRE_TAG),
            (OL_ITEM_REGEX, OL_ITEM_TAG),
            (UL_ITEM_REGEX, UL_ITEM_TAG),
            (P_REGEX, P_TAG),
            (STRONG_REGEX, STRONG_TAG),
            (I_REGEX, I_TAG),
            (IMG_REGEX, IMG_TAG),
            (A_REGEX, A_TAG),
            (HR_REGEX, HR_TAG),
            (BR_REGEX, BR_TAG),
            (UL_REGEX, UL_TAG),
            (OL_REGEX, OL_TAG),
        ]

    def convert(self, markdown_text: str) -> str:
        html = markdown_text
        for pattern, replacement in self._patterns:
            html = re.sub(pattern, replacement, html)
            print(html)
        return html
