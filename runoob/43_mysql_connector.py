"""43 Python3 MySQL(mysql-connector)

来源: https://www.runoob.com/python3/python-mysql-connector.html
可单独运行: python 43_mysql_connector.py
"""

from __future__ import annotations

import sqlite3


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 mysql-connector 页面中的操作步骤。"""
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


def connect_demo_db() -> sqlite3.Connection:
    """用内存 sqlite 数据库模拟 MySQL 连接，避免依赖本地 MySQL 服务。"""
    return sqlite3.connect(":memory:")


def demo_install_and_connect_note() -> None:
    """保留 mysql-connector 安装和连接代码结构。"""
    show_table(
        ("步骤", "MySQL 页面代码", "本文件处理"),
        [
            ("安装", "python -m pip install mysql-connector", "只保留命令，不联网安装"),
            ("导入", "import mysql.connector", "用 sqlite3 模拟数据库行为"),
            ("连接", "mysql.connector.connect(...)", "sqlite3.connect(':memory:')"),
            ("游标", "mydb.cursor()", "conn.cursor()"),
            ("提交", "mydb.commit()", "conn.commit()"),
        ],
    )


def demo_create_table(conn: sqlite3.Connection) -> None:
    """模拟 CREATE TABLE sites，并展示 SHOW TABLES 的效果。"""
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE sites (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT)")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cursor.fetchall())


def demo_insert_records(conn: sqlite3.Connection) -> None:
    """模拟 executemany 插入多条记录，并输出 rowcount 和 lastrowid。"""
    cursor = conn.cursor()
    sql = "INSERT INTO sites (name, url) VALUES (?, ?)"
    values = [
        ("RUNOOB", "https://www.runoob.com"),
        ("Google", "https://www.google.com"),
        ("Github", "https://www.github.com"),
        ("Taobao", "https://www.taobao.com"),
        ("stackoverflow", "https://www.stackoverflow.com/"),
    ]
    cursor.executemany(sql, values)
    conn.commit()
    print(cursor.rowcount, "记录插入成功。")
    cursor.execute(sql, ("Zhihu", "https://www.zhihu.com"))
    conn.commit()
    print("1 条记录已插入, ID:", cursor.lastrowid)


def demo_select_fetch(conn: sqlite3.Connection) -> None:
    """模拟 SELECT *、指定字段查询、fetchall 和 fetchone。"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sites")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("SELECT name, url FROM sites")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM sites")
    print(cursor.fetchone())


def demo_where_order_limit(conn: sqlite3.Connection) -> None:
    """模拟 WHERE、ORDER BY、LIMIT 和 OFFSET 查询。"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sites WHERE name = ?", ("RUNOOB",))
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM sites ORDER BY name")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM sites ORDER BY name DESC")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM sites LIMIT 3")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")
    print(cursor.fetchall())


def demo_delete_update_drop(conn: sqlite3.Connection) -> None:
    """模拟 DELETE、UPDATE 和 DROP TABLE，并强调参数化防 SQL 注入。"""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sites WHERE name = ?", ("stackoverflow",))
    conn.commit()
    print(cursor.rowcount, "条记录删除")
    cursor.execute("UPDATE sites SET name = ? WHERE name = ?", ("RUNOOB-UPDATED", "RUNOOB"))
    conn.commit()
    print(cursor.rowcount, "条记录修改")
    cursor.execute("SELECT * FROM sites WHERE name = ?", ("RUNOOB-UPDATED",))
    print(cursor.fetchall())
    cursor.execute("DROP TABLE sites")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sites'")
    print("sites 表是否还存在:", cursor.fetchall())


def main() -> None:
    """按 mysql-connector 页面顺序运行数据库操作模拟示例。"""
    print("Python3 MySQL(mysql-connector)")
    show_section("1. 安装和连接")
    demo_install_and_connect_note()
    conn = connect_demo_db()
    try:
        show_section("2. 创建数据表")
        demo_create_table(conn)
        show_section("3. 插入数据")
        demo_insert_records(conn)
        show_section("4. 查询数据")
        demo_select_fetch(conn)
        show_section("5. WHERE、排序和限制")
        demo_where_order_limit(conn)
        show_section("6. 删除、更新和删除表")
        demo_delete_update_drop(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
