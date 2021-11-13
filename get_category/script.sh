#!/bin/bash
. /code/env.sh
python /code/get_category/main.py >> /var/log/get_category_cron.log
