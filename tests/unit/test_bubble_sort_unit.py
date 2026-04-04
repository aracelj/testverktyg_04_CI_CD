import pytest
from src.algorithms.bubble_sort import bubble_sort

# ------------------
# Unit Test
# ------------------
@pytest.mark.unit
def test_bubble_sort_basic():
    """Test bubble_sort with a small, fixed list."""
    data = [5, 3, 2, 4, 1]
    sorted_data = bubble_sort(data.copy())
    assert sorted_data == [1, 2, 3, 4, 5]

