# file lib/ansible/modules/apt_repository.py:249-278
# lines [263, 264, 276]
# branches ['262->263', '269->275', '271->275', '275->276']

import pytest
from ansible.modules.apt_repository import SourcesList, InvalidSource

@pytest.fixture
def mock_apt_pkg(mocker):
    apt_pkg_mock = mocker.patch('ansible.modules.apt_repository.apt_pkg', autospec=True)
    apt_pkg_mock.config.find_file.return_value = '/dev/null'
    return apt_pkg_mock

def test_parse_with_comment_and_invalid_source(mocker, mock_apt_pkg):
    module_mock = mocker.Mock()
    sources_list = SourcesList(module=module_mock)
    
    # Test case to cover lines 263-264
    line_with_comment = "deb http://example.com/ubuntu focal main # this is a comment"
    valid, enabled, source, comment = sources_list._parse(line_with_comment)
    assert valid
    assert enabled
    assert source == "deb http://example.com/ubuntu focal main"
    assert comment == "this is a comment"
    
    # Test case to cover branches 269->275, 271->275 and line 276
    line_invalid_source = "invalidsource http://example.com/ubuntu focal main"
    with pytest.raises(InvalidSource):
        sources_list._parse(line_invalid_source, raise_if_invalid_or_disabled=True)
    
    # Test case to cover line 276 with disabled source
    line_disabled_source = "# deb http://example.com/ubuntu focal main"
    with pytest.raises(InvalidSource):
        sources_list._parse(line_disabled_source, raise_if_invalid_or_disabled=True)
