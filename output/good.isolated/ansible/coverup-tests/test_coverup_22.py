# file lib/ansible/plugins/filter/core.py:572-662
# lines [572, 573, 575, 578, 579, 582, 585, 586, 587, 590, 591, 592, 593, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 609, 612, 613, 616, 619, 623, 625, 627, 629, 630, 633, 634, 635, 636, 639, 642, 643, 646, 649, 652, 655, 656, 657, 658, 659, 660, 661]
# branches []

import pytest
from ansible.plugins.filter.core import FilterModule
from ansible.errors import AnsibleFilterError
import json
import os
import tempfile
import shutil

# Define a fixture for creating a temporary directory that will be cleaned up after the test
@pytest.fixture
def temp_dir():
    new_dir = tempfile.mkdtemp()
    yield new_dir
    shutil.rmtree(new_dir)

# Test function to cover 'expanduser' filter
def test_expanduser_filter(temp_dir, mocker):
    # Mock the os.path.expanduser function to return the temp_dir regardless of input
    mocker.patch('os.path.expanduser', return_value=temp_dir)
    
    # Instantiate the FilterModule
    filters = FilterModule().filters()
    
    # Call the 'expanduser' filter with any input, since it's mocked to return temp_dir
    result = filters['expanduser']('~/fakepath')
    
    # Assert that the result is equal to the temp_dir path
    assert result == temp_dir

# Test function to cover 'expandvars' filter
def test_expandvars_filter(mocker):
    # Mock the os.path.expandvars function to return a specific string
    mocker.patch('os.path.expandvars', return_value='expanded_var')
    
    # Instantiate the FilterModule
    filters = FilterModule().filters()
    
    # Call the 'expandvars' filter with any input, since it's mocked to return 'expanded_var'
    result = filters['expandvars']('$VAR')
    
    # Assert that the result is the mocked string
    assert result == 'expanded_var'

# Test function to cover 'realpath' filter
def test_realpath_filter(temp_dir, mocker):
    # Mock the os.path.realpath function to return the temp_dir regardless of input
    mocker.patch('os.path.realpath', return_value=temp_dir)
    
    # Instantiate the FilterModule
    filters = FilterModule().filters()
    
    # Call the 'realpath' filter with any input, since it's mocked to return temp_dir
    result = filters['realpath']('/fakepath')
    
    # Assert that the result is equal to the temp_dir path
    assert result == temp_dir

# Test function to cover 'relpath' filter
def test_relpath_filter(mocker):
    # Mock the os.path.relpath function to return a specific string
    mocker.patch('os.path.relpath', return_value='relative/path')
    
    # Instantiate the FilterModule
    filters = FilterModule().filters()
    
    # Call the 'relpath' filter with any input, since it's mocked to return 'relative/path'
    result = filters['relpath']('/fakepath', '/basepath')
    
    # Assert that the result is the mocked string
    assert result == 'relative/path'

# Test function to cover 'splitext' filter
def test_splitext_filter(mocker):
    # Mock the os.path.splitext function to return a tuple
    mocker.patch('os.path.splitext', return_value=('filename', '.ext'))
    
    # Instantiate the FilterModule
    filters = FilterModule().filters()
    
    # Call the 'splitext' filter with any input, since it's mocked to return the tuple
    result = filters['splitext']('filename.ext')
    
    # Assert that the result is the mocked tuple
    assert result == ('filename', '.ext')
