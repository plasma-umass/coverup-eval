# file: lib/ansible/cli/doc.py:363-382
# asked: {"lines": [363, 364, 367, 368, 369, 370, 371, 372, 373, 374, 377, 378, 379, 380, 382], "branches": []}
# gained: {"lines": [363, 364, 367, 368, 369, 370, 371, 372, 373, 374, 377, 378, 379, 380, 382], "branches": []}

import pytest
from ansible.cli.doc import DocCLI

@pytest.mark.parametrize("input_text, expected_output", [
    ("I(word)", "`word'"),
    ("B(word)", "*word*"),
    ("M(word)", "[word]"),
    ("U(word)", "word"),
    ("L(word, url)", "word <url>"),
    ("R(word, sphinx-ref)", "word"),
    ("C(word)", "`word'"),
    ("HORIZONTALLINE", "\n-------------\n"),
    (".. seealso::", "See website for:"),
    (".. note::", "Note:"),
    (":ref:`", "website for `"),
    (".. code::", ""),
])
def test_tty_ify(input_text, expected_output):
    result = DocCLI.tty_ify(input_text)
    assert result == expected_output
