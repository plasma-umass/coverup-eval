# file: lib/ansible/cli/doc.py:1001-1010
# asked: {"lines": [1001, 1002, 1003, 1004, 1006, 1007, 1008, 1009, 1010], "branches": [[1003, 1004], [1003, 1008], [1006, 1007], [1006, 1008], [1008, 1009], [1008, 1010]]}
# gained: {"lines": [1001, 1002, 1003, 1004, 1006, 1007, 1008, 1009, 1010], "branches": [[1003, 1004], [1003, 1008], [1006, 1007], [1006, 1008], [1008, 1009], [1008, 1010]]}

import pytest
from ansible.cli.doc import DocCLI

@pytest.mark.parametrize("version_added, version_added_collection, expected", [
    ('2.0', None, 'version 2.0'),
    ('2.0', 'ansible.builtin', 'version 2.0 of ansible-core'),
    ('historical', 'ansible.builtin', 'historical'),
    ('2.0', 'some_collection', 'version 2.0 of some_collection'),
])
def test_format_version_added(version_added, version_added_collection, expected):
    result = DocCLI._format_version_added(version_added, version_added_collection)
    assert result == expected
