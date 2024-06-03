# file lib/ansible/module_utils/facts/collector.py:266-280
# lines []
# branches ['277->276']

import pytest
from unittest.mock import patch

# Assuming the function find_unresolved_requires is imported from the module
from ansible.module_utils.facts.collector import find_unresolved_requires

# Mock function to replace _get_requires_by_collector_name
def mock_get_requires_by_collector_name(collector_name, all_fact_subsets):
    if collector_name == "collector1":
        return ["fact1", "fact2"]
    elif collector_name == "collector2":
        return ["fact2", "fact3"]
    return []

@patch('ansible.module_utils.facts.collector._get_requires_by_collector_name', side_effect=mock_get_requires_by_collector_name)
def test_find_unresolved_requires(mock_get_requires):
    collector_names = ["collector1", "collector2", "fact2"]
    all_fact_subsets = {}

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)

    assert unresolved == {"fact1", "fact3"}

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
