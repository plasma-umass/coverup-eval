# file: flutils/setuputils/cfg.py:32-41
# asked: {"lines": [], "branches": [[40, 35]]}
# gained: {"lines": [], "branches": [[40, 35]]}

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command_section

def test_each_setup_cfg_command_section():
    parser = ConfigParser()
    parser.add_section('setup.command.install')
    parser.add_section('setup.command.build')
    parser.add_section('other.section')

    sections = list(_each_setup_cfg_command_section(parser))

    assert sections == [
        ('setup.command.install', 'install'),
        ('setup.command.build', 'build')
    ]

def test_each_setup_cfg_command_section_empty_command():
    parser = ConfigParser()
    parser.add_section('setup.command.')

    sections = list(_each_setup_cfg_command_section(parser))

    assert sections == []

def test_each_setup_cfg_command_section_no_command():
    parser = ConfigParser()
    parser.add_section('other.section')

    sections = list(_each_setup_cfg_command_section(parser))

    assert sections == []
