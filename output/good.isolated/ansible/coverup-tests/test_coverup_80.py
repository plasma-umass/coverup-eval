# file lib/ansible/modules/apt_repository.py:249-278
# lines [249, 250, 251, 252, 253, 255, 256, 257, 258, 261, 262, 263, 264, 268, 269, 270, 271, 272, 273, 275, 276, 278]
# branches ['256->257', '256->261', '262->263', '262->268', '269->270', '269->275', '271->272', '271->275', '275->276', '275->278']

import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.apt_repository import SourcesList, InvalidSource

VALID_SOURCE_TYPES = ['deb', 'deb-src']

@pytest.fixture
def sources_list():
    mock_module = MagicMock()
    with patch('ansible.modules.apt_repository.apt_pkg', create=True):
        yield SourcesList(mock_module)

def test_parse_valid_source(sources_list):
    valid, enabled, source, comment = sources_list._parse("deb http://example.com/ubuntu bionic main")
    assert valid
    assert enabled
    assert source == "deb http://example.com/ubuntu bionic main"
    assert comment == ""

def test_parse_disabled_source(sources_list):
    valid, enabled, source, comment = sources_list._parse("# deb http://example.com/ubuntu bionic main")
    assert not enabled
    assert valid
    assert source == "deb http://example.com/ubuntu bionic main"
    assert comment == ""

def test_parse_source_with_comment(sources_list):
    valid, enabled, source, comment = sources_list._parse("deb http://example.com/ubuntu bionic main # This is a comment")
    assert valid
    assert enabled
    assert source == "deb http://example.com/ubuntu bionic main"
    assert comment == "This is a comment"

def test_parse_invalid_source_raises_exception(sources_list):
    with pytest.raises(InvalidSource):
        sources_list._parse("invalid http://example.com/ubuntu bionic main", raise_if_invalid_or_disabled=True)

def test_parse_disabled_invalid_source_raises_exception(sources_list):
    with pytest.raises(InvalidSource):
        sources_list._parse("# invalid http://example.com/ubuntu bionic main", raise_if_invalid_or_disabled=True)

def test_parse_valid_source_with_duplicated_whitespaces(sources_list):
    valid, enabled, source, comment = sources_list._parse("deb    http://example.com/ubuntu    bionic    main")
    assert valid
    assert enabled
    assert source == "deb http://example.com/ubuntu bionic main"
    assert comment == ""
