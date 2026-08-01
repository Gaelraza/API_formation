import os
import sqlite3
import json
import uuid


class SQLiteAdapter:

    def __init__(self) -> None:
        database_path = os.environ.get("DATABASE_PATH")
        if not database_path:
            raise RuntimeError("DATABASE_PATH environment variable is not set")
        self._database_path = database_path

    def _get_connection(self, table: str):
        conn = sqlite3.connect(self._database_path)
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} (id TEXT PRIMARY KEY, data TEXT)")
        return conn

    def create(self, table: str, data: dict) -> dict:
        record_id = str(uuid.uuid4())
        serialized_data = json.dumps(data)
        conn = self._get_connection(table)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {table} (id, data) VALUES (?, ?)", (record_id, serialized_data))
        conn.commit()
        conn.close()
        return {"id": record_id, **data}

    def read(self, table: str, record_id: str) -> dict:
        conn = self._get_connection(table)
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, data FROM {table} WHERE id = ?", (record_id,))
        row = cursor.fetchone()
        conn.close()
        if row is None:
            raise LookupError(f"Record with id {record_id} not found in table {table}")
        stored_id, serialized_data = row
        data = json.loads(serialized_data)
        return {"id": stored_id, **data}

    def update(self, table: str, record_id: str, data: dict) -> dict:
        conn = self._get_connection(table)
        cursor = conn.cursor()
        cursor.execute(f"SELECT id FROM {table} WHERE id = ?", (record_id,))
        row = cursor.fetchone()
        if row is None:
            conn.close()
            raise LookupError(f"Record with id {record_id} not found in table {table}")
        serialized_data = json.dumps(data)
        cursor.execute(f"UPDATE {table} SET data = ? WHERE id = ?", (serialized_data, record_id))
        conn.commit()
        conn.close()
        return {"id": record_id, **data}

    def delete(self, table: str, record_id: str) -> None:
        conn = self._get_connection(table)
        cursor = conn.cursor()
        cursor.execute(f"SELECT id FROM {table} WHERE id = ?", (record_id,))
        row = cursor.fetchone()
        if row is None:
            conn.close()
            raise LookupError(f"Record with id {record_id} not found in table {table}")
        cursor.execute(f"DELETE FROM {table} WHERE id = ?", (record_id,))
        conn.commit()
        conn.close()
        return None
