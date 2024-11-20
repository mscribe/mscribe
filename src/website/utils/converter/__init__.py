from __future__ import annotations

import re
from uuid import uuid4


ULI = str(uuid4())
OLI = str(uuid4())

H1_REGEX = re.compile(r'(^# )(.+)', re.MULTILINE)
H1_TAG = r'<h1>\2</h1>'

H2_REGEX = re.compile(r'(^## )(.+)', re.MULTILINE)
H2_TAG = r'<h2>\2</h2>'

H3_REGEX = re.compile(r'(^### )(.+)', re.MULTILINE)
H3_TAG = r'<h3>\2</h3>'

H4_REGEX = re.compile(r'(^#### )(.+)', re.MULTILINE)
H4_TAG = r'<h4>\2</h4>'

H5_REGEX = re.compile(r'(^##### )(.+)', re.MULTILINE)
H5_TAG = r'<h5>\2</h5>'

H6_REGEX = re.compile(r'(^###### )(.+)', re.MULTILINE)
H6_TAG = r'<h6>\2</h6>'

OLI_REGEX = re.compile(r'^([0-9]+.\s?)(.+)\n', re.MULTILINE)
OLI_TAG = rf'<{OLI}>\2</{OLI}>'

ULI_REGEX = re.compile(r'^(\*\s?)(.+)\n', re.MULTILINE)
ULI_TAG = rf'<{ULI}>\2</{ULI}>'

P_REGEX = re.compile(r'(^[A-Za-z0-9].+)', re.MULTILINE)
P_TAG = r'<p>\1</p>'

STRONG_REGEX = re.compile(r'\*\*(.+?)\*\*', re.MULTILINE)
STRONG_TAG = r'<strong>\1</strong>'

I_REGEX = re.compile(r'\*(.+?)\*', re.MULTILINE)
I_TAG = r'<em>\1</em>'

IMG_REGEX = re.compile(r'^\!\[(.+)\]\((.+)\)', re.MULTILINE)
IMG_TAG = r'<img src="\2" alt="\1"/>'

A_REGEX = re.compile(r'^\[(.+)\]\((.+)\)', re.MULTILINE)
A_TAG = r'<a href="\2">\1</a>'

HR_REGEX = re.compile(r'^(___)$', re.MULTILINE)
HR_TAG = r'<hr>'

BR_REGEX = re.compile(r'^\s*$')
BR_TAG = r'<br>'

UL_REGEX = re.compile(rf'(<{ULI}>.*<\/{ULI}>)')
UL_TAG = r'<ul>\1</ul>\n'

OL_REGEX = re.compile(rf'(<{OLI}>.*<\/{OLI}>)')
OL_TAG = r'<ol>\1</ol>\n'

PRE_REGEX = re.compile(r'```([a-z]+)\n([\s\S]*?)\n```', re.MULTILINE)
PRE_TAG = r'<pre><code language="\1">\2</code></pre>'

LIST_ITEM_REGEX = re.compile(rf'(\<\/?)({OLI}|{ULI})(\>)')
LIST_ITEM_TAG = r'\1li\3'


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
            (OLI_REGEX, OLI_TAG),
            (ULI_REGEX, ULI_TAG),
            (P_REGEX, P_TAG),
            (STRONG_REGEX, STRONG_TAG),
            (I_REGEX, I_TAG),
            (IMG_REGEX, IMG_TAG),
            (A_REGEX, A_TAG),
            (HR_REGEX, HR_TAG),
            (BR_REGEX, BR_TAG),
            (UL_REGEX, UL_TAG),
            (OL_REGEX, OL_TAG),
            (LIST_ITEM_REGEX, LIST_ITEM_TAG),
        ]

    def convert(self, markdown_text: str) -> str:
        html = markdown_text
        for pattern, replacement in self._patterns:
            html = re.sub(pattern, replacement, html)
        return html
