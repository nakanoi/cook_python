import requests
from load_env import APP_ID


BASE_URL = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426'


def ger_recipes(categories):
    recipes = []
    _url = BASE_URL + '?applicationId={}'.format(APP_ID)

    for _cat in categories:
        _cat_url = _url + '&categoryId={}'.format(_cat)
        _res = requests.get(_cat_url)

        try:
            _res.raise_for_status()
            recipes += _res.json()['result']

        except Exception as e:
            print('Something wrong happened.\n', e)

    return recipes
