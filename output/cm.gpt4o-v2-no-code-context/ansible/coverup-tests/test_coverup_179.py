# file: lib/ansible/module_utils/facts/network/darwin.py:23-44
# asked: {"lines": [23, 24, 28, 31, 33, 34, 35, 38, 39, 40, 42, 43, 44], "branches": [[35, 38], [35, 43], [38, 39], [38, 42], [43, 0], [43, 44]]}
# gained: {"lines": [23, 24, 28, 31, 33, 34, 35, 38, 39, 40, 42, 43, 44], "branches": [[35, 38], [38, 39], [38, 42], [43, 0], [43, 44]]}

import pytest
from ansible.module_utils.facts.network.darwin import DarwinNetwork
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

class MockModule:
    pass

@pytest.fixture
def darwin_network():
    module = MockModule()
    return DarwinNetwork(module)

def test_parse_media_line_unknown_type(darwin_network):
    words = ['media:', '<unknown', 'type>']
    current_if = {}
    ips = []

    darwin_network.parse_media_line(words, current_if, ips)

    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'

def test_parse_media_line_with_options(darwin_network, mocker):
    words = ['media:', 'media_select', '(media_type)', 'media_options']
    current_if = {}
    ips = []

    mocker.patch.object(darwin_network, 'get_options', return_value='mocked_options')

    darwin_network.parse_media_line(words, current_if, ips)

    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'media_select'
    assert current_if['media_type'] == 'media_type'
    assert current_if['media_options'] == 'mocked_options'

def test_parse_media_line_without_options(darwin_network):
    words = ['media:', 'media_select', '(media_type)']
    current_if = {}
    ips = []

    darwin_network.parse_media_line(words, current_if, ips)

    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'media_select'
    assert current_if['media_type'] == 'media_type'
    assert 'media_options' not in current_if
