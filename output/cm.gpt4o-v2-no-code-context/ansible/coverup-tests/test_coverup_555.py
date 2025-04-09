# file: lib/ansible/cli/arguments/option_helpers.py:373-378
# asked: {"lines": [373, 375, 376, 377, 378], "branches": []}
# gained: {"lines": [373, 375, 376, 377, 378], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_subset_options
import ansible.constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_subset_options_tags(parser):
    add_subset_options(parser)
    args = parser.parse_args(['--tags', 'test_tag'])
    assert args.tags == ['test_tag']

def test_add_subset_options_skip_tags(parser):
    add_subset_options(parser)
    args = parser.parse_args(['--skip-tags', 'skip_tag'])
    assert args.skip_tags == ['skip_tag']

def test_add_subset_options_default_tags(parser, monkeypatch):
    default_tags = ['default_tag']
    monkeypatch.setattr(C, 'TAGS_RUN', default_tags)
    add_subset_options(parser)
    args = parser.parse_args([])
    assert args.tags == default_tags

def test_add_subset_options_default_skip_tags(parser, monkeypatch):
    default_skip_tags = ['default_skip_tag']
    monkeypatch.setattr(C, 'TAGS_SKIP', default_skip_tags)
    add_subset_options(parser)
    args = parser.parse_args([])
    assert args.skip_tags == default_skip_tags
