import pytest
from src.merge_customer_data import merge_customer_data

# -------------------------
# Normal cases (3+)
# -------------------------

def test_example_1():
    a = [101, 104, 107, 0, 0, 0]
    merge_customer_data(a, 3, [102, 105, 108], 3)
    assert a == [101, 102, 104, 105, 107, 108]

def test_overlap_values():
    a = [1, 3, 7, 0, 0, 0]
    merge_customer_data(a, 3, [2, 6, 8], 3)
    assert a == [1, 2, 3, 6, 7, 8]

def test_duplicates():
    a = [2, 2, 3, 0, 0, 0]
    merge_customer_data(a, 3, [2, 3, 3], 3)
    assert a == [2, 2, 2, 3, 3, 3]

# -------------------------
# Edge cases (3+)
# -------------------------

def test_n_zero_no_merge():
    a = [103]
    merge_customer_data(a, 1, [], 0)
    assert a == [103]

def test_m_zero_all_from_second_array():
    a = [0, 0, 0]
    merge_customer_data(a, 0, [1, 2, 3], 3)
    assert a == [1, 2, 3]

def test_second_all_smaller():
    a = [5, 6, 7, 0, 0, 0]
    merge_customer_data(a, 3, [1, 2, 3], 3)
    assert a == [1, 2, 3, 5, 6, 7]

def test_second_all_larger():
    a = [1, 2, 3, 0, 0, 0]
    merge_customer_data(a, 3, [4, 5, 6], 3)
    assert a == [1, 2, 3, 4, 5, 6]
