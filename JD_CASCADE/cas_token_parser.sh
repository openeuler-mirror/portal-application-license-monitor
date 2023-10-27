#!/bin/bash
workdir=$(cd $(dirname $0); pwd)

# cas认证使用http协议
output=$(python ${workdir}/token_parser.py "$1")
if [[ $? -eq 0 && -n "${output}" ]]; then
    username=$(echo -e "$output" | grep -oP '^.+$' | tail -n 1)
    echo "${username}" && exit 0
fi
echo "Error: token parser scripts return null." && exit 1

# cas认证使用https协议
# echo "$1" | grep -oP '(?<=<cas:user>).*(?=</cas:user>)'
# exit $?
