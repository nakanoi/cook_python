from datetime import datetime


def _create_sql(category_dict, json):
    sql = 'INSERT INTO categories (\
        category_id, name, url, query, created_at, updated_at\
        ) VALUES'
    _value = " ({}, '{}', '{}', '{}', '{}', '{}'),"
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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


def recording(cur, category_dict, json):
    _sql = _create_sql(category_dict, json)
    print('\nCategory SQL:', _sql)
    cur.record(_sql)
    cur.close()

    return
