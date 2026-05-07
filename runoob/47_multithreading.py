"""47 Python3 多线程

来源: https://www.runoob.com/python3/python3-multithreading.html
可单独运行: python 47_multithreading.py
"""

from __future__ import annotations

import queue
import threading
import time


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留线程模块和方法说明。"""
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


def print_time(thread_name: str, delay: float, count_limit: int = 3) -> None:
    """页面 _thread 示例中的线程函数，缩短延迟并限制次数避免无限运行。"""
    count = 0
    while count < count_limit:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))


def demo_thread_function() -> None:
    """复刻两个线程同时打印时间的逻辑，使用 threading.Thread 便于 join。"""
    threads = [
        threading.Thread(target=print_time, args=("Thread-1", 0.01)),
        threading.Thread(target=print_time, args=("Thread-2", 0.02)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


class MyThread(threading.Thread):
    """页面中的 threading.Thread 子类写法。"""

    def __init__(self, thread_id: int, name: str, delay: float) -> None:
        """初始化线程编号、名称和延迟。"""
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.delay = delay

    def run(self) -> None:
        """线程启动后执行的逻辑。"""
        print("开始线程：" + self.name)
        print_time(self.name, self.delay, 2)
        print("退出线程：" + self.name)


def demo_thread_class() -> None:
    """执行 Thread 子类示例。"""
    thread1 = MyThread(1, "Thread-1", 0.01)
    thread2 = MyThread(2, "Thread-2", 0.02)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("退出主线程")


def demo_thread_methods_table() -> None:
    """保留 threading.Thread 常用方法表。"""
    show_table(
        ("方法", "描述"),
        [
            ("start()", "启动线程活动"),
            ("run()", "线程活动方法，可在子类中重写"),
            ("join([time])", "等待线程终止"),
            ("is_alive()", "判断线程是否仍在运行"),
            ("getName()/name", "获取线程名"),
            ("setName()/name=", "设置线程名"),
        ],
    )


class QueueWorker(threading.Thread):
    """页面队列示例中的工作线程。"""

    def __init__(self, thread_id: int, name: str, work_queue: queue.Queue[str]) -> None:
        """保存线程信息和共享队列。"""
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.work_queue = work_queue

    def run(self) -> None:
        """持续处理队列中的任务，遇到哨兵值 None 退出。"""
        print("开启线程：" + self.name)
        while True:
            data = self.work_queue.get()
            try:
                if data is None:
                    break
                print("%s processing %s" % (self.name, data))
                time.sleep(0.01)
            finally:
                self.work_queue.task_done()
        print("退出线程：" + self.name)


def demo_queue_threads() -> None:
    """复刻线程队列示例，使用 Queue.join 和哨兵值优雅退出。"""
    thread_names = ["Thread-1", "Thread-2", "Thread-3"]
    name_list = ["One", "Two", "Three", "Four", "Five"]
    work_queue: queue.Queue[str | None] = queue.Queue(10)
    threads = [QueueWorker(index + 1, name, work_queue) for index, name in enumerate(thread_names)]
    for thread in threads:
        thread.start()
    for word in name_list:
        work_queue.put(word)
    for _ in threads:
        work_queue.put(None)
    work_queue.join()
    for thread in threads:
        thread.join()
    print("退出主线程")


def demo_lock() -> None:
    """演示 Lock 保护共享计数器，保留线程同步思想。"""
    lock = threading.Lock()
    counter = {"value": 0}

    def increase() -> None:
        """安全递增共享计数器。"""
        for _ in range(100):
            with lock:
                counter["value"] += 1

    threads = [threading.Thread(target=increase) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("counter:", counter["value"])


def main() -> None:
    """按多线程页面顺序运行全部示例。"""
    print("Python3 多线程")
    show_section("1. 线程函数")
    demo_thread_function()
    show_section("2. Thread 子类")
    demo_thread_class()
    show_section("3. Thread 方法")
    demo_thread_methods_table()
    show_section("4. 队列多线程")
    demo_queue_threads()
    show_section("5. 线程锁")
    demo_lock()


if __name__ == "__main__":
    main()
