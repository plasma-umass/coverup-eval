# file: lib/ansible/cli/doc.py:363-382
# asked: {"lines": [367, 368, 369, 370, 371, 372, 373, 374, 377, 378, 379, 380, 382], "branches": []}
# gained: {"lines": [367, 368, 369, 370, 371, 372, 373, 374, 377, 378, 379, 380, 382], "branches": []}

import pytest
import re
from ansible.cli.doc import DocCLI

@pytest.fixture
def setup_doc_cli():
    class TestDocCLI(DocCLI):
        _ITALIC = re.compile(r'I\((.*?)\)')
        _BOLD = re.compile(r'B\((.*?)\)')
        _MODULE = re.compile(r'M\((.*?)\)')
        _URL = re.compile(r'U\((.*?)\)')
        _LINK = re.compile(r'L\((.*?),(.*?)\)')
        _REF = re.compile(r'R\((.*?)\)')
        _CONST = re.compile(r'C\((.*?)\)')
        _RULER = re.compile(r'HORIZONTALLINE')
        _RST_SEEALSO = re.compile(r'\.\. seealso::')
        _RST_NOTE = re.compile(r'\.\. note::')
        _RST_ROLES = re.compile(r':ref:`(.*?)`')
        _RST_DIRECTIVES = re.compile(r'\.\. .*?::')
    
    return TestDocCLI

def test_tty_ify_italic(setup_doc_cli):
    text = "I(word)"
    result = setup_doc_cli.tty_ify(text)
    assert result == "`word'"

def test_tty_ify_bold(setup_doc_cli):
    text = "B(word)"
    result = setup_doc_cli.tty_ify(text)
    assert result == "*word*"

def test_tty_ify_module(setup_doc_cli):
    text = "M(word)"
    result = setup_doc_cli.tty_ify(text)
    assert result == "[word]"

def test_tty_ify_url(setup_doc_cli):
    text = "U(word)"
    result = setup_doc_cli.tty_ify(text)
    assert result == "word"

def test_tty_ify_link(setup_doc_cli):
    text = "L(word,url)"
    result = setup_doc_cli.tty_ify(text)
    assert result == "word <url>"

def test_tty_ify_ref(setup_doc_cli):
    text = "R(word)"
    result = setup_doc_cli.tty_ify(text)
    assert result == "word"

def test_tty_ify_const(setup_doc_cli):
    text = "C(word)"
    result = setup_doc_cli.tty_ify(text)
    assert result == "`word'"

def test_tty_ify_ruler(setup_doc_cli):
    text = "HORIZONTALLINE"
    result = setup_doc_cli.tty_ify(text)
    assert result == "\n-------------\n"

def test_tty_ify_rst_seealso(setup_doc_cli):
    text = ".. seealso::"
    result = setup_doc_cli.tty_ify(text)
    assert result == "See website for:"

def test_tty_ify_rst_note(setup_doc_cli):
    text = ".. note::"
    result = setup_doc_cli.tty_ify(text)
    assert result == "Note:"

def test_tty_ify_rst_roles(setup_doc_cli):
    text = ":ref:`word`"
    result = setup_doc_cli.tty_ify(text)
    assert result == "website for `"

def test_tty_ify_rst_directives(setup_doc_cli):
    text = ".. directive::"
    result = setup_doc_cli.tty_ify(text)
    assert result == ""
