# file: lib/ansible/cli/doc.py:1012-1111
# asked: {"lines": [1012, 1013, 1015, 1017, 1019, 1020, 1021, 1022, 1023, 1025, 1027, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1037, 1038, 1039, 1040, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1057, 1058, 1060, 1061, 1062, 1063, 1065, 1066, 1067, 1069, 1070, 1071, 1072, 1073, 1075, 1076, 1077, 1078, 1079, 1081, 1082, 1084, 1085, 1087, 1088, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1101, 1103, 1104, 1106, 1107, 1108, 1109, 1110, 1111], "branches": [[1015, 0], [1015, 1017], [1020, 1021], [1020, 1022], [1022, 1023], [1022, 1025], [1029, 1030], [1029, 1031], [1031, 1032], [1031, 1037], [1032, 1033], [1032, 1040], [1033, 1034], [1033, 1035], [1037, 1038], [1037, 1039], [1043, 1044], [1043, 1047], [1044, 1045], [1044, 1046], [1048, 1049], [1048, 1052], [1049, 1050], [1049, 1051], [1053, 1054], [1053, 1057], [1054, 1055], [1054, 1057], [1061, 1062], [1061, 1065], [1062, 1061], [1062, 1063], [1066, 1067], [1066, 1075], [1067, 1066], [1067, 1069], [1070, 1066], [1070, 1071], [1071, 1070], [1071, 1072], [1072, 1071], [1072, 1073], [1075, 1076], [1075, 1084], [1077, 1078], [1077, 1082], [1078, 1079], [1078, 1081], [1084, 1085], [1084, 1087], [1090, 1091], [1090, 1103], [1091, 1092], [1091, 1093], [1093, 1094], [1093, 1098], [1098, 1099], [1098, 1101], [1103, 1104], [1103, 1106], [1106, 1107], [1106, 1110], [1110, 1015], [1110, 1111]]}
# gained: {"lines": [1012, 1013, 1015, 1017, 1019, 1020, 1022, 1023, 1025, 1027, 1029, 1031, 1037, 1039, 1040, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1057, 1058, 1060, 1061, 1062, 1063, 1065, 1066, 1067, 1075, 1084, 1087, 1088, 1090, 1103, 1104, 1106, 1107, 1108, 1109, 1110, 1111], "branches": [[1015, 0], [1015, 1017], [1020, 1022], [1022, 1023], [1022, 1025], [1029, 1031], [1031, 1037], [1037, 1039], [1043, 1044], [1043, 1047], [1044, 1045], [1048, 1049], [1048, 1052], [1049, 1050], [1053, 1054], [1054, 1055], [1061, 1062], [1061, 1065], [1062, 1061], [1062, 1063], [1066, 1067], [1066, 1075], [1067, 1066], [1075, 1084], [1084, 1087], [1090, 1103], [1103, 1104], [1103, 1106], [1106, 1107], [1106, 1110], [1110, 1015], [1110, 1111]]}

import pytest
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleError
from ansible.module_utils.six import string_types

def test_add_fields(monkeypatch):
    text = []
    fields = {
        'option1': {
            'required': True,
            'description': 'This is a required option.',
            'aliases': ['opt1', 'o1'],
            'choices': ['choice1', 'choice2'],
            'default': 'choice1',
            'version_added': '2.0',
            'version_added_collection': 'ansible.builtin',
            'options': {
                'suboption1': {
                    'required': False,
                    'description': 'This is a suboption.'
                }
            }
        },
        'option2': {
            'required': False,
            'description': 'This is an optional option.',
            'default': 'default_value'
        }
    }
    limit = 80
    opt_indent = '  '
    base_indent = ''

    def mock_tty_ify(text):
        return text

    def mock_dump_yaml(struct, indent):
        return 'yaml_dump'

    def mock_format_version_added(version_added, version_added_collection=None):
        return f"{version_added} ({version_added_collection})"

    monkeypatch.setattr(DocCLI, 'tty_ify', staticmethod(mock_tty_ify))
    monkeypatch.setattr(DocCLI, '_dump_yaml', staticmethod(mock_dump_yaml))
    monkeypatch.setattr(DocCLI, '_format_version_added', staticmethod(mock_format_version_added))

    DocCLI.add_fields(text, fields, limit, opt_indent, base_indent=base_indent)

    assert len(text) > 0
    assert any('option1' in line for line in text)
    assert any('This is a required option.' in line for line in text)
    assert any('Aliases: opt1, o1' in line for line in text)
    assert any('Choices: choice1, choice2' in line for line in text)
    assert any('[Default: choice1]' in line for line in text)
    assert any('added in: 2.0 (ansible.builtin)' in line for line in text)
    assert any('suboption1' in line for line in text)
    assert any('This is a suboption.' in line for line in text)
    assert any('option2' in line for line in text)
    assert any('This is an optional option.' in line for line in text)
    assert any('[Default: default_value]' in line for line in text)
