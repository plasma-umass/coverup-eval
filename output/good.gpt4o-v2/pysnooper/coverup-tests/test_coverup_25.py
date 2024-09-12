# file: pysnooper/tracer.py:111-133
# asked: {"lines": [114, 121, 123, 126, 127, 129, 131, 132], "branches": [[113, 114], [124, 126], [126, 127], [126, 129]]}
# gained: {"lines": [114, 121, 123, 126, 127, 129, 131, 132], "branches": [[113, 114], [124, 126], [126, 127], [126, 129]]}

import pytest
from pysnooper.tracer import get_write_function
from pysnooper import utils
import sys

def test_overwrite_true_with_non_path():
    with pytest.raises(Exception, match='`overwrite=True` can only be used when writing content to file.'):
        get_write_function(output=sys.stdout, overwrite=True)

def test_write_function_with_none_output(monkeypatch):
    output = None
    write_function = get_write_function(output, overwrite=False)
    
    class MockStderr:
        def __init__(self):
            self.content = ""
        
        def write(self, s):
            self.content += s
    
    mock_stderr = MockStderr()
    monkeypatch.setattr(sys, 'stderr', mock_stderr)
    
    write_function("test")
    assert mock_stderr.content == "test"

def test_write_function_with_none_output_unicode_error(monkeypatch):
    output = None
    write_function = get_write_function(output, overwrite=False)
    
    class MockStderr:
        def __init__(self):
            self.content = ""
        
        def write(self, s):
            if s == "test":
                raise UnicodeEncodeError("mock", "mock", 0, 1, "mock")
            self.content += s
    
    mock_stderr = MockStderr()
    monkeypatch.setattr(sys, 'stderr', mock_stderr)
    monkeypatch.setattr(utils, 'shitcode', lambda s: "shitcode")
    
    write_function("test")
    assert mock_stderr.content == "shitcode"

def test_write_function_with_callable_output():
    output = lambda s: s
    write_function = get_write_function(output, overwrite=False)
    assert write_function("test") == "test"

def test_write_function_with_writable_stream():
    class MockWritableStream:
        def __init__(self):
            self.content = ""
        
        def write(self, s):
            self.content += s
    
    output = MockWritableStream()
    write_function = get_write_function(output, overwrite=False)
    write_function("test")
    assert output.content == "test"
