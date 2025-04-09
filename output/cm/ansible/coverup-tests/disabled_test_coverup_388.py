# file lib/ansible/playbook/play.py:121-131
# lines [121, 123, 124, 126, 127, 129, 131]
# branches ['123->124', '123->126', '126->127', '126->129']

import pytest
from ansible.playbook.play import Play

# Mocking the Base and CollectionSearch classes since they are not provided
class Base:
    def __init__(self):
        pass

class CollectionSearch:
    def __init__(self):
        pass

# Test function to cover the case when self.name is not set and self.hosts is a sequence
def test_play_get_name_with_sequence_hosts():
    play = Play()
    play.name = None
    play.hosts = ['host1', 'host2', 'host3']
    assert play.get_name() == 'host1,host2,host3'

# Test function to cover the case when self.name is not set and self.hosts is not a sequence
def test_play_get_name_with_non_sequence_hosts():
    play = Play()
    play.name = None
    play.hosts = 'all'
    assert play.get_name() == 'all'

# Test function to cover the case when self.name is already set
def test_play_get_name_with_existing_name():
    play = Play()
    play.name = 'existing_name'
    play.hosts = 'all'
    assert play.get_name() == 'existing_name'
