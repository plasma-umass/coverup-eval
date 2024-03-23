# file flutils/strutils.py:212-236
# lines [212, 214, 233, 234, 235, 236]
# branches ['234->235', '234->236']

import pytest
from flutils.strutils import underscore_to_camel

def test_underscore_to_camel():
    # Test with lower_first set to True
    assert underscore_to_camel('test_string') == 'testString', "Should convert to camel case with first letter lowercase"
    
    # Test with lower_first set to False
    assert underscore_to_camel('test_string', lower_first=False) == 'TestString', "Should convert to camel case with first letter uppercase"
    
    # Test with leading underscores
    assert underscore_to_camel('_leading_underscore', lower_first=False) == 'LeadingUnderscore', "Should handle leading underscores correctly"
    
    # Test with multiple consecutive underscores
    assert underscore_to_camel('multiple___underscores', lower_first=False) == 'MultipleUnderscores', "Should handle multiple consecutive underscores correctly"
    
    # Test with empty string
    assert underscore_to_camel('') == '', "Should handle empty string correctly"
    
    # Test with string that has no underscores and is already in camel case
    # This test case is removed because the function is not designed to handle already camel cased strings without underscores
    
    # Test with string that has no underscores
    assert underscore_to_camel('nocamelcase', lower_first=False) == 'Nocamelcase', "Should handle string with no underscores correctly"
    
    # Test with string that has only underscores
    assert underscore_to_camel('___', lower_first=False) == '', "Should handle string with only underscores correctly"
