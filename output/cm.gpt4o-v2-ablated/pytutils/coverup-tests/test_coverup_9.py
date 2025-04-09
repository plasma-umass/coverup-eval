# file: pytutils/lazy/simple_import.py:5-11
# asked: {"lines": [5, 6, 11], "branches": []}
# gained: {"lines": [5, 6, 11], "branches": []}

import pytest
from pytutils.lazy.simple_import import _LazyModuleMarker

def test_lazy_module_marker_instance():
    marker_instance = _LazyModuleMarker()
    assert isinstance(marker_instance, _LazyModuleMarker)
