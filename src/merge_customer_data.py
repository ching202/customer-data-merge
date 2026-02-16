from typing import List

def merge_customer_data(customerData1: List[int], m: int, customerData2: List[int], n: int) -> None:
    """
    Merges customerData2 into customerData1 in-place.
    customerData1 has length m+n, with last n slots as placeholders (0s).
    """
    i = m - 1
    j = n - 1
    k = m + n - 1

    # Merge from the back so we don't overwrite customerData1's valid values.
    while j >= 0:
        if i >= 0 and customerData1[i] > customerData2[j]:
            customerData1[k] = customerData1[i]
            i -= 1
        else:
            customerData1[k] = customerData2[j]
            j -= 1
        k -= 1
