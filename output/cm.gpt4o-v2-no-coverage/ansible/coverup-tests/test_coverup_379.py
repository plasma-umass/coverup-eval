# file: lib/ansible/module_utils/facts/network/generic_bsd.py:184-192
# asked: {"lines": [184, 186, 187, 188, 189, 190, 191, 192], "branches": [[187, 188], [187, 189], [189, 190], [189, 191], [191, 0], [191, 192]]}
# gained: {"lines": [184, 186, 187, 188, 189, 190, 191, 192], "branches": [[187, 188], [187, 189], [189, 190], [189, 191], [191, 0], [191, 192]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

class MockModule:
    pass

@pytest.fixture
def network():
    return GenericBsdIfconfigNetwork(MockModule())

def test_parse_media_line_minimal(network):
    words = ["media", "1000baseT"]
    current_if = {}
    ips = []
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == "1000baseT"
    assert 'media_select' not in current_if
    assert 'media_type' not in current_if
    assert 'media_options' not in current_if

def test_parse_media_line_with_select(network):
    words = ["media", "1000baseT", "full-duplex"]
    current_if = {}
    ips = []
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == "1000baseT"
    assert current_if['media_select'] == "full-duplex"
    assert 'media_type' not in current_if
    assert 'media_options' not in current_if

def test_parse_media_line_with_type(network):
    words = ["media", "1000baseT", "full-duplex", "(autoselect)"]
    current_if = {}
    ips = []
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == "1000baseT"
    assert current_if['media_select'] == "full-duplex"
    assert current_if['media_type'] == "autoselect)"
    assert 'media_options' not in current_if

def test_parse_media_line_with_options(network, mocker):
    mocker.patch.object(network, 'get_options', return_value="some_options")
    words = ["media", "1000baseT", "full-duplex", "(autoselect)", "options"]
    current_if = {}
    ips = []
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == "1000baseT"
    assert current_if['media_select'] == "full-duplex"
    assert current_if['media_type'] == "autoselect)"
    assert current_if['media_options'] == "some_options"
    network.get_options.assert_called_once_with("options")
