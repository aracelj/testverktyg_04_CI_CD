import pytest
from src.algorithms.bubble_sort import (bubble_sort)


# ------------------
# Integration Test
# ------------------
@pytest.mark.integration
def test_bubble_sort_with_real_data():
    """Integration test"""
    import random
    data = random.sample(range(100), 20)  # 20 unique random numbers
    sorted_data = bubble_sort(data.copy())
    assert sorted_data == sorted(data)  # compare with Python's built-in sort