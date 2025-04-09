import os
import pytest
from tornado.options import OptionParser, Error, define, options

# Define a temporary config file for testing
@pytest.fixture
def temp_config_file(tmp_path):
    config_file = tmp_path / "test_config.py"
    config_file.write_text(
        "port = 80\n"
        "multiple_option = 'value1,value2'\n"
        "invalid_multiple_option = 123\n",
        encoding="utf-8"
    )
    return str(config_file)

# Define options for testing
@pytest.fixture(autouse=True)
def define_options():
    define("port", type=int)
    define("multiple_option", multiple=True)
    define("invalid_multiple_option", multiple=True)
    yield
    options._options.clear()

# Test parsing a config file with a multiple option as a string
def test_parse_config_file_with_multiple_option_as_string(temp_config_file):
    parser = OptionParser()
    parser.parse_config_file(temp_config_file)
    assert options.port == 80
    assert options.multiple_option == ['value1', 'value2']

# Test parsing a config file with an invalid multiple option
def test_parse_config_file_with_invalid_multiple_option(temp_config_file):
    parser = OptionParser()
    with pytest.raises(Error):
        parser.parse_config_file(temp_config_file)
