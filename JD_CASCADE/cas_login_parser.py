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
    else:
        if 'parameters' in data and 'ticket' in data['parameters']:
      	    result = data['parameters']['ticket'][0]
	    if len(result) == 0:
		print("Error: scripts return null.")
		sys.exit(1)
	    else:
		print(result)
		sys.exit(0)
        else:
            print("Error: Param is error.")
            sys.exit(1)

if __name__ == '__main__':
    main()

