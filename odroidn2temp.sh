#!/usr/bin/env bash
# set line separator to Unix LF!
# set access rights to 0774
#   sudo chmod 0774 odroidn2temp.sh
# set up cron scheduler
#   crontab -l (list user's crontab)
#   crontab -e (edit user's crontab)
#   EDITOR=nano crontab -e
#   e.g. */15 * * * * /home/jo6r/projects/OdroidN2Temp/odroidn2temp.sh   # At every 15th minute

export PIPENV_VENV_IN_PROJECT=1

#pipenv install
pipenv run python odroidn2temp.py