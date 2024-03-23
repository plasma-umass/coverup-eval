# file py_backwards/utils/snippet.py:62-70
# lines []
# branches ['65->68']

import pytest
import ast
from py_backwards.utils.snippet import VariablesReplacer

def test_variables_replacer_replaces_variable_with_string():
    # Setup the VariablesReplacer with a dictionary containing a string replacement
    replacer = VariablesReplacer(variables={'old_name': 'new_name'})

    # Create a simple module string that needs to be replaced
    module_str = 'old_name.submodule'

    # Replace the variable in the module string
    new_module_str = replacer._replace_module(module_str)

    # Assert that the replacement was successful
    assert new_module_str == 'new_name.submodule'

def test_variables_replacer_does_not_replace_non_string():
    # Setup the VariablesReplacer with a dictionary containing a non-string replacement
    replacer = VariablesReplacer(variables={'old_name': 123})

    # Create a simple module string that should not be replaced
    module_str = 'old_name.submodule'

    # Replace the variable in the module string
    new_module_str = replacer._replace_module(module_str)

    # Assert that the replacement was not done
    assert new_module_str == 'old_name.submodule'
