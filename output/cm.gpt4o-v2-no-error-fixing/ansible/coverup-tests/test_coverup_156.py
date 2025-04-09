# file: lib/ansible/playbook/block.py:95-103
# asked: {"lines": [95, 96, 97, 98, 99, 100, 101, 102, 103], "branches": [[98, 99], [98, 103], [99, 100], [99, 103], [100, 99], [100, 101]]}
# gained: {"lines": [95, 96, 97, 98, 99, 100, 101, 102, 103], "branches": [[98, 99], [98, 103], [99, 100], [99, 103], [100, 99], [100, 101]]}

import pytest
from ansible.playbook.block import Block

@pytest.mark.parametrize("input_data, expected", [
    ({"block": []}, True),
    ({"rescue": []}, True),
    ({"always": []}, True),
    ({"other": []}, False),
    ([], False),
    ("string", False),
    (123, False),
])
def test_is_block(input_data, expected):
    assert Block.is_block(input_data) == expected
