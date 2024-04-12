# file lib/ansible/module_utils/facts/collector.py:89-96
# lines [89, 92, 93, 95, 96]
# branches ['92->93', '92->96']

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class TestFactCollector(BaseFactCollector):
    def _transform_name(self, name):
        return name.upper()

@pytest.fixture
def fact_collector():
    return TestFactCollector()

def test_transform_dict_keys(fact_collector):
    original_dict = {'key1': 'value1', 'key2': 'value2'}
    expected_dict = {'KEY1': 'value1', 'KEY2': 'value2'}
    transformed_dict = fact_collector._transform_dict_keys(original_dict)
    assert transformed_dict == expected_dict
