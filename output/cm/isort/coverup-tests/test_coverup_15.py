# file isort/exceptions.py:122-137
# lines [122, 123, 127, 128, 129, 130, 137]
# branches []

import pytest

from isort.exceptions import AssignmentsFormatMismatch

def test_assignments_format_mismatch():
    code_sample = "x = 1\ny=2"
    exception = AssignmentsFormatMismatch(code_sample)
    
    assert exception.code == code_sample
    assert "isort was told to sort a section of assignments" in str(exception)
    assert "Does not match isort's strict single line formatting requirement" in str(exception)
    assert "{variable_name} = {value}" in str(exception)
