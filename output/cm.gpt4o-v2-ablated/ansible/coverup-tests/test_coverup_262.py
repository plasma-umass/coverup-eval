# file: lib/ansible/module_utils/api.py:121-131
# asked: {"lines": [121, 130, 131], "branches": [[130, 0], [130, 131]]}
# gained: {"lines": [121, 130, 131], "branches": [[130, 0], [130, 131]]}

import pytest
import random
from ansible.module_utils.api import generate_jittered_backoff

def test_generate_jittered_backoff(monkeypatch):
    # Mock random.randint to control the output
    mock_randint = lambda a, b: b
    monkeypatch.setattr(random, 'randint', mock_randint)
    
    retries = 5
    delay_base = 2
    delay_threshold = 10
    
    expected_delays = [
        min(delay_threshold, delay_base * 2 ** retry) for retry in range(retries)
    ]
    
    actual_delays = list(generate_jittered_backoff(retries, delay_base, delay_threshold))
    
    assert actual_delays == expected_delays

def test_generate_jittered_backoff_default_values(monkeypatch):
    # Mock random.randint to control the output
    mock_randint = lambda a, b: b
    monkeypatch.setattr(random, 'randint', mock_randint)
    
    retries = 10
    delay_base = 3
    delay_threshold = 60
    
    expected_delays = [
        min(delay_threshold, delay_base * 2 ** retry) for retry in range(retries)
    ]
    
    actual_delays = list(generate_jittered_backoff())
    
    assert actual_delays == expected_delays

def test_generate_jittered_backoff_threshold(monkeypatch):
    # Mock random.randint to control the output
    mock_randint = lambda a, b: b
    monkeypatch.setattr(random, 'randint', mock_randint)
    
    retries = 5
    delay_base = 2
    delay_threshold = 5
    
    expected_delays = [
        min(delay_threshold, delay_base * 2 ** retry) for retry in range(retries)
    ]
    
    actual_delays = list(generate_jittered_backoff(retries, delay_base, delay_threshold))
    
    assert actual_delays == expected_delays
