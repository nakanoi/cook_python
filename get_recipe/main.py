import sys
import os
_pwd = os.path.dirname(__file__)
sys.path.append(_pwd)
sys.path.append(os.path.abspath(os.path.join(_pwd, '..')))

from datetime import datetime
from request import ger_recipes
from set_record import recording, get_category
from cur import Cur


def main():
    print('Getting menu started at {}.'.format(datetime.now()))

    _cur = Cur()
    _categories = get_category(_cur)
    _recipes = ger_recipes(_categories)
    if _recipes:
        recording(_cur, _recipes)
    _cur.close()

    print('Done at {}.'.format(datetime.now()))

    return


if __name__ == '__main__':
    main()
