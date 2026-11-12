"""Show step numbers in the left menu as badges ("1. Evaluate…" -> (1) Evaluate…).

Only the primary navigation sidebar is changed, so the header title, the
table of contents and the footer links keep their plain text. The badge is
styled by .nav-num in assets/css/custom.css, matching the Home page's
workflow map (.wf-num).
"""

import re

_NUMBERED = re.compile(r'(<span class="md-ellipsis">\s*)(\d+)\.\s+')


def on_post_page(output, page, config):
    start = output.find('md-nav--primary')
    end = output.find('class="md-content"', start)
    if start == -1 or end == -1:
        return output
    nav = _NUMBERED.sub(r'\1<span class="nav-num">\2</span>', output[start:end])
    return output[:start] + nav + output[end:]
