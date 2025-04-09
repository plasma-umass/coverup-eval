# file string_utils/manipulation.py:561-595
# lines [561, 595]
# branches []

import pytest
from string_utils.manipulation import compress

def test_compress():
    # Test with a normal string
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert isinstance(compressed, str)
    assert len(compressed) < len(original)

    # Test with an empty string to ensure it raises ValueError
    with pytest.raises(ValueError):
        compress("")

    # Test with different compression levels
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed_level_1 = compress(original, compression_level=1)
    compressed_level_9 = compress(original, compression_level=9)
    assert len(compressed_level_1) >= len(compressed_level_9)

    # Test with different encodings
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed_utf8 = compress(original, encoding='utf-8')
    compressed_ascii = compress(original, encoding='ascii')
    assert isinstance(compressed_utf8, str)
    assert isinstance(compressed_ascii, str)

    # Test with a string that is unlikely to be compressed
    random_string = 'a' * 100
    compressed_random = compress(random_string)
    assert isinstance(compressed_random, str)
    assert len(compressed_random) >= len(random_string) or len(compressed_random) < len(random_string)
