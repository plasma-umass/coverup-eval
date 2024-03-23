# file lib/ansible/cli/doc.py:1001-1010
# lines [1001, 1002, 1003, 1004, 1006, 1007, 1008, 1009, 1010]
# branches ['1003->1004', '1003->1008', '1006->1007', '1006->1008', '1008->1009', '1008->1010']

import pytest
from ansible.cli.doc import DocCLI

def test_format_version_added(mocker):
    # Test with version_added_collection as 'ansible.builtin'
    result = DocCLI._format_version_added('2.9', 'ansible.builtin')
    assert result == 'version 2.9 of ansible-core'

    # Test with version_added_collection as 'ansible.builtin' and version_added as 'historical'
    result = DocCLI._format_version_added('historical', 'ansible.builtin')
    assert result == 'historical'

    # Test with version_added_collection not 'ansible.builtin'
    result = DocCLI._format_version_added('2.9', 'community.example')
    assert result == 'version 2.9 of community.example'

    # Test with no version_added_collection
    result = DocCLI._format_version_added('2.9')
    assert result == 'version 2.9'

    # Test with version_added_collection as None
    result = DocCLI._format_version_added('2.9', None)
    assert result == 'version 2.9'
