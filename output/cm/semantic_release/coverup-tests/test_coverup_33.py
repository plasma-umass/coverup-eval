# file semantic_release/settings.py:80-94
# lines [80, 87, 89, 90, 92, 93, 94]
# branches []

import os
import pytest
from semantic_release.settings import current_commit_parser, ImproperConfigurationError
from unittest.mock import patch

def test_current_commit_parser_success(mocker):
    # Mock the config to return a valid module and function
    mocker.patch('semantic_release.settings.config.get', return_value='os.path.exists')
    assert current_commit_parser() == os.path.exists

def test_current_commit_parser_import_error(mocker):
    # Mock the config to return a non-existing module
    mocker.patch('semantic_release.settings.config.get', return_value='non.existing.module')
    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()

def test_current_commit_parser_attribute_error(mocker):
    # Mock the config to return a non-existing function in an existing module
    mocker.patch('semantic_release.settings.config.get', return_value='os.non_existing_function')
    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()
