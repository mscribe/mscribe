from __future__ import annotations

import regex as re
from website.utils.uuid import uuid


ULI_OBJECT = f"<{uuid.uuid()}>"
OLI_OBJECT = f"<{uuid.uuid()}>"
BR_OBJECT = f"<{uuid.uuid()}>"

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
OLI_TAG = rf'<{OLI_OBJECT}>\2</{OLI_OBJECT}>'

ULI_REGEX = re.compile(r'^(\*\s?)(.+)\n', re.MULTILINE)
ULI_TAG = rf'<{ULI_OBJECT}>\2</{ULI_OBJECT}>'

P_REGEX = re.compile(r'(?<!code.+)(^[A-Za-z0-9].+)', re.MULTILINE)
P_TAG = r'<p>\1</p>'

BOLD_REGEX = re.compile(r'(?<!\*)\*\*(.+?)\*\*(?!\*)', re.MULTILINE)
BOLD_TAG = r'<strong>\1</strong>'

ITALIC_REGEX = re.compile(r'(?<!\*)\*(.+?)\*(?!\*)', re.MULTILINE)
ITALIC_TAG = r'<em>\1</em>'

UNDLINE_REGEX = re.compile(r'(?<!_)_([^_]+?)_(?!_)', re.MULTILINE)
UNDLINE_TAG = r'<u>\1</u>'

STROKE_REGEX = re.compile(r'~(.+?)~', re.MULTILINE)
STROKE_TAG = r'<del>\1</del>'

BLOCKQUOTE_REGEX = re.compile(r'^>\s?(.+)', re.MULTILINE)
BLOCKQUOTE_TAG = r'<blockquote>\1</blockquote>'

IMG_REGEX = re.compile(r'^\!\[(.+)\]\((.+)\)', re.MULTILINE)
IMG_TAG = r'<img src="\2" alt="\1"/>'

LINK_REGEX = re.compile(r'^\[(.+)\]\((.+)\)', re.MULTILINE)
LINK_TAG = r'<a href="\2">\1</a>'

HR_REGEX = re.compile(r'^(___)$', re.MULTILINE)
HR_TAG = r'<hr>'

BR_REGEX = re.compile(BR_OBJECT)
BR_TAG = r'<br>'

UL_REGEX = re.compile(rf'(<{ULI_OBJECT}>.*<\/{ULI_OBJECT}>)', re.MULTILINE)
UL_TAG = r'<ul>\1</ul>'

OL_REGEX = re.compile(rf'(<{OLI_OBJECT}>.*<\/{OLI_OBJECT}>)')
OL_TAG = r'<ol>\1</ol>'

CODEBLOCK_REGEX = re.compile(r'```[a-z]+\n[\s\S]*?\n```', re.MULTILINE)

PRE_REGEX = re.compile(r'```([a-z]+)\n([\s\S]*?)\n```', re.MULTILINE)
PRE_TAG = r'<pre><code language="\1">\2</code></pre>'

LIST_ITEM_REGEX = re.compile(rf'(\<\/?)({OLI_OBJECT}|{ULI_OBJECT})(\>)')
LIST_ITEM_TAG = r'\1li\3'

TABLE_REGEX = re.compile(r'^\|(?:#[^|]+#\|)+$\n(^\|.+\|$\n?)+', re.MULTILINE)
TABLE_CELL_REGEX = re.compile(r'\|([^|]+)')
TABLE_ROW_REGEX = re.compile(r'^\|.+\|$')


class Converter:
    def __new__(cls) -> Converter:
        if not hasattr(cls, 'instance'):
            cls.instance = super(Converter, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self._pre_patterns = [
            (H1_REGEX, H1_TAG),
            (H2_REGEX, H2_TAG),
            (H3_REGEX, H3_TAG),
            (H4_REGEX, H4_TAG),
            (H5_REGEX, H5_TAG),
            (H6_REGEX, H6_TAG),
            (P_REGEX, P_TAG),
            (BOLD_REGEX, BOLD_TAG),
            (ITALIC_REGEX, ITALIC_TAG),
            (UNDLINE_REGEX, UNDLINE_TAG),
            (STROKE_REGEX, STROKE_TAG),
            (IMG_REGEX, IMG_TAG),
            (LINK_REGEX, LINK_TAG),
            (BLOCKQUOTE_REGEX, BLOCKQUOTE_TAG),
            (HR_REGEX, HR_TAG),
            (OLI_REGEX, OLI_TAG),
            (ULI_REGEX, ULI_TAG),
            (UL_REGEX, UL_TAG),
            (OL_REGEX, OL_TAG),
            (TABLE_REGEX, lambda match: self._parse_table(match.group(0))),
        ]

        self._post_patterns = [
            (PRE_REGEX, PRE_TAG),
            (LIST_ITEM_REGEX, LIST_ITEM_TAG),
            (BR_REGEX, BR_TAG),
        ]

        self._code_blocks = {}

    def _set_newlines(self, html: str) -> str:
        html_lines = []
        for x in html.splitlines():
            if not x:
                html_lines.append(BR_OBJECT)
            else:
                html_lines.append(x)
        return "\n".join(html_lines)

    def _preserve_code_blocks(self, html: str) -> str:
        for x in re.findall(CODEBLOCK_REGEX, html):
            uid = f"<{uuid.uuid()}>"
            html = html.replace(x, uid)
            self._code_blocks[uid] = x
        return html

    def _parse_table(self, html: str) -> str:
        lines = html.strip().splitlines()
        html_table = ["<table>"]

        headers = TABLE_CELL_REGEX.findall(lines[0])
        html_table.append("<thead><tr>")
        for header in headers:
            html_table.append(f"<th>{header.strip('#').strip()}</th>")
        html_table.append("</tr></thead>")

        html_table.append("<tbody>")
        for line in lines[1:]:
            if TABLE_ROW_REGEX.match(line):
                cells = TABLE_CELL_REGEX.findall(line)
                html_table.append("<tr>")
                for cell in cells:
                    html_table.append(f"<td>{cell.strip()}</td>")
                html_table.append("</tr>")
        html_table.append("</tbody>")

        html_table.append("</table>")
        return "".join(html_table)

    def _set_code_blocks(self, html: str) -> str:
        for uid, code in self._code_blocks.items():
            html = html.replace(uid, code)
        return html

    def _apply_pre_patterns(self, html: str) -> str:
        for pattern, replacement in self._pre_patterns:
            html = re.sub(pattern, replacement, html)
        return html

    def _apply_post_patterns(self, html: str) -> str:
        for pattern, replacement in self._post_patterns:
            html = re.sub(pattern, replacement, html)
        return html

    def convert(self, markdown_text: str) -> str:
        html = markdown_text
        html = self._set_newlines(html)
        html = self._preserve_code_blocks(html)
        html = self._apply_pre_patterns(html)
        html = self._set_code_blocks(html)
        html = self._apply_post_patterns(html)
        return html
