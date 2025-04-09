# file: lib/ansible/utils/color.py:104-112
# asked: {"lines": [104, 105, 106, 107, 108, 109, 111, 112], "branches": [[105, 106], [105, 112], [106, 107], [106, 108], [108, 109], [108, 111]]}
# gained: {"lines": [104, 105, 106, 107, 108, 109, 111, 112], "branches": [[105, 106], [105, 112], [106, 107], [106, 108], [108, 109], [108, 111]]}

import pytest
from ansible.utils.color import hostcolor, stringc
from ansible import constants as C

@pytest.mark.parametrize("host, stats, color, expected", [
    ("host1", {'failures': 1, 'unreachable': 0, 'changed': 0}, True, u"\x1b[0;31mhost1\x1b[0m"),  # COLOR_ERROR
    ("host2", {'failures': 0, 'unreachable': 1, 'changed': 0}, True, u"\x1b[0;31mhost2\x1b[0m"),  # COLOR_ERROR
    ("host3", {'failures': 0, 'unreachable': 0, 'changed': 1}, True, u"\x1b[0;33mhost3\x1b[0m"),  # COLOR_CHANGED
    ("host4", {'failures': 0, 'unreachable': 0, 'changed': 0}, True, u"\x1b[0;32mhost4\x1b[0m"),  # COLOR_OK
    ("host5", {'failures': 0, 'unreachable': 0, 'changed': 0}, False, u"host5"),  # No color
])
def test_hostcolor(monkeypatch, host, stats, color, expected):
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", True)
    result = hostcolor(host, stats, color)
    assert result.strip() == expected.strip()
