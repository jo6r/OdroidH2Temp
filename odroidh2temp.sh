#!/usr/bin/env bash
# set line separator to Unix LF!
# set access rights to 0774
#   sudo chmod 0774 odroidh2temp.sh
# set up cron scheduler
#   crontab -l (list user's crontab)
#   crontab -e (edit user's crontab)
#   EDITOR=nano crontab -e
#   e.g. */15 * * * * /home/jo6r/projects/OdroidH2Temp/odroidh2temp.sh   # At every 15th minute

PROJECT_DIR=/home/jo6r/projects/OdroidH2Temp
"${PROJECT_DIR}"/.venv/bin/python "${PROJECT_DIR}"/odroidh2temp.py