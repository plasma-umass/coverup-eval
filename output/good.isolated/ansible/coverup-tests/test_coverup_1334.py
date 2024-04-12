# file lib/ansible/module_utils/common/text/converters.py:33-147
# lines [121, 122, 123, 134, 136]
# branches ['116->121']

import pytest
from ansible.module_utils.common.text.converters import to_bytes, _COMPOSED_ERROR_HANDLERS

# Define a test function to cover the missing lines
def test_to_bytes_surrogate_then_replace_error_handler(mocker):
    # Mock the HAS_SURROGATEESCAPE to be False to trigger the fallback
    mocker.patch('ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE', False)

    # Create a string with a surrogate character that will cause UnicodeEncodeError
    surrogate_string = u'This is a test \ud800'

    # Call to_bytes with the surrogate_then_replace error handler
    result = to_bytes(surrogate_string, errors='surrogate_then_replace', encoding='ascii')

    # Assert that the result is a bytes object
    assert isinstance(result, bytes)

    # Assert that the surrogate character is replaced with the unicode replacement character
    assert b'?' in result  # Unicode replacement character in ASCII

def test_to_bytes_nonstring_simplerepr_exception(mocker):
    # Create a class that raises UnicodeError on str() and repr()
    class BadStrRepr:
        def __str__(self):
            raise UnicodeError("Bad __str__")

        def __repr__(self):
            raise UnicodeError("Bad __repr__")

    # Instantiate the class
    bad_obj = BadStrRepr()

    # Call to_bytes with the simplerepr nonstring strategy
    result = to_bytes(bad_obj, nonstring='simplerepr')

    # Assert that the result is an empty bytes object
    assert result == b''

# Run the tests
pytest.main()
