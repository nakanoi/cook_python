#!/bin/bash
printenv | awk '{print "export " $1}' > /code/env.sh
/usr/sbin/cron -f
