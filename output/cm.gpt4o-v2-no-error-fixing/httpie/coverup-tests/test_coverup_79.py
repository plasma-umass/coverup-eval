# file: httpie/context.py:104-114
# asked: {"lines": [], "branches": [[107, 114]]}
# gained: {"lines": [], "branches": [[107, 114]]}

import pytest
from httpie.context import Environment
from httpie.config import Config, ConfigFileError

def test_environment_config_load(monkeypatch):
    env = Environment()
    
    # Ensure _config is None to trigger the branch
    env._config = None
    
    # Mock the Config class to control its behavior
    class MockConfig(Config):
        def __init__(self, directory):
            super().__init__(directory)
            self._is_new = False
        
        def is_new(self):
            return self._is_new
        
        def load(self):
            raise ConfigFileError("Mocked config load error")
    
    monkeypatch.setattr('httpie.context.Config', MockConfig)
    
    # Mock the log_error method to verify it gets called
    def mock_log_error(msg, level='warning'):
        assert str(msg) == "Mocked config load error"
        assert level == 'warning'
    
    monkeypatch.setattr(env, 'log_error', mock_log_error)
    
    # Access the config property to trigger the code path
    config = env.config
    
    # Verify that the config is an instance of MockConfig
    assert isinstance(config, MockConfig)
    assert env._config is config

    # Access the config property again to ensure the cached config is used
    config_cached = env.config
    assert config_cached is config
