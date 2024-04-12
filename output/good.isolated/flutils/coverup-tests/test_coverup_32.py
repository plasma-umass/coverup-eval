# file flutils/setuputils/cfg.py:82-105
# lines [82, 86, 87, 88, 89, 90, 91, 93, 94, 95, 97, 99, 100, 101, 103, 105]
# branches ['99->100', '99->105']

import pytest
from configparser import ConfigParser, NoSectionError, NoOptionError
from flutils.setuputils.cfg import _get_name

def test_get_name_missing_metadata_section(tmp_path, mocker):
    setup_cfg_path = tmp_path / "setup.cfg"
    setup_cfg_path.write_text("")

    parser = ConfigParser()
    parser.read(str(setup_cfg_path))

    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, str(setup_cfg_path))
    assert "is missing the 'metadata' section" in str(excinfo.value)

def test_get_name_missing_name_option(tmp_path, mocker):
    setup_cfg_path = tmp_path / "setup.cfg"
    setup_cfg_path.write_text("[metadata]\n")

    parser = ConfigParser()
    parser.read(str(setup_cfg_path))

    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, str(setup_cfg_path))
    assert "is missing the 'name' option" in str(excinfo.value)

def test_get_name_empty_name_option(tmp_path, mocker):
    setup_cfg_path = tmp_path / "setup.cfg"
    setup_cfg_path.write_text("[metadata]\nname=\n")

    parser = ConfigParser()
    parser.read(str(setup_cfg_path))

    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, str(setup_cfg_path))
    assert "option is not set" in str(excinfo.value)

def test_get_name_success(tmp_path, mocker):
    setup_cfg_path = tmp_path / "setup.cfg"
    setup_cfg_path.write_text("[metadata]\nname=example\n")

    parser = ConfigParser()
    parser.read(str(setup_cfg_path))

    name = _get_name(parser, str(setup_cfg_path))
    assert name == "example"
