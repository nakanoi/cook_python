import pymysql
from load_env import (
    MYSQL_CHARSET, MYSQL_HOST, MYSQL_USER, 
    MYSQL_PASSWORD, MYSQL_DATABASE,
)


class Cur:
    def __init__(self) -> None:
        self._conn = pymysql.connect(
            db='mysql',
            host=MYSQL_HOST,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset=MYSQL_CHARSET,
        )
        self._cur = self._conn.cursor()

    def record(self, sql):
        try:
            self._cur.execute(sql)
            self._cur.connection.commit()
        except Exception as e:
            print(e)

        return

    def get_category(self, sql):
        res = []
        try:
            self._cur.execute(sql)
            res = self._cur.fetchall()
        except Exception as e:
            print(e)

        return [r[0] for r in res]

    def close(self):
        self._cur.close()
        self._conn.close()

        return
