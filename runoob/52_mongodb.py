"""52 Python3 MongoDB

来源: https://www.runoob.com/python3/python-mongodb.html
可单独运行: python 52_mongodb.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 PyMongo 页面中的安装和操作流程。"""
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


@dataclass
class FakeCollection:
    """用列表模拟 MongoDB collection，保留 PyMongo 常见 API 形状。"""

    documents: list[dict[str, Any]] = field(default_factory=list)
    next_id: int = 1

    def insert_one(self, document: dict[str, Any]) -> dict[str, int]:
        """模拟 insert_one，返回 inserted_id。"""
        document = document.copy()
        document.setdefault("_id", self.next_id)
        self.next_id += 1
        self.documents.append(document)
        return {"inserted_id": document["_id"]}

    def insert_many(self, documents: list[dict[str, Any]]) -> dict[str, list[int]]:
        """模拟 insert_many，返回 inserted_ids。"""
        ids = []
        for document in documents:
            ids.append(self.insert_one(document)["inserted_id"])
        return {"inserted_ids": ids}

    def find_one(self) -> dict[str, Any] | None:
        """返回第一条文档。"""
        return self.documents[0] if self.documents else None

    def find(self, query: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        """按简单等值条件查询文档。"""
        if query is None:
            return list(self.documents)
        return [doc for doc in self.documents if all(doc.get(key) == value for key, value in query.items())]

    def update_one(self, query: dict[str, Any], update: dict[str, dict[str, Any]]) -> int:
        """模拟 update_one 的 $set 操作。"""
        for document in self.find(query):
            document.update(update.get("$set", {}))
            return 1
        return 0

    def delete_one(self, query: dict[str, Any]) -> int:
        """模拟 delete_one 删除第一条匹配文档。"""
        for index, document in enumerate(self.documents):
            if all(document.get(key) == value for key, value in query.items()):
                del self.documents[index]
                return 1
        return 0

    def sort(self, key: str, direction: int = 1) -> list[dict[str, Any]]:
        """按指定字段排序，direction 为 1 升序，-1 降序。"""
        return sorted(self.documents, key=lambda item: item.get(key, ""), reverse=direction == -1)


def demo_install_and_connect() -> None:
    """保留 PyMongo 安装、升级和连接代码流程。"""
    show_table(
        ("主题", "页面示例", "本文件处理"),
        [
            ("安装", "python3 -m pip3 install pymongo", "保留命令，不实际安装"),
            ("指定版本", "python3 -m pip3 install pymongo==3.5.1", "保留命令"),
            ("升级", "python3 -m pip3 install --upgrade pymongo", "保留命令"),
            ("连接", "pymongo.MongoClient('mongodb://localhost:27017/')", "FakeCollection 模拟"),
            ("数据库", "myclient['runoobdb']", "内存对象模拟"),
            ("集合", "mydb['sites']", "FakeCollection"),
        ],
    )


def demo_insert_find() -> FakeCollection:
    """模拟插入单条、多条文档，以及 find_one 和 find。"""
    collection = FakeCollection()
    result = collection.insert_one({"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"})
    print(result)
    result_many = collection.insert_many(
        [
            {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
            {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
            {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        ]
    )
    print(result_many)
    print(collection.find_one())
    for document in collection.find():
        print(document)
    return collection


def demo_query_update_delete(collection: FakeCollection) -> None:
    """模拟查询、修改、排序和删除文档。"""
    print(collection.find({"name": "RUNOOB"}))
    print(collection.update_one({"name": "RUNOOB"}, {"$set": {"alexa": "12345"}}))
    print(collection.find({"name": "RUNOOB"}))
    print(collection.sort("alexa", 1))
    print(collection.delete_one({"name": "Taobao"}))
    print(collection.find())


def main() -> None:
    """按 MongoDB 页面顺序运行全部示例。"""
    print("Python3 MongoDB")
    show_section("1. PyMongo 安装和连接")
    demo_install_and_connect()
    show_section("2. 插入和查询")
    collection = demo_insert_find()
    show_section("3. 查询、更新、排序和删除")
    demo_query_update_delete(collection)


if __name__ == "__main__":
    main()
