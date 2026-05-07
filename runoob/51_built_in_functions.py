"""51 Python3 内置函数

来源: https://www.runoob.com/python3/python3-built-in-functions.html
可单独运行: python 51_built_in_functions.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留内置函数分类和速查表。"""
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


def demo_categories() -> None:
    """保留页面中的内置函数常见分类。"""
    show_table(
        ("分类", "代表函数"),
        [
            ("数值计算", "abs, round, min, max, sum, pow, divmod"),
            ("类型转换", "int, float, str, list, tuple, set, dict, bool"),
            ("迭代与函数式", "map, filter, zip, enumerate, iter, next, sorted"),
            ("反射与对象", "type, isinstance, getattr, setattr, hasattr, dir"),
            ("输入输出", "print, input, open"),
            ("作用域与调试", "locals, globals, vars, id, hash"),
        ],
    )


def demo_quick_table() -> None:
    """保留页面内置函数速查表。"""
    rows = [
        ("abs()", "dict()", "help()", "min()", "setattr()"),
        ("all()", "dir()", "hex()", "next()", "slice()"),
        ("any()", "divmod()", "id()", "object()", "sorted()"),
        ("ascii()", "enumerate()", "input()", "oct()", "staticmethod()"),
        ("bin()", "eval()", "int()", "open()", "str()"),
        ("bool()", "exec()", "isinstance()", "ord()", "sum()"),
        ("bytearray()", "filter()", "issubclass()", "pow()", "super()"),
        ("bytes()", "float()", "iter()", "print()", "tuple()"),
        ("callable()", "format()", "len()", "property()", "type()"),
        ("chr()", "frozenset()", "list()", "range()", "vars()"),
        ("classmethod()", "getattr()", "locals()", "repr()", "zip()"),
        ("compile()", "globals()", "map()", "reversed()", "__import__()"),
        ("complex()", "hasattr()", "max()", "round()", "reload()"),
        ("delattr()", "hash()", "memoryview()", "set()", ""),
    ]
    show_table(("列1", "列2", "列3", "列4", "列5"), rows)


def demo_numeric_functions() -> None:
    """执行数值计算类内置函数示例。"""
    print(abs(-10))
    print(round(3.14159, 2))
    print(min([3, 6, 2]))
    print(max([3, 6, 2]))
    print(sum([1, 2, 3]))
    print(pow(2, 3))
    print(divmod(10, 3))


def demo_type_conversion_functions() -> None:
    """执行类型转换类内置函数示例。"""
    print(int("123"))
    print(float("3.14"))
    print(str(123))
    print(list((1, 2, 3)))
    print(tuple([1, 2, 3]))
    print(set([1, 1, 2]))
    print(dict([("a", 1), ("b", 2)]))
    print(bool(""))


def demo_iteration_functions() -> None:
    """执行 map、filter、zip、enumerate、iter、next、sorted、reversed 示例。"""
    print(list(map(lambda x: x * 2, [1, 2, 3])))
    print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
    print(list(zip(["a", "b"], [1, 2])))
    for index, value in enumerate(["a", "b"]):
        print(index, value)
    iterator = iter([10, 20])
    print(next(iterator))
    print(next(iterator))
    print(sorted([3, 1, 2]))
    print(list(reversed([1, 2, 3])))


def demo_reflection_functions() -> None:
    """执行对象反射相关内置函数示例。"""

    class Demo:
        """用于反射示例的简单类。"""

        value = 1

    obj = Demo()
    print(type(obj))
    print(isinstance(obj, Demo))
    print(hasattr(obj, "value"))
    print(getattr(obj, "value"))
    setattr(obj, "name", "Runoob")
    print(obj.name)
    delattr(obj, "name")
    print("value" in dir(obj))


def demo_eval_exec_compile() -> None:
    """执行 eval、exec 和 compile 示例，并限制表达式内容保证安全。"""
    print(eval("1 + 2"))
    namespace: dict[str, object] = {}
    exec("result = 3 + 4", {}, namespace)
    print(namespace["result"])
    code = compile("x = 5\nprint(x)", "<demo>", "exec")
    exec(code, {})


def demo_locals_globals_debug() -> None:
    """保留页面笔记中的 locals 和 globals 调试说明。"""
    local_value = "local"
    local_vars = locals()
    print(local_vars["local_value"])
    print("show_section" in globals())


def main() -> None:
    """按内置函数页面顺序运行全部示例。"""
    print("Python3 内置函数")
    show_section("1. 常见分类")
    demo_categories()
    show_section("2. 函数速查表")
    demo_quick_table()
    show_section("3. 数值计算")
    demo_numeric_functions()
    show_section("4. 类型转换")
    demo_type_conversion_functions()
    show_section("5. 迭代与函数式")
    demo_iteration_functions()
    show_section("6. 反射与对象")
    demo_reflection_functions()
    show_section("7. eval、exec、compile")
    demo_eval_exec_compile()
    show_section("8. locals 和 globals")
    demo_locals_globals_debug()


if __name__ == "__main__":
    main()
