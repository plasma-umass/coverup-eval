# file lib/ansible/module_utils/facts/network/darwin.py:23-44
# lines [23, 24, 28, 31, 33, 34, 35, 38, 39, 40, 42, 43, 44]
# branches ['35->38', '35->43', '38->39', '38->42', '43->exit', '43->44']

import pytest
from ansible.module_utils.facts.network.darwin import DarwinNetwork

@pytest.fixture
def mock_darwin_network(mocker):
    mocker.patch.object(DarwinNetwork, '__init__', return_value=None)
    darwin_network = DarwinNetwork()
    darwin_network.get_options = lambda x: [x]  # Mock get_options to return a list containing the input
    return darwin_network

def test_parse_media_line_unknown_type(mock_darwin_network):
    current_if = {}
    ips = []
    words = ['media', '<unknown', 'type>']
    mock_darwin_network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'Unknown'
    assert current_if['media_type'] == 'unknown type'
    assert 'media_options' not in current_if

def test_parse_media_line_with_options(mock_darwin_network):
    current_if = {}
    ips = []
    words = ['media', 'select', '(type)', 'option1']
    mock_darwin_network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'select'
    assert current_if['media_type'] == 'type'
    assert current_if['media_options'] == ['option1']

def test_parse_media_line_without_type(mock_darwin_network):
    current_if = {}
    ips = []
    words = ['media', 'select']
    mock_darwin_network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Unknown'
    assert current_if['media_select'] == 'select'
    assert 'media_type' not in current_if
    assert 'media_options' not in current_if
