"""34 Python3 面向对象

来源: https://www.runoob.com/python3/python3-class.html
可单独运行: python 34_object_oriented_programming.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的类专有方法表。"""
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


class MyClass:
    """页面中最简单的类示例。"""

    i = 12345

    def f(self) -> str:
        """返回 hello world。"""
        return "hello world"


def demo_class_and_instance() -> None:
    """演示类定义、类属性、实例化和方法调用。"""
    instance = MyClass()
    print(instance.i)
    print(instance.f())


class Complex:
    """页面中的 __init__ 构造方法示例。"""

    def __init__(self, realpart: float, imagpart: float) -> None:
        """初始化复数的实部和虚部。"""
        self.r = realpart
        self.i = imagpart


def demo_init_method() -> None:
    """执行构造函数示例。"""
    x = Complex(3.0, -4.5)
    print(x.r, x.i)


class Test:
    """演示 self 代表类的实例。"""

    def prt(self) -> None:
        """输出 self 和 self.__class__。"""
        print(self)
        print(self.__class__)


def demo_self() -> None:
    """执行 self 示例。"""
    test = Test()
    test.prt()


class People:
    """页面中的父类 People。"""

    name = ""
    age = 0
    __weight = 0

    def __init__(self, name: str, age: int, weight: int) -> None:
        """初始化姓名、年龄和私有体重。"""
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self) -> None:
        """输出 People 的说话内容。"""
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


class Student(People):
    """页面中的 Student 子类，继承 People。"""

    grade = ""

    def __init__(self, name: str, age: int, weight: int, grade: str) -> None:
        """初始化父类字段并设置年级。"""
        People.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self) -> None:
        """重写父类 speak 方法。"""
        print("%s 说: 我 %d 岁了，我在读 %s 年级" % (self.name, self.age, self.grade))


def demo_inheritance() -> None:
    """演示单继承和方法重写。"""
    student = Student("ken", 10, 60, "三")
    student.speak()


class Speaker:
    """多继承示例中的 Speaker 类。"""

    topic = ""
    name = ""

    def __init__(self, name: str, topic: str) -> None:
        """初始化演讲者姓名和主题。"""
        self.name = name
        self.topic = topic

    def speak(self) -> None:
        """输出演讲内容。"""
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


class Sample(Speaker, Student):
    """多继承示例，优先使用继承列表中靠前类的方法。"""

    def __init__(self, name: str, age: int, weight: int, grade: str, topic: str) -> None:
        """同时初始化 Student 和 Speaker 所需属性。"""
        Student.__init__(self, name, age, weight, grade)
        Speaker.__init__(self, name, topic)


def demo_multiple_inheritance() -> None:
    """演示多继承及方法解析顺序。"""
    sample = Sample("Tim", 25, 80, "四", "Python")
    sample.speak()
    print([cls.__name__ for cls in Sample.__mro__])


class Parent:
    """方法重写示例中的父类。"""

    def my_method(self) -> None:
        """父类方法。"""
        print("调用父类方法")


class Child(Parent):
    """方法重写示例中的子类。"""

    def my_method(self) -> None:
        """子类重写父类方法。"""
        print("调用子类方法")


def demo_method_override() -> None:
    """执行方法重写示例。"""
    child = Child()
    child.my_method()
    super(Child, child).my_method()


class JustCounter:
    """私有属性示例，__secretCount 会触发名称改写。"""

    __secretCount = 0
    publicCount = 0

    def count(self) -> None:
        """分别修改私有变量和公开变量。"""
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


def demo_private_attributes() -> None:
    """演示类的私有属性不能通过原名直接访问。"""
    counter = JustCounter()
    counter.count()
    counter.count()
    print(counter.publicCount)
    try:
        print(counter.__secretCount)  # type: ignore[attr-defined]
    except AttributeError as exc:
        print(f"访问私有变量失败: {exc.__class__.__name__}: {exc}")


class Site:
    """私有方法示例。"""

    def __init__(self, name: str, url: str) -> None:
        """初始化公开 name 和私有 url。"""
        self.name = name
        self.__url = url

    def who(self) -> None:
        """输出公开和私有属性。"""
        print("name : ", self.name)
        print("url : ", self.__url)

    def __foo(self) -> None:
        """私有方法。"""
        print("这是私有方法")

    def foo(self) -> None:
        """公共方法，内部调用私有方法。"""
        print("这是公共方法")
        self.__foo()


def demo_private_methods() -> None:
    """演示私有方法只能在类内部直接访问。"""
    site = Site("菜鸟教程", "www.runoob.com")
    site.who()
    site.foo()
    try:
        site.__foo()  # type: ignore[attr-defined]
    except AttributeError as exc:
        print(f"访问私有方法失败: {exc.__class__.__name__}: {exc}")


def demo_special_methods_table() -> None:
    """保留类的专有方法表。"""
    show_table(
        ("专有方法", "说明"),
        [
            ("__init__", "构造函数，在生成对象时调用"),
            ("__del__", "析构函数，释放对象时使用"),
            ("__repr__", "对象打印和转换"),
            ("__setitem__", "按索引赋值"),
            ("__getitem__", "按索引获取值"),
            ("__len__", "获得长度"),
            ("__call__", "函数调用"),
            ("__add__", "加运算"),
            ("__sub__", "减运算"),
            ("__mul__", "乘运算"),
            ("__truediv__", "除运算"),
            ("__mod__", "求余运算"),
            ("__pow__", "乘方"),
        ],
    )


class Vector:
    """运算符重载示例：二维向量相加。"""

    def __init__(self, a: int, b: int) -> None:
        """初始化向量两个分量。"""
        self.a = a
        self.b = b

    def __str__(self) -> str:
        """返回向量字符串表示。"""
        return "Vector (%d, %d)" % (self.a, self.b)

    def __add__(self, other: Vector) -> Vector:
        """重载 + 运算符。"""
        return Vector(self.a + other.a, self.b + other.b)


def demo_operator_overload() -> None:
    """执行运算符重载示例。"""
    v1 = Vector(2, 10)
    v2 = Vector(5, -2)
    print(v1 + v2)


def main() -> None:
    """按面向对象页面顺序运行全部示例。"""
    print("Python3 面向对象")

    show_section("1. 类和实例")
    demo_class_and_instance()

    show_section("2. 构造方法")
    demo_init_method()

    show_section("3. self")
    demo_self()

    show_section("4. 继承")
    demo_inheritance()

    show_section("5. 多继承")
    demo_multiple_inheritance()

    show_section("6. 方法重写")
    demo_method_override()

    show_section("7. 私有属性")
    demo_private_attributes()

    show_section("8. 私有方法")
    demo_private_methods()

    show_section("9. 类的专有方法")
    demo_special_methods_table()

    show_section("10. 运算符重载")
    demo_operator_overload()


if __name__ == "__main__":
    main()
