#!/bin/sh 

python --version 
pip --version 
pip list | grep mlrun 
echo "Using API key: $API_KEY" 
mlrun project -n cancer-project -u "git://https://github.com/BaldeThierno/MLOps.git" ./project 
mlrun project -r main -w ./project/MLRun/cancer-project