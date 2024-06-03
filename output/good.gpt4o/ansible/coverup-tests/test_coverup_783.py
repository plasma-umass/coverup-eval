# file lib/ansible/module_utils/compat/version.py:272-305
# lines [272, 273, 304]
# branches []

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_comparison():
    # Test numeric comparison
    assert LooseVersion('1.5.1') < LooseVersion('1.5.2b2')
    assert LooseVersion('1.5.2b2') < LooseVersion('1.6')
    assert LooseVersion('3.10a') < LooseVersion('3.10b')
    assert LooseVersion('1996.07.12') < LooseVersion('1996.07.13')
    
    # Test alphanumeric comparison
    assert LooseVersion('2g6') < LooseVersion('2g7')
    assert LooseVersion('11g') > LooseVersion('2g6')
    assert LooseVersion('1.13++') > LooseVersion('1.13+')
    
    # Test mixed comparison
    assert LooseVersion('3.2.pl0') < LooseVersion('3.2.pl1')
    assert LooseVersion('2.0b1pl0') < LooseVersion('2.0b2pl0')
    assert LooseVersion('5.5.kw') > LooseVersion('5.5.kv')
    
    # Test edge cases
    assert LooseVersion('0.960923') < LooseVersion('0.960924')
    assert LooseVersion('161') > LooseVersion('3.10a')
    assert LooseVersion('8.02') == LooseVersion('8.2')
    assert LooseVersion('3.4j') < LooseVersion('3.5')
    assert LooseVersion('3.1.1.6') < LooseVersion('3.1.1.7')

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # No specific cleanup required for this test
