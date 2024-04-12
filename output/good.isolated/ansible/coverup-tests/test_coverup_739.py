# file lib/ansible/plugins/filter/core.py:440-457
# lines [440, 441, 457]
# branches []

import pytest
from jinja2.runtime import Context
from ansible.plugins.filter.core import do_groupby

class MockEnvironment:
    def getitem(self, obj, attribute):
        return obj.get(attribute)

@pytest.fixture
def mock_environment(mocker):
    env = MockEnvironment()
    mocker.patch('ansible.plugins.filter.core._do_groupby', return_value=[('group1', [{'attr': 'value1'}, {'attr': 'value2'}]), ('group2', [{'attr': 'value3'}])])
    return env

def test_do_groupby(mock_environment):
    value = [{'attr': 'value1'}, {'attr': 'value2'}, {'attr': 'value3'}]
    attribute = 'attr'
    expected_result = [('group1', [{'attr': 'value1'}, {'attr': 'value2'}]), ('group2', [{'attr': 'value3'}])]
    
    result = do_groupby(mock_environment, value, attribute)
    
    assert result == expected_result, "The do_groupby function did not return the expected result."
