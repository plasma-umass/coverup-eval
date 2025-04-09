# file: lib/ansible/module_utils/facts/system/chroot.py:42-47
# asked: {"lines": [42, 43, 44, 46, 47], "branches": []}
# gained: {"lines": [42, 43, 44, 46, 47], "branches": []}

import pytest
from ansible.module_utils.facts.system.chroot import ChrootFactCollector
from ansible.module_utils.facts.system.chroot import is_chroot

@pytest.fixture
def mock_is_chroot(mocker):
    return mocker.patch('ansible.module_utils.facts.system.chroot.is_chroot')

def test_chroot_fact_collector_collect_true(mock_is_chroot):
    mock_is_chroot.return_value = True
    collector = ChrootFactCollector()
    result = collector.collect()
    assert result == {'is_chroot': True}

def test_chroot_fact_collector_collect_false(mock_is_chroot):
    mock_is_chroot.return_value = False
    collector = ChrootFactCollector()
    result = collector.collect()
    assert result == {'is_chroot': False}
