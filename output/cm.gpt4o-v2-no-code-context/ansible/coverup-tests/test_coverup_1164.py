# file: lib/ansible/module_utils/facts/network/generic_bsd.py:184-192
# asked: {"lines": [186, 187, 188, 189, 190, 191, 192], "branches": [[187, 188], [187, 189], [189, 190], [189, 191], [191, 0], [191, 192]]}
# gained: {"lines": [186, 187, 188, 189, 190, 191, 192], "branches": [[187, 188], [187, 189], [189, 190], [189, 191], [191, 0], [191, 192]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    pass

@pytest.fixture
def network_instance():
    module = MockModule()
    return GenericBsdIfconfigNetwork(module)

def test_parse_media_line_minimal(network_instance):
    current_if = {}
    words = ["media", "1000baseT"]
    network_instance.parse_media_line(words, current_if, None)
    assert current_if['media'] == "1000baseT"
    assert 'media_select' not in current_if
    assert 'media_type' not in current_if
    assert 'media_options' not in current_if

def test_parse_media_line_with_select(network_instance):
    current_if = {}
    words = ["media", "1000baseT", "full-duplex"]
    network_instance.parse_media_line(words, current_if, None)
    assert current_if['media'] == "1000baseT"
    assert current_if['media_select'] == "full-duplex"
    assert 'media_type' not in current_if
    assert 'media_options' not in current_if

def test_parse_media_line_with_type(network_instance):
    current_if = {}
    words = ["media", "1000baseT", "full-duplex", "type"]
    network_instance.parse_media_line(words, current_if, None)
    assert current_if['media'] == "1000baseT"
    assert current_if['media_select'] == "full-duplex"
    assert current_if['media_type'] == "ype"
    assert 'media_options' not in current_if

def test_parse_media_line_with_options(network_instance, mocker):
    current_if = {}
    words = ["media", "1000baseT", "full-duplex", "type", "options"]
    mocker.patch.object(network_instance, 'get_options', return_value="mocked_options")
    network_instance.parse_media_line(words, current_if, None)
    assert current_if['media'] == "1000baseT"
    assert current_if['media_select'] == "full-duplex"
    assert current_if['media_type'] == "ype"
    assert current_if['media_options'] == "mocked_options"
