# file: pytutils/lazy/simple_import.py:5-11
# asked: {"lines": [5, 6, 11], "branches": []}
# gained: {"lines": [5, 6, 11], "branches": []}

import pytest
from pytutils.lazy.simple_import import _LazyModuleMarker

def test_lazy_module_marker_instance():
    marker_instance = _LazyModuleMarker()
    assert isinstance(marker_instance, _LazyModuleMarker)

def test_lazy_module_marker_docstring():
    expected_docstring = (
        "A marker to indicate a LazyModule type.\n"
        "    Allows us to check module's with `isinstance(mod, _LazyModuleMarker)`\n"
        "    to know if the module is lazy."
    )
    assert _LazyModuleMarker.__doc__.strip() == expected_docstring
