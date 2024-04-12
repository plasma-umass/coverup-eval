# file pytutils/urls.py:9-31
# lines [9, 23, 25, 26, 28, 30, 31]
# branches []

import pytest
from urllib import parse
from pytutils.urls import update_query_params

def test_update_query_params():
    original_url = 'http://example.com?foo=bar&biz=baz'
    new_params = {'foo': 'stuff', 'new_param': 'new_value'}
    
    # Call the function with new parameters
    updated_url = update_query_params(original_url, new_params)
    
    # Parse the updated URL to verify the query parameters
    scheme, netloc, path, query_string, fragment = parse.urlsplit(updated_url)
    query_params = parse.parse_qs(query_string)
    
    # Assertions to check if the parameters are updated correctly
    assert query_params['foo'] == ['stuff']
    assert query_params['new_param'] == ['new_value']
    assert query_params['biz'] == ['baz']
    
    # Check if the rest of the URL is unchanged
    assert scheme == 'http'
    assert netloc == 'example.com'
    assert path == ''
    assert fragment == ''

def test_update_query_params_with_doseq_false():
    original_url = 'http://example.com?foo=bar&foo=baz'
    new_params = {'foo': ['new1', 'new2']}
    
    # Call the function with new parameters and doseq=False
    updated_url = update_query_params(original_url, new_params, doseq=False)
    
    # Parse the updated URL to verify the query parameters
    scheme, netloc, path, query_string, fragment = parse.urlsplit(updated_url)
    query_params = parse.parse_qsl(query_string)
    
    # Assertions to check if the parameters are updated correctly
    # With doseq=False, the list should be converted to a single value with the first item
    # Since doseq=False, the list is converted to a single string representation of the list
    assert ('foo', "['new1', 'new2']") in query_params
    
    # Check if the rest of the URL is unchanged
    assert scheme == 'http'
    assert netloc == 'example.com'
    assert path == ''
    assert fragment == ''
