# file lib/ansible/utils/_junit_xml.py:256-258
# lines [258]
# branches []

import pytest
from unittest import mock
from ansible.utils._junit_xml import TestSuites

@pytest.fixture
def mock_pretty_xml(mocker):
    return mocker.patch('ansible.utils._junit_xml._pretty_xml')

def test_to_pretty_xml(mock_pretty_xml):
    # Arrange
    test_suites = TestSuites()
    mock_element = mock.Mock()
    
    # Mock the get_xml_element method to return a mock element
    with mock.patch.object(TestSuites, 'get_xml_element', return_value=mock_element):
        # Act
        result = test_suites.to_pretty_xml()
        
        # Assert
        mock_pretty_xml.assert_called_once_with(mock_element)
        assert result == mock_pretty_xml.return_value
