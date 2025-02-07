# file: lib/ansible/cli/doc.py:519-583
# asked: {"lines": [519, 520, 522, 523, 524, 526, 528, 529, 531, 533, 535, 537, 540, 541, 542, 543, 544, 545, 547, 548, 551, 553, 554, 555, 556, 558, 560, 561, 562, 563, 565, 568, 569, 572, 573, 574, 576, 578, 579, 580, 581, 583], "branches": [[524, 526], [524, 583], [526, 528], [526, 529], [529, 531], [529, 533], [541, 542], [541, 572], [542, 543], [542, 547], [547, 541], [547, 548], [551, 541], [551, 553], [554, 555], [554, 558], [560, 561], [560, 562], [562, 563], [562, 565], [568, 541], [568, 569], [572, 573], [572, 576], [573, 572], [573, 574], [580, 524], [580, 581]]}
# gained: {"lines": [519, 520, 522, 523, 524, 526, 528, 529, 531, 533, 535, 537, 540, 541, 542, 543, 544, 545, 547, 548, 551, 553, 554, 558, 560, 562, 563, 565, 568, 569, 572, 573, 576, 578, 579, 580, 581, 583], "branches": [[524, 526], [524, 583], [526, 528], [526, 529], [529, 531], [529, 533], [541, 542], [541, 572], [542, 543], [547, 548], [551, 541], [551, 553], [554, 558], [560, 562], [562, 563], [562, 565], [568, 541], [568, 569], [572, 573], [572, 576], [573, 572], [580, 581]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_importlib():
    with patch('ansible.cli.doc.importlib') as mock_importlib:
        yield mock_importlib

@pytest.fixture
def mock_display():
    with patch('ansible.cli.doc.display') as mock_display:
        mock_display.verbosity = 2  # Set default verbosity level
        yield mock_display

@pytest.fixture
def mock_pb_objects():
    with patch('ansible.cli.doc.PB_OBJECTS', ['Playbook1', 'Playbook2']):
        with patch('ansible.cli.doc.PB_LOADED', {}):
            yield

@pytest.fixture
def mock_list_keywords():
    with patch.object(DocCLI, '_list_keywords', return_value={
        'with_items': 'description for with_items',
        'async': 'description for async',
        'normal_key': 'description for normal_key'
    }):
        yield

def test_get_keywords_docs_with_items(mock_importlib, mock_display, mock_pb_objects, mock_list_keywords):
    mock_playbook = MagicMock()
    mock_playbook._valid_attrs = ['loop']
    mock_playbook._loop = MagicMock(private=False, isa='string', static=False, alias='alias_value', priority='priority_value')
    mock_importlib.import_module.return_value = MagicMock(Playbook1=mock_playbook, Playbook2=mock_playbook)

    result = DocCLI._get_keywords_docs(['with_items'])

    assert 'with_items' in result
    assert result['with_items']['description'] == 'description for with_items'
    assert result['with_items']['applies_to'] == ['Playbook1', 'Playbook2']
    assert result['with_items']['type'] == 'string'
    assert result['with_items']['template'] == 'explicit'
    assert result['with_items']['alias'] == 'alias_value'
    assert result['with_items']['priority'] == 'priority_value'

def test_get_keywords_docs_async(mock_importlib, mock_display, mock_pb_objects, mock_list_keywords):
    mock_playbook = MagicMock()
    mock_playbook._valid_attrs = ['async_val']
    mock_playbook._async_val = MagicMock(private=False, isa='string', static=True, alias='alias_value', priority='priority_value')
    mock_importlib.import_module.return_value = MagicMock(Playbook1=mock_playbook, Playbook2=mock_playbook)

    result = DocCLI._get_keywords_docs(['async'])

    assert 'async' in result
    assert result['async']['description'] == 'description for async'
    assert result['async']['applies_to'] == ['Playbook1', 'Playbook2']
    assert result['async']['type'] == 'string'
    assert result['async']['template'] == 'static'
    assert result['async']['alias'] == 'alias_value'
    assert result['async']['priority'] == 'priority_value'

def test_get_keywords_docs_normal_key(mock_importlib, mock_display, mock_pb_objects, mock_list_keywords):
    mock_playbook = MagicMock()
    mock_playbook._valid_attrs = ['normal_key']
    mock_playbook._normal_key = MagicMock(private=False, isa='string', static=False, alias='alias_value', priority='priority_value')
    mock_importlib.import_module.return_value = MagicMock(Playbook1=mock_playbook, Playbook2=mock_playbook)

    result = DocCLI._get_keywords_docs(['normal_key'])

    assert 'normal_key' in result
    assert result['normal_key']['description'] == 'description for normal_key'
    assert result['normal_key']['applies_to'] == ['Playbook1', 'Playbook2']
    assert result['normal_key']['type'] == 'string'
    assert result['normal_key']['template'] == 'explicit'
    assert result['normal_key']['alias'] == 'alias_value'
    assert result['normal_key']['priority'] == 'priority_value'

def test_get_keywords_docs_invalid_key(mock_importlib, mock_display, mock_pb_objects, mock_list_keywords):
    mock_playbook = MagicMock()
    mock_playbook._valid_attrs = []
    mock_importlib.import_module.return_value = MagicMock(Playbook1=mock_playbook, Playbook2=mock_playbook)

    mock_display.verbosity = 3  # Set verbosity level to trigger verbose output

    result = DocCLI._get_keywords_docs(['invalid_key'])

    assert 'invalid_key' not in result
    mock_display.warning.assert_called_once()
    mock_display.verbose.assert_called_once()
