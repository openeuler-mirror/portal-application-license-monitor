#!/bin/bash
workdir=$(cd $(dirname $0); pwd)
python ${workdir}/login_parser.py "$1"
exit $?
