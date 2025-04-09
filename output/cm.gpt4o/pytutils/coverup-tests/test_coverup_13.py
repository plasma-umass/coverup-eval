# file pytutils/log.py:81-97
# lines [81, 89, 91, 92, 93, 94, 95, 96, 97]
# branches []

import pytest
import logging
import logging.config
from unittest import mock
from pytutils.log import configure

def test_configure_with_dictConfig(mocker):
    mock_dictConfig = mocker.patch('logging.config.dictConfig')
    mock_basicConfig = mocker.patch('logging.basicConfig')

    config = {
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

    configure(config=config)
    mock_dictConfig.assert_called_once_with(config)
    mock_basicConfig.assert_not_called()

def test_configure_with_basicConfig(mocker):
    mock_dictConfig = mocker.patch('logging.config.dictConfig', side_effect=TypeError)
    mock_basicConfig = mocker.patch('logging.basicConfig')

    config = {
        'level': 'DEBUG',
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    }

    configure(config=config)
    mock_dictConfig.assert_called_once_with(config)
    mock_basicConfig.assert_called_once_with(**config)

def test_configure_with_exception(mocker):
    mock_dictConfig = mocker.patch('logging.config.dictConfig', side_effect=TypeError)
    mock_basicConfig = mocker.patch('logging.basicConfig', side_effect=ValueError)

    config = {
        'level': 'DEBUG',
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    }

    with pytest.raises(ValueError):
        configure(config=config)
    mock_dictConfig.assert_called_once_with(config)
    mock_basicConfig.assert_called_once_with(**config)
