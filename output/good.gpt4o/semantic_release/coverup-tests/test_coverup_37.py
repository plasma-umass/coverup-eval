# file semantic_release/settings.py:80-94
# lines [80, 87, 89, 90, 92, 93, 94]
# branches []

import pytest
import importlib
import os
from unittest.mock import patch, Mock
from semantic_release.settings import current_commit_parser, ImproperConfigurationError

def test_current_commit_parser_success(mocker):
    # Mock the config.get to return a valid parser path
    mocker.patch('semantic_release.settings.config.get', return_value='os.path.basename')
    
    # Call the function and assert the correct parser is returned
    parser = current_commit_parser()
    assert parser == os.path.basename

def test_current_commit_parser_import_error(mocker):
    # Mock the config.get to return an invalid module path
    mocker.patch('semantic_release.settings.config.get', return_value='nonexistent.module.parser')
    
    # Call the function and assert that ImproperConfigurationError is raised
    with pytest.raises(ImproperConfigurationError, match='Unable to import parser'):
        current_commit_parser()

def test_current_commit_parser_attribute_error(mocker):
    # Mock the config.get to return a valid module but invalid attribute
    mocker.patch('semantic_release.settings.config.get', return_value='os.nonexistent_parser')
    
    # Call the function and assert that ImproperConfigurationError is raised
    with pytest.raises(ImproperConfigurationError, match='Unable to import parser'):
        current_commit_parser()
