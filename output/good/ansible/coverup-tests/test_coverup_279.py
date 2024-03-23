# file lib/ansible/cli/doc.py:332-357
# lines [332, 333, 339, 343, 344, 345, 346, 347, 348, 349, 350, 353, 354, 355, 356]
# branches []

import re
import pytest
from unittest.mock import MagicMock

# Assuming the DocCLI class is part of a module named ansible.cli.doc
# If the actual import path is different, adjust the following line accordingly
from ansible.cli.doc import DocCLI

@pytest.fixture
def doc_cli(mocker):
    mocker.patch('ansible.cli.doc.CLI.__init__', return_value=None)
    return DocCLI([])

def test_doc_cli_regex_patterns(doc_cli):
    # Test the regex patterns to ensure they match the expected strings
    italic_match = DocCLI._ITALIC.search("I(some italic text)")
    bold_match = DocCLI._BOLD.search("B(some bold text)")
    module_match = DocCLI._MODULE.search("M(some module)")
    link_match = DocCLI._LINK.search("L(link text, link_url)")
    url_match = DocCLI._URL.search("U(http://example.com)")
    ref_match = DocCLI._REF.search("R(reference text, reference_url)")
    const_match = DocCLI._CONST.search("C(some constant)")
    ruler_match = DocCLI._RULER.search("HORIZONTALLINE")

    assert italic_match.group(1) == "some italic text"
    assert bold_match.group(1) == "some bold text"
    assert module_match.group(1) == "some module"
    assert link_match.group(1) == "link text"
    assert link_match.group(2) == "link_url"
    assert url_match.group(1) == "http://example.com"
    assert ref_match.group(1) == "reference text"
    assert ref_match.group(2) == "reference_url"
    assert const_match.group(1) == "some constant"
    assert ruler_match.group(0) == "HORIZONTALLINE"

    # Test the rst specific regex patterns
    rst_note_match = DocCLI._RST_NOTE.search(".. note::")
    rst_seealso_match = DocCLI._RST_SEEALSO.search(".. seealso::")
    rst_roles_match = DocCLI._RST_ROLES.search(":role:`some_role`")
    rst_directives_match = DocCLI._RST_DIRECTIVES.search(".. directive::")

    assert rst_note_match.group(0) == ".. note::"
    assert rst_seealso_match.group(0) == ".. seealso::"
    assert rst_roles_match.group(0) == ":role:`"
    assert rst_directives_match.group(0) == ".. directive::"
