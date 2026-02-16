# Customer Data Merge (In-Place Merge Sorted Arrays)

## Problem
Given two sorted arrays:
- customerData1 (length m+n, first m are valid, last n are placeholders)
- customerData2 (length n)

Merge customerData2 into customerData1 in-place so customerData1 becomes fully sorted.

## Clarifying Assumptions
- Arrays are already sorted in non-decreasing order.
- We must modify customerData1 in place (no returning a new array).
- Duplicates are allowed and should remain.
- If m=0 or n=0, handle without errors.

## Approach
Use three pointers and merge from the end:
- i = m-1 (end of valid customerData1)
- j = n-1 (end of customerData2)
- k = m+n-1 (end of customerData1)

##
Fill customerData1 from the back to avoid overwriting.
##

Do we need to modify customerData1 in place?
Yes — result must be stored inside customerData1.

Are arrays already sorted in non-decreasing order?
Yes.

Can there be duplicates?
Yes — keep duplicates, still sorted.

What if n = 0 or m = 0?
Handle cleanly (no crash).

Are the trailing zeros always placeholders?
Yes — only the first m values in customerData1 matter.

Time: O(m + n) (each element is placed once)

Space: O(1) (in-place merge, only pointers)

## Diagram
See `diagrams/flowchart_merge_sorted_arrays.png`

## Run Tests
```bash
pip install -r requirements.txt
pytest -q

