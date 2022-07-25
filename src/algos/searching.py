
from typing import Union, List, Optional

Real = Union[int, float]


def linear_search(lst: List[Real], v: Real) -> Optional[int]:
    """Searches for an element `v` in a list `lst`, returning its index if found.

    See Also
    ----------
    Introduction to Algorithm page 5.

    Parameters
    ----------
    lst : List[Real]
        list to search in.
    v : Real
        element to be searched for in the list.

    Returns
    -------
    Optional[int]
        Index of the element found in the list.
    """

    for i in range(len(lst)):
        if lst[i] == v:
            return i

print(linear_search([1, 4], 1))
print(linear_search([1, 4], 6))