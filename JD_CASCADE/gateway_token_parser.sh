#!/bin/bash
# 获取参数
JSON_PARAM=$1

# 参数解析 
workdir=$(cd $(dirname $0); pwd)
python ${workdir}/gateway_token_parser.py "$1"
exit $?