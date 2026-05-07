"""35 Python3 命名空间/作用域

来源: https://www.runoob.com/python3/python3-namespace-scope.html
可单独运行: python 35_namespaces_scope.py
"""

from __future__ import annotations

import builtins


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的命名空间和作用域说明。"""
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


def demo_namespace_table() -> None:
    """保留三类命名空间说明。"""
    show_table(
        ("命名空间", "说明", "例子"),
        [
            ("内置名称", "Python 语言内置名称", "abs, Exception, len"),
            ("全局名称", "模块中定义的名称", "函数、类、模块变量"),
            ("局部名称", "函数中定义的名称", "参数、局部变量"),
        ],
    )


def demo_namespace_lifecycle() -> None:
    """演示局部命名空间在函数执行期间存在，外部无法直接访问局部变量。"""
    var1 = 5

    def some_func() -> None:
        """创建局部变量和内嵌局部变量。"""
        var2 = 6

        def some_inner_func() -> None:
            """创建更内层的局部变量。"""
            var3 = 7
            print("inner locals:", locals())

        some_inner_func()
        print("func locals:", locals())

    some_func()
    print("global-like var1:", var1)


def demo_scope_table() -> None:
    """保留 LEGB 四类作用域说明。"""
    show_table(
        ("作用域", "名称", "说明"),
        [
            ("L", "Local", "当前函数的局部作用域"),
            ("E", "Enclosing", "外层非全局函数作用域"),
            ("G", "Global", "当前模块全局作用域"),
            ("B", "Built-in", "Python 内置作用域"),
        ],
    )


def demo_legb_lookup() -> None:
    """演示 Python 按 Local -> Enclosing -> Global -> Built-in 查找变量。"""
    name = "global name"

    def outer() -> None:
        """创建 enclosing 作用域。"""
        name = "enclosing name"

        def inner() -> None:
            """创建 local 作用域并访问多层名称。"""
            name = "local name"
            print(name)
            print(len([1, 2, 3]))

        inner()

    outer()
    print(name)
    print("len 来自 builtins:", builtins.len("abc"))


total = 0


def sum_demo(arg1: int, arg2: int) -> int:
    """复刻页面 total 示例：函数内 total 是局部变量。"""
    total = arg1 + arg2
    print("函数内是局部变量 : ", total)
    return total


def demo_local_global_same_name() -> None:
    """演示局部变量会遮蔽同名全局变量。"""
    sum_demo(10, 20)
    print("函数外是全局变量 : ", total)


def demo_global_keyword() -> None:
    """演示 global 关键字修改全局变量。"""
    num = 1
    print("局部演示初始 num:", num)

    global global_num
    global_num = 1

    def fun1() -> None:
        """使用 global 修改模块级变量。"""
        global global_num
        print(global_num)
        global_num = 123
        print(global_num)

    fun1()
    print(global_num)


def demo_nonlocal_keyword() -> None:
    """演示 nonlocal 修改外层非全局作用域变量。"""

    def outer() -> None:
        """外层函数持有 num。"""
        num = 10

        def inner() -> None:
            """内层函数通过 nonlocal 修改 outer 的 num。"""
            nonlocal num
            num = 100
            print(num)

        inner()
        print(num)

    outer()


def demo_unbound_local_error() -> None:
    """演示未使用 global 时修改同名全局变量会触发 UnboundLocalError。"""
    a = 10

    def test() -> None:
        """这个函数会因局部变量未赋值就读取而报错。"""
        a = a + 1  # type: ignore[has-type]
        print(a)

    try:
        test()
    except UnboundLocalError as exc:
        print(f"UnboundLocalError: {exc}")

    def fixed_by_argument(value: int) -> None:
        """通过参数传递避免作用域修改问题。"""
        value = value + 1
        print(value)

    fixed_by_argument(a)


def main() -> None:
    """按命名空间和作用域页面顺序运行全部示例。"""
    print("Python3 命名空间和作用域")

    show_section("1. 命名空间")
    demo_namespace_table()

    show_section("2. 命名空间生命周期")
    demo_namespace_lifecycle()

    show_section("3. LEGB 作用域")
    demo_scope_table()

    show_section("4. LEGB 查找顺序")
    demo_legb_lookup()

    show_section("5. 局部和全局同名")
    demo_local_global_same_name()

    show_section("6. global")
    demo_global_keyword()

    show_section("7. nonlocal")
    demo_nonlocal_keyword()

    show_section("8. UnboundLocalError")
    demo_unbound_local_error()


if __name__ == "__main__":
    main()
