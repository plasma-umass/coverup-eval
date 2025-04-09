# file lib/ansible/config/manager.py:198-260
# lines [198, 202, 204, 208, 210, 213, 214, 215, 216, 217, 218, 221, 222, 223, 224, 225, 226, 229, 230, 232, 233, 235, 238, 241, 243, 244, 245, 246, 248, 253, 254, 258, 260]
# branches ['202->204', '202->208', '214->215', '214->221', '216->217', '216->218', '226->229', '226->232', '229->230', '229->238', '243->244', '243->248', '245->243', '245->246', '253->254', '253->260']

import os
import stat
import pytest
from ansible.config.manager import find_ini_config_file
from ansible.utils.path import unfrackpath
from ansible.module_utils._text import to_bytes, to_text

@pytest.fixture
def clean_env():
    # Backup the original ANSIBLE_CONFIG environment variable
    original_ansible_config = os.environ.get('ANSIBLE_CONFIG')
    yield
    # Restore the original ANSIBLE_CONFIG environment variable
    if original_ansible_config is not None:
        os.environ['ANSIBLE_CONFIG'] = original_ansible_config
    else:
        os.environ.pop('ANSIBLE_CONFIG', None)

def test_find_ini_config_file_world_writable_dir(clean_env, tmp_path, mocker):
    # Set up a world-writable directory with an ansible.cfg file
    world_writable_dir = tmp_path / "world_writable"
    world_writable_dir.mkdir(mode=0o777)
    ansible_cfg = world_writable_dir / "ansible.cfg"
    ansible_cfg.touch()

    # Change the current working directory to the world-writable directory
    mocker.patch('os.getcwd', return_value=str(world_writable_dir))
    mocker.patch('os.stat', return_value=os.stat_result((stat.S_IFDIR | stat.S_IWOTH, 0, 0, 0, 0, 0, 0, 0, 0, 0)))

    # Ensure ANSIBLE_CONFIG is not set
    if 'ANSIBLE_CONFIG' in os.environ:
        del os.environ['ANSIBLE_CONFIG']

    # Call the function and collect warnings
    warnings = set()
    result = find_ini_config_file(warnings=warnings)

    # Assert that the result is None since we should not use the world-writable directory
    assert result is None

    # Assert that the warning was added
    expected_warning = u"Ansible is being run in a world writable directory (%s)," \
                       u" ignoring it as an ansible.cfg source." \
                       u" For more information see" \
                       u" https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir" \
                       % to_text(str(world_writable_dir))
    assert expected_warning in warnings

    # Clean up by removing the world-writable directory
    ansible_cfg.unlink()
    world_writable_dir.rmdir()
