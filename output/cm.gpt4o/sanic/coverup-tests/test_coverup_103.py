# file sanic/blueprint_group.py:202-223
# lines [215, 216, 217, 219, 220, 221, 222, 223]
# branches ['216->exit', '216->217', '219->220', '219->223']

import pytest
from unittest.mock import Mock
from sanic.blueprint_group import BlueprintGroup

class TestBlueprintGroup:
    @pytest.fixture
    def blueprint_group(self):
        class MockBlueprint:
            def middleware(self, fn, *args, **kwargs):
                self.fn = fn
                self.args = args
                self.kwargs = kwargs

        group = BlueprintGroup()
        group._blueprints = [MockBlueprint(), MockBlueprint()]
        return group

    def test_middleware_decorator_with_callable(self, blueprint_group):
        def sample_middleware(request):
            pass

        blueprint_group.middleware(sample_middleware)

        for blueprint in blueprint_group._blueprints:
            assert blueprint.fn == sample_middleware
            assert blueprint.args == ()
            assert blueprint.kwargs == {}

    def test_middleware_decorator_without_callable(self, blueprint_group):
        def sample_middleware(request):
            pass

        middleware_decorator = blueprint_group.middleware()
        middleware_decorator(sample_middleware)

        for blueprint in blueprint_group._blueprints:
            assert blueprint.fn == sample_middleware
            assert blueprint.args == ()
            assert blueprint.kwargs == {}
