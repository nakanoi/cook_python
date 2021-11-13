from datetime import datetime
from load_env import QUERY_NUM


def _create_set_sql(recipe_list):
    menu_sql = 'INSERT INTO menus (\
        name, img, medium_img, small_img, title, menu_id, content,\
        url, poster, indication, cost, created_at, updated_at\
        ) VALUES'
    ingredient_sql = 'INSERT INTO ingredients (\
        menu_id, name, menu_id_name, created_at, updated_at\
        ) VALUES'
    _menu_value = " ('{}', '{}', '{}', '{}', '{}', {}, '{}',\
        '{}', '{}', '{}', '{}', '{}', '{}'),"
    _ingredient_value = " ({}, '{}', '{}', '{}', '{}'),"
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for _recipe in recipe_list:
        menu_sql += _menu_value.format(
            _recipe['recipeTitle'],
            _recipe['foodImageUrl'],
            _recipe['mediumImageUrl'],
            _recipe['smallImageUrl'],
            _recipe['recipeTitle'],
            _recipe['recipeId'],
            _recipe['recipeDescription'],
            _recipe['recipeUrl'],
            _recipe['nickname'],
            _recipe['recipeIndication'],
            _recipe['recipeCost'],
            now,
            now
        )
        for _ingre in _recipe['recipeMaterial']:
            ingredient_sql += _ingredient_value.format(
                _recipe['recipeId'],
                _ingre,
                str(_recipe['recipeId']) + _ingre,
                now,
                now
            )
    menu_sql = menu_sql.rstrip(',') +\
        ' ON DUPLICATE KEY UPDATE\
        name = VALUES(name), \
        img = VALUES(img), \
        medium_img = VALUES(medium_img), \
        small_img = VALUES(small_img), \
        title = VALUES(title), \
        content = VALUES(content), \
        url = VALUES(url), \
        poster = VALUES(poster), \
        indication = VALUES(indication), \
        cost = VALUES(cost);'
    ingredient_sql = ingredient_sql.rstrip(',') +\
        ' ON DUPLICATE KEY UPDATE\
        name = VALUES(name), \
        updated_at = VALUES(updated_at);'

    return menu_sql, ingredient_sql


def _create_get_category_sql():
    sql = 'SELECT query FROM categories ORDER BY updated_at DESC;'

    return sql


def _create_date_update_sql(category_list):
    _now = datetime.now()
    sql = "UPDATE categories SET updated_at='{}'\
        WHERE query IN ('{}')".format(
        _now.strftime('%Y-%m-%d %H:%M:%S'),
        '\', \''.join(category_list)
    )

    return sql


def get_category(cur):
    _sql = _create_get_category_sql()
    print('\nCategory SQL:', _sql)
    categories = cur.get_category(_sql)
    _update_sql = _create_date_update_sql(
        categories[:2]
    )
    print('\nUpdate SQL:', _update_sql)
    cur.record(_update_sql)

    return categories[int(QUERY_NUM)]


def recording(cur, recipes):
    _menu_sql, _ingre_sql = _create_set_sql(recipes)
    print('\nMenu SQL:', _menu_sql)
    print('\nRecipe SQL:', _ingre_sql)
    cur.record(_menu_sql)
    cur.record(_ingre_sql)

    return
