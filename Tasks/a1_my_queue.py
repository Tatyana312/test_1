"""
My little Queue
"""
from typing import Any


queue = []

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue
    добавить элемент на первое место
    сложить списки [0] + [1,2,3] или (insert pop(0))  (append pop(last elem))
    :param elem: element to be added
    :return: Nothing
    """
    my_queue.append(elem)
    print(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.
    элемент удаляется

    :return: dequeued element
    """


    return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    print(ind)
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    return None

if __name__ == '__main__':
