# file: pytutils/files.py:55-68
# asked: {"lines": [], "branches": [[62, 64], [64, 67]]}
# gained: {"lines": [], "branches": [[62, 64], [64, 67]]}

import os
import pytest
import sys
from unittest import mock
from pytutils.files import burp

def test_burp_expanduser_and_expandvars(tmpdir):
    # Create a temporary directory and file
    temp_dir = tmpdir.mkdir("sub")
    temp_file = temp_dir.join("testfile.txt")
    
    # Mock environment variable
    with mock.patch.dict(os.environ, {"TESTVAR": "testvalue"}):
        # Use a filename with ~ and $TESTVAR to trigger expanduser and expandvars
        filename = os.path.join(str(temp_dir), "~$TESTVAR.txt")
        expanded_filename = os.path.expanduser(os.path.expandvars(filename))
        
        # Call the burp function
        burp(filename, "test content", expanduser=True, expandvars=True)
        
        # Verify the file was created with the expanded filename
        assert os.path.isfile(expanded_filename)
        
        # Verify the content of the file
        with open(expanded_filename, "r") as f:
            assert f.read() == "test content"
        
        # Clean up
        os.remove(expanded_filename)

def test_burp_no_expanduser_and_expandvars(tmpdir):
    # Create a temporary directory and file
    temp_dir = tmpdir.mkdir("sub")
    temp_file = temp_dir.join("testfile.txt")
    
    # Mock environment variable
    with mock.patch.dict(os.environ, {"TESTVAR": "testvalue"}):
        # Use a filename with ~ and $TESTVAR to trigger expanduser and expandvars
        filename = os.path.join(str(temp_dir), "~$TESTVAR.txt")
        
        # Call the burp function without expanding user and vars
        burp(filename, "test content", expanduser=False, expandvars=False)
        
        # Verify the file was created with the original filename
        assert os.path.isfile(filename)
        
        # Verify the content of the file
        with open(filename, "r") as f:
            assert f.read() == "test content"
        
        # Clean up
        os.remove(filename)
