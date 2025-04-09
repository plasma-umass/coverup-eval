# file: lib/ansible/executor/powershell/module_manifest.py:264-283
# asked: {"lines": [264, 266, 267, 268, 269, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 282, 283], "branches": [[268, 269], [268, 283], [271, 272], [271, 274], [274, 275], [274, 276], [276, 277], [276, 279], [279, 280], [279, 282]]}
# gained: {"lines": [264, 266, 267, 268, 269, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 282, 283], "branches": [[268, 269], [268, 283], [271, 272], [271, 274], [274, 275], [274, 276], [276, 277], [276, 279], [279, 280], [279, 282]]}

import pytest

from ansible.executor.powershell.module_manifest import _strip_comments

def test_strip_comments_single_line_comment():
    source = b"# This is a comment\nThis is code"
    expected = b"This is code"
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_multiline_comment():
    source = b"<#\nThis is a\nmultiline comment\n#>\nThis is code"
    expected = b"This is code"
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_mixed_comments():
    source = b"# Single line comment\n<#\nMultiline comment\n#>\nThis is code\n# Another comment"
    expected = b"This is code"
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_no_comments():
    source = b"This is code\nMore code"
    expected = b"This is code\nMore code"
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_empty_source():
    source = b""
    expected = b""
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_only_comments():
    source = b"# Comment\n<#\nMultiline\n#>\n# Another comment"
    expected = b""
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_multiline_comment_with_code():
    source = b"<#\nMultiline comment\n#>\nThis is code\n<#\nAnother multiline\n#>\nMore code"
    expected = b"This is code\nMore code"
    result = _strip_comments(source)
    assert result == expected
