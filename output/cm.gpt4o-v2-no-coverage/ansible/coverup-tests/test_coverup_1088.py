# file: lib/ansible/galaxy/api.py:664-728
# asked: {"lines": [673, 674, 677, 678, 679, 681, 682, 684, 685, 686, 688, 689, 690, 691, 692, 693, 694, 696, 697, 698, 700, 702, 703, 705, 706, 707, 710, 711, 712, 713, 715, 716, 717, 718, 719, 720, 722, 724, 725, 726, 727, 728], "branches": [[677, 678], [677, 681], [688, 689], [688, 711], [693, 694], [693, 696], [702, 703], [702, 705], [711, 712], [711, 715], [715, 716], [715, 724], [717, 718], [717, 719], [719, 720], [719, 722], [724, 0], [724, 725]]}
# gained: {"lines": [673, 674, 677, 678, 679, 684, 685, 686, 688, 689, 690, 691, 700, 702, 703, 705, 706, 707, 710, 711, 712, 713, 715, 716, 717, 718, 719, 720, 722, 724, 725, 726, 727, 728], "branches": [[677, 678], [688, 689], [688, 711], [702, 703], [702, 705], [711, 712], [711, 715], [715, 716], [715, 724], [717, 718], [717, 719], [719, 720], [719, 722], [724, 0], [724, 725]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.plugins.loader import display
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy='test_galaxy', name='test_name', url='http://testserver/api/', available_api_versions={'v2': 'v2', 'v3': 'v3'})

@patch('ansible.galaxy.api._urljoin', return_value='http://testserver/api/v3/imports/collections/1/')
@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_wait_import_task_success(mock_call_galaxy, mock_urljoin, galaxy_api):
    mock_call_galaxy.return_value = {'state': 'completed', 'finished_at': 'some_time', 'messages': []}
    galaxy_api.wait_import_task(task_id='1', timeout=5)
    mock_call_galaxy.assert_called_once_with('http://testserver/api/v3/imports/collections/1/', method='GET', auth_required=True, error_context_msg='Error when getting import task results at http://testserver/api/v3/imports/collections/1/')

@patch('ansible.galaxy.api._urljoin', return_value='http://testserver/api/v3/imports/collections/1/')
@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_wait_import_task_timeout(mock_call_galaxy, mock_urljoin, galaxy_api):
    mock_call_galaxy.return_value = {'state': 'waiting', 'messages': []}
    with pytest.raises(AnsibleError, match="Timeout while waiting for the Galaxy import process to finish"):
        galaxy_api.wait_import_task(task_id='1', timeout=1)

@patch('ansible.galaxy.api._urljoin', return_value='http://testserver/api/v3/imports/collections/1/')
@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_wait_import_task_failed(mock_call_galaxy, mock_urljoin, galaxy_api):
    mock_call_galaxy.return_value = {'state': 'failed', 'error': {'code': 'ERROR_CODE', 'description': 'Error description'}, 'messages': []}
    with pytest.raises(AnsibleError, match="Galaxy import process failed: Error description \(Code: ERROR_CODE\)"):
        galaxy_api.wait_import_task(task_id='1', timeout=5)

@patch('ansible.galaxy.api._urljoin', return_value='http://testserver/api/v3/imports/collections/1/')
@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_wait_import_task_with_messages(mock_call_galaxy, mock_urljoin, galaxy_api):
    mock_call_galaxy.return_value = {'state': 'completed', 'finished_at': 'some_time', 'messages': [{'level': 'error', 'message': 'Error message'}, {'level': 'warning', 'message': 'Warning message'}, {'level': 'info', 'message': 'Info message'}]}
    with patch.object(display, 'error') as mock_display_error, patch.object(display, 'warning') as mock_display_warning, patch.object(display, 'vvv') as mock_display_vvv:
        galaxy_api.wait_import_task(task_id='1', timeout=5)
        mock_display_error.assert_called_once_with('Galaxy import error message: Error message')
        mock_display_warning.assert_called_once_with('Galaxy import warning message: Warning message')
        mock_display_vvv.assert_called_once_with('Galaxy import message: info - Info message')
