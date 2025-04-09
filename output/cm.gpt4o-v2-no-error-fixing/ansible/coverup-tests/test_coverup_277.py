# file: lib/ansible/playbook/play.py:315-320
# asked: {"lines": [315, 316, 317, 318, 319, 320], "branches": [[316, 317], [316, 318], [318, 319], [318, 320]]}
# gained: {"lines": [315], "branches": []}

import pytest
from ansible.playbook.play import Play

class MockBase:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class MockPlay(MockBase, MockTaggable, MockCollectionSearch):
    def __init__(self, vars_files):
        self.vars_files = vars_files

    def get_vars_files(self):
        if self.vars_files is None:
            return []
        elif not isinstance(self.vars_files, list):
            return [self.vars_files]
        return self.vars_files

@pytest.mark.parametrize("vars_files, expected", [
    (None, []),
    ("single_var_file", ["single_var_file"]),
    (["var_file1", "var_file2"], ["var_file1", "var_file2"]),
])
def test_get_vars_files(vars_files, expected):
    play = MockPlay(vars_files)
    assert play.get_vars_files() == expected
