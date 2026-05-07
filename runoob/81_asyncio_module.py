"""81 Python asyncio 模块

来源: https://www.runoob.com/python3/python-asyncio.html
可单独运行: python 81_asyncio_module.py
"""

from __future__ import annotations

import asyncio
import time


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 asyncio 核心函数、事件循环和任务方法表。"""
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


async def say_hello() -> None:
    """页面中的 hello/world 协程示例。"""
    print("Hello")
    await asyncio.sleep(0.01)
    print("World")


async def demo_coroutine_run() -> None:
    """演示 async def、await 和 asyncio.run 的协程执行逻辑。"""
    await say_hello()


async def task1() -> str:
    """并发任务 1。"""
    print("Task 1 started")
    await asyncio.sleep(0.01)
    print("Task 1 finished")
    return "task1"


async def task2() -> str:
    """并发任务 2。"""
    print("Task 2 started")
    await asyncio.sleep(0.02)
    print("Task 2 finished")
    return "task2"


async def demo_gather_tasks() -> None:
    """演示 create_task 和 gather 并发执行多个协程。"""
    task = asyncio.create_task(say_hello())
    await task
    results = await asyncio.gather(task1(), task2())
    print(results)


async def long_task() -> None:
    """用于 wait_for 超时示例的长任务。"""
    await asyncio.sleep(1)
    print("Task finished")


async def demo_timeout() -> None:
    """演示 wait_for 超时控制。"""
    try:
        await asyncio.wait_for(long_task(), timeout=0.01)
    except asyncio.TimeoutError:
        print("Task timed out")


async def fetch(url: str) -> str:
    """模拟异步网络请求，避免真实联网。"""
    print(f"Fetching {url}")
    await asyncio.sleep(0.02)
    return f"Data from {url}"


async def demo_async_fetch() -> None:
    """复刻并发访问多个网址的例子，用 sleep 模拟 I/O。"""
    start = time.time()
    urls = ["url1.com", "url2.com", "url3.com"]
    results = await asyncio.gather(*(fetch(url) for url in urls))
    end = time.time()
    print(f"异步版本总耗时: {end - start:.2f} 秒")
    print(results)


async def producer(q: asyncio.Queue[int | None]) -> None:
    """异步队列生产者。"""
    for i in range(5):
        await q.put(i)
        await asyncio.sleep(0.01)
    await q.put(None)


async def consumer(q: asyncio.Queue[int | None]) -> None:
    """异步队列消费者。"""
    while True:
        item = await q.get()
        try:
            if item is None:
                break
            print(f"Consumed {item}")
        finally:
            q.task_done()


async def demo_async_queue() -> None:
    """执行页面异步队列示例，并使用哨兵值结束消费者。"""
    q: asyncio.Queue[int | None] = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))


async def demo_cancel_task() -> None:
    """演示取消任务会引发 CancelledError。"""
    task = asyncio.create_task(long_task())
    await asyncio.sleep(0.01)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("task cancelled")


def demo_core_tables() -> None:
    """保留 asyncio 核心函数、事件循环和任务方法表。"""
    show_table(
        ("方法/函数", "说明", "示例"),
        [
            ("asyncio.run(coro)", "运行异步主函数", "asyncio.run(main())"),
            ("asyncio.create_task(coro)", "创建任务并加入事件循环", "task = asyncio.create_task(fetch())"),
            ("asyncio.gather(*coros)", "并发运行多个协程", "await asyncio.gather(a(), b())"),
            ("asyncio.sleep(delay)", "异步等待，非阻塞", "await asyncio.sleep(1)"),
            ("asyncio.wait(coros)", "控制任务完成方式", "done, pending = await asyncio.wait(tasks)"),
            ("asyncio.wait_for(coro, timeout)", "超时控制", "await asyncio.wait_for(task(), 5)"),
        ],
    )
    show_table(
        ("Task 方法", "说明"),
        [
            ("task.cancel()", "取消任务"),
            ("task.done()", "检查任务是否完成"),
            ("task.result()", "获取任务结果"),
            ("task.exception()", "获取任务异常"),
        ],
    )


async def run_all_async_demos() -> None:
    """依次运行所有异步示例。"""
    await demo_coroutine_run()
    await demo_gather_tasks()
    await demo_timeout()
    await demo_async_fetch()
    await demo_async_queue()
    await demo_cancel_task()


def main() -> None:
    """按 asyncio 页面顺序运行全部示例。"""
    print("Python asyncio 模块")
    show_section("1. 核心函数表")
    demo_core_tables()
    show_section("2. 异步示例")
    asyncio.run(run_all_async_demos())


if __name__ == "__main__":
    main()
