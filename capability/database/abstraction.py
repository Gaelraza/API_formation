from capability.database.interface import DatabaseInterface


class DatabaseAbstraction(DatabaseInterface):

    def __init__(self, adapter: DatabaseInterface) -> None:
        self._adapter = adapter

    def create(self, table: str, data: dict) -> dict:
        return self._adapter.create(table, data)

    def read(self, table: str, record_id: str) -> dict:
        return self._adapter.read(table, record_id)

    def update(self, table: str, record_id: str, data: dict) -> dict:
        return self._adapter.update(table, record_id, data)

    def delete(self, table: str, record_id: str) -> None:
        return self._adapter.delete(table, record_id)
