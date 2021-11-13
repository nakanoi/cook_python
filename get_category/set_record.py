import pymysql
from datetime import datetime
from  load_env import (
    MYSQL_CHARSET, MYSQL_HOST, MYSQL_USER, 
    MYSQL_PASSWORD, MYSQL_DATABASE,
)


def _create_sql(category_dict, json):
    sql = 'INSERT INTO categories (\
        category_id, name, url, query, created_at, updated_at\
        ) VALUES'
    _value = " ({}, '{}', '{}', '{}', '{}', '{}'),"
    now = datetime.now().strftime('%Y-%m-%d')

    for _, _val in json['result'].items():
        for _v in _val:
            sql += _value.format(
                _v.get('categoryId'),
                _v.get('categoryName'),
                _v.get('categoryUrl'),
                category_dict[str(_v.get('categoryId'))],
                now,
                now,
            )
    sql = sql.rstrip(',') + ' ON DUPLICATE KEY UPDATE\
        category_id = VALUES(category_id), \
        name = VALUES(name), \
        url = VALUES(url), \
        query = VALUES(query);'

    return sql


def recording(category_dict, json):
    _conn = pymysql.connect(
        db='mysql',
        host=MYSQL_HOST,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        charset=MYSQL_CHARSET,
    )
    _cur = _conn.cursor()
    try:
        _sql = _create_sql(category_dict, json)
        _cur.execute(_sql)
        _cur.connection.commit()
    finally:
        _cur.close()
        _conn.close()

    return
