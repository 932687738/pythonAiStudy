"""82 Python PyQt

来源: https://www.runoob.com/python3/python-pyqt.html
可单独运行: python 82_pyqt_tutorial.py
"""

from __future__ import annotations

import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 PyQt 组件和流程说明。"""
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


class Signal:
    """模拟 PyQt 信号，支持 connect 和 emit。"""

    def __init__(self) -> None:
        """初始化槽函数列表。"""
        self.slots: list[Callable[..., None]] = []

    def connect(self, slot: Callable[..., None]) -> None:
        """连接槽函数。"""
        self.slots.append(slot)

    def emit(self, *args) -> None:
        """发射信号并调用所有槽函数。"""
        for slot in self.slots:
            slot(*args)


@dataclass
class FakeWidget:
    """模拟 QWidget 基础窗口。"""

    title: str = ""
    geometry: tuple[int, int, int, int] = (0, 0, 0, 0)
    children: list[object] = field(default_factory=list)

    def setWindowTitle(self, title: str) -> None:
        """设置窗口标题。"""
        self.title = title

    def setGeometry(self, x: int, y: int, width: int, height: int) -> None:
        """设置窗口位置和大小。"""
        self.geometry = (x, y, width, height)

    def show(self) -> None:
        """模拟显示窗口。"""
        print(f"show window: {self.title}, geometry={self.geometry}")


class FakeButton:
    """模拟 QPushButton。"""

    def __init__(self, text: str, parent: FakeWidget | None = None) -> None:
        """初始化按钮文本、父窗口和 clicked 信号。"""
        self.text = text
        self.parent = parent
        self.geometry = (0, 0, 0, 0)
        self.clicked = Signal()
        if parent is not None:
            parent.children.append(self)

    def setGeometry(self, x: int, y: int, width: int, height: int) -> None:
        """设置按钮位置和大小。"""
        self.geometry = (x, y, width, height)

    def click(self) -> None:
        """模拟点击按钮。"""
        self.clicked.emit()


class FakeLabel:
    """模拟 QLabel。"""

    def __init__(self, text: str, parent: FakeWidget | None = None) -> None:
        """初始化标签文本。"""
        self.text = text
        if parent is not None:
            parent.children.append(self)


class FakeLineEdit:
    """模拟 QLineEdit。"""

    def __init__(self, parent: FakeWidget | None = None) -> None:
        """初始化输入框。"""
        self.text = ""
        if parent is not None:
            parent.children.append(self)

    def setText(self, text: str) -> None:
        """设置输入框文本。"""
        self.text = text


def demo_install_and_intro() -> None:
    """保留 PyQt 介绍、版本和安装命令。"""
    show_table(
        ("主题", "说明"),
        [
            ("PyQt", "Qt 框架的 Python 绑定，用于创建 GUI 应用"),
            ("PyQt4", "基于 Qt4"),
            ("PyQt5", "基于 Qt5"),
            ("PyQt6", "基于 Qt6"),
            ("安装 PyQt5", "pip install PyQt5"),
            ("安装工具", "pip install PyQt5-tools"),
        ],
    )


def demo_simple_window() -> None:
    """复刻第一个 PyQt 程序：创建 QApplication、QWidget、设置标题和大小、显示窗口。"""
    print("app = QApplication([])")
    window = FakeWidget()
    window.setWindowTitle("我的第一个 PyQt 程序")
    window.setGeometry(100, 100, 400, 300)
    window.show()
    print("app.exec_()")


class MainWindow(FakeWidget):
    """模拟页面中的 QMainWindow 示例。"""

    def __init__(self) -> None:
        """初始化主窗口和按钮，并连接 clicked 信号。"""
        super().__init__()
        self.setWindowTitle("我的第一个PyQt应用")
        self.setGeometry(100, 100, 400, 300)
        self.button = FakeButton("点击我", self)
        self.button.setGeometry(150, 150, 100, 30)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self) -> None:
        """按钮点击槽函数。"""
        print("按钮被点击了!")


def demo_main_window_button() -> None:
    """执行主窗口、按钮和信号槽连接示例。"""
    window = MainWindow()
    window.show()
    window.button.click()


def demo_widgets_layouts() -> None:
    """保留按钮、标签、文本框和 QVBoxLayout 示例。"""
    window = FakeWidget("组件窗口")
    button = FakeButton("点击我", window)
    label = FakeLabel("Hello PyQt!", window)
    textbox = FakeLineEdit(window)
    textbox.setText("用户名")
    print(button.text, label.text, textbox.text)
    print("QVBoxLayout().addWidget(QLabel('用户名')); addWidget(QLineEdit()); addWidget(QPushButton('登录'))")


class MyEmitter:
    """模拟 PyQt 自定义信号对象。"""

    def __init__(self) -> None:
        """初始化自定义信号。"""
        self.my_signal = Signal()


def demo_signals_slots() -> None:
    """复刻信号与槽机制和自定义信号示例。"""
    button = FakeButton("点击我")
    button.clicked.connect(lambda: print("按钮被点击了！"))
    button.click()
    emitter = MyEmitter()
    emitter.my_signal.connect(lambda value: print(f"收到信号: {value}"))
    emitter.my_signal.emit("Hello")
    print("disconnect() 可断开连接；blockSignals(True) 可临时阻塞信号。")


def demo_qt_designer() -> None:
    """保留 Qt Designer 和 pyuic5 工作流。"""
    commands = [
        "启动 Designer 设计界面并保存为 .ui 文件",
        "pyuic5 input.ui -o output.py",
        "from PyQt5 import uic",
        "Form, Window = uic.loadUiType('output.ui')",
    ]
    for command in commands:
        print(command)


class Notepad:
    """模拟页面中的简易记事本应用逻辑。"""

    def __init__(self) -> None:
        """初始化文本内容。"""
        self.text = ""

    def new_file(self) -> None:
        """新建文件时清空文本。"""
        self.text = ""

    def open_file(self, filename: Path) -> None:
        """打开文件并读取文本。"""
        self.text = filename.read_text(encoding="utf-8")

    def save_file(self, filename: Path) -> None:
        """保存文本到文件。"""
        filename.write_text(self.text, encoding="utf-8")

    def copy(self) -> str:
        """模拟复制文本。"""
        return self.text

    def paste(self, text: str) -> None:
        """模拟粘贴文本。"""
        self.text += text

    def cut(self) -> str:
        """模拟剪切文本。"""
        value = self.text
        self.text = ""
        return value


def demo_notepad() -> None:
    """执行简易记事本的核心文件操作逻辑。"""
    app = Notepad()
    app.text = "Runoob Notepad"
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "note.txt"
        app.save_file(path)
        app.new_file()
        print(app.text)
        app.open_file(path)
        print(app.text)
        copied = app.copy()
        app.cut()
        app.paste(copied)
        print(app.text)


def demo_components_table() -> None:
    """保留 PyQt5 核心组件类别表。"""
    show_table(
        ("组件类别", "组件名称", "说明"),
        [
            ("基础窗口组件", "QWidget, QMainWindow, QDialog", "窗口和对话框"),
            ("布局管理", "QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout", "自动安排控件"),
            ("按钮类", "QPushButton, QRadioButton, QCheckBox, QToolButton", "用户点击和选择"),
            ("输入控件", "QLineEdit, QTextEdit, QSpinBox, QComboBox", "文本、数字和选项输入"),
            ("显示控件", "QLabel, QLCDNumber, QProgressBar, QStatusBar", "文本、数字和状态显示"),
            ("容器类", "QGroupBox, QTabWidget, QStackedWidget, QScrollArea", "组织多个控件"),
            ("列表/表格/树", "QListWidget, QTableWidget, QTreeWidget", "展示结构化数据"),
            ("菜单/工具栏", "QMenuBar, QMenu, QToolBar, QAction", "应用命令入口"),
            ("对话框", "QFileDialog, QColorDialog, QFontDialog, QMessageBox", "弹窗交互"),
            ("其他功能组件", "QCalendarWidget, QSystemTrayIcon, QWebEngineView", "高级功能"),
        ],
    )


def main() -> None:
    """按 PyQt 页面顺序运行全部示例。"""
    print("Python PyQt")
    show_section("1. 安装和介绍")
    demo_install_and_intro()
    show_section("2. 简单窗口")
    demo_simple_window()
    show_section("3. 主窗口和按钮")
    demo_main_window_button()
    show_section("4. 常用组件和布局")
    demo_widgets_layouts()
    show_section("5. 信号与槽")
    demo_signals_slots()
    show_section("6. Qt Designer")
    demo_qt_designer()
    show_section("7. 简易记事本")
    demo_notepad()
    show_section("8. 核心组件表")
    demo_components_table()


if __name__ == "__main__":
    main()
