# file: lib/ansible/executor/stats.py:60-71
# asked: {"lines": [60, 63, 64, 65, 66, 67, 68, 69, 70], "branches": []}
# gained: {"lines": [60, 63, 64, 65, 66, 67, 68, 69, 70], "branches": []}

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_summarize_all_keys_present(aggregate_stats):
    host = 'test_host'
    aggregate_stats.ok[host] = 1
    aggregate_stats.failures[host] = 2
    aggregate_stats.dark[host] = 3
    aggregate_stats.changed[host] = 4
    aggregate_stats.skipped[host] = 5
    aggregate_stats.rescued[host] = 6
    aggregate_stats.ignored[host] = 7

    summary = aggregate_stats.summarize(host)
    
    assert summary['ok'] == 1
    assert summary['failures'] == 2
    assert summary['unreachable'] == 3
    assert summary['changed'] == 4
    assert summary['skipped'] == 5
    assert summary['rescued'] == 6
    assert summary['ignored'] == 7

def test_summarize_missing_keys(aggregate_stats):
    host = 'test_host'

    summary = aggregate_stats.summarize(host)
    
    assert summary['ok'] == 0
    assert summary['failures'] == 0
    assert summary['unreachable'] == 0
    assert summary['changed'] == 0
    assert summary['skipped'] == 0
    assert summary['rescued'] == 0
    assert summary['ignored'] == 0
