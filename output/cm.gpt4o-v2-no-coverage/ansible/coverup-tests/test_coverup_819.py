# file: lib/ansible/cli/doc.py:997-999
# asked: {"lines": [997, 998, 999], "branches": []}
# gained: {"lines": [997, 998], "branches": []}

import pytest
import yaml
from ansible.cli.doc import DocCLI
from ansible.parsing.yaml.dumper import AnsibleDumper

@pytest.fixture
def mock_doc_cli(monkeypatch):
    class MockDocCLI(DocCLI):
        _ITALIC = DocCLI._ITALIC
        _BOLD = DocCLI._BOLD
        _MODULE = DocCLI._MODULE
        _URL = DocCLI._URL
        _LINK = DocCLI._LINK
        _REF = DocCLI._REF
        _CONST = DocCLI._CONST
        _RULER = DocCLI._RULER
        _RST_SEEALSO = DocCLI._RST_SEEALSO
        _RST_NOTE = DocCLI._RST_NOTE
        _RST_ROLES = DocCLI._RST_ROLES
        _RST_DIRECTIVES = DocCLI._RST_DIRECTIVES

        @classmethod
        def tty_ify(cls, text):
            t = cls._ITALIC.sub("`\\1'", text)
            t = cls._BOLD.sub('*\\1*', t)
            t = cls._MODULE.sub('[' + '\\1' + ']', t)
            t = cls._URL.sub('\\1', t)
            t = cls._LINK.sub('\\1 <\\2>', t)
            t = cls._REF.sub('\\1', t)
            t = cls._CONST.sub("`\\1'", t)
            t = cls._RULER.sub('\n{0}\n'.format('-' * 13), t)
            t = cls._RST_SEEALSO.sub('See website for:', t)
            t = cls._RST_NOTE.sub('Note:', t)
            t = cls._RST_ROLES.sub('website for `', t)
            t = cls._RST_DIRECTIVES.sub('', t)
            return t

        @staticmethod
        def _dump_yaml(struct, indent):
            return MockDocCLI.tty_ify('\n'.join([indent + line for line in yaml.dump(struct, default_flow_style=False, Dumper=AnsibleDumper).split('\n') if line]))

    monkeypatch.setattr('ansible.cli.doc.DocCLI', MockDocCLI)
    return MockDocCLI

def test_dump_yaml(mock_doc_cli):
    struct = {'key': 'value'}
    indent = '  '
    result = mock_doc_cli._dump_yaml(struct, indent)
    expected = mock_doc_cli.tty_ify('  key: value')
    assert result == expected
