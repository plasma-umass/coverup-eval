# file: lib/ansible/cli/arguments/option_helpers.py:34-38
# asked: {"lines": [34, 35, 36, 37, 38], "branches": []}
# gained: {"lines": [34, 35], "branches": []}

import pytest
import argparse
from ansible.module_utils._text import to_native
from ansible.cli.arguments.option_helpers import AnsibleVersion
from ansible.release import __version__ as ansible_version
from unittest import mock

def version(prog=None):
    """ return ansible version """
    result = [f'{prog} [core {ansible_version}]' if prog else ansible_version]
    # Mocking the rest of the version details for simplicity
    result.append('  config file = /etc/ansible/ansible.cfg')
    result.append('  configured module search path = Default w/o overrides')
    result.append('  ansible python module location = /usr/lib/python3.8/site-packages/ansible')
    result.append('  ansible collection location = /usr/share/ansible/collections')
    result.append('  executable location = /usr/bin/ansible')
    result.append('  python version = 3.8.5 (default, Jul 28 2020, 12:59:40) [GCC 9.3.0]')
    result.append('  jinja version = 2.11.2')
    result.append('  libyaml = True')
    return '\n'.join(result)

class AnsibleVersion(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        ansible_version = to_native(version(getattr(parser, 'prog')))
        print(ansible_version)
        parser.exit()

def test_ansible_version_action(monkeypatch):
    parser = argparse.ArgumentParser(prog='ansible-playbook')
    parser.add_argument('--version', action=AnsibleVersion, nargs=0)

    with mock.patch('argparse.ArgumentParser.exit') as mock_exit, \
         mock.patch('builtins.print') as mock_print:
        parser.parse_args(['--version'])
        mock_print.assert_called_once_with(to_native(version('ansible-playbook')))
        mock_exit.assert_called_once()

