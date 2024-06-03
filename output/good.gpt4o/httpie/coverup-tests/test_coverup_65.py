# file httpie/output/streams.py:17-18
# lines [17, 18]
# branches []

import pytest
from httpie.output.streams import DataSuppressedError

def test_data_suppressed_error():
    # Test instantiation of the DataSuppressedError
    error = DataSuppressedError()
    assert isinstance(error, DataSuppressedError)
    assert error.message is None

    # Test raising the DataSuppressedError
    with pytest.raises(DataSuppressedError) as exc_info:
        raise DataSuppressedError()
    assert exc_info.value.message is None
