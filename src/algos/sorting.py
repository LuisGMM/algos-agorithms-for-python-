
from typing import Optional, Union, List

Real = Union[int, float]

lst1 = [1, 3, 0.3, 23, 4, 3214, 5]
lst2 = [5, 2, 4, 6, 1, 3]
lst3 = [31, 41, 59, 26, 41, 58]


def insertion_sort(lst: List[Real]) -> None:
    """It sorts in place the list `lst` by the insertion sort algorithm (nondecreasing order).

    It scans the list, for each element, from the start to an element.
    During the way, if the element to be sorted is smaller than some element
    in the list (element b), we move the sorting element before the element b.

    See Also
    ----------
    Introduction to Algorithm page 3.

    Parameters
    ----------
    lst : list
        list to be sorted in place
    """
