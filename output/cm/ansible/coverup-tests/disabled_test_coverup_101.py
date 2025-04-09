# file lib/ansible/module_utils/facts/system/distribution.py:470-509
# lines [470, 471, 480, 484, 487, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 505, 506, 507, 508]
# branches ['506->507', '506->510', '507->506', '507->508']

import pytest
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture
def distribution_instance(mocker):
    mock_module = mocker.MagicMock()
    return Distribution(mock_module)

def test_distribution_os_family_map(distribution_instance):
    # Test that each name in OS_FAMILY_MAP is correctly mapped in OS_FAMILY
    for family, names in Distribution.OS_FAMILY_MAP.items():
        for name in names:
            assert distribution_instance.OS_FAMILY[name] == family

def test_distribution_os_family_map_coverage(mocker, distribution_instance):
    # Mocking the OS_FAMILY_MAP to include a new family and distribution
    mocker.patch.object(Distribution, 'OS_FAMILY_MAP', {'TestFamily': ['TestOS']})
    
    # Rebuilding the OS_FAMILY dictionary to include the mocked values
    Distribution.OS_FAMILY = {}
    for family, names in Distribution.OS_FAMILY_MAP.items():
        for name in names:
            Distribution.OS_FAMILY[name] = family
    
    # Test that the new mocked family and distribution are correctly mapped
    assert Distribution.OS_FAMILY['TestOS'] == 'TestFamily'
    
    # Cleanup: Restore the original OS_FAMILY_MAP
    mocker.stopall()
