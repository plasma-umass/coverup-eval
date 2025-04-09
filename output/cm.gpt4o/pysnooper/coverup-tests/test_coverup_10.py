# file pysnooper/tracer.py:151-200
# lines [151, 152]
# branches []

import pytest
import pysnooper
import os
import threading

def test_tracer_with_file_output(tmp_path):
    log_file = tmp_path / "log.txt"
    
    @pysnooper.snoop(str(log_file))
    def sample_function():
        x = 1
        y = 2
        return x + y
    
    result = sample_function()
    assert result == 3
    
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    assert "sample_function" in log_content
    assert "x = 1" in log_content
    assert "y = 2" in log_content
    assert "return x + y" in log_content

def test_tracer_with_watch():
    @pysnooper.snoop(watch=('x', 'y'))
    def sample_function():
        x = 1
        y = 2
        return x + y
    
    result = sample_function()
    assert result == 3

def test_tracer_with_watch_explode():
    @pysnooper.snoop(watch_explode=('x',))
    def sample_function():
        x = {'a': 1, 'b': 2}
        return x['a'] + x['b']
    
    result = sample_function()
    assert result == 3

def test_tracer_with_depth():
    @pysnooper.snoop(depth=2)
    def outer_function():
        def inner_function():
            x = 1
            y = 2
            return x + y
        return inner_function()
    
    result = outer_function()
    assert result == 3

def test_tracer_with_prefix():
    @pysnooper.snoop(prefix='ZZZ ')
    def sample_function():
        x = 1
        y = 2
        return x + y
    
    result = sample_function()
    assert result == 3

def test_tracer_with_thread_info():
    @pysnooper.snoop(thread_info=True)
    def sample_function():
        x = 1
        y = 2
        return x + y
    
    result = sample_function()
    assert result == 3

def test_tracer_with_custom_repr():
    def custom_repr(value):
        return f"<CustomRepr: {value}>"
    
    @pysnooper.snoop(custom_repr=((int, custom_repr),))
    def sample_function():
        x = 1
        y = 2
        return x + y
    
    result = sample_function()
    assert result == 3

def test_tracer_with_max_variable_length():
    @pysnooper.snoop(max_variable_length=5)
    def sample_function():
        x = "This is a long string"
        return x
    
    result = sample_function()
    assert result == "This is a long string"

def test_tracer_with_no_truncate():
    @pysnooper.snoop(max_variable_length=None)
    def sample_function():
        x = "This is a long string"
        return x
    
    result = sample_function()
    assert result == "This is a long string"
