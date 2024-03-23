# file thefuck/shells/generic.py:116-122
# lines [116]
# branches []

import pytest
from thefuck.shells import generic

# Assuming the module structure is as follows:
# thefuck/
#   shells/
#     __init__.py
#     generic.py

# Test function to cover put_to_history method
def test_put_to_history(mocker):
    mocker.patch('thefuck.shells.generic.Generic.put_to_history')
    shell = generic.Generic()
    command = 'ls -la'
    shell.put_to_history(command)
    generic.Generic.put_to_history.assert_called_once_with(command)

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])
