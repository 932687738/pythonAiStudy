"""40 Python 测验

来源: https://www.runoob.com/quiz/python-quiz.html
可单独运行: python 40_quiz.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Question:
    """保存一道测验题的题干、选项、答案和解释。"""

    title: str
    options: tuple[str, ...]
    answer: str
    explanation: str


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def run_quiz(questions: list[Question], selected_answers: list[str]) -> None:
    """运行一组测验题，用预设答案代替交互输入，保证脚本可直接运行。"""
    score = 0
    for index, question in enumerate(questions, 1):
        selected = selected_answers[index - 1]
        print(f"{index}. {question.title}")
        for option in question.options:
            print(f"   {option}")
        print(f"选择: {selected}")
        if selected == question.answer:
            print("结果: 正确")
            score += 1
        else:
            print(f"结果: 错误，正确答案是 {question.answer}")
        print(f"解释: {question.explanation}")
    print(f"得分: {score}/{len(questions)}")


def demo_basic_quiz() -> None:
    """保留主测验页的基础知识挑战形式，覆盖变量、类型、列表、字典、函数。"""
    questions = [
        Question("Python 中用来定义函数的关键字是？", ("A. func", "B. def", "C. function"), "B", "Python 使用 def 定义函数。"),
        Question("哪个类型是不可变类型？", ("A. list", "B. dict", "C. tuple"), "C", "元组 tuple 创建后不能修改元素绑定。"),
        Question("len([1, 2, 3]) 的结果是？", ("A. 2", "B. 3", "C. 4"), "B", "len 返回容器元素个数。"),
        Question("字典通过什么访问值？", ("A. 键", "B. 下标位置", "C. 行号"), "A", "dict 是键值映射，使用键访问值。"),
    ]
    run_quiz(questions, ["B", "C", "B", "A"])


def demo_operator_quiz() -> None:
    """保留操作符相关测验，覆盖算术、逻辑、成员和身份判断。"""
    questions = [
        Question("7 // 2 的结果是？", ("A. 3", "B. 3.5", "C. 4"), "A", "// 是向下取整除。"),
        Question("'a' in 'cat' 的结果是？", ("A. True", "B. False"), "A", "in 用于成员判断。"),
        Question("not False 的结果是？", ("A. True", "B. False"), "A", "not 会取反布尔值。"),
    ]
    run_quiz(questions, ["A", "A", "A"])


def demo_if_loop_quiz() -> None:
    """保留条件判断与循环测验中的代表性代码题。"""
    questions = [
        Question("if None: print('Hello') 会输出什么？", ("A. Hello", "B. 不输出"), "B", "None 在布尔上下文中为 False。"),
        Question("for i in [1, 0]: print(i+1) 会输出？", ("A. 2 和 1", "B. 1 和 0"), "A", "循环依次取 1、0，并各自加 1。"),
        Question("while 循环中 break 的作用是？", ("A. 跳过本次", "B. 终止循环"), "B", "break 会直接结束当前循环。"),
    ]
    run_quiz(questions, ["B", "A", "B"])


def demo_function_quiz() -> None:
    """保留函数测验，覆盖返回值、默认参数、lambda 和作用域。"""
    questions = [
        Question("没有 return 的函数默认返回什么？", ("A. None", "B. 0", "C. False"), "A", "Python 函数没有显式 return 时返回 None。"),
        Question("lambda x: x * 2 表示？", ("A. 匿名函数", "B. 类", "C. 模块"), "A", "lambda 用于创建简单匿名函数。"),
        Question("默认参数应通常写在哪里？", ("A. 必需参数前", "B. 必需参数后"), "B", "带默认值的参数通常放在必需参数之后。"),
    ]
    run_quiz(questions, ["A", "A", "B"])


def main() -> None:
    """按测验页面和相关测验类别运行模拟测验。"""
    print("Python 测验")
    show_section("1. Python 基础测验")
    demo_basic_quiz()
    show_section("2. 操作符测验")
    demo_operator_quiz()
    show_section("3. 条件判断与循环测验")
    demo_if_loop_quiz()
    show_section("4. 函数测验")
    demo_function_quiz()


if __name__ == "__main__":
    main()
