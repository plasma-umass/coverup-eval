# file lib/ansible/module_utils/common/text/converters.py:33-147
# lines [33, 97, 98, 102, 103, 104, 105, 106, 107, 109, 111, 112, 114, 115, 116, 121, 122, 123, 124, 128, 129, 130, 131, 132, 133, 134, 136, 137, 138, 139, 141, 142, 143, 145, 147]
# branches ['97->98', '97->102', '103->104', '103->111', '104->105', '104->106', '106->107', '106->109', '111->112', '111->128', '116->121', '116->124', '128->129', '128->137', '137->138', '137->139', '139->141', '139->142', '142->143', '142->145']

import pytest
from ansible.module_utils.common.text.converters import to_bytes, binary_type, text_type

# Define a test function to cover the missing branches
def test_to_bytes_surrogate_then_replace_error_handler(mocker):
    # Mock the HAS_SURROGATEESCAPE to be False to test the fallback
    mocker.patch('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)

    # Create a string with a surrogate character that will cause UnicodeEncodeError
    surrogate_string = u'This is a test \ud800'

    # Test the 'surrogate_then_replace' error handler
    result = to_bytes(surrogate_string, errors='surrogate_then_replace')
    assert isinstance(result, bytes)
    assert b'This is a test ' in result  # The surrogate character should be replaced

    # Test the 'surrogate_or_strict' error handler
    with pytest.raises(UnicodeEncodeError):
        to_bytes(surrogate_string, errors='surrogate_or_strict')

    # Test the 'surrogate_or_replace' error handler
    result = to_bytes(surrogate_string, errors='surrogate_or_replace')
    assert isinstance(result, bytes)
    assert b'This is a test ' in result  # The surrogate character should be replaced

    # Test the 'strict' nonstring parameter
    with pytest.raises(TypeError):
        to_bytes(object(), nonstring='strict')

    # Test the 'empty' nonstring parameter
    result = to_bytes(object(), nonstring='empty')
    assert result == b''

    # Test the 'passthru' nonstring parameter
    obj = object()
    result = to_bytes(obj, nonstring='passthru')
    assert result is obj

    # Test the 'simplerepr' nonstring parameter with an object that raises UnicodeError on str()
    class TestObject:
        def __str__(self):
            raise UnicodeError

        def __repr__(self):
            return 'TestObjectRepresentation'

    test_obj = TestObject()
    result = to_bytes(test_obj, nonstring='simplerepr')
    assert b'TestObjectRepresentation' in result

    # Test invalid nonstring parameter
    with pytest.raises(TypeError):
        to_bytes(object(), nonstring='invalid')
