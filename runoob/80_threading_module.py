"""80 Python threading 模块

来源: https://www.runoob.com/python3/python-threading.html
可单独运行: python 80_threading_module.py
"""

from __future__ import annotations

import threading
import time


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 threading 类和方法说明。"""
    widths = [len(item) for item in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    def format_row(values: tuple[str, ...]) -> str:
        """格式化一行表格。"""
        return " | ".join(values[index].ljust(widths[index]) for index in range(len(values)))

    print(format_row(headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_row(row))


def demo_thread_function() -> None:
    """执行 Thread(target=...) 形式创建线程的示例。"""

    def print_numbers(name: str) -> None:
        """打印一组数字。"""
        for index in range(3):
            time.sleep(0.01)
            print(f"{name}: {index}")

    threads = [threading.Thread(target=print_numbers, args=(f"Thread-{i}",)) for i in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


class MyThread(threading.Thread):
    """继承 threading.Thread 的自定义线程。"""

    def __init__(self, name: str) -> None:
        """初始化线程名称。"""
        super().__init__(name=name)

    def run(self) -> None:
        """线程启动后执行的逻辑。"""
        for index in range(3):
            time.sleep(0.01)
            print(f"{self.name}: {index}")


def demo_thread_subclass() -> None:
    """执行继承 Thread 的示例。"""
    thread = MyThread("Worker")
    thread.start()
    thread.join()
    print("is_alive:", thread.is_alive())


def demo_lock_rlock() -> None:
    """演示 Lock 和 RLock 保护共享资源。"""
    lock = threading.Lock()
    counter = {"value": 0}

    def increase() -> None:
        """在锁保护下递增计数器。"""
        for _ in range(100):
            with lock:
                counter["value"] += 1

    threads = [threading.Thread(target=increase) for _ in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(counter["value"])

    rlock = threading.RLock()
    with rlock:
        with rlock:
            print("RLock 可重入")


def demo_event_condition_semaphore() -> None:
    """演示 Event、Condition 和 Semaphore 的基本用法。"""
    event = threading.Event()

    def waiter() -> None:
        """等待事件被设置。"""
        event.wait()
        print("event received")

    thread = threading.Thread(target=waiter)
    thread.start()
    event.set()
    thread.join()

    condition = threading.Condition()
    shared: list[str] = []

    def consumer() -> None:
        """等待共享列表有数据。"""
        with condition:
            condition.wait_for(lambda: bool(shared))
            print("condition data:", shared.pop())

    thread = threading.Thread(target=consumer)
    thread.start()
    with condition:
        shared.append("ready")
        condition.notify()
    thread.join()

    semaphore = threading.Semaphore(2)
    with semaphore:
        print("semaphore acquired")


def demo_timer_local_barrier() -> None:
    """演示 Timer、local 和 Barrier。"""
    timer_done = threading.Event()

    def timer_task() -> None:
        """Timer 到期后执行的任务。"""
        print("timer fired")
        timer_done.set()

    timer = threading.Timer(0.01, timer_task)
    timer.start()
    timer_done.wait()

    local_data = threading.local()
    local_data.value = "main"
    print(local_data.value)

    barrier = threading.Barrier(2)

    def pass_barrier(name: str) -> None:
        """等待两个线程都到达屏障。"""
        print(name, "before")
        barrier.wait()
        print(name, "after")

    threads = [threading.Thread(target=pass_barrier, args=(f"T{i}",)) for i in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def demo_classes_table() -> None:
    """保留 threading 常用类和函数表。"""
    show_table(
        ("类/函数", "说明"),
        [
            ("Thread", "表示一个线程"),
            ("Lock", "互斥锁"),
            ("RLock", "可重入锁"),
            ("Condition", "条件变量"),
            ("Semaphore", "信号量"),
            ("Event", "线程间事件通知"),
            ("Timer", "定时器线程"),
            ("Barrier", "屏障同步"),
            ("local", "线程局部数据"),
            ("active_count()", "当前活动线程数量"),
            ("current_thread()", "当前线程对象"),
            ("enumerate()", "活动线程列表"),
        ],
    )
    print(threading.active_count())
    print(threading.current_thread().name)
    print([thread.name for thread in threading.enumerate()])


def main() -> None:
    """按 threading 页面顺序运行全部示例。"""
    print("Python threading 模块")
    show_section("1. 函数线程")
    demo_thread_function()
    show_section("2. Thread 子类")
    demo_thread_subclass()
    show_section("3. Lock 和 RLock")
    demo_lock_rlock()
    show_section("4. Event、Condition、Semaphore")
    demo_event_condition_semaphore()
    show_section("5. Timer、local、Barrier")
    demo_timer_local_barrier()
    show_section("6. 常用类和函数")
    demo_classes_table()


if __name__ == "__main__":
    main()
