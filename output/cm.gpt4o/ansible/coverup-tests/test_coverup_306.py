# file lib/ansible/cli/doc.py:332-357
# lines [332, 333, 339, 343, 344, 345, 346, 347, 348, 349, 350, 353, 354, 355, 356]
# branches []

import pytest
import re
from ansible.cli.doc import DocCLI

@pytest.fixture
def doc_cli_instance(mocker):
    mocker.patch.object(DocCLI, '__abstractmethods__', set())
    return DocCLI(args=['dummy_arg'])

def test_doc_cli_ignore_list(doc_cli_instance):
    assert 'module' in doc_cli_instance.IGNORE
    assert 'docuri' in doc_cli_instance.IGNORE
    assert 'version_added' in doc_cli_instance.IGNORE
    assert 'short_description' in doc_cli_instance.IGNORE
    assert 'now_date' in doc_cli_instance.IGNORE
    assert 'plainexamples' in doc_cli_instance.IGNORE
    assert 'returndocs' in doc_cli_instance.IGNORE
    assert 'collection' in doc_cli_instance.IGNORE

def test_doc_cli_regex_patterns(doc_cli_instance):
    assert doc_cli_instance._ITALIC.pattern == r"\bI\(([^)]+)\)"
    assert doc_cli_instance._BOLD.pattern == r"\bB\(([^)]+)\)"
    assert doc_cli_instance._MODULE.pattern == r"\bM\(([^)]+)\)"
    assert doc_cli_instance._LINK.pattern == r"\bL\(([^)]+), *([^)]+)\)"
    assert doc_cli_instance._URL.pattern == r"\bU\(([^)]+)\)"
    assert doc_cli_instance._REF.pattern == r"\bR\(([^)]+), *([^)]+)\)"
    assert doc_cli_instance._CONST.pattern == r"\bC\(([^)]+)\)"
    assert doc_cli_instance._RULER.pattern == r"\bHORIZONTALLINE\b"
    assert doc_cli_instance._RST_NOTE.pattern == r".. note::"
    assert doc_cli_instance._RST_SEEALSO.pattern == r".. seealso::"
    assert doc_cli_instance._RST_ROLES.pattern == r":\w+?:`"
    assert doc_cli_instance._RST_DIRECTIVES.pattern == r".. \w+?::"

@pytest.mark.parametrize("pattern, test_string, expected", [
    (DocCLI._ITALIC, "I(italic_text)", True),
    (DocCLI._BOLD, "B(bold_text)", True),
    (DocCLI._MODULE, "M(module_name)", True),
    (DocCLI._LINK, "L(link_text, link_url)", True),
    (DocCLI._URL, "U(url_text)", True),
    (DocCLI._REF, "R(ref_text, ref_url)", True),
    (DocCLI._CONST, "C(const_text)", True),
    (DocCLI._RULER, "HORIZONTALLINE", True),
    (DocCLI._RST_NOTE, ".. note::", True),
    (DocCLI._RST_SEEALSO, ".. seealso::", True),
    (DocCLI._RST_ROLES, ":role:`", True),
    (DocCLI._RST_DIRECTIVES, ".. directive::", True),
])
def test_doc_cli_regex_matching(pattern, test_string, expected):
    assert bool(pattern.search(test_string)) == expected
