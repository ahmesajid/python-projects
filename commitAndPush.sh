#!/bin/bash

echo "Enter commit message : "
read MSG
LOGFILE="git_log.txt"

echo "adding git files .." | tee -a "$LOGFILE"
git add . 2>&1 | tee -a "$LOGFILE"

echo "committing files .." | tee -a "$LOGFILE"
git commit -m "${MSG}" 2>&1 | tee -a "$LOGFILE"

echo "pushing code .." | tee -a "$LOGFILE"
git push -u origin main 2>&1| tee -a "$LOGFILE"

echo "logs saved in ${LOGFILE}" | tee -a "$LOGFILE"