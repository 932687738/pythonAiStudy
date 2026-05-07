"""44 Python3 MySQL(PyMySQL)

来源: https://www.runoob.com/python3/python3-mysql.html
可单独运行: python 44_mysql_pymysql.py
"""

from __future__ import annotations

import sqlite3


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 PyMySQL 页面中的数据库流程。"""
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


def demo_pymysql_note() -> None:
    """保留 PyMySQL 安装、连接和 DB API v2.0 说明。"""
    show_table(
        ("主题", "页面示例", "本文件处理"),
        [
            ("安装", "pip3 install PyMySQL", "保留命令，不联网安装"),
            ("连接", "pymysql.connect(host, user, password, database)", "sqlite3.connect(':memory:') 模拟"),
            ("游标", "db.cursor()", "cursor = conn.cursor()"),
            ("执行 SQL", "cursor.execute(sql)", "执行兼容 SQL"),
            ("事务", "db.commit() / db.rollback()", "conn.commit() / conn.rollback()"),
            ("关闭", "db.close()", "conn.close()"),
        ],
    )


def setup_employee_table(conn: sqlite3.Connection) -> None:
    """模拟创建 EMPLOYEE 表。"""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    cursor.execute(
        """
        CREATE TABLE EMPLOYEE (
            FIRST_NAME TEXT NOT NULL,
            LAST_NAME TEXT,
            AGE INTEGER,
            SEX TEXT,
            INCOME REAL
        )
        """
    )


def demo_connect_and_version(conn: sqlite3.Connection) -> None:
    """模拟 SELECT VERSION()，展示当前 SQLite 版本作为可运行替代。"""
    cursor = conn.cursor()
    cursor.execute("select sqlite_version()")
    data = cursor.fetchone()
    print("Database version : %s " % data)


def demo_insert_fetch(conn: sqlite3.Connection) -> None:
    """模拟 INSERT INTO EMPLOYEE 和 SELECT 查询。"""
    cursor = conn.cursor()
    sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, ("Mac", "Mohan", 20, "M", 2000))
    conn.commit()
    cursor.execute("SELECT * FROM EMPLOYEE")
    print(cursor.fetchall())


def demo_update_delete_transaction(conn: sqlite3.Connection) -> None:
    """模拟 UPDATE、DELETE 和事务回滚。"""
    cursor = conn.cursor()
    cursor.execute("UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = ?", ("M",))
    conn.commit()
    print("更新行数:", cursor.rowcount)
    cursor.execute("SELECT * FROM EMPLOYEE")
    print(cursor.fetchall())

    try:
        cursor.execute("DELETE FROM EMPLOYEE WHERE AGE > ?", (20,))
        raise RuntimeError("模拟异常，触发 rollback")
    except RuntimeError as exc:
        conn.rollback()
        print("回滚事务:", exc)
    cursor.execute("SELECT * FROM EMPLOYEE")
    print(cursor.fetchall())


def demo_fetch_methods(conn: sqlite3.Connection) -> None:
    """保留 fetchone、fetchmany、fetchall 查询方式。"""
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (?, ?, ?, ?, ?)",
        [("Tom", "Cat", 25, "M", 3000), ("Lucy", "Green", 23, "F", 4000)],
    )
    conn.commit()
    cursor.execute("SELECT * FROM EMPLOYEE ORDER BY AGE")
    print("fetchone:", cursor.fetchone())
    print("fetchmany:", cursor.fetchmany(2))
    cursor.execute("SELECT * FROM EMPLOYEE ORDER BY AGE")
    print("fetchall:", cursor.fetchall())


def main() -> None:
    """按 PyMySQL 页面顺序运行数据库操作模拟示例。"""
    print("Python3 MySQL(PyMySQL)")
    show_section("1. PyMySQL 说明")
    demo_pymysql_note()
    conn = sqlite3.connect(":memory:")
    try:
        show_section("2. 数据库版本")
        demo_connect_and_version(conn)
        show_section("3. 创建 EMPLOYEE 表")
        setup_employee_table(conn)
        print("EMPLOYEE 表创建成功")
        show_section("4. 插入和查询")
        demo_insert_fetch(conn)
        show_section("5. 更新、删除和事务")
        demo_update_delete_transaction(conn)
        show_section("6. fetch 方法")
        demo_fetch_methods(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
