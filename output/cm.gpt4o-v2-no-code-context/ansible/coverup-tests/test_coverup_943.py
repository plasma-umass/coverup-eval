# file: lib/ansible/executor/powershell/module_manifest.py:264-283
# asked: {"lines": [266, 267, 268, 269, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 282, 283], "branches": [[268, 269], [268, 283], [271, 272], [271, 274], [274, 275], [274, 276], [276, 277], [276, 279], [279, 280], [279, 282]]}
# gained: {"lines": [266, 267, 268, 269, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 282, 283], "branches": [[268, 269], [268, 283], [271, 272], [271, 274], [274, 275], [274, 276], [276, 277], [276, 279], [279, 280], [279, 282]]}

import pytest

from ansible.executor.powershell.module_manifest import _strip_comments

def test_strip_comments_removes_single_line_comments():
    source = b"# This is a comment\nThis is code\n# Another comment"
    expected = b"This is code"
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_removes_multiline_comments():
    source = b"<#\nThis is a\nmultiline comment\n#>\nThis is code"
    expected = b"This is code"
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_removes_mixed_comments():
    source = b"# Single line comment\n<#\nMultiline\ncomment\n#>\nCode line 1\n# Another single line comment\nCode line 2"
    expected = b"Code line 1\nCode line 2"
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_handles_no_comments():
    source = b"Code line 1\nCode line 2"
    expected = b"Code line 1\nCode line 2"
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_handles_empty_source():
    source = b""
    expected = b""
    result = _strip_comments(source)
    assert result == expected

def test_strip_comments_handles_only_comments():
    source = b"# Comment 1\n# Comment 2\n<#\nMultiline\ncomment\n#>"
    expected = b""
    result = _strip_comments(source)
    assert result == expected
