# file tornado/escape.py:67-75
# lines [67, 75]
# branches []

import pytest
import json
from tornado.escape import json_encode

def test_json_encode():
    # Test encoding a simple dictionary
    data = {"key": "value"}
    encoded = json_encode(data)
    assert encoded == '{"key": "value"}'
    
    # Test encoding a string with a forward slash
    data = {"key": "</script>"}
    encoded = json_encode(data)
    assert encoded == '{"key": "<\\/script>"}'
    
    # Test encoding a list with a forward slash
    data = ["</script>"]
    encoded = json_encode(data)
    assert encoded == '["<\\/script>"]'
    
    # Test encoding a nested structure with a forward slash
    data = {"key": ["</script>"]}
    encoded = json_encode(data)
    assert encoded == '{"key": ["<\\/script>"]}'
    
    # Test encoding a string without a forward slash
    data = {"key": "no_slash"}
    encoded = json_encode(data)
    assert encoded == '{"key": "no_slash"}'
    
    # Test encoding a number
    data = {"key": 123}
    encoded = json_encode(data)
    assert encoded == '{"key": 123}'
    
    # Test encoding a boolean
    data = {"key": True}
    encoded = json_encode(data)
    assert encoded == '{"key": true}'
    
    # Test encoding None
    data = {"key": None}
    encoded = json_encode(data)
    assert encoded == '{"key": null}'
