"""
My little Stack
"""
from typing import Any

my_stack = []  # в качестве стека список, чтобы функции работали как стек  список. Вершина справа. Как из списка достать последний элемент,


def push(elem: Any) -> None:
    """
    Operation that add element to stack
добавляет элемент на вершину стека
    :param elem: element to be pushed
    :return: Nothing
    """
    my_stack.append(elem)
    print(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.
  #принимает индекс должны вернуть элемент  с вершины - элемент. Из стека не удаляется. Из стека не удаляет
  достать элемент последнйи и удалить его
    :return: popped element
    """
    if my_stack:
        last_elem = my_stack.pop() # моделировать ситуации, забирает элемент с конца и удаляет его   проверить длину списка. если стек не пустой, то забираем элемент и возвращаем этот элемент
        return last_elem


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.
    увидеть элемент без его снятия
    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    len(my_stack)
    if ind <= (len(my_stack)-1):
        print(my_stack[-ind])
        print(ind)
        return my_stack[-1-ind]


def clear() -> None:
    """
    Clear my stack
    должно чистить функцию
    :return: None
    """

    my_stack.clear()
    print(my_stack)
    return None

if __name__ == '__main__':
    push(1)
    print(my_stack)
    push(100)
    push(1000)
    print(my_stack)
    pop()
    peek(0)
    clear()




    # новое задание от Master
    # перед checkout обязательно commit cntrl+k


