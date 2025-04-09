# file thefuck/conf.py:82-89
# lines [82, 84, 85, 86, 87, 88, 89]
# branches ['84->exit', '84->85']

import pytest
from thefuck.conf import Settings

def test_priority_from_env(mocker):
    mocker.patch.dict('os.environ', {'THEFUCK_RULES_PRIORITY': 'rule1=10:rule2=wrong:rule3=20'})
    settings = Settings()
    priorities = list(settings._priority_from_env('rule1=10:rule2=wrong:rule3=20'))
    assert ('rule1', 10) in priorities
    assert ('rule2', 'wrong') not in priorities
    assert ('rule3', 20) in priorities
