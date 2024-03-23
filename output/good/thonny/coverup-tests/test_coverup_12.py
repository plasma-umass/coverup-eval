# file thonny/jedi_utils.py:123-131
# lines [123, 124, 126, 127, 128, 130, 131]
# branches ['126->127', '126->130']

import pytest
from thonny.jedi_utils import get_definitions
from unittest.mock import patch

# Assuming the existence of a function _using_older_jedi in thonny.jedi_utils
# which is not shown in the provided code snippet.

@pytest.fixture
def source_code():
    return "import math\nresult = math.sqrt(4)"

@pytest.fixture
def temp_file(tmp_path, source_code):
    file = tmp_path / "temp.py"
    file.write_text(source_code)
    return str(file)

def test_get_definitions_with_older_jedi(mocker, source_code, temp_file):
    # Mocking the _using_older_jedi function to return True
    mocker.patch('thonny.jedi_utils._using_older_jedi', return_value=True)
    # Mocking jedi.Script to verify the correct call with older jedi version
    with patch('jedi.Script') as mock_script:
        mock_script.return_value.goto_definitions.return_value = ['definition']
        definitions = get_definitions(source_code, 2, 8, temp_file)
        mock_script.assert_called_once_with(source_code, 2, 8, temp_file)
        assert definitions == ['definition']

def test_get_definitions_with_newer_jedi(mocker, source_code, temp_file):
    # Mocking the _using_older_jedi function to return False
    mocker.patch('thonny.jedi_utils._using_older_jedi', return_value=False)
    # Mocking jedi.Script to verify the correct call with newer jedi version
    with patch('jedi.Script') as mock_script:
        mock_script.return_value.infer.return_value = ['inferred']
        definitions = get_definitions(source_code, 2, 8, temp_file)
        mock_script.assert_called_once_with(code=source_code, path=temp_file)
        assert definitions == ['inferred']
