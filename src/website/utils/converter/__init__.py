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

P_REGEX = re.compile(r'(^[A-Z-a-z0-9].+$)', re.MULTILINE)
P_TAG = r'<p class="blogcontent-p">\0</p>'

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

    def __init__(self) -> None:
        self._patterns = [
            (H1_REGEX, H1_TAG),
            (H2_REGEX, H2_TAG),
            (H3_REGEX, H3_TAG),
            (H4_REGEX, H4_TAG),
            (H5_REGEX, H5_TAG),
            (H6_REGEX, H6_TAG),
            (P_REGEX, P_TAG),
        ]

    def convert(self, markdown_text: str) -> str:
        html = markdown_text
        for pattern, replacement in self._patterns:
            html = re.sub(pattern, replacement, html)
        return html


"""
# Header 1
## Header 2
# Header 1
### Header 3
#### Header 4
##### Header 5
###### Header 6

This is a normal text.

This is a paragrah with many sentences, that will take a placeholder here. Hopefully this is going to be clear.

Some **bold text** and *italic text*.

1. Ordered item 1
2. Ordered item 2

* Unordered item
* Unordered item

[Link text](http://example.com)

![Alt text](http://example.com/image.jpg)

___

```python
print("Hello, World!")
```
"""