class QueryBuilder:
    """Un Query Builder liviano para generar sentencias SQL básicas."""
    
    @staticmethod
    def insert(table: str, data: dict):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        return sql, tuple(data.values())

    @staticmethod
    def select(table: str, columns: list = None, where: dict = None, order_by: str = None):
        cols = ", ".join(columns) if columns else "*"
        sql = f"SELECT {cols} FROM {table}"
        values = []
        
        if where:
            conditions = " AND ".join([f"{k} = ?" for k in where])
            sql += f" WHERE {conditions}"
            values = list(where.values())
            
        if order_by:
            sql += f" ORDER BY {order_by}"
            
        return sql, tuple(values)

    @staticmethod
    def update(table: str, data: dict, where: dict):
        set_clause = ", ".join([f"{k} = ?" for k in data])
        where_clause = " AND ".join([f"{k} = ?" for k in where])
        sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        values = list(data.values()) + list(where.values())
        return sql, tuple(values)

    @staticmethod
    def delete(table: str, where: dict):
        where_clause = " AND ".join([f"{k} = ?" for k in where])
        sql = f"DELETE FROM {table} WHERE {where_clause}"
        return sql, tuple(where.values())
