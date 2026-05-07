"""22 Python3 迭代器与生成器

来源: https://www.runoob.com/python3/python3-iterator-generator.html
可单独运行: python 22_iterators_generators.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def demo_iter_next() -> None:
    """执行页面中的 iter() 和 next() 示例，说明迭代器只能向前访问。"""
    values = [1, 2, 3, 4]
    iterator = iter(values)
    print(next(iterator))
    print(next(iterator))


def demo_for_iterator() -> None:
    """执行页面中用 for 遍历迭代器对象的示例。"""
    values = [1, 2, 3, 4]
    iterator = iter(values)
    for item in iterator:
        print(item, end=" ")
    print()


def demo_next_until_stop_iteration() -> None:
    """复刻 while + next() 示例，并捕获 StopIteration 避免退出整个脚本。"""
    values = [1, 2, 3, 4]
    iterator = iter(values)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("StopIteration: 迭代结束")
            break


class MyNumbers:
    """页面中的自定义迭代器：每次 next 返回递增数字。"""

    def __iter__(self) -> MyNumbers:
        """返回迭代器对象本身。"""
        self.current = 1
        return self

    def __next__(self) -> int:
        """返回下一个数字，并把内部状态加一。"""
        value = self.current
        self.current += 1
        return value


def demo_custom_iterator() -> None:
    """执行页面中自定义迭代器连续 next 五次的示例。"""
    myiter = iter(MyNumbers())
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))


class LimitedNumbers:
    """页面中的 StopIteration 示例：最多迭代 20 次。"""

    def __iter__(self) -> LimitedNumbers:
        """初始化计数器并返回自身。"""
        self.current = 1
        return self

    def __next__(self) -> int:
        """返回 1 到 20，超过后抛出 StopIteration。"""
        if self.current <= 20:
            value = self.current
            self.current += 1
            return value
        raise StopIteration


def demo_stop_iteration_class() -> None:
    """执行页面中 20 次后停止的自定义迭代器示例。"""
    for item in LimitedNumbers():
        print(item, end=" ")
    print()


def countdown(number: int):
    """页面中的 countdown 生成器：用 yield 逐步返回倒数值。"""
    while number > 0:
        yield number
        number -= 1


def demo_countdown_generator() -> None:
    """执行页面中 next() 与 for 混合消费生成器的示例。"""
    generator = countdown(5)
    print(next(generator))
    print(next(generator))
    print(next(generator))
    for value in generator:
        print(value)


def fibonacci(limit: int):
    """页面中的斐波那契生成器：yield 每一个序列值，超过 limit 后停止。"""
    a, b, counter = 0, 1, 0
    while True:
        if counter > limit:
            return
        yield a
        a, b = b, a + b
        counter += 1


def demo_fibonacci_generator() -> None:
    """执行页面中 yield 实现斐波那契数列的示例。"""
    for item in fibonacci(10):
        print(item, end=" ")
    print()


def main() -> None:
    """按迭代器与生成器页面顺序运行全部示例。"""
    print("Python3 迭代器与生成器")

    show_section("1. iter() 与 next()")
    demo_iter_next()

    show_section("2. for 遍历迭代器")
    demo_for_iterator()

    show_section("3. next() 直到 StopIteration")
    demo_next_until_stop_iteration()

    show_section("4. 自定义迭代器")
    demo_custom_iterator()

    show_section("5. StopIteration")
    demo_stop_iteration_class()

    show_section("6. countdown 生成器")
    demo_countdown_generator()

    show_section("7. 斐波那契生成器")
    demo_fibonacci_generator()


if __name__ == "__main__":
    main()
