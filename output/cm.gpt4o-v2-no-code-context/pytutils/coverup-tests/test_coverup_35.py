# file: pytutils/log.py:81-97
# asked: {"lines": [81, 89, 91, 92, 93, 94, 95, 96, 97], "branches": []}
# gained: {"lines": [81, 89, 91, 92, 93, 94, 95, 96, 97], "branches": []}

import pytest
import logging
import logging.config
from unittest import mock
from pytutils.log import configure, DEFAULT_CONFIG

def test_configure_with_default_config(monkeypatch):
    log = logging.getLogger(__name__)
    monkeypatch.setattr('pytutils.log.get_config', lambda config, env_var, default: default)
    
    configure()
    
    assert log.level == logging.NOTSET  # Default level for a new logger

def test_configure_with_custom_config(monkeypatch):
    custom_config = {
        'version': 1,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
    monkeypatch.setattr('pytutils.log.get_config', lambda config, env_var, default: custom_config)
    
    configure()
    
    log = logging.getLogger()
    assert log.level == logging.DEBUG

def test_configure_with_type_error(monkeypatch):
    def mock_get_config(config, env_var, default):
        return {'invalid': 'config'}
    
    monkeypatch.setattr('pytutils.log.get_config', mock_get_config)
    
    with mock.patch('logging.config.dictConfig', side_effect=TypeError('Test TypeError')):
        with mock.patch('logging.basicConfig') as mock_basicConfig:
            configure()
            mock_basicConfig.assert_called_once_with(**{'invalid': 'config'})

def test_configure_with_exception(monkeypatch):
    def mock_get_config(config, env_var, default):
        return {'invalid': 'config'}
    
    monkeypatch.setattr('pytutils.log.get_config', mock_get_config)
    
    with mock.patch('logging.config.dictConfig', side_effect=TypeError('Test TypeError')):
        with mock.patch('logging.basicConfig', side_effect=Exception('Test Exception')) as mock_basicConfig:
            with pytest.raises(Exception, match='Test Exception'):
                configure()
            mock_basicConfig.assert_called_once_with(**{'invalid': 'config'})
