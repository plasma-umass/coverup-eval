# file mimesis/random.py:24-31
# lines [24, 25]
# branches []

import pytest
from mimesis.random import Random

def test_custom_random_class_methods():
    custom_random = Random()

    # Test if custom_random is an instance of Random
    assert isinstance(custom_random, Random)

    # Test if custom_random has the method 'random' from the superclass
    assert hasattr(custom_random, 'random')
    assert callable(getattr(custom_random, 'random'))

    # Test if custom_random has the method 'uniform' from the superclass
    assert hasattr(custom_random, 'uniform')
    assert callable(getattr(custom_random, 'uniform'))

    # Test if custom_random has the method 'randint' from the superclass
    assert hasattr(custom_random, 'randint')
    assert callable(getattr(custom_random, 'randint'))

    # Test if custom_random has the method 'choice' from the superclass
    assert hasattr(custom_random, 'choice')
    assert callable(getattr(custom_random, 'choice'))

    # Test if custom_random has the method 'randrange' from the superclass
    assert hasattr(custom_random, 'randrange')
    assert callable(getattr(custom_random, 'randrange'))

    # Test if custom_random has the method 'sample' from the superclass
    assert hasattr(custom_random, 'sample')
    assert callable(getattr(custom_random, 'sample'))

    # Test if custom_random has the method 'seed' from the superclass
    assert hasattr(custom_random, 'seed')
    assert callable(getattr(custom_random, 'seed'))

    # Test if custom_random has the method 'shuffle' from the superclass
    assert hasattr(custom_random, 'shuffle')
    assert callable(getattr(custom_random, 'shuffle'))

    # Test if custom_random has the method 'choices' from the superclass
    assert hasattr(custom_random, 'choices')
    assert callable(getattr(custom_random, 'choices'))

    # Test if custom_random has the method 'getrandbits' from the superclass
    assert hasattr(custom_random, 'getrandbits')
    assert callable(getattr(custom_random, 'getrandbits'))

    # Test if custom_random has the method 'betavariate' from the superclass
    assert hasattr(custom_random, 'betavariate')
    assert callable(getattr(custom_random, 'betavariate'))

    # Test if custom_random has the method 'expovariate' from the superclass
    assert hasattr(custom_random, 'expovariate')
    assert callable(getattr(custom_random, 'expovariate'))

    # Test if custom_random has the method 'gammavariate' from the superclass
    assert hasattr(custom_random, 'gammavariate')
    assert callable(getattr(custom_random, 'gammavariate'))

    # Test if custom_random has the method 'gauss' from the superclass
    assert hasattr(custom_random, 'gauss')
    assert callable(getattr(custom_random, 'gauss'))

    # Test if custom_random has the method 'lognormvariate' from the superclass
    assert hasattr(custom_random, 'lognormvariate')
    assert callable(getattr(custom_random, 'lognormvariate'))

    # Test if custom_random has the method 'normalvariate' from the superclass
    assert hasattr(custom_random, 'normalvariate')
    assert callable(getattr(custom_random, 'normalvariate'))

    # Test if custom_random has the method 'vonmisesvariate' from the superclass
    assert hasattr(custom_random, 'vonmisesvariate')
    assert callable(getattr(custom_random, 'vonmisesvariate'))

    # Test if custom_random has the method 'paretovariate' from the superclass
    assert hasattr(custom_random, 'paretovariate')
    assert callable(getattr(custom_random, 'paretovariate'))

    # Test if custom_random has the method 'weibullvariate' from the superclass
    assert hasattr(custom_random, 'weibullvariate')
    assert callable(getattr(custom_random, 'weibullvariate'))
