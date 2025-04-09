# file isort/exceptions.py:122-137
# lines [122, 123, 127, 128, 129, 130, 137]
# branches []

import pytest
from isort.exceptions import AssignmentsFormatMismatch

def test_assignments_format_mismatch():
    code_snippet = "a = 1\nb = 2\nc = 3"
    exception = AssignmentsFormatMismatch(code_snippet)
    
    expected_message = (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        "a = 1\nb = 2\nc = 3\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )
    
    assert str(exception) == expected_message
    assert exception.code == code_snippet
