# file: lib/ansible/utils/color.py:104-112
# asked: {"lines": [105, 106, 107, 108, 109, 111, 112], "branches": [[105, 106], [105, 112], [106, 107], [106, 108], [108, 109], [108, 111]]}
# gained: {"lines": [105, 106, 107, 108, 109, 111, 112], "branches": [[105, 106], [105, 112], [106, 107], [106, 108], [108, 109], [108, 111]]}

import pytest
from ansible.utils.color import hostcolor, stringc
from ansible import constants as C

@pytest.fixture
def mock_constants(monkeypatch):
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", True)
    yield
    monkeypatch.undo()

def test_hostcolor_failures(mock_constants):
    host = "test_host"
    stats = {'failures': 1, 'unreachable': 0, 'changed': 0}
    result = hostcolor(host, stats)
    assert result == u"%-37s" % stringc(host, C.COLOR_ERROR)

def test_hostcolor_unreachable(mock_constants):
    host = "test_host"
    stats = {'failures': 0, 'unreachable': 1, 'changed': 0}
    result = hostcolor(host, stats)
    assert result == u"%-37s" % stringc(host, C.COLOR_ERROR)

def test_hostcolor_changed(mock_constants):
    host = "test_host"
    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}
    result = hostcolor(host, stats)
    assert result == u"%-37s" % stringc(host, C.COLOR_CHANGED)

def test_hostcolor_ok(mock_constants):
    host = "test_host"
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    result = hostcolor(host, stats)
    assert result == u"%-37s" % stringc(host, C.COLOR_OK)

def test_hostcolor_no_color(mock_constants, monkeypatch):
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", False)
    host = "test_host"
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    result = hostcolor(host, stats, color=False)
    assert result == u"%-26s" % host
