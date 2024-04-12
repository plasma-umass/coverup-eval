# file flutils/pathutils.py:461-501
# lines [461, 485, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 498, 499, 500]
# branches ['485->486', '485->493', '493->494', '493->495']

import pytest
import pwd
import getpass
from flutils.pathutils import get_os_user

def test_get_os_user_with_invalid_uid(mocker):
    invalid_uid = 999999  # Assuming this UID does not exist on the system
    mocker.patch('pwd.getpwuid', side_effect=KeyError)
    with pytest.raises(OSError) as exc_info:
        get_os_user(invalid_uid)
    assert str(exc_info.value) == (
        f"The given uid: {invalid_uid!r}, is not a valid uid for this operating system."
    )

def test_get_os_user_with_invalid_name(mocker):
    invalid_name = 'nonexistentuser'  # Assuming this user does not exist on the system
    mocker.patch('pwd.getpwnam', side_effect=KeyError)
    with pytest.raises(OSError) as exc_info:
        get_os_user(invalid_name)
    assert str(exc_info.value) == (
        f"The given name: {invalid_name!r}, is not a valid \"login name\" "
        f"for this operating system."
    )

def test_get_os_user_with_none(mocker):
    mocker.patch('getpass.getuser', return_value='currentuser')
    mocker.patch('pwd.getpwnam', return_value=pwd.struct_passwd(
        ('currentuser', 'x', 1000, 1000, 'Current User', '/home/currentuser', '/bin/bash')
    ))
    user = get_os_user()
    assert user.pw_name == 'currentuser'
    assert user.pw_dir == '/home/currentuser'
