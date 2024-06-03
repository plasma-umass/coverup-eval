# file lib/ansible/cli/doc.py:644-760
# lines [646, 648, 649, 650, 651, 652, 653, 655, 656, 664, 665, 666, 667, 669, 670, 671, 673, 674, 675, 676, 677, 679, 680, 681, 683, 684, 685, 686, 687, 688, 689, 691, 693, 695, 698, 699, 700, 701, 703, 704, 705, 706, 709, 711, 712, 714, 716, 717, 719, 720, 721, 722, 723, 724, 725, 726, 728, 729, 730, 731, 732, 733, 735, 738, 740, 741, 742, 743, 744, 746, 748, 749, 750, 751, 752, 754, 755, 757, 758, 760]
# branches ['655->656', '655->669', '665->666', '665->667', '669->670', '669->671', '671->673', '671->680', '673->674', '673->676', '676->677', '676->679', '680->681', '680->695', '681->683', '681->693', '684->685', '684->688', '686->687', '686->691', '688->689', '688->691', '699->700', '699->703', '703->704', '703->709', '704->705', '704->709', '705->704', '705->706', '711->712', '711->714', '716->717', '716->719', '720->721', '720->748', '721->722', '721->723', '723->724', '723->738', '724->725', '724->728', '728->729', '728->757', '738->740', '738->757', '743->744', '743->746', '748->749', '748->754', '749->750', '749->751', '751->752', '751->757', '754->755', '754->757', '757->758', '757->760']

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleOptionsError, AnsibleError
from ansible.utils.display import Display

@pytest.fixture
def mock_context(mocker):
    context_mock = mocker.patch('ansible.cli.doc.context')
    context_mock.CLIARGS = {
        'basedir': '/fake/dir',
        'type': 'role',
        'json_format': False,
        'dump': False,
        'roles_path': ('/fake/roles',),
        'list_files': False,
        'list_dir': False,
        'args': [],
        'entry_point': None,
        'module_path': [],
        'show_snippet': False
    }
    return context_mock

@pytest.fixture
def mock_loader(mocker):
    loader_mock = mocker.patch('ansible.cli.doc.plugin_loader')
    loader_mock.role_loader = MagicMock()
    return loader_mock

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.doc.display', new_callable=Display)

@pytest.fixture
def mock_pkgutil(mocker):
    pkgutil_mock = mocker.patch('ansible.cli.doc.pkgutil')
    pkgutil_mock.get_data.return_value = b"{}"
    return pkgutil_mock

def test_doc_cli_run(mock_context, mock_loader, mock_display, mock_pkgutil):
    cli = DocCLI(['ansible-doc'])
    
    with patch.object(DocCLI, '_create_role_doc', return_value={'role': 'doc'}), \
         patch.object(DocCLI, '_display_role_doc') as mock_display_role_doc:
        mock_context.CLIARGS['args'] = ['test_role']
        result = cli.run()
        assert result == 0
        mock_display_role_doc.assert_called_once_with({'role': 'doc'})

    with patch.object(DocCLI, '_create_role_list', return_value={'role': 'list'}), \
         patch.object(DocCLI, '_display_available_roles') as mock_display_available_roles:
        mock_context.CLIARGS['list_dir'] = True
        mock_context.CLIARGS['args'] = []
        result = cli.run()
        assert result == 0
        mock_display_available_roles.assert_called_once_with({'role': 'list'})

    with patch.object(DocCLI, '_list_keywords', return_value={'keyword': 'doc'}), \
         patch.object(DocCLI, '_get_keywords_docs', return_value={'keyword': 'doc'}):
        mock_context.CLIARGS['type'] = 'keyword'
        mock_context.CLIARGS['dump'] = True
        result = cli.run()
        assert result == 0

    with patch.object(DocCLI, '_list_keywords', return_value={'keyword': 'doc'}):
        mock_context.CLIARGS['dump'] = False
        mock_context.CLIARGS['list_files'] = True
        result = cli.run()
        assert result == 0

    with patch.object(DocCLI, '_get_keywords_docs', return_value={'keyword': 'doc'}):
        mock_context.CLIARGS['list_files'] = False
        mock_context.CLIARGS['args'] = ['test_keyword']
        result = cli.run()
        assert result == 0

    with pytest.raises(AnsibleOptionsError):
        mock_context.CLIARGS['type'] = 'unknown'
        cli.run()

    with pytest.raises(AnsibleError):
        mock_context.CLIARGS['type'] = 'role'
        mock_context.CLIARGS['list_dir'] = True
        mock_context.CLIARGS['args'] = ['invalid_collection']
        with patch('ansible.cli.doc.AnsibleCollectionRef.is_valid_collection_name', return_value=False):
            cli.run()
