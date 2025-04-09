# file: lib/ansible/cli/doc.py:644-760
# asked: {"lines": [644, 646, 648, 649, 650, 651, 652, 653, 655, 656, 664, 665, 666, 667, 669, 670, 671, 673, 674, 675, 676, 677, 679, 680, 681, 683, 684, 685, 686, 687, 688, 689, 691, 693, 695, 698, 699, 700, 701, 703, 704, 705, 706, 709, 711, 712, 714, 716, 717, 719, 720, 721, 722, 723, 724, 725, 726, 728, 729, 730, 731, 732, 733, 735, 738, 740, 741, 742, 743, 744, 746, 748, 749, 750, 751, 752, 754, 755, 757, 758, 760], "branches": [[655, 656], [655, 669], [665, 666], [665, 667], [669, 670], [669, 671], [671, 673], [671, 680], [673, 674], [673, 676], [676, 677], [676, 679], [680, 681], [680, 695], [681, 683], [681, 693], [684, 685], [684, 688], [686, 687], [686, 691], [688, 689], [688, 691], [699, 700], [699, 703], [703, 704], [703, 709], [704, 705], [704, 709], [705, 704], [705, 706], [711, 712], [711, 714], [716, 717], [716, 719], [720, 721], [720, 748], [721, 722], [721, 723], [723, 724], [723, 738], [724, 725], [724, 728], [728, 729], [728, 757], [738, 740], [738, 757], [743, 744], [743, 746], [748, 749], [748, 754], [749, 750], [749, 751], [751, 752], [751, 757], [754, 755], [754, 757], [757, 758], [757, 760]]}
# gained: {"lines": [644, 646, 648, 649, 650, 651, 652, 653, 655, 656, 664, 665, 666, 667, 669, 670, 671, 673, 674, 675, 680, 681, 683, 684, 685, 686, 687, 688, 689, 691, 693, 695, 698, 699, 700, 701, 703, 704, 705, 706, 709, 711, 712, 714, 716, 717, 719, 720, 721, 722, 723, 724, 728, 729, 730, 735, 738, 748, 749, 751, 752, 757, 758, 760], "branches": [[655, 656], [655, 669], [665, 666], [665, 667], [669, 670], [669, 671], [671, 673], [671, 680], [673, 674], [680, 681], [680, 695], [681, 683], [681, 693], [684, 685], [684, 688], [686, 687], [686, 691], [688, 689], [699, 700], [699, 703], [703, 704], [703, 709], [704, 705], [704, 709], [705, 706], [711, 712], [711, 714], [716, 717], [716, 719], [720, 721], [720, 748], [721, 722], [721, 723], [723, 724], [723, 738], [724, 728], [728, 729], [728, 757], [738, 757], [748, 749], [749, 751], [751, 752], [751, 757], [757, 758], [757, 760]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleOptionsError, AnsibleError
from ansible.utils.display import Display

@pytest.fixture
def mock_context(mocker):
    context = mocker.patch('ansible.cli.doc.context')
    context.CLIARGS = {
        'basedir': None,
        'type': 'role',
        'json_format': False,
        'dump': False,
        'roles_path': (),
        'list_files': False,
        'list_dir': False,
        'args': [],
        'entry_point': None,
        'module_path': [],
        'show_snippet': False
    }
    return context

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.doc.display', new_callable=Display)

@pytest.fixture
def doc_cli(mocker):
    mocker.patch('ansible.cli.CLI.__init__', return_value=None)
    instance = DocCLI(['ansible-doc'])
    instance.args = ['ansible-doc']
    return instance

def test_run_with_basedir(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['basedir'] = '/some/path'
    mock_context.CLIARGS['type'] = 'role'
    mock_context.CLIARGS['roles_path'] = ('/another/path',)
    mocker.patch('os.path.isdir', return_value=True)
    mocker.patch('ansible.cli.doc.AnsibleCollectionConfig')
    mocker.patch('ansible.cli.doc.DocCLI._create_role_list', return_value={})
    mocker.patch('ansible.cli.doc.DocCLI._create_role_doc', return_value={})

    doc_cli.run()

    assert mock_context.CLIARGS['basedir'] == '/some/path'

def test_run_with_invalid_plugin_type(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'invalid_type'

    with pytest.raises(AnsibleOptionsError, match="Unknown or undocumentable plugin type: invalid_type"):
        doc_cli.run()

def test_run_with_keyword_plugin_type(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'keyword'
    mock_context.CLIARGS['dump'] = True
    mocker.patch('ansible.cli.doc.DocCLI._list_keywords', return_value={})
    mocker.patch('ansible.cli.doc.DocCLI._get_keywords_docs', return_value={})

    doc_cli.run()

    assert mock_context.CLIARGS['type'] == 'keyword'

def test_run_with_role_plugin_type_list_dir(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'role'
    mock_context.CLIARGS['list_dir'] = True
    mock_context.CLIARGS['args'] = ['namespace.collection']
    mocker.patch('ansible.cli.doc.AnsibleCollectionRef.is_valid_collection_name', return_value=True)
    mocker.patch('ansible.cli.doc.DocCLI._create_role_list', return_value={})

    doc_cli.run()

    assert mock_context.CLIARGS['list_dir'] is True

def test_run_with_role_plugin_type_invalid_collection_name(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'role'
    mock_context.CLIARGS['list_dir'] = True
    mock_context.CLIARGS['args'] = ['invalid_collection']
    mocker.patch('ansible.cli.doc.AnsibleCollectionRef.is_valid_collection_name', return_value=False)

    with pytest.raises(AnsibleError, match="Invalid collection name"):
        doc_cli.run()

def test_run_with_role_plugin_type_multiple_args(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'role'
    mock_context.CLIARGS['list_dir'] = True
    mock_context.CLIARGS['args'] = ['arg1', 'arg2']

    with pytest.raises(AnsibleOptionsError, match="Only a single collection filter is supported."):
        doc_cli.run()

def test_run_with_role_plugin_type_create_role_doc(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'role'
    mock_context.CLIARGS['args'] = ['some_role']
    mocker.patch('ansible.cli.doc.DocCLI._create_role_doc', return_value={})

    doc_cli.run()

    assert mock_context.CLIARGS['type'] == 'role'

def test_run_with_plugin_loader(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'module'
    mock_context.CLIARGS['basedir'] = '/some/path'
    mock_context.CLIARGS['module_path'] = ['/module/path']
    mocker.patch('ansible.cli.doc.plugin_loader')
    mocker.patch('ansible.cli.doc.DocCLI._list_plugins', return_value={})
    mocker.patch('ansible.cli.doc.DocCLI._get_plugins_docs', return_value={})

    doc_cli.run()

    assert mock_context.CLIARGS['type'] == 'module'

def test_run_with_json_output(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'role'
    mock_context.CLIARGS['json_format'] = True
    mocker.patch('ansible.cli.doc.DocCLI._create_role_doc', return_value={})
    mocker.patch('ansible.cli.doc.jdump')

    doc_cli.run()

    assert mock_context.CLIARGS['json_format'] is True

def test_run_with_show_snippet(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'module'
    mock_context.CLIARGS['show_snippet'] = True
    mocker.patch('ansible.cli.doc.DocCLI._get_plugins_docs', return_value={'plugin': {'doc': {}}})
    mocker.patch('ansible.cli.doc.DocCLI.format_snippet', return_value='snippet')

    doc_cli.run()

    assert mock_context.CLIARGS['show_snippet'] is True

def test_run_with_display_plugin_list(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'module'
    mock_context.CLIARGS['list_files'] = True
    mocker.patch('ansible.cli.doc.DocCLI._list_plugins', return_value={'plugin': {}})
    mocker.patch('ansible.cli.doc.DocCLI.display_plugin_list')

    doc_cli.run()

    assert mock_context.CLIARGS['list_files'] is True

def test_run_with_display_role_doc(mocker, mock_context, doc_cli):
    mock_context.CLIARGS['type'] = 'role'
    mock_context.CLIARGS['args'] = ['some_role']
    mocker.patch('ansible.cli.doc.DocCLI._create_role_doc', return_value={'role': {}})
    mocker.patch('ansible.cli.doc.DocCLI._display_role_doc')

    doc_cli.run()

    assert mock_context.CLIARGS['type'] == 'role'
