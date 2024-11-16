from __future__ import annotations

import re


H1_TAG = r'<h1 class="blogcontent-h1">{{text}}</h1>'
H2_TAG = r'<h2 class="blogcontent-h2">{{text}}</h2>'
H3_TAG = r'<h3 class="blogcontent-h3">{{text}}</h3>'
H4_TAG = r'<h4 class="blogcontent-h4">{{text}}</h4>'
H5_TAG = r'<h5 class="blogcontent-h5">{{text}}</h5>'
H6_TAG = r'<h6 class="blogcontent-h6">{{text}}</h6>'
P_TAG = r'<p class="blogcontent-p">{{text}}</p>'
OL_TAG = r'<ol class="blogcontent-ol">{{text}}</ol>'
UL_TAG = r'<ul class="blogcontent-ul">{{text}}</ul>'
OL_ITEM = r'<li class="blogcontent-ol-item">{{text}}</li>'
UL_ITEM = r'<li class="blogcontent-ul-item">{{text}}</li>'
STRONG_TAG = r'<strong class="blogcontent-strong">{{text}}</strong>'
I_TAG = r'<em class="blogcontent-em">{{text}}</em>'
IMG_TAG = r'<center><img class="blogcontent-img" src="\2" alt="\1"/></center>'
A_TAG = r'<a class="blogcontent-a" href="\2">\1</a>'
HR_TAG = r'<hr class="blogcontent-hr">'
BR_TAG = r'<br class="blogcontent-br">'

OL_ITEM_REGEX = r'(?:<li class="blogcontent-ol-item"[^>]*>.*?<\/li>\s*)+'
UL_ITEM_REGEX = r'(?:<li class="blogcontent-ul-item"[^>]*>.*?<\/li>\s*)+'

H_REGEX = r'[#]+ '
OL_REGEX = r'^[0-9]+\.'
BOLD_REGEX = r'\*\*.+\*\*'
ITALIC_REGEX = r'\*.+\\*'
IMAGE_REGEX = r'!\[([^\]]+)]\(([^)]+)\)'
LINK_REGEX = r'\[([^\]]+)]\(([^)]+)\)'


class Converter:
    def __new__(cls) -> Converter:
        if not hasattr(cls, 'instance'):
            cls.instance = super(Converter, cls).__new__(cls)
        return cls.instance

    def _build(self, line: str) -> str:
        self._headers = {1: H1_TAG, 2: H2_TAG, 3: H3_TAG,
                         4: H4_TAG, 5: H5_TAG, 6: H6_TAG}

        if line.startswith("#"):
            count = line.count("#")
            print(count)
            line = re.sub(H_REGEX, "", line)
            return self._headers.get(count).replace("{{text}}", line)
        elif re.search(OL_REGEX, line):
            line = re.sub(OL_REGEX, "", line)
            return OL_ITEM.replace("{{text}}", line)
        elif line.startswith("*") and line.count("*") % 2 != 0:
            return UL_ITEM.replace("{{text}}", line[1:])
        elif re.search(IMAGE_REGEX, line):
            return re.sub(IMAGE_REGEX, IMG_TAG, line)
        elif re.search(LINK_REGEX, line):
            return re.sub(LINK_REGEX, A_TAG, line)
        elif line == "___":
            return HR_TAG
        elif not len(line):
            return BR_TAG
        else:
            return P_TAG.replace("{{text}}", line)

    def _format_bold(self, line: str) -> str:
        while True:
            groups = re.search(BOLD_REGEX, line)
            if groups:
                group = groups.group(0)
                text = group.replace("**", "")
                text = STRONG_TAG.replace("{{text}}", text)
                line = line.replace(group, text)
            else:
                break
        return line

    def _format_italic(self, line: str) -> str:
        while True:
            groups = re.search(ITALIC_REGEX, line)
            if groups:
                group = groups.group(0)
                text = group.replace("*", "")
                text = I_TAG.replace("{{text}}", text)
                line = line.replace(group, text)
            else:
                break
        return line

    def _format(self, line: str) -> str:
        line = self._format_bold(line)
        line = self._format_italic(line)
        return line

    def _build_orderlist(self, html_text: str) -> str:
        for x in re.findall(OL_ITEM_REGEX, html_text):
            html_text = html_text.replace(x, OL_TAG.replace("{{text}}", x))
        return html_text

    def _build_unordedlist(self, html_text: str) -> str:
        for x in re.findall(UL_ITEM_REGEX, html_text):
            html_text = html_text.replace(x, UL_TAG.replace("{{text}}", x))
        return html_text

    def _build_lists(self, html_text: str) -> str:
        html_text = self._build_orderlist(html_text)
        html_text = self._build_unordedlist(html_text)
        return html_text

    def convert(self, markdown_text: str) -> str:
        html = []
        lines = markdown_text.split("\n")
        for line in lines:
            line = line.strip()
            line = self._build(line)
            line = self._format(line)
            html.append(line)
        html = "".join(html)
        html = self._build_lists(html)
        return html
