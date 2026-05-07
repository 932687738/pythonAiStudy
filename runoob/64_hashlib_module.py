"""64 Python hashlib

来源: https://www.runoob.com/python3/python-hashlib.html
可单独运行: python 64_hashlib_module.py
"""

from __future__ import annotations

import hashlib


def show_section(title: str) -> None:
    """打印章节标题，让输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 hashlib 算法说明。"""
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


def demo_dir_hashlib() -> None:
    """保留 dir(hashlib) 查看模块内容的逻辑。"""
    names = [name for name in dir(hashlib) if not name.startswith("_")]
    print(names)


def demo_new_update_digest() -> None:
    """执行 hashlib.new、update、hexdigest 和 digest 示例。"""
    sha256_hash = hashlib.new("sha256")
    sha256_hash.update(b"RUNOOB")
    print(sha256_hash.hexdigest())

    incremental = hashlib.sha256()
    incremental.update(b"Hello, ")
    incremental.update(b"Runoob!")
    print(incremental.hexdigest())
    print(hashlib.sha1(b"RUNOOB").digest())


def demo_common_algorithms() -> None:
    """执行 MD5、SHA-1、SHA-256、SHA-512 示例。"""
    data = b"RUNOOB"
    show_table(
        ("算法", "结果"),
        [
            ("md5", hashlib.md5(data).hexdigest()),
            ("sha1", hashlib.sha1(data).hexdigest()),
            ("sha256", hashlib.sha256(data).hexdigest()),
            ("sha512", hashlib.sha512(data).hexdigest()),
        ],
    )


def demo_algorithm_table() -> None:
    """保留页面中的常见哈希算法含义表。"""
    show_table(
        ("算法名称", "摘要长度（位）", "输出长度（字节）", "安全性", "用途"),
        [
            ("md5", "128", "16", "不安全", "数据完整性验证、密码存储等"),
            ("sha1", "160", "20", "不安全", "数据完整性验证、密码存储等"),
            ("sha224", "224", "28", "低", "数据完整性验证、数字签名等"),
            ("sha256", "256", "32", "中等", "数据完整性验证、数字签名等"),
            ("sha384", "384", "48", "高", "数字签名、加密算法等"),
            ("sha512", "512", "64", "高", "数字签名、加密算法等"),
            ("sha3_256", "256", "32", "高", "SHA-3 家族成员"),
            ("shake_128", "可变", "可变", "高", "可变长度摘要"),
        ],
    )


def demo_password_hash_note() -> None:
    """演示 pbkdf2_hmac 派生密钥，补充安全存储密码思路。"""
    password = b"runoob-password"
    salt = b"runoob-salt"
    key = hashlib.pbkdf2_hmac("sha256", password, salt, 100_000)
    print(key.hex())
    print("MD5 和 SHA-1 已不适合安全密码存储，推荐使用更强算法和盐。")


def main() -> None:
    """按 hashlib 页面顺序运行全部示例。"""
    print("Python hashlib")
    show_section("1. dir(hashlib)")
    demo_dir_hashlib()
    show_section("2. new/update/digest")
    demo_new_update_digest()
    show_section("3. 常见算法")
    demo_common_algorithms()
    show_section("4. 算法说明表")
    demo_algorithm_table()
    show_section("5. 密码哈希补充")
    demo_password_hash_note()


if __name__ == "__main__":
    main()
