#!/bin/bash
workdir=$(cd $(dirname $0); pwd)
python ${workdir}/cas_login_parser.py "$1"
exit $?
