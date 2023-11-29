from typing import Any, Optional

import numpy as np

from eidolon_sdk.agent_memory import FileMemory, SimilarityMemory, SymbolicMemory


class NoopFileMemory(FileMemory):
    def start(self):
        pass

    def stop(self):
        pass

    async def read_file(self, file_path: str) -> bytes:
        pass

    async def write_file(self, file_path: str, file_contents: bytes) -> None:
        pass

    def mkdir(self, directory: str, exist_ok: bool = False):
        pass

    def exists(self, file_name: str):
        pass


class NoopSymbolicMemory(SymbolicMemory):
    def start(self):
        pass

    def stop(self):
        pass

    async def count(self, symbol_collection: str, query: dict[str, Any]) -> int:
        return 0

    def find(self, symbol_collection: str, query: dict[str, Any]):
        pass

    async def find_one(self, symbol_collection: str, query: dict[str, Any]) -> Optional[dict[str, Any]]:
        pass

    async def insert(self, symbol_collection: str, documents: list[dict[str, Any]]) -> None:
        pass

    async def insert_one(self, symbol_collection: str, document: dict[str, Any]) -> None:
        pass

    async def upsert_one(self, symbol_collection: str, document: dict[str, Any], query: dict[str, Any]) -> None:
        pass

    async def update_many(self, symbol_collection: str, query: dict[str, Any], document: dict[str, Any]) -> None:
        pass

    async def delete(self, symbol_collection, query):
        pass


class NoopSimilarityMemory(SimilarityMemory):
    def start(self):
        pass

    def stop(self):
        pass

    async def query(self, query: np.array) -> list[dict[str, Any]]:
        pass

    async def insert(self,  embedding: np.array) -> None:
        pass
