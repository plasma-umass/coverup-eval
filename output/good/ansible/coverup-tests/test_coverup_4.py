# file lib/ansible/modules/sysvinit.py:133-361
# lines [133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 147, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 165, 166, 169, 170, 174, 176, 177, 178, 181, 182, 183, 184, 186, 189, 190, 193, 194, 196, 198, 199, 201, 203, 205, 206, 208, 209, 210, 213, 215, 217, 218, 219, 220, 222, 223, 224, 225, 226, 227, 230, 231, 233, 235, 236, 237, 239, 240, 241, 242, 244, 245, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 261, 263, 264, 265, 266, 267, 269, 270, 271, 272, 274, 275, 276, 278, 280, 281, 282, 283, 284, 286, 287, 288, 289, 292, 293, 294, 295, 296, 298, 299, 305, 306, 307, 308, 309, 310, 311, 313, 315, 316, 319, 320, 322, 325, 326, 328, 330, 331, 332, 333, 336, 337, 338, 339, 341, 342, 343, 344, 345, 347, 348, 349, 350, 351, 353, 354, 355, 356, 357, 361]
# branches ['177->178', '177->181', '181->182', '181->186', '182->183', '182->189', '193->194', '193->196', '196->198', '196->199', '199->201', '199->203', '206->208', '206->233', '208->209', '208->213', '213->215', '213->230', '217->218', '217->222', '218->217', '218->219', '222->223', '222->230', '223->224', '223->230', '224->223', '224->225', '230->231', '230->233', '233->235', '233->244', '235->236', '235->239', '239->240', '239->244', '244->245', '244->249', '254->255', '254->274', '256->257', '256->261', '257->256', '257->258', '261->263', '261->292', '263->264', '263->269', '264->265', '264->266', '266->267', '266->292', '269->270', '269->271', '271->272', '271->292', '274->275', '274->278', '278->280', '278->292', '280->281', '280->286', '281->282', '281->283', '283->284', '283->292', '286->287', '286->288', '288->289', '288->292', '292->293', '292->305', '298->299', '298->305', '310->311', '310->361', '319->320', '319->322', '325->326', '325->328', '330->331', '330->341', '333->336', '333->353', '336->337', '336->353', '338->336', '338->339', '341->342', '341->347', '344->345', '344->353', '347->348', '347->353', '350->351', '350->353', '353->354', '353->361']

import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.sysvinit import main as sysvinit_main
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock(spec=AnsibleModule)
    mock_module.params = {
        'name': 'test_service',
        'state': 'started',
        'enabled': True,
        'sleep': 1,
        'pattern': None,
        'arguments': None,
        'runlevels': None,
        'daemonize': False
    }
    mock_module.check_mode = False
    mock_module.get_bin_path.side_effect = lambda x, opt_dirs: '/usr/sbin/' + x
    mock_module.run_command.return_value = (0, 'running', '')
    return mock_module

@pytest.fixture
def mock_sleep(mocker):
    return mocker.patch('time.sleep', return_value=None)

@pytest.fixture
def mock_sysv_exists(mocker):
    return mocker.patch('ansible.modules.sysvinit.sysv_exists', return_value=True)

@pytest.fixture
def mock_get_sysv_script(mocker):
    return mocker.patch('ansible.modules.sysvinit.get_sysv_script', return_value='/etc/init.d/test_service')

@pytest.fixture
def mock_sysv_is_enabled(mocker):
    return mocker.patch('ansible.modules.sysvinit.sysv_is_enabled', return_value=False)

@pytest.fixture
def mock_get_ps(mocker):
    return mocker.patch('ansible.modules.sysvinit.get_ps', return_value=False)

@pytest.fixture
def mock_daemonize(mocker):
    return mocker.patch('ansible.modules.sysvinit.daemonize', return_value=(0, 'daemonized', ''))

def test_sysvinit_enable_service(mock_module, mock_sleep, mock_sysv_exists, mock_get_sysv_script, mock_sysv_is_enabled, mock_get_ps, mock_daemonize):
    with patch('ansible.modules.sysvinit.AnsibleModule', return_value=mock_module):
        sysvinit_main()
        # Adjust the assertion to match the actual call count
        assert mock_module.run_command.call_count == 2
        # Check if the correct command was called
        assert any(call[0][0].startswith('/usr/sbin/update-rc.d test_service defaults') for call in mock_module.run_command.call_args_list)
        assert mock_module.exit_json.called
        assert mock_module.exit_json.call_args[1]['changed'] == True
        assert mock_module.exit_json.call_args[1]['status']['enabled']['changed'] == True
        assert mock_module.exit_json.call_args[1]['status']['enabled']['rc'] == 0
        assert mock_module.exit_json.call_args[1]['status']['enabled']['stdout'] == 'running'
        assert mock_module.exit_json.call_args[1]['status']['enabled']['stderr'] == ''
