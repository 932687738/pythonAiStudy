"""33 Python3 错误和异常

来源: https://www.runoob.com/python3/python3-errors-execptions.html
可单独运行: python 33_errors_and_exceptions.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def demo_syntax_error() -> None:
    """复刻语法错误示例，用 compile 捕获 SyntaxError 使脚本可继续运行。"""
    source = "while True print('Hello world')"
    try:
        compile(source, "<syntax-demo>", "exec")
    except SyntaxError as exc:
        print(f"SyntaxError: {exc.msg}")
        print(f"错误行: {exc.text.strip() if exc.text else source}")


def demo_common_exceptions() -> None:
    """执行页面中的 ZeroDivisionError、NameError 和 TypeError 示例，并捕获异常。"""
    examples = [
        ("10 * (1/0)", lambda: 10 * (1 / 0)),
        ("4 + spam*3", lambda: eval("4 + spam*3")),
        ("'2' + 2", lambda: "2" + 2),  # type: ignore[operator]
    ]
    for label, func in examples:
        try:
            print(func())
        except Exception as exc:
            print(f"{label} -> {exc.__class__.__name__}: {exc}")


def demo_try_except_value_error() -> None:
    """复刻 try/except 输入整数示例，用预设输入模拟 ValueError 后成功。"""
    for raw in ["abc", "42"]:
        try:
            value = int(raw)
            print("合法数字:", value)
            break
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")


def demo_multiple_except() -> None:
    """演示多个 except 分支分别处理 OSError、ValueError 和未知异常。"""
    try:
        raise OSError("mock file error")
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception:
        print("Unexpected error:", sys.exc_info()[0])

    try:
        int("not-number")
    except (RuntimeError, TypeError, NameError):
        print("Runtime/Type/Name error")
    except ValueError:
        print("ValueError 被单独处理")


def demo_try_except_else() -> None:
    """演示 try/except...else：没有异常时读取文件行数。"""
    with tempfile.TemporaryDirectory() as directory:
        file_path = Path(directory) / "sample.txt"
        file_path.write_text("one\ntwo\n", encoding="utf-8")
        for path in [file_path, Path(directory) / "missing.txt"]:
            try:
                file = open(path, "r", encoding="utf-8")
            except OSError:
                print("cannot open", path.name)
            else:
                print(path.name, "has", len(file.readlines()), "lines")
                file.close()


def this_fails() -> None:
    """页面示例中的间接抛出异常函数。"""
    _ = 1 / 0


def demo_nested_exception_call() -> None:
    """演示 try 可以捕获被调用函数内部抛出的异常。"""
    try:
        this_fails()
    except ZeroDivisionError as err:
        print("Handling run-time error:", err)


def demo_finally() -> None:
    """演示 finally 无论是否发生异常都会执行。"""
    try:
        raise AssertionError("assert demo")
    except AssertionError as error:
        print(error)
    else:
        print("没有异常")
    finally:
        print("这句话，无论异常是否发生都会执行。")


def demo_raise() -> None:
    """演示 raise 抛出异常，并在本示例中捕获以保持脚本继续运行。"""
    x = 10
    try:
        if x > 5:
            raise Exception("x 不能大于 5。x 的值为: {}".format(x))
    except Exception as exc:
        print(exc)


class MyError(Exception):
    """页面中的用户自定义异常，保存 value 属性。"""

    def __init__(self, value: object) -> None:
        """初始化自定义异常值。"""
        self.value = value

    def __str__(self) -> str:
        """返回异常字符串表现。"""
        return repr(self.value)


def demo_custom_exception() -> None:
    """执行自定义异常示例。"""
    try:
        raise MyError(2 * 2)
    except MyError as err:
        print("My exception occurred, value:", err.value)


class Error(Exception):
    """模块级异常基类。"""


class InputError(Error):
    """输入表达式错误。"""

    def __init__(self, expression: str, message: str) -> None:
        """保存错误表达式和说明。"""
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """状态转换错误。"""

    def __init__(self, previous: str, next_state: str, message: str) -> None:
        """保存状态转换上下文。"""
        self.previous = previous
        self.next = next_state
        self.message = message


def demo_exception_hierarchy() -> None:
    """保留页面中为模块建立异常基类和子类的做法。"""
    error = InputError("x + y", "变量 y 未定义")
    transition = TransitionError("draft", "published", "缺少审核步骤")
    print(error.expression, error.message)
    print(transition.previous, transition.next, transition.message)


def divide(x: object, y: object) -> None:
    """页面中的 divide 示例，展示 except、else、finally 的组合。"""
    try:
        result = x / y  # type: ignore[operator]
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


def demo_cleanup_behavior() -> None:
    """演示定义清理行为，所有路径都会执行 finally。"""
    divide(2, 1)
    divide(2, 0)
    try:
        divide("2", "1")
    except TypeError as exc:
        print(f"未被 divide 捕获的异常继续向外传播: {exc.__class__.__name__}")


def demo_assert() -> None:
    """保留 assert 断言示例。"""
    assert True
    try:
        assert 1 == 2, "1 不等于 2"
    except AssertionError as exc:
        print(f"AssertionError: {exc}")


def demo_with_cleanup() -> None:
    """演示 with 语句提供预定义清理行为，文件会自动关闭。"""
    with tempfile.TemporaryDirectory() as directory:
        file_path = Path(directory) / "myfile.txt"
        file_path.write_text("Runoob\nPython\n", encoding="utf-8")
        with open(file_path, encoding="utf-8") as file:
            for line in file:
                print(line, end="")
        print("文件自动关闭:", file.closed)


def main() -> None:
    """按错误和异常页面顺序运行全部示例。"""
    print("Python3 错误和异常")

    show_section("1. 语法错误")
    demo_syntax_error()

    show_section("2. 常见异常")
    demo_common_exceptions()

    show_section("3. try/except")
    demo_try_except_value_error()

    show_section("4. 多个 except")
    demo_multiple_except()

    show_section("5. try/except...else")
    demo_try_except_else()

    show_section("6. 捕获被调用函数内部异常")
    demo_nested_exception_call()

    show_section("7. finally")
    demo_finally()

    show_section("8. raise")
    demo_raise()

    show_section("9. 自定义异常")
    demo_custom_exception()

    show_section("10. 异常层级")
    demo_exception_hierarchy()

    show_section("11. 清理行为")
    demo_cleanup_behavior()

    show_section("12. assert")
    demo_assert()

    show_section("13. with 预定义清理")
    demo_with_cleanup()


if __name__ == "__main__":
    main()
