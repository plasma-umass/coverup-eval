# file lib/ansible/cli/doc.py:1001-1010
# lines [1001, 1002, 1003, 1004, 1006, 1007, 1008, 1009, 1010]
# branches ['1003->1004', '1003->1008', '1006->1007', '1006->1008', '1008->1009', '1008->1010']

import pytest
from ansible.cli.doc import DocCLI

def test_format_version_added():
    # Test when version_added_collection is 'ansible.builtin' and version_added is 'historical'
    result = DocCLI._format_version_added('historical', 'ansible.builtin')
    assert result == 'historical'

    # Test when version_added_collection is 'ansible.builtin' and version_added is not 'historical'
    result = DocCLI._format_version_added('2.9', 'ansible.builtin')
    assert result == 'version 2.9 of ansible-core'

    # Test when version_added_collection is provided
    result = DocCLI._format_version_added('2.9', 'some_collection')
    assert result == 'version 2.9 of some_collection'

    # Test when version_added_collection is None
    result = DocCLI._format_version_added('2.9')
    assert result == 'version 2.9'
