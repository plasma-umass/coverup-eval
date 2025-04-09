# file: lib/ansible/executor/powershell/module_manifest.py:264-283
# asked: {"lines": [264, 266, 267, 268, 269, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 282, 283], "branches": [[268, 269], [268, 283], [271, 272], [271, 274], [274, 275], [274, 276], [276, 277], [276, 279], [279, 280], [279, 282]]}
# gained: {"lines": [264, 266, 267, 268, 269, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 282, 283], "branches": [[268, 269], [268, 283], [271, 272], [271, 274], [274, 275], [274, 276], [276, 277], [276, 279], [279, 280], [279, 282]]}

import pytest

def test_strip_comments():
    from ansible.executor.powershell.module_manifest import _strip_comments

    # Test case 1: Single line comment
    source = b"# This is a comment\nThis is code"
    expected = b"This is code"
    assert _strip_comments(source) == expected

    # Test case 2: Multi-line comment block
    source = b"<#\nThis is a comment block\n#>\nThis is code"
    expected = b"This is code"
    assert _strip_comments(source) == expected

    # Test case 3: Mixed comments and code
    source = b"# Comment\nCode line 1\n<#\nBlock comment\n#>\nCode line 2"
    expected = b"Code line 1\nCode line 2"
    assert _strip_comments(source) == expected

    # Test case 4: No comments
    source = b"Code line 1\nCode line 2"
    expected = b"Code line 1\nCode line 2"
    assert _strip_comments(source) == expected

    # Test case 5: Only comments
    source = b"# Comment 1\n<#\nBlock comment\n#>\n# Comment 2"
    expected = b""
    assert _strip_comments(source) == expected

    # Test case 6: Empty source
    source = b""
    expected = b""
    assert _strip_comments(source) == expected
