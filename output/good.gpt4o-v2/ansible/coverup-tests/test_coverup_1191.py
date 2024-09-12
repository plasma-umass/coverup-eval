# file: lib/ansible/executor/powershell/module_manifest.py:264-283
# asked: {"lines": [272, 273, 275, 277, 278, 280], "branches": [[271, 272], [274, 275], [276, 277], [279, 280]]}
# gained: {"lines": [272, 273, 275, 277, 278, 280], "branches": [[271, 272], [274, 275], [276, 277], [279, 280]]}

import pytest

def test_strip_comments():
    from ansible.executor.powershell.module_manifest import _strip_comments

    # Test case to cover lines 272-273
    source = b"""
    <#
    This is a block comment
    #>
    """
    result = _strip_comments(source)
    assert result == b""

    # Test case to cover line 275
    source = b"""
    <#
    This is a block comment
    """
    result = _strip_comments(source)
    assert result == b""

    # Test case to cover lines 277-278
    source = b"""
    <#
    This is a block comment
    #>
    """
    result = _strip_comments(source)
    assert result == b""

    # Test case to cover line 280
    source = b"""
    # This is a comment
    """
    result = _strip_comments(source)
    assert result == b""

    # Test case to cover normal lines
    source = b"""
    # This is a comment
    This is code
    """
    result = _strip_comments(source)
    assert result == b"    This is code"
