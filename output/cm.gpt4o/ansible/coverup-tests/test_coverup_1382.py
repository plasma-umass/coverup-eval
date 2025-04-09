# file lib/ansible/executor/powershell/module_manifest.py:264-283
# lines [266, 267, 268, 269, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 282, 283]
# branches ['268->269', '268->283', '271->272', '271->274', '274->275', '274->276', '276->277', '276->279', '279->280', '279->282']

import pytest
from ansible.executor.powershell.module_manifest import _strip_comments

def test_strip_comments(mocker):
    source = b"""
    # This is a comment
    <#
    This is a block comment
    #>
    This is code
    # Another comment
    <#
    Another block comment
    #>
    More code
    """
    
    expected_output = b"This is code\nMore code"
    
    result = _strip_comments(source)
    
    # Strip leading and trailing whitespace from each line in the result
    result = b'\n'.join(line.strip() for line in result.split(b'\n'))
    
    assert result == expected_output
