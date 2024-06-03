# file lib/ansible/module_utils/facts/network/generic_bsd.py:184-192
# lines [184, 186, 187, 188, 189, 190, 191, 192]
# branches ['187->188', '187->189', '189->190', '189->191', '191->exit', '191->192']

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    pass

@pytest.fixture
def network():
    module = MockModule()
    return GenericBsdIfconfigNetwork(module)

def test_parse_media_line(network):
    current_if = {}
    ips = []

    # Test case where words has exactly 2 elements
    words = ['media:', '1000baseT']
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == '1000baseT'
    assert 'media_select' not in current_if
    assert 'media_type' not in current_if
    assert 'media_options' not in current_if

    # Test case where words has exactly 3 elements
    words = ['media:', '1000baseT', 'full-duplex']
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == '1000baseT'
    assert current_if['media_select'] == 'full-duplex'
    assert 'media_type' not in current_if
    assert 'media_options' not in current_if

    # Test case where words has exactly 4 elements
    words = ['media:', '1000baseT', 'full-duplex', 'type']
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == '1000baseT'
    assert current_if['media_select'] == 'full-duplex'
    assert current_if['media_type'] == 'ype'
    assert 'media_options' not in current_if

    # Test case where words has more than 4 elements
    words = ['media:', '1000baseT', 'full-duplex', 'type', 'options']
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == '1000baseT'
    assert current_if['media_select'] == 'full-duplex'
    assert current_if['media_type'] == 'ype'
    assert current_if['media_options'] == network.get_options('options')
