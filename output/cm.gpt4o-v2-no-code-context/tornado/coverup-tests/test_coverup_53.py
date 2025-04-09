# file: tornado/util.py:411-432
# asked: {"lines": [411, 423, 425, 426, 427, 430, 431, 432], "branches": [[423, 425], [423, 430]]}
# gained: {"lines": [411, 423, 425, 426, 427, 430, 431, 432], "branches": [[423, 425], [423, 430]]}

import pytest
from tornado.util import ArgReplacer

class TestArgReplacer:
    @pytest.fixture
    def arg_replacer(self):
        def dummy_func():
            pass
        replacer = ArgReplacer(dummy_func, 'test_arg')
        return replacer

    def test_replace_positional_arg(self, arg_replacer):
        arg_replacer.arg_pos = 1
        args = (1, 2, 3)
        kwargs = {}
        new_value = 99

        old_value, new_args, new_kwargs = arg_replacer.replace(new_value, args, kwargs)

        assert old_value == 2
        assert new_args == [1, 99, 3]
        assert new_kwargs == {}

    def test_replace_keyword_arg(self, arg_replacer):
        args = (1, 2, 3)
        kwargs = {'test_arg': 42}
        new_value = 99

        old_value, new_args, new_kwargs = arg_replacer.replace(new_value, args, kwargs)

        assert old_value == 42
        assert new_args == args
        assert new_kwargs == {'test_arg': 99}

    def test_replace_missing_keyword_arg(self, arg_replacer):
        args = (1, 2, 3)
        kwargs = {}
        new_value = 99

        old_value, new_args, new_kwargs = arg_replacer.replace(new_value, args, kwargs)

        assert old_value is None
        assert new_args == args
        assert new_kwargs == {'test_arg': 99}
