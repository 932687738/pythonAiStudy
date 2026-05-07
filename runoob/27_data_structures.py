"""27 Python3 数据结构

来源: https://www.runoob.com/python3/python3-data-structure.html
可单独运行: python 27_data_structures.py
"""

from __future__ import annotations

from collections import deque


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的列表方法和遍历技巧说明。"""
    widths = [len(item) for item in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    def format_row(values: tuple[str, ...]) -> str:
        return " | ".join(values[index].ljust(widths[index]) for index in range(len(values)))

    print(format_row(headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_row(row))


def demo_list_methods_table() -> None:
    """保留列表方法表，并执行页面中的列表方法示例。"""
    show_table(
        ("方法", "描述"),
        [
            ("append(x)", "把元素添加到列表结尾"),
            ("extend(L)", "通过另一个列表扩充当前列表"),
            ("insert(i, x)", "在指定位置插入元素"),
            ("remove(x)", "删除第一个值为 x 的元素"),
            ("pop([i])", "移除指定位置元素并返回"),
            ("clear()", "移除列表所有项"),
            ("index(x)", "返回第一个值为 x 的元素索引"),
            ("count(x)", "返回 x 出现的次数"),
            ("sort()", "原地排序"),
            ("reverse()", "原地反转"),
            ("copy()", "返回浅复制"),
        ],
    )
    values = [66.25, 333, 333, 1, 1234.5]
    print(values.count(333), values.count(66.25), values.count("x"))
    values.insert(2, -1)
    values.append(333)
    print(values)
    print(values.index(333))
    values.remove(333)
    print(values)
    values.reverse()
    print(values)
    values.sort()
    print(values)


class Stack:
    """使用列表实现栈，后进先出。"""

    def __init__(self) -> None:
        """初始化空栈。"""
        self.stack: list[object] = []

    def push(self, item: object) -> None:
        """把元素压入栈顶。"""
        self.stack.append(item)

    def pop(self) -> object:
        """弹出栈顶元素，空栈时抛出异常。"""
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")

    def peek(self) -> object:
        """查看栈顶元素但不移除。"""
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self) -> bool:
        """判断栈是否为空。"""
        return len(self.stack) == 0

    def size(self) -> int:
        """返回栈大小。"""
        return len(self.stack)


def demo_stack() -> None:
    """执行页面中 Stack 类的使用示例。"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("栈顶元素:", stack.peek())
    print("栈大小:", stack.size())
    print("弹出元素:", stack.pop())
    print("栈是否为空:", stack.is_empty())
    print("栈大小:", stack.size())


class Queue:
    """使用列表实现队列，先进先出。"""

    def __init__(self) -> None:
        """初始化空队列。"""
        self.queue: list[object] = []

    def enqueue(self, item: object) -> None:
        """将元素添加到队尾。"""
        self.queue.append(item)

    def dequeue(self) -> object:
        """移除并返回队首元素。"""
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self) -> object:
        """查看队首元素但不移除。"""
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("peek from empty queue")

    def is_empty(self) -> bool:
        """判断队列是否为空。"""
        return len(self.queue) == 0

    def size(self) -> int:
        """返回队列大小。"""
        return len(self.queue)


def demo_queue() -> None:
    """执行页面中 Queue 类和 collections.deque 队列示例。"""
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    print("队首元素:", queue.peek())
    print("队列大小:", queue.size())
    print("移除的元素:", queue.dequeue())
    print("队列是否为空:", queue.is_empty())
    print("队列大小:", queue.size())

    fast_queue = deque(["Eric", "John", "Michael"])
    fast_queue.append("Terry")
    fast_queue.append("Graham")
    print(fast_queue.popleft())
    print(fast_queue.popleft())
    print(fast_queue)


def demo_list_comprehensions() -> None:
    """保留列表推导式章节中的乘三、嵌套、过滤和复杂表达式示例。"""
    vec = [2, 4, 6]
    print([3 * x for x in vec])
    print([[x, x**2] for x in vec])
    freshfruit = ["  banana", "  loganberry ", "passion fruit  "]
    print([weapon.strip() for weapon in freshfruit])
    print([3 * x for x in vec if x > 3])
    print([3 * x for x in vec if x < 2])
    vec1 = [2, 4, 6]
    vec2 = [4, 3, -9]
    print([x * y for x in vec1 for y in vec2])
    print([x + y for x in vec1 for y in vec2])
    print([vec1[i] * vec2[i] for i in range(len(vec1))])
    print([str(round(355 / 113, i)) for i in range(1, 6)])


def demo_nested_list_comprehension() -> None:
    """演示 3x4 矩阵转置的三种写法。"""
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print([[row[i] for row in matrix] for i in range(4)])

    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    print(transposed)

    transposed = []
    for i in range(4):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print(transposed)


def demo_del_statement() -> None:
    """演示 del 语句按索引、切片删除列表，以及清空列表。"""
    values = [-1, 1, 66.25, 333, 333, 1234.5]
    del values[0]
    print(values)
    del values[2:4]
    print(values)
    del values[:]
    print(values)


def demo_tuple_set_dict() -> None:
    """保留元组、集合和字典结构示例。"""
    t = 12345, 54321, "hello!"
    print(t[0])
    print(t)
    u = t, (1, 2, 3, 4, 5)
    print(u)

    basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
    print(basket)
    print("orange" in basket)
    a = set("abracadabra")
    b = set("alacazam")
    print(a - b)
    print(a | b)
    print(a & b)
    print(a ^ b)
    print({x for x in "abracadabra" if x not in "abc"})

    tel = {"jack": 4098, "sape": 4139}
    tel["guido"] = 4127
    print(tel)
    print(tel["jack"])
    del tel["sape"]
    tel["irv"] = 4127
    print(tel)
    print(list(tel.keys()))
    print(sorted(tel.keys()))
    print("guido" in tel)
    print("jack" not in tel)
    print(dict([("sape", 4139), ("guido", 4127), ("jack", 4098)]))
    print({x: x**2 for x in (2, 4, 6)})
    print(dict(sape=4139, guido=4127, jack=4098))


def demo_looping_techniques() -> None:
    """保留遍历技巧：items、enumerate、zip、reversed、sorted。"""
    knights = {"gallahad": "the pure", "robin": "the brave"}
    for key, value in knights.items():
        print(key, value)

    for index, value in enumerate(["tic", "tac", "toe"]):
        print(index, value)

    questions = ["name", "quest", "favorite color"]
    answers = ["lancelot", "the holy grail", "blue"]
    for question, answer in zip(questions, answers):
        print("What is your {0}?  It is {1}.".format(question, answer))

    for item in reversed(range(1, 10, 2)):
        print(item)

    basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
    for fruit in sorted(set(basket)):
        print(fruit)


def main() -> None:
    """按数据结构页面顺序运行全部示例。"""
    print("Python3 数据结构")

    show_section("1. 列表方法")
    demo_list_methods_table()

    show_section("2. 栈")
    demo_stack()

    show_section("3. 队列")
    demo_queue()

    show_section("4. 列表推导式")
    demo_list_comprehensions()

    show_section("5. 嵌套列表解析")
    demo_nested_list_comprehension()

    show_section("6. del 语句")
    demo_del_statement()

    show_section("7. 元组、集合和字典")
    demo_tuple_set_dict()

    show_section("8. 遍历技巧")
    demo_looping_techniques()


if __name__ == "__main__":
    main()
