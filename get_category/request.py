import requests
from load_env import APP_ID


BASE_URL = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426'


def _json_to_dict(json):
    _category_dict = {}

    for _, _val in json['result'].items():
        for _v in _val:
            _id = str(_v['categoryId'])
            _query = _v['categoryUrl'].split('/')[-2]
            _category_dict[_id] = _query

    return _category_dict


def get_category():
    _url = BASE_URL + '?applicationId={}'.format(APP_ID)
    _res = requests.get(_url)

    try:
        _res.raise_for_status()
        _json = _res.json()
        _category_dict = _json_to_dict(_json)

        return _category_dict, _json

    except Exception as e:
        print('Something wrong happened.\n', e)

        return None, None
