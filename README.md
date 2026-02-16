# Customer Data Merge (In-Place Merge Sorted Arrays)

## Problem
Given two sorted arrays:
- **customerData1** (length `m + n`, where the first `m` elements are valid data and the last `n` elements are placeholders)
- **customerData2** (length `n`)

Merge `customerData2` into `customerData1` **in place** so that `customerData1` becomes a single sorted array in non-decreasing order.

## Clarifying Assumptions
- Both input arrays are already sorted in non-decreasing order.
- The merge must be done **in place** (no new array should be returned).
- Duplicate values are allowed and should remain in sorted order.
- If `m = 0` or `n = 0`, the function should still run without errors.
- The trailing zeros in `customerData1` are placeholders and should be ignored during the merge.

## Approach
This solution uses **three pointers** and merges from the **end of the array** to avoid overwriting valid data in `customerData1`.

- `i = m - 1` → last valid element in `customerData1`
- `j = n - 1` → last element in `customerData2`
- `k = m + n - 1` → last position in `customerData1`

While `j >= 0`, place the larger of `customerData1[i]` and `customerData2[j]` into `customerData1[k]`, then move pointers left.

## Diagram
See `diagrams/flowchart_merge_sorted_customer_data.png`

## Run Tests
```bash
pip install -r requirements.txt
pytest -q
