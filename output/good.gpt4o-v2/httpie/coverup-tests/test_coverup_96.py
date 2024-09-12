# file: httpie/config.py:84-97
# asked: {"lines": [85, 86, 87, 88, 89, 90, 91, 92, 94, 95, 96, 97], "branches": [[96, 0], [96, 97]]}
# gained: {"lines": [85, 86, 87, 88, 89, 90, 91, 92, 94, 95, 96, 97], "branches": [[96, 0], [96, 97]]}

import pytest
import json
import errno
from pathlib import Path
from httpie.config import BaseConfigDict, ConfigFileError

class TestBaseConfigDict:
    @pytest.fixture
    def temp_file(self, tmp_path):
        temp_file = tmp_path / "config.json"
        yield temp_file
        if temp_file.exists():
            temp_file.unlink()

    def test_load_valid_json(self, temp_file):
        temp_file.write_text(json.dumps({"key": "value"}))
        config = BaseConfigDict(temp_file)
        config.load()
        assert config["key"] == "value"

    def test_load_invalid_json(self, temp_file):
        temp_file.write_text("{invalid json}")
        config = BaseConfigDict(temp_file)
        with pytest.raises(ConfigFileError, match="invalid baseconfigdict file"):
            config.load()

    def test_load_io_error(self, mocker, temp_file):
        mocker.patch("pathlib.Path.open", side_effect=IOError(errno.EACCES, "Permission denied"))
        config = BaseConfigDict(temp_file)
        with pytest.raises(ConfigFileError, match="cannot read baseconfigdict file"):
            config.load()

    def test_load_file_not_found(self, temp_file):
        config = BaseConfigDict(temp_file)
        config.load()  # Should not raise an exception
