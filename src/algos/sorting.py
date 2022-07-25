
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

    for i in range(1, len(lst)):
        for j in range(i):

            if i == j:
                continue

            sorting_item = lst[i]
            if lst[i] < lst[j]:
                del lst[i]
                lst.insert(j, sorting_item)


def inverted_insertion_sort(lst: List[Real]) -> None:
    """It sorts in place the list `lst` by the insertion sort algorithm (nonincreasing order).

    It scans the list, for each element, from the start to an element.
    During the way, if the element to be sorted is smaller than some element
    in the list (element b), we move the sorting element before the element b.

    See Also
    ----------
    Introduction to Algorithm page 5.

    Parameters
    ----------
    lst : list
        list to be sorted in place
    """

    for i in range(1, len(lst)):
        for j in range(i):

            if i == j:
                continue

            sorting_item = lst[i]
            if lst[i] > lst[j]:
                del lst[i]
                lst.insert(j, sorting_item)


# TODO: Finish this function.
def selection_sort(lst: List[Real], n: Optional[int] = None) -> List[Real]:
    """
    See Also
    ----------
    Introduction to Algorithm page 10.
    """

    n = len(lst) if n is None else n

    lst_b = []
    smallest_temp = lst[0]

    for _ in range(n):
        for i in range(1, n):

            if lst[i] < smallest_temp and smallest_temp not in lst_b:
                smallest_temp = lst[i]

        lst_b.append(smallest_temp)

    return lst_b


print(selection_sort(lst1))