# file cookiecutter/repository.py:31-46
# lines [31, 37, 38, 42, 43, 44, 46]
# branches ['37->38', '37->42', '43->44', '43->46']

import pytest
from cookiecutter.repository import expand_abbreviations

def test_expand_abbreviations():
    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}.git',
        'cookiecutter': 'https://github.com/cookiecutter/cookiecutter.git'
    }

    # Test case where template is in abbreviations
    assert expand_abbreviations('cookiecutter', abbreviations) == 'https://github.com/cookiecutter/cookiecutter.git'

    # Test case where template has a prefix in abbreviations
    assert expand_abbreviations('gh:myrepo', abbreviations) == 'https://github.com/myrepo.git'
    assert expand_abbreviations('bb:myrepo', abbreviations) == 'https://bitbucket.org/myrepo.git'

    # Test case where template is not in abbreviations and has no prefix in abbreviations
    assert expand_abbreviations('unknown:myrepo', abbreviations) == 'unknown:myrepo'
    assert expand_abbreviations('unknown', abbreviations) == 'unknown'
