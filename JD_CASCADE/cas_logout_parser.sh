#!/bin/bash
workdir=$(cd $(dirname $0); pwd)
python ${workdir}/logout_parser.py "$1"
exit $?
