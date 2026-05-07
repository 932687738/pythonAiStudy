"""26 Python3 装饰器

来源: https://www.runoob.com/python3/python-decorators.html
可单独运行: python 26_decorators.py
"""

from __future__ import annotations

import functools
import time


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def my_decorator(func):
    """基础装饰器：在原函数执行前后打印日志。"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """包装函数：扩展原函数调用。"""
        print("在原函数之前执行")
        result = func(*args, **kwargs)
        print("在原函数之后执行")
        return result

    return wrapper


@my_decorator
def say_hello() -> None:
    """页面中的 say_hello 示例。"""
    print("Hello!")


def demo_basic_decorator() -> None:
    """执行基础装饰器示例，并说明 @ 语法糖等价于重新赋值。"""
    say_hello()
    print("@my_decorator 等价于 say_hello = my_decorator(say_hello)")


@my_decorator
def greet(name: str) -> None:
    """带参数函数被装饰时，wrapper 需要接收 *args 和 **kwargs。"""
    print(f"Hello, {name}!")


def demo_decorator_with_args() -> None:
    """执行带参数函数的装饰器示例。"""
    greet("Alice")


def timer(func):
    """性能分析装饰器：统计函数执行耗时。"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """记录开始和结束时间，并返回原函数结果。"""
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.6f} 秒")
        return result

    return wrapper


@timer
def compute_sum(limit: int) -> int:
    """用于性能分析示例的求和函数。"""
    return sum(range(limit))


def demo_timer_decorator() -> None:
    """执行页面应用场景中的性能分析装饰器示例。"""
    print(compute_sum(10000))


def require_role(role: str):
    """权限控制装饰器工厂：根据角色决定是否执行函数。"""

    def decorator(func):
        """接收目标函数并返回包装函数。"""

        @functools.wraps(func)
        def wrapper(user_role: str):
            """检查角色后决定是否调用原函数。"""
            if user_role != role:
                print("权限不足")
                return None
            return func(user_role)

        return wrapper

    return decorator


@require_role("admin")
def delete_data(user_role: str) -> str:
    """权限控制示例中的敏感操作。"""
    return f"{user_role} 已删除数据"


def demo_decorator_factory() -> None:
    """执行带参数装饰器示例：装饰器外层先接收配置。"""
    print(delete_data("guest"))
    print(delete_data("admin"))


def log_class(cls):
    """类装饰器：包装类并在 display 前后打印日志。"""

    class Wrapper:
        """代理原始类实例的包装类。"""

        def __init__(self, *args, **kwargs):
            """实例化原始类并保存。"""
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            """未定义属性转发给原始实例。"""
            return getattr(self.wrapped, name)

        def display(self):
            """在原始 display 前后加入输出。"""
            print(f"调用 {cls.__name__}.display() 前")
            self.wrapped.display()
            print(f"调用 {cls.__name__}.display() 后")

    return Wrapper


@log_class
class MyClass:
    """页面中的类装饰器目标类。"""

    def display(self) -> None:
        """输出类方法内容。"""
        print("这是 MyClass 的 display 方法")


def demo_class_decorator() -> None:
    """执行类装饰器示例。"""
    obj = MyClass()
    obj.display()


class SingletonDecorator:
    """类形式装饰器：让目标类变成单例模式。"""

    def __init__(self, cls):
        """保存被装饰的类。"""
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        """拦截实例化过程，确保只创建一个实例。"""
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance


@SingletonDecorator
class Database:
    """页面中的单例 Database 示例。"""

    def __init__(self) -> None:
        """初始化数据库对象。"""
        print("Database 初始化")


def demo_callable_class_decorator() -> None:
    """执行实现 __call__ 的类装饰器示例。"""
    db1 = Database()
    db2 = Database()
    print(db1 is db2)


class BuiltinDecoratorDemo:
    """演示 staticmethod、classmethod 和 property 三个内置装饰器。"""

    def __init__(self) -> None:
        """初始化内部 name 属性。"""
        self._name = ""

    @staticmethod
    def static_method() -> None:
        """静态方法不需要实例或类作为第一个参数。"""
        print("This is a static method.")

    @classmethod
    def class_method(cls) -> None:
        """类方法第一个参数是类本身。"""
        print(f"This is a class method of {cls.__name__}.")

    @property
    def name(self) -> str:
        """把方法变成可读取属性。"""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """给 property 添加设置逻辑。"""
        self._name = value


def demo_builtin_decorators() -> None:
    """执行页面中的内置装饰器示例。"""
    BuiltinDecoratorDemo.static_method()
    BuiltinDecoratorDemo.class_method()
    obj = BuiltinDecoratorDemo()
    obj.name = "Alice"
    print(obj.name)


def decorator1(func):
    """第一个堆叠装饰器。"""

    @functools.wraps(func)
    def wrapper():
        """输出 Decorator 1 后调用下一个包装函数。"""
        print("Decorator 1")
        func()

    return wrapper


def decorator2(func):
    """第二个堆叠装饰器。"""

    @functools.wraps(func)
    def wrapper():
        """输出 Decorator 2 后调用原函数。"""
        print("Decorator 2")
        func()

    return wrapper


@decorator1
@decorator2
def stacked_hello() -> None:
    """页面中的多个装饰器堆叠示例。"""
    print("Hello!")


def demo_stacked_decorators() -> None:
    """执行多个装饰器堆叠示例，展示从下到上应用、从上到下执行。"""
    stacked_hello()


def main() -> None:
    """按装饰器页面顺序运行全部示例。"""
    print("Python3 装饰器")

    show_section("1. 基础装饰器")
    demo_basic_decorator()

    show_section("2. 带参数函数的装饰器")
    demo_decorator_with_args()

    show_section("3. 性能分析装饰器")
    demo_timer_decorator()

    show_section("4. 带参数装饰器")
    demo_decorator_factory()

    show_section("5. 类装饰器")
    demo_class_decorator()

    show_section("6. 类形式装饰器")
    demo_callable_class_decorator()

    show_section("7. 内置装饰器")
    demo_builtin_decorators()

    show_section("8. 多个装饰器堆叠")
    demo_stacked_decorators()


if __name__ == "__main__":
    main()
