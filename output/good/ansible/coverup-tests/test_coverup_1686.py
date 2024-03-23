# file lib/ansible/utils/version.py:42-82
# lines [52, 56, 60, 63, 66, 67, 68, 69, 70, 71, 73, 76, 79, 82]
# branches ['55->56', '57->60', '66->67', '66->68', '68->69', '68->70', '70->71', '70->73']

import pytest
from ansible.utils.version import _Alpha, _Numeric

@pytest.fixture
def alpha_instance():
    return _Alpha('a')

@pytest.fixture
def numeric_instance():
    return _Numeric(1)

def test_alpha_comparison(alpha_instance, numeric_instance):
    # Test __repr__
    assert repr(alpha_instance) == repr('a')

    # Test __eq__
    assert alpha_instance == 'a'
    assert alpha_instance == _Alpha('a')
    assert not (alpha_instance == 'b')
    assert not (alpha_instance == _Alpha('b'))
    assert not (alpha_instance == 1)

    # Test __ne__
    assert not (alpha_instance != 'a')
    assert not (alpha_instance != _Alpha('a'))
    assert alpha_instance != 'b'
    assert alpha_instance != _Alpha('b')
    assert alpha_instance != 1

    # Test __lt__
    assert alpha_instance < 'b'
    assert alpha_instance < _Alpha('b')
    with pytest.raises(ValueError):
        assert alpha_instance < 1
    assert not (alpha_instance < 'a')
    assert not (alpha_instance < _Alpha('a'))
    assert not (alpha_instance < numeric_instance)

    # Test __le__
    assert alpha_instance <= 'a'
    assert alpha_instance <= _Alpha('a')
    assert alpha_instance <= 'b'
    assert not (alpha_instance <= '0')

    # Test __gt__
    assert alpha_instance > '0'
    assert not (alpha_instance > 'a')
    assert not (alpha_instance > _Alpha('a'))
    assert not (alpha_instance > 'b')

    # Test __ge__
    assert alpha_instance >= 'a'
    assert alpha_instance >= _Alpha('a')
    assert not (alpha_instance >= 'b')
    assert alpha_instance >= '0'
