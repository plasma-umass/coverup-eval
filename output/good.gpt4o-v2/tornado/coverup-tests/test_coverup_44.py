# file: tornado/options.py:488-515
# asked: {"lines": [488, 489, 501, 503, 504, 506, 507, 509, 510, 511, 512, 514, 515], "branches": []}
# gained: {"lines": [488, 489, 501, 503, 504, 506, 507, 509, 510, 511, 512, 514, 515], "branches": []}

import pytest
from unittest import mock
from tornado.options import OptionParser
from tornado.options import _Mockable

class TestMockable:
    @pytest.fixture
    def option_parser(self):
        parser = OptionParser()
        parser.define("test_option", default=42)
        return parser

    @pytest.fixture
    def mockable(self, option_parser):
        return _Mockable(option_parser)

    def test_getattr(self, mockable):
        assert mockable.test_option == 42

    def test_setattr(self, mockable):
        mockable.test_option = 100
        assert mockable.test_option == 100
        assert mockable._options.test_option == 100
        assert mockable._originals["test_option"] == 42

    def test_setattr_reuse(self, mockable):
        mockable.test_option = 100
        with pytest.raises(AssertionError, match="don't reuse mockable objects"):
            mockable.test_option = 200

    def test_delattr(self, mockable):
        mockable.test_option = 100
        del mockable.test_option
        assert mockable.test_option == 42
        assert "test_option" not in mockable._originals
