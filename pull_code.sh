#!/bin/bash

FILE_NAME="fetch_code.logs"

echo "PULLING LATEST CODE FROM REPO.."  | tee -a $FILE_NAME
git pull origin main 2>&1 | tee -a $FILE_NAME

echo "CODE FETCHED FROM BRANCH MAIN"  | tee -a $FILE_NAME

