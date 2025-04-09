# file: lib/ansible/module_utils/facts/system/chroot.py:42-47
# asked: {"lines": [42, 43, 44, 46, 47], "branches": []}
# gained: {"lines": [42, 43, 44, 46, 47], "branches": []}

import pytest
from ansible.module_utils.facts.system.chroot import ChrootFactCollector
from ansible.module_utils.facts.system.chroot import is_chroot

class MockModule:
    def __init__(self, chroot_status):
        self.chroot_status = chroot_status

    def get_chroot_status(self):
        return self.chroot_status

@pytest.fixture
def mock_module_true(mocker):
    mock_module = MockModule(True)
    mocker.patch('ansible.module_utils.facts.system.chroot.is_chroot', return_value=True)
    return mock_module

@pytest.fixture
def mock_module_false(mocker):
    mock_module = MockModule(False)
    mocker.patch('ansible.module_utils.facts.system.chroot.is_chroot', return_value=False)
    return mock_module

def test_collect_chroot_true(mock_module_true):
    collector = ChrootFactCollector()
    result = collector.collect(module=mock_module_true)
    assert result == {'is_chroot': True}

def test_collect_chroot_false(mock_module_false):
    collector = ChrootFactCollector()
    result = collector.collect(module=mock_module_false)
    assert result == {'is_chroot': False}
