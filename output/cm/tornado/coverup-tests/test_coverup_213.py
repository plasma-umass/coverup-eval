# file tornado/options.py:217-302
# lines [264, 265, 266, 277, 286, 288]
# branches ['263->264', '273->277', '283->286', '287->288']

import pytest
from tornado.options import OptionParser, Error

class TestOptionParser:
    def test_define_option_already_defined(self, mocker):
        parser = OptionParser()
        parser.define("foo", default=42)
        with pytest.raises(Error):
            parser.define("foo", default=23)

    def test_define_option_with_group(self, mocker):
        parser = OptionParser()
        parser.define("bar", group="Test Group")
        assert parser._options["bar"].group_name == "Test Group"

    def test_define_option_without_type_and_default(self, mocker):
        parser = OptionParser()
        parser.define("baz")
        assert parser._options["baz"].type == str

    def test_define_option_without_type_with_multiple(self, mocker):
        parser = OptionParser()
        parser.define("qux", multiple=True)
        assert parser._options["qux"].type == str

    def test_define_option_with_callback(self, mocker):
        callback_mock = mocker.Mock()
        parser = OptionParser()
        parser.define("quux", callback=callback_mock)
        assert parser._options["quux"].callback == callback_mock
