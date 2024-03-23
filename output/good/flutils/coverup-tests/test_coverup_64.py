# file flutils/namedtupleutils.py:141-177
# lines [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177]
# branches ['146->154', '154->155', '154->171', '156->157', '156->169', '159->160', '159->163', '163->165', '163->169', '172->173', '172->175', '175->176', '175->177']

import pytest
from collections import namedtuple
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_with_namedtuple_input(mocker):
    # Create a namedtuple type and instance
    MockNamedTuple = namedtuple('MockNamedTuple', 'field1 field2')
    mock_namedtuple_instance = MockNamedTuple(field1='value1', field2='value2')

    # Mock the _to_namedtuple function to just return the value it's given
    # This is to prevent recursion and to check that it's called correctly
    mock_to_namedtuple = mocker.patch('flutils.namedtupleutils._to_namedtuple', side_effect=lambda x, _started=False: x)

    # Call the function with the namedtuple instance
    result = _to_namedtuple(mock_namedtuple_instance)

    # Check that the result is a new namedtuple with the same values
    assert isinstance(result, tuple)  # The result is a generic tuple, not the specific MockNamedTuple
    assert result == mock_namedtuple_instance  # The values should be the same as the original

    # Check that _to_namedtuple was called for each field of the namedtuple
    assert mock_to_namedtuple.call_count == 2
    mock_to_namedtuple.assert_any_call('value1', _started=True)
    mock_to_namedtuple.assert_any_call('value2', _started=True)

    # Clean up the patch
    mocker.stopall()
