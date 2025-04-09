# file pymonet/task.py:1-6
# lines [1, 2]
# branches []

import pytest
from pymonet.task import Task

def test_task_class_docstring():
    # Verify that the Task class has the correct docstring
    expected_docstring = (
        "Task are data-type for handle execution of functions (in lazy way)\n"
        "    transform results of this function and handle errors."
    )
    assert Task.__doc__.strip() == expected_docstring
