# file string_utils/generation.py:88-140
# lines [106, 107, 109, 110, 112, 113, 115, 116, 118, 119, 122, 123, 124, 127, 130, 131, 132, 135, 136, 137, 138, 140]
# branches ['109->110', '109->112', '112->113', '112->115', '115->exit', '115->116', '122->123', '122->127', '137->138', '137->140']

import pytest
from string_utils.generation import roman_range

def test_roman_range_full_coverage(mocker):
    # Mock the roman_encode function to avoid dependency on its implementation
    mocker.patch('string_utils.generation.roman_encode', side_effect=lambda x: str(x))

    # Test the normal forward range
    assert list(roman_range(5)) == ['1', '2', '3', '4', '5']

    # Test the normal backward range
    assert list(roman_range(start=5, stop=1, step=-1)) == ['5', '4', '3', '2', '1']

    # Test the validation of non-integer input for stop
    with pytest.raises(ValueError):
        next(roman_range('5'))

    # Test the validation of non-integer input for start
    with pytest.raises(ValueError):
        next(roman_range(5, start='1'))

    # Test the validation of non-integer input for step
    with pytest.raises(ValueError):
        next(roman_range(5, step='1'))

    # Test the validation of out-of-range input for stop
    with pytest.raises(ValueError):
        next(roman_range(0))

    # Test the validation of out-of-range input for start
    with pytest.raises(ValueError):
        next(roman_range(5, start=0))

    # Test the validation of out-of-range input for stop
    with pytest.raises(ValueError):
        next(roman_range(4000))

    # Test the validation of negative step
    with pytest.raises(ValueError):
        next(roman_range(5, step=-4000))

    # Test the OverflowError for invalid start/stop/step configuration
    with pytest.raises(OverflowError):
        next(roman_range(start=1, stop=5, step=-1))

    with pytest.raises(OverflowError):
        next(roman_range(start=5, stop=1, step=1))
