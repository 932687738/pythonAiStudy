"""67 Python selenium 库

来源: https://www.runoob.com/python3/python-selenium.html
可单独运行: python 67_selenium_tutorial.py
"""

from __future__ import annotations

from dataclasses import dataclass


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 Selenium 常用方法表。"""
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


@dataclass
class FakeElement:
    """模拟 Selenium 页面元素，支持 text、send_keys、click、get_attribute。"""

    tag: str
    text: str = ""
    attributes: dict[str, str] | None = None

    def send_keys(self, value: str) -> None:
        """模拟向输入框输入文本。"""
        self.text += value
        print(f"send_keys({value!r})")

    def click(self) -> None:
        """模拟点击元素。"""
        print(f"click({self.tag})")

    def get_attribute(self, name: str) -> str | None:
        """模拟获取元素属性。"""
        return (self.attributes or {}).get(name)


class FakeWebDriver:
    """模拟 Selenium WebDriver，保留常见 API 形状但不打开真实浏览器。"""

    def __init__(self) -> None:
        """初始化当前 URL、标题和元素映射。"""
        self.current_url = ""
        self.title = ""
        self.elements = {
            ("id", "kw"): FakeElement("input", attributes={"placeholder": "请输入关键词"}),
            ("class name", "s_ipt"): FakeElement("button", "百度一下"),
            ("tag name", "a"): FakeElement("a", "链接"),
        }

    def get(self, url: str) -> None:
        """模拟访问指定 URL。"""
        self.current_url = url
        self.title = "模拟页面标题"
        print(f"driver.get({url!r})")

    def find_element(self, by: str, value: str) -> FakeElement:
        """模拟查找单个元素。"""
        return self.elements.get((by, value), FakeElement("unknown"))

    def find_elements(self, by: str, value: str) -> list[FakeElement]:
        """模拟查找多个元素。"""
        return [self.find_element(by, value)]

    def implicitly_wait(self, seconds: int) -> None:
        """模拟隐式等待。"""
        print(f"implicitly_wait({seconds})")

    def back(self) -> None:
        """模拟浏览器后退。"""
        print("back()")

    def forward(self) -> None:
        """模拟浏览器前进。"""
        print("forward()")

    def refresh(self) -> None:
        """模拟刷新页面。"""
        print("refresh()")

    def execute_script(self, script: str) -> None:
        """模拟执行 JavaScript。"""
        print(f"execute_script({script!r})")

    def quit(self) -> None:
        """模拟关闭浏览器。"""
        print("quit()")


def demo_install_and_driver() -> None:
    """保留安装 Selenium、查看版本和下载 WebDriver 的说明。"""
    show_table(
        ("步骤", "命令或说明"),
        [
            ("安装 Selenium", "pip install selenium"),
            ("查看版本", "pip show selenium / import selenium; print(selenium.__version__)"),
            ("Chrome", "ChromeDriver"),
            ("Firefox", "GeckoDriver"),
            ("Edge", "EdgeDriver"),
            ("Safari", "SafariDriver"),
            ("Selenium 4", "可尝试自动检测浏览器并下载驱动"),
        ],
    )


def demo_basic_usage() -> None:
    """复刻初始化浏览器、打开网页、查找元素、输入、点击和关闭浏览器。"""
    driver = FakeWebDriver()
    driver.get("https://www.baidu.com")
    search_box = driver.find_element("id", "kw")
    search_button = driver.find_element("class name", "s_ipt")
    links = driver.find_elements("tag name", "a")
    search_box.send_keys("Selenium Python")
    search_button.click()
    print(search_box.text)
    print(search_box.get_attribute("placeholder"))
    print([link.text for link in links])
    print(driver.title)
    driver.quit()


def demo_wait_and_navigation() -> None:
    """保留显式等待、隐式等待、后退、前进、刷新和执行 JS 的操作逻辑。"""
    driver = FakeWebDriver()
    driver.get("https://www.baidu.com")
    print("WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kw')))")
    driver.implicitly_wait(10)
    driver.back()
    driver.forward()
    driver.refresh()
    driver.execute_script("alert('Hello!')")
    driver.quit()


def demo_methods_table() -> None:
    """保留 Selenium 常用方法表。"""
    show_table(
        ("方法", "说明", "示例"),
        [
            ("webdriver.Chrome()", "初始化 Chrome 浏览器实例", "driver = webdriver.Chrome()"),
            ("driver.get(url)", "访问指定 URL 地址", "driver.get('https://example.com')"),
            ("driver.find_element(By, value)", "查找第一个匹配元素", "driver.find_element(By.ID, 'id')"),
            ("driver.find_elements(By, value)", "查找所有匹配元素", "driver.find_elements(By.CLASS_NAME, 'class')"),
            ("element.click()", "点击元素", "element.click()"),
            ("element.send_keys(value)", "向输入框输入", "element.send_keys('text')"),
            ("element.text", "获取文本", "text = element.text"),
            ("driver.back()", "浏览器后退", "driver.back()"),
            ("driver.forward()", "浏览器前进", "driver.forward()"),
            ("driver.refresh()", "刷新当前页面", "driver.refresh()"),
            ("driver.execute_script()", "执行 JavaScript", "driver.execute_script('alert(1)')"),
            ("driver.quit()", "关闭浏览器", "driver.quit()"),
        ],
    )


def main() -> None:
    """按 selenium 页面顺序运行全部示例。"""
    print("Python selenium 库")
    show_section("1. 安装和 WebDriver")
    demo_install_and_driver()
    show_section("2. 基本用法")
    demo_basic_usage()
    show_section("3. 等待和导航")
    demo_wait_and_navigation()
    show_section("4. 常用方法")
    demo_methods_table()


if __name__ == "__main__":
    main()
