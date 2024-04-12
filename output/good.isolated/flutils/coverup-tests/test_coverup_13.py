# file flutils/pathutils.py:417-458
# lines [417, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 452, 453, 454, 455, 456, 457]
# branches ['441->442', '441->444', '444->445', '444->452']

import grp
import pytest
from unittest.mock import patch
from flutils.pathutils import get_os_group


def test_get_os_group_with_invalid_gid():
    invalid_gid = -1
    with pytest.raises(OSError) as excinfo:
        get_os_group(invalid_gid)
    assert str(excinfo.value) == (
        f"The given gid: {invalid_gid!r}, is not a valid gid for this operating system."
    )


def test_get_os_group_with_invalid_group_name():
    invalid_group_name = "nonexistent_group_name"
    with pytest.raises(OSError) as excinfo:
        get_os_group(invalid_group_name)
    assert str(excinfo.value) == (
        f"The given name: {invalid_group_name!r}, is not a valid \"group name\" "
        f"for this operating system."
    )


def test_get_os_group_with_none_and_mocked_user(mocker):
    mocked_user = mocker.patch('flutils.pathutils.get_os_user')
    mocked_user.return_value.pw_gid = 1000
    with patch('grp.getgrgid') as mock_getgrgid:
        mock_getgrgid.return_value = grp.struct_group(
            ('mockgroup', '*', 1000, ['user1', 'user2'])
        )
        group = get_os_group()
        assert group.gr_gid == 1000
        assert group.gr_name == 'mockgroup'
        mock_getgrgid.assert_called_once_with(1000)
