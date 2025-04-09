# file lib/ansible/executor/stats.py:83-99
# lines [83, 86, 87, 88, 89, 92, 93, 95, 96, 99]
# branches ['86->87', '86->88', '88->89', '88->92', '92->93', '92->95', '95->96', '95->99']

import pytest
from ansible.executor.stats import AggregateStats
from collections.abc import MutableMapping

# Mocking the merge_hash function as it is not provided in the snippet
def mock_merge_hash(existing, new):
    for k, v in new.items():
        if k in existing:
            existing[k] += v
        else:
            existing[k] = v
    return existing

@pytest.fixture
def aggregate_stats(mocker):
    stats = AggregateStats()
    stats.custom = {'_run': {}}
    mocker.patch('ansible.executor.stats.merge_hash', side_effect=mock_merge_hash)
    return stats

def test_update_custom_stats_with_mutable_mapping(aggregate_stats):
    # Setup
    which = 'test_dict'
    what = {'key1': 1}
    aggregate_stats.set_custom_stats(which, {}, host='_run')

    # Exercise
    aggregate_stats.update_custom_stats(which, what, host='_run')

    # Verify
    assert aggregate_stats.custom['_run'][which] == {'key1': 1}

    # Exercise again with an update
    what_update = {'key2': 2}
    aggregate_stats.update_custom_stats(which, what_update, host='_run')

    # Verify update
    assert aggregate_stats.custom['_run'][which] == {'key1': 1, 'key2': 2}

def test_update_custom_stats_with_non_matching_types(aggregate_stats):
    # Setup
    which = 'test_mismatch'
    what = {'key1': 1}
    aggregate_stats.set_custom_stats(which, 10, host='_run')

    # Exercise
    result = aggregate_stats.update_custom_stats(which, what, host='_run')

    # Verify
    assert result is None
    assert aggregate_stats.custom['_run'][which] == 10

def test_update_custom_stats_with_overloaded_plus(aggregate_stats):
    # Setup
    which = 'test_number'
    what = 5
    aggregate_stats.set_custom_stats(which, 10, host='_run')

    # Exercise
    aggregate_stats.update_custom_stats(which, what, host='_run')

    # Verify
    assert aggregate_stats.custom['_run'][which] == 15
