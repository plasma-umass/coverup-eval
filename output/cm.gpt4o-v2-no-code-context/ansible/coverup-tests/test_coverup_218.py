# file: lib/ansible/cli/doc.py:1001-1010
# asked: {"lines": [1001, 1002, 1003, 1004, 1006, 1007, 1008, 1009, 1010], "branches": [[1003, 1004], [1003, 1008], [1006, 1007], [1006, 1008], [1008, 1009], [1008, 1010]]}
# gained: {"lines": [1001, 1002, 1003, 1004, 1006, 1007, 1008, 1009, 1010], "branches": [[1003, 1004], [1003, 1008], [1006, 1007], [1006, 1008], [1008, 1009], [1008, 1010]]}

import pytest
from ansible.cli.doc import DocCLI

def test_format_version_added_builtin():
    result = DocCLI._format_version_added('2.9', 'ansible.builtin')
    assert result == 'version 2.9 of ansible-core'

def test_format_version_added_historical():
    result = DocCLI._format_version_added('historical', 'ansible.builtin')
    assert result == 'historical'

def test_format_version_added_with_collection():
    result = DocCLI._format_version_added('2.9', 'community.general')
    assert result == 'version 2.9 of community.general'

def test_format_version_added_without_collection():
    result = DocCLI._format_version_added('2.9')
    assert result == 'version 2.9'
