# file lib/ansible/executor/stats.py:60-71
# lines [63, 64, 65, 66, 67, 68, 69, 70]
# branches []

import pytest
from ansible.executor.stats import AggregateStats

@pytest.fixture
def mock_aggregate_stats(mocker):
    stats = AggregateStats()
    mocker.patch.object(stats, 'ok', {'host1': 1})
    mocker.patch.object(stats, 'failures', {'host1': 2})
    mocker.patch.object(stats, 'dark', {'host1': 3})
    mocker.patch.object(stats, 'changed', {'host1': 4})
    mocker.patch.object(stats, 'skipped', {'host1': 5})
    mocker.patch.object(stats, 'rescued', {'host1': 6})
    mocker.patch.object(stats, 'ignored', {'host1': 7})
    return stats

def test_summarize(mock_aggregate_stats):
    result = mock_aggregate_stats.summarize('host1')
    assert result == {
        'ok': 1,
        'failures': 2,
        'unreachable': 3,
        'changed': 4,
        'skipped': 5,
        'rescued': 6,
        'ignored': 7
    }
