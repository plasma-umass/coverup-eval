# file lib/ansible/cli/doc.py:363-382
# lines [363, 364, 367, 368, 369, 370, 371, 372, 373, 374, 377, 378, 379, 380, 382]
# branches []

import pytest
from unittest.mock import patch

# Assuming the necessary imports and class definitions are available
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_regex_patterns(mocker):
    patterns = {
        '_ITALIC': mocker.patch.object(DocCLI, '_ITALIC', create=True),
        '_BOLD': mocker.patch.object(DocCLI, '_BOLD', create=True),
        '_MODULE': mocker.patch.object(DocCLI, '_MODULE', create=True),
        '_URL': mocker.patch.object(DocCLI, '_URL', create=True),
        '_LINK': mocker.patch.object(DocCLI, '_LINK', create=True),
        '_REF': mocker.patch.object(DocCLI, '_REF', create=True),
        '_CONST': mocker.patch.object(DocCLI, '_CONST', create=True),
        '_RULER': mocker.patch.object(DocCLI, '_RULER', create=True),
        '_RST_SEEALSO': mocker.patch.object(DocCLI, '_RST_SEEALSO', create=True),
        '_RST_NOTE': mocker.patch.object(DocCLI, '_RST_NOTE', create=True),
        '_RST_ROLES': mocker.patch.object(DocCLI, '_RST_ROLES', create=True),
        '_RST_DIRECTIVES': mocker.patch.object(DocCLI, '_RST_DIRECTIVES', create=True),
    }
    return patterns

def test_tty_ify(mock_regex_patterns):
    # Mock the regex patterns to return specific values
    mock_regex_patterns['_ITALIC'].sub.return_value = "italic"
    mock_regex_patterns['_BOLD'].sub.return_value = "bold"
    mock_regex_patterns['_MODULE'].sub.return_value = "module"
    mock_regex_patterns['_URL'].sub.return_value = "url"
    mock_regex_patterns['_LINK'].sub.return_value = "link"
    mock_regex_patterns['_REF'].sub.return_value = "ref"
    mock_regex_patterns['_CONST'].sub.return_value = "const"
    mock_regex_patterns['_RULER'].sub.return_value = "ruler"
    mock_regex_patterns['_RST_SEEALSO'].sub.return_value = "seealso"
    mock_regex_patterns['_RST_NOTE'].sub.return_value = "note"
    mock_regex_patterns['_RST_ROLES'].sub.return_value = "roles"
    mock_regex_patterns['_RST_DIRECTIVES'].sub.return_value = "directives"

    text = "Some text with various patterns"
    result = DocCLI.tty_ify(text)

    # Assertions to verify the expected transformations
    assert result == "directives"
    mock_regex_patterns['_ITALIC'].sub.assert_called_once_with(r"`\1'", text)
    mock_regex_patterns['_BOLD'].sub.assert_called_once_with(r"*\1*", "italic")
    mock_regex_patterns['_MODULE'].sub.assert_called_once_with("[" + r"\1" + "]", "bold")
    mock_regex_patterns['_URL'].sub.assert_called_once_with(r"\1", "module")
    mock_regex_patterns['_LINK'].sub.assert_called_once_with(r"\1 <\2>", "url")
    mock_regex_patterns['_REF'].sub.assert_called_once_with(r"\1", "link")
    mock_regex_patterns['_CONST'].sub.assert_called_once_with(r"`\1'", "ref")
    mock_regex_patterns['_RULER'].sub.assert_called_once_with("\n{0}\n".format("-" * 13), "const")
    mock_regex_patterns['_RST_SEEALSO'].sub.assert_called_once_with(r"See website for:", "ruler")
    mock_regex_patterns['_RST_NOTE'].sub.assert_called_once_with(r"Note:", "seealso")
    mock_regex_patterns['_RST_ROLES'].sub.assert_called_once_with(r"website for `", "note")
    mock_regex_patterns['_RST_DIRECTIVES'].sub.assert_called_once_with(r"", "roles")
