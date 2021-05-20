import unittest
import Tasks.a0_my_stack as my_stack


class MyTestCase(unittest.TestCase):  #запуск тестирования функции
    def setUp(self):  #встроенная функция в классе предподготовка
        my_stack.clear()

    def test_clear(self):  # все функции несут смысл по тестированию, при автоматическом тестировании - в последнюю очередь
        my_stack.push(3)  # положить
        my_stack.clear()  # очистить

        self.assertIsNone(my_stack.pop(), msg="Did you clear the stack?") # проверяет, в тот момент когда выполняем ПОП - достаем элемент, а стек пустой, должно вернуться NONE, то что вернулось - действительно NONE

    def test_empty_stack(self):
        self.assertIsNone(my_stack.pop(), msg="Should return None if no elements")

    def test_push_pop(self):
        initial_elem = 3
        my_stack.push(initial_elem)

        self.assertEqual(initial_elem, my_stack.pop())  #левый аргумент равен правому, достаем 3. То что положили и то что дстали - Tru

    def test_multiple_pushes_pops(self):
        items = [i for i in range(10)]

        for i in items:
            my_stack.push(i)

        received_items = []
        for _ in items:
            received_items.append(my_stack.pop())

        self.assertEqual(list(reversed(items)), received_items)

    def test_peek(self):
        my_stack.push(7)
        my_stack.push(3)
        my_stack.push(5)

        self.assertEqual(5, my_stack.peek())
        self.assertEqual(3, my_stack.peek(1))
        self.assertEqual(5, my_stack.peek())

        self.assertIsNone(my_stack.peek(100), msg="Should return None if no elements")


if __name__ == '__main__':
    unittest.main()
