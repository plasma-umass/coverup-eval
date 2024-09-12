# file: pytutils/log.py:81-97
# asked: {"lines": [81, 89, 91, 92, 93, 94, 95, 96, 97], "branches": []}
# gained: {"lines": [81, 89, 91, 92, 93, 94, 95, 96, 97], "branches": []}

import pytest
import logging
import os
from unittest import mock
from pytutils.log import configure, DEFAULT_CONFIG

def test_configure_with_default_config(monkeypatch):
    # Mock the get_config function to return the default config
    from pytutils.log import get_config
    monkeypatch.setattr('pytutils.log.get_config', lambda config, env_var, default: default)

    # Capture the logs
    log = logging.getLogger(__name__)
    with mock.patch('logging.config.dictConfig') as mock_dictConfig:
        configure()
        mock_dictConfig.assert_called_once_with(DEFAULT_CONFIG)

def test_configure_with_env_var(monkeypatch):
    # Set an environment variable for logging config
    env_config = '{"version": 1, "disable_existing_loggers": false}'
    monkeypatch.setenv('LOGGING', env_config)

    # Capture the logs
    log = logging.getLogger(__name__)
    with mock.patch('logging.config.dictConfig') as mock_dictConfig:
        configure()
        mock_dictConfig.assert_called_once_with({"version": 1, "disable_existing_loggers": False})

def test_configure_with_invalid_config(monkeypatch):
    # Mock the get_config function to return an invalid config
    from pytutils.log import get_config
    monkeypatch.setattr('pytutils.log.get_config', lambda config, env_var, default: {"invalid": "config"})

    # Capture the logs
    log = logging.getLogger(__name__)
    with mock.patch('logging.config.dictConfig', side_effect=TypeError):
        with mock.patch('logging.basicConfig', side_effect=ValueError) as mock_basicConfig:
            with pytest.raises(ValueError):
                configure()
            mock_basicConfig.assert_called_once_with(invalid="config")

def test_configure_with_type_error(monkeypatch):
    # Mock the get_config function to return a config that will cause a TypeError
    from pytutils.log import get_config
    monkeypatch.setattr('pytutils.log.get_config', lambda config, env_var, default: {"version": 1, "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "simple"}}})

    # Capture the logs
    log = logging.getLogger(__name__)
    with mock.patch('logging.config.dictConfig', side_effect=TypeError):
        with mock.patch('logging.basicConfig') as mock_basicConfig:
            configure()
            mock_basicConfig.assert_called_once_with(version=1, handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}})
