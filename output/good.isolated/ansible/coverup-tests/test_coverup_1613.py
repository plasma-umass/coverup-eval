# file lib/ansible/executor/powershell/module_manifest.py:264-283
# lines [272, 273, 275, 277, 278]
# branches ['271->272', '274->275', '276->277']

import pytest

from ansible.executor.powershell.module_manifest import _strip_comments

@pytest.fixture
def powershell_script_with_comments():
    return b"""
    # This is a single line comment
    <# This is a
    multiline comment #>
    $data = "This is data"
    # Another single line comment
    """.strip()

def test_strip_comments_with_multiline_comment(powershell_script_with_comments):
    expected_output = b"$data = \"This is data\""
    output = _strip_comments(powershell_script_with_comments).strip()
    assert output == expected_output, "Multiline comments were not stripped correctly"
