from __future__ import annotations

import re


UL_ITEM_REGEX = r'(<li class="blogcontent-ul-item"[^>]*>.*?</li>\s*)+'
OL_ITEM_REGEX = r'(<li class="blogcontent-ol-item"[^>]*>.*?</li>\s*)+'

BOLD_REGEX = r'\*\*[A-Za-z0-9 ]+\*\*'
ITALIC_REGEX = r'\*[A-Za-z0-9 ]+\\*'


class Converter:
    def __new__(cls) -> Converter:
        if not hasattr(cls, 'instance'):
            cls.instance = super(Converter, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.h1 = '<h1 class="blogcontent-h1">{{text}}</h1>'
        self.h2 = '<h2 class="blogcontent-h2">{{text}}</h2>'
        self.h3 = '<h3 class="blogcontent-h3">{{text}}</h3>'
        self.h4 = '<h4 class="blogcontent-h4">{{text}}</h4>'
        self.h5 = '<h5 class="blogcontent-h5">{{text}}</h5>'
        self.h6 = '<h6 class="blogcontent-h6">{{text}}</h6>'

        self.headers = {
            1: self.h1, 2: self.h2, 3: self.h3,
            4: self.h4, 5: self.h5, 6: self.h6
        }

        self.p = '<p class="blogcontent-p>{{text}}</p>'
        self.ol = '<ol class="blogcontent-ol>{{items}}</ol>'
        self.ul = '<ul class="blogcontent-ul>{{items}}</ul>'
        self.ul_item = '<li class="blogcontent-ul-item>{{text}}</li>'
        self.ol_item = '<li class="blogcontent-ol-item>{{text}}</li>'

        self.b = '<strong class="blogcontent-strong>{{text}}</strong>'
        self.i = '<em class="blogcontent-em>{{text}}</em>'

        self.a = '<a class="blogcontent-a" href="{{url}}">{{text}}</a>'
        self.img = '<img class="blogcontent-img" src="{{url}}" alt="{{alt}}" />'  # noqa
        self.blockquote = '<blockquote class="blogcontent-blockquote">{{text}}</blockquote>'  # noqa

        self.hr = '<hr class="blogcontent-hr'
        self.br = '<br class="blogcontent-hr'

    def _build(self, line: str) -> None:
        if line.startswith("# "):
            count = line.count("#")
            line = line.replace("# ", "")
            return self.headers.get(count).replace("{{text}}", line)
        elif re.search(r"^[0-9]+\.", line):
            return self.ol_item.replace("{{text}}", line)
        elif line.count("*") % 2 != 0:
            return self.ul_item.replace("{{text}}", line)
        else:
            return self.p.replace("{{text}}", line)

    def _format(self, line: str) -> None:
        ...

    def convert(markdown_text: str) -> str:
        html = []
        lines = markdown_text.split()
        for line in lines:
            ...
