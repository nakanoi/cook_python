#!/bin/bash
. /code/env.sh
python /code/get_recipe/main.py >> /var/log/get_recipe_cron.log
