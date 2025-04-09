# file: pytutils/lazy/lazy_regex.py:140-145
# asked: {"lines": [140, 142, 143, 144], "branches": []}
# gained: {"lines": [140, 142, 143, 144], "branches": []}

import pytest
import pickle
from pytutils.lazy.lazy_regex import LazyRegex

class TestLazyRegex:
    @pytest.fixture
    def lazy_regex_instance(self):
        instance = LazyRegex()
        instance._regex_args = ('pattern',)
        instance._regex_kwargs = {'flags': 0}
        return instance

    def test_getstate(self, lazy_regex_instance):
        state = lazy_regex_instance.__getstate__()
        assert state == {
            "args": ('pattern',),
            "kwargs": {'flags': 0}
        }

    def test_pickle_lazy_regex(self, lazy_regex_instance):
        pickled_instance = pickle.dumps(lazy_regex_instance)
        unpickled_instance = pickle.loads(pickled_instance)
        assert unpickled_instance._regex_args == ('pattern',)
        assert unpickled_instance._regex_kwargs == {'flags': 0}
