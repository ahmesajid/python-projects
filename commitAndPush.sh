#!/bin/bash

MSG="commiting files 4/12/2026 new python project(password checker)"
LOGFILE="git_log.txt"

echo "adding git files .." | tee -a "$LOGFILE"
git add . 2>&1 | tee -a "$LOGFILE"

echo "committing files .." | tee -a "$LOGFILE"
git commit -m "${MSG}s" 2>&1 | tee -a "$LOGFILE"

echo "pushing code .." | tee -a "$LOGFILE"
git push -u origin master 2>&1| tee -a "$LOGFILE"

echo "logs saved in ${LOGFILE}" | tee -a "$LOGFILE"