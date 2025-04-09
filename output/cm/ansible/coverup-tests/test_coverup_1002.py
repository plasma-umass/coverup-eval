# file lib/ansible/vars/fact_cache.py:57-59
# lines [57, 59]
# branches []

import pytest
from ansible.vars.fact_cache import FactCache

# Mocking the FactCache plugin
class MockPlugin:
    def __init__(self):
        self.flush_called = False

    def flush(self):
        self.flush_called = True

@pytest.fixture
def fact_cache(mocker):
    # Setup the FactCache with a mock plugin
    plugin = MockPlugin()
    fact_cache = FactCache()
    mocker.patch.object(fact_cache, '_plugin', plugin)
    return fact_cache, plugin

def test_fact_cache_flush(fact_cache):
    fact_cache_instance, mock_plugin = fact_cache
    # Ensure flush has not been called yet
    assert not mock_plugin.flush_called
    # Call the flush method
    fact_cache_instance.flush()
    # Verify that the flush method was called on the plugin
    assert mock_plugin.flush_called
