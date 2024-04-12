# file pysnooper/tracer.py:257-287
# lines [267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 281, 283, 285]
# branches ['269->270', '280->281', '282->283', '284->285']

import pytest
from pysnooper.tracer import Tracer
import inspect

def test_generator_wrapper():
    tracer = Tracer()

    def my_generator():
        yield 1
        yield 2
        raise Exception("Test Exception")

    wrapped_gen = tracer._wrap_function(my_generator)

    assert inspect.isgeneratorfunction(wrapped_gen), "Wrapped function should be a generator"

    gen = wrapped_gen()

    with pytest.raises(Exception) as exc_info:
        next(gen)
        next(gen)
        next(gen)  # This should raise the "Test Exception"

    assert str(exc_info.value) == "Test Exception", "The exception raised from the generator should be propagated"

    # Cleanup
    tracer.target_codes.remove(my_generator.__code__)
