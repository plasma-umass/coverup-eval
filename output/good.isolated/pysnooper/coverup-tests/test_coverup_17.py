# file pysnooper/utils.py:50-56
# lines [50, 51, 52, 53, 54, 55, 56]
# branches ['51->52', '51->56', '52->53', '52->54', '54->51', '54->55']

import pytest
from pysnooper.utils import get_repr_function

class CustomType:
    pass

def test_get_repr_function_with_custom_repr_conditions():
    item = CustomType()
    custom_repr = [
        (CustomType, lambda x: 'CustomTypeRepresentation'),
        (int, lambda x: 'intRepresentation')
    ]
    
    # Test with a type condition
    repr_function = get_repr_function(item, custom_repr)
    assert repr_function(item) == 'CustomTypeRepresentation'
    
    # Test with a lambda condition
    custom_repr_with_lambda = [
        (lambda x: isinstance(x, CustomType), lambda x: 'CustomTypeLambdaRepresentation'),
        (lambda x: isinstance(x, int), lambda x: 'intLambdaRepresentation')
    ]
    repr_function_with_lambda = get_repr_function(item, custom_repr_with_lambda)
    assert repr_function_with_lambda(item) == 'CustomTypeLambdaRepresentation'
    
    # Test with no matching condition
    item_int = 42
    custom_repr_no_match = [
        (str, lambda x: 'strRepresentation'),
        (list, lambda x: 'listRepresentation')
    ]
    repr_function_no_match = get_repr_function(item_int, custom_repr_no_match)
    assert repr_function_no_match(item_int) == repr(item_int)
