import sys
import os
_pwd = os.path.dirname(__file__)
sys.path.append(_pwd)
sys.path.append(os.path.abspath(os.path.join(_pwd, '..')))

from datetime import datetime
from request import get_category
from set_record import recording
from cur import Cur


def main():
    print('Getting category started at {}.'.format(datetime.now()))

    _cur = Cur()
    _category_dict, _json = get_category()
    if _category_dict and _json:
        recording(_cur, _category_dict, _json)

    print('Done at {}.'.format(datetime.now()))

    return


if __name__ == '__main__':
    main()
