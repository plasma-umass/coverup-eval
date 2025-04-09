# file: thonny/roughparse.py:183-231
# asked: {"lines": [190, 203, 204, 217, 222, 223, 224, 225, 226, 227, 228, 230, 231], "branches": [[188, 190], [196, 206], [202, 203], [206, 222], [216, 217], [223, 224], [225, 226], [225, 230], [227, 223], [227, 228]]}
# gained: {"lines": [190, 203, 204, 222, 223, 224, 225, 226, 227, 228, 230, 231], "branches": [[188, 190], [202, 203], [206, 222], [223, 224], [225, 226], [225, 230], [227, 228]]}

import pytest
import re
from thonny.roughparse import RoughParser, _synchre

class TestRoughParser:
    @pytest.fixture
    def parser(self):
        class MockRoughParser(RoughParser):
            def __init__(self, string):
                self.str = string
        return MockRoughParser

    def test_find_good_parse_start_no_is_char_in_string(self, parser):
        rp = parser("def foo():\n    pass\n")
        assert rp.find_good_parse_start() is None

    def test_find_good_parse_start_no_synch_point(self, parser, mocker):
        rp = parser("def foo():\n    pass\n")
        mock_is_char_in_string = mocker.Mock(return_value=False)
        mock_synchre = mocker.Mock(return_value=None)
        assert rp.find_good_parse_start(mock_is_char_in_string, mock_synchre) is None

    def test_find_good_parse_start_synch_point_found(self, parser, mocker):
        rp = parser("def foo():\n    pass\n")
        mock_is_char_in_string = mocker.Mock(return_value=False)
        mock_synchre = mocker.Mock(side_effect=[
            mocker.Mock(start=mocker.Mock(return_value=0)),
            None
        ])
        assert rp.find_good_parse_start(mock_is_char_in_string, mock_synchre) == 0

    def test_find_good_parse_start_in_string(self, parser, mocker):
        rp = parser("def foo():\n    pass\n")
        mock_is_char_in_string = mocker.Mock(return_value=True)
        mock_synchre = mocker.Mock(side_effect=[
            mocker.Mock(start=mocker.Mock(return_value=0)),
            None
        ])
        assert rp.find_good_parse_start(mock_is_char_in_string, mock_synchre) is None

    def test_find_good_parse_start_peek_back_and_forward(self, parser, mocker):
        rp = parser("def foo():\n    pass\n")
        mock_is_char_in_string = mocker.Mock(return_value=False)
        mock_synchre = mocker.Mock(side_effect=[
            mocker.Mock(start=mocker.Mock(return_value=0)),
            mocker.Mock(span=mocker.Mock(return_value=(0, 1))),
            None
        ])
        assert rp.find_good_parse_start(mock_is_char_in_string, mock_synchre) == 0
