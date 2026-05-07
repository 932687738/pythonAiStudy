"""74 Python queue 模块

来源: https://www.runoob.com/python3/python-queue.html
可单独运行: python 74_queue_module.py
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
    """用纯文本表格保留 queue 类、方法和参数表。"""
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


def demo_queue_types_table() -> None:
    """保留 queue 模块核心类表。"""
    show_table(
        ("类", "说明", "适用场景"),
        [
            ("queue.Queue", "先进先出 FIFO", "通用任务队列"),
            ("queue.LifoQueue", "后进先出 LIFO", "栈式任务"),
            ("queue.PriorityQueue", "按优先级取出", "优先级任务"),
            ("queue.SimpleQueue", "更简单的 FIFO", "不需要高级功能"),
        ],
    )


def demo_fifo_queue() -> None:
    """执行 Queue 先进先出示例。"""
    q: queue.Queue[int] = queue.Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    print(q.get())
    print(q.get())
    print(q.get())


def demo_lifo_queue() -> None:
    """执行 LifoQueue 后进先出示例。"""
    q: queue.LifoQueue[int] = queue.LifoQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    print(q.get())
    print(q.get())
    print(q.get())


def demo_priority_queue() -> None:
    """执行 PriorityQueue 优先级队列示例。"""
    q: queue.PriorityQueue[tuple[int, str]] = queue.PriorityQueue()
    q.put((3, "Low priority"))
    q.put((1, "High priority"))
    q.put((2, "Medium priority"))
    print(q.get())
    print(q.get())
    print(q.get())


def demo_methods_and_nonblocking() -> None:
    """演示 put、get、qsize、empty、full、非阻塞获取和异常。"""
    q: queue.Queue[str] = queue.Queue(maxsize=2)
    q.put("task1")
    q.put("task2")
    print(q.qsize())
    print(q.full())
    print(q.get())
    print(q.empty())
    try:
        empty_queue: queue.Queue[str] = queue.Queue()
        empty_queue.get_nowait()
    except queue.Empty:
        print("队列为空")


def demo_producer_consumer() -> None:
    """执行页面中的生产者消费者模型，使用 None 作为结束信号。"""
    q: queue.Queue[int | None] = queue.Queue()

    def producer() -> None:
        """生产 5 个任务。"""
        for i in range(5):
            print(f"生产 {i}")
            q.put(i)
            time.sleep(0.01)

    def consumer() -> None:
        """消费任务直到收到 None。"""
        while True:
            item = q.get()
            try:
                if item is None:
                    break
                print(f"消费 {item}")
            finally:
                q.task_done()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    q.join()
    q.put(None)
    consumer_thread.join()


def demo_methods_table() -> None:
    """保留 queue 通用方法和阻塞参数表。"""
    show_table(
        ("方法/参数", "说明", "示例"),
        [
            ("put(item)", "放入元素", "q.put('task1')"),
            ("get()", "取出并移除元素", "item = q.get()"),
            ("empty()", "判断是否为空", "q.empty()"),
            ("full()", "判断是否已满", "q.full()"),
            ("qsize()", "返回当前大小", "q.qsize()"),
            ("task_done()", "标记任务完成", "q.task_done()"),
            ("join()", "等待所有任务完成", "q.join()"),
            ("block", "是否阻塞", "q.get(block=False)"),
            ("timeout", "阻塞超时时间", "q.put(x, timeout=5)"),
        ],
    )


def main() -> None:
    """按 queue 页面顺序运行全部示例。"""
    print("Python queue 模块")
    show_section("1. 队列类型")
    demo_queue_types_table()
    show_section("2. Queue")
    demo_fifo_queue()
    show_section("3. LifoQueue")
    demo_lifo_queue()
    show_section("4. PriorityQueue")
    demo_priority_queue()
    show_section("5. 常用方法")
    demo_methods_and_nonblocking()
    show_section("6. 生产者消费者")
    demo_producer_consumer()
    show_section("7. 方法和参数表")
    demo_methods_table()


if __name__ == "__main__":
    main()
