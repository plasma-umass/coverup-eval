# file typesystem/base.py:178-179
# lines [178, 179]
# branches []

import pytest
from typesystem.base import BaseError

def test_base_error_iteration():
    error = BaseError(text='error message')
    error._message_dict = {'field': 'error message'}

    # Verify that the __iter__ method works as expected
    assert list(iter(error)) == ['field']

    # Clean up by deleting the instance
    del error
