"""24 Python3 函数

来源: https://www.runoob.com/python3/python3-function.html
可单独运行: python 24_functions.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的函数规则和参数类型表。"""
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


def hello() -> None:
    """页面第一个函数示例：输出 Hello World。"""
    print("Hello World!")


def max_value(a: int, b: int) -> int:
    """比较两个数，并返回较大的数。"""
    if a > b:
        return a
    return b


def area(width: int, height: int) -> int:
    """计算矩形面积。"""
    return width * height


def print_welcome(name: str) -> None:
    """输出欢迎信息。"""
    print("Welcome", name)


def printme(text: str) -> None:
    """打印任何传入的字符串。"""
    print(text)


def demo_definition_and_call() -> None:
    """演示 def 定义函数、调用函数、参数传入和 return 返回值。"""
    show_table(
        ("规则", "说明"),
        [
            ("def", "函数代码块以 def 关键词开头"),
            ("参数", "参数放在圆括号中"),
            ("文档字符串", "函数第一行可放说明文字"),
            ("冒号和缩进", "函数体以冒号开始并缩进"),
            ("return", "结束函数并可返回值"),
        ],
    )
    hello()
    print(max_value(4, 5))
    print_welcome("Runoob")
    print("width =", 4, " height =", 5, " area =", area(4, 5))
    printme("我要调用用户自定义函数!")
    printme("再次调用同一函数")


def change_number(a: int) -> None:
    """演示不可变对象传参：函数内重新赋值不会影响外部变量。"""
    print("函数内修改前 id:", id(a))
    a = 10
    print("函数内修改后 id:", id(a))


def change_list(mylist: list[object]) -> None:
    """演示可变对象传参：函数内修改列表会影响外部列表。"""
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)


def demo_mutable_immutable() -> None:
    """复刻参数传递章节：不可变对象和可变对象在函数中的表现不同。"""
    number = 1
    print("调用前 id:", id(number))
    change_number(number)
    print("调用后 number:", number)

    mylist: list[object] = [10, 20, 30]
    change_list(mylist)
    print("函数外取值: ", mylist)


def demo_required_argument() -> None:
    """演示必需参数数量不正确时会抛出 TypeError。"""
    try:
        printme()  # type: ignore[call-arg]
    except TypeError as exc:
        print(f"缺少必需参数: {exc.__class__.__name__}: {exc}")


def printinfo(name: str, age: int = 35) -> None:
    """演示关键字参数和默认参数。"""
    print("名字: ", name)
    print("年龄: ", age)


def demo_keyword_and_default_argument() -> None:
    """演示关键字参数可改变传入顺序，默认参数可省略。"""
    printme(text="菜鸟教程")
    printinfo(age=50, name="runoob")
    printinfo(age=50, name="runoob")
    print("------------------------")
    printinfo(name="runoob")


def print_variable_args(arg1: str, *vartuple: object) -> None:
    """演示不定长参数 *args，接收额外的位置参数。"""
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)


def print_keyword_args(arg1: str, **vardict: object) -> None:
    """演示不定长关键字参数 **kwargs，接收额外的命名参数。"""
    print("输出: ")
    print(arg1)
    print(vardict)


def demo_variable_arguments() -> None:
    """复刻不定长参数章节的 *args 和 **kwargs 示例。"""
    print_variable_args(70, 60, 50)  # type: ignore[arg-type]
    print_keyword_args(1, a=2, b=3)  # type: ignore[arg-type]


def demo_keyword_only_arguments() -> None:
    """演示单独星号 * 后的参数必须使用关键字传入。"""

    def keyword_only(a: int, b: int, *, c: int) -> None:
        """c 是关键字专用参数。"""
        print(a + b + c)

    keyword_only(1, 2, c=3)
    try:
        keyword_only(1, 2, 3)  # type: ignore[misc]
    except TypeError as exc:
        print(f"关键字专用参数不能位置传入: {exc.__class__.__name__}")


def demo_anonymous_function() -> None:
    """保留函数页里的 lambda 匿名函数示例。"""
    sum_value = lambda arg1, arg2: arg1 + arg2
    print("相加后的值为 : ", sum_value(10, 20))
    print("相加后的值为 : ", sum_value(20, 20))


def sum_numbers(arg1: int, arg2: int) -> int:
    """演示 return 语句返回计算结果。"""
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


def demo_return_statement() -> None:
    """执行 return 示例，并在函数外接收返回值。"""
    total = sum_numbers(10, 20)
    print("函数外 : ", total)


def demo_global_and_nonlocal() -> None:
    """演示 global 和 nonlocal 关键字改变变量作用域绑定。"""
    global global_number
    global_number = 0

    def set_global() -> None:
        """修改模块级变量。"""
        global global_number
        global_number = 10

    def outer() -> int:
        """通过 nonlocal 修改外层函数变量。"""
        value = 1

        def inner() -> None:
            """修改 outer 中的 value。"""
            nonlocal value
            value = 2

        inner()
        return value

    set_global()
    print(global_number)
    print(outer())


def main() -> None:
    """按函数页面顺序运行全部示例。"""
    print("Python3 函数")

    show_section("1. 定义和调用函数")
    demo_definition_and_call()

    show_section("2. 参数传递")
    demo_mutable_immutable()

    show_section("3. 必需参数")
    demo_required_argument()

    show_section("4. 关键字参数和默认参数")
    demo_keyword_and_default_argument()

    show_section("5. 不定长参数")
    demo_variable_arguments()

    show_section("6. 强制关键字参数")
    demo_keyword_only_arguments()

    show_section("7. 匿名函数")
    demo_anonymous_function()

    show_section("8. return 语句")
    demo_return_statement()

    show_section("9. global 和 nonlocal")
    demo_global_and_nonlocal()


if __name__ == "__main__":
    main()
