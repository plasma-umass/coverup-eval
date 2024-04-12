# file httpie/cli/argparser.py:428-438
# lines [429, 430, 431, 432, 433, 434, 435, 436, 437, 438]
# branches ['429->430', '429->433', '433->434', '433->436', '434->435', '434->436', '436->exit', '436->438']

import pytest
from httpie.cli.argparser import HTTPieArgumentParser
from unittest.mock import MagicMock

class TestHTTPieArgumentParser:

    @pytest.fixture
    def parser(self):
        parser = HTTPieArgumentParser()
        parser.args = MagicMock()
        parser.env = MagicMock(stdout=MagicMock(), stderr=MagicMock())
        return parser

    def test_process_download_options_offline(self, parser):
        parser.args.offline = True
        parser._process_download_options()
        assert not parser.args.download
        assert not parser.args.download_resume

    def test_process_download_options_continue_without_download(self, parser):
        parser.args.offline = False
        parser.args.download = False
        parser.args.download_resume = True
        with pytest.raises(SystemExit):
            parser._process_download_options()

    def test_process_download_options_continue_requires_output(self, parser):
        parser.args.offline = False
        parser.args.download = True
        parser.args.download_resume = True
        parser.args.output_file = None
        with pytest.raises(SystemExit):
            parser._process_download_options()
