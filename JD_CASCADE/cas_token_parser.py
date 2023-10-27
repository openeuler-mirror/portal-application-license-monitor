#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) Huawei Technologies Co., Ltd. 2023-2023. All rights reserved.
import sys
import json

param = sys.argv[1]
data = json.loads(param)

def main():
    if len(data) == 0:
        print("Error: Param is null.")
        sys.exit(1)
    elif 'body' in data:
        print(data['body'])
        sys.exit(0)
    else:
        print("Error: script parameter is wrong.")
        sys.exit(1)

if __name__ == '__main__':
    main()
