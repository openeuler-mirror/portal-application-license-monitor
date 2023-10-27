#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) Huawei Technologies Co., Ltd. 2023-2023. All rights reserved.
import sys
import json

PARAM = sys.argv[1]
DATA = json.loads(PARAM)

def main():
    if len(DATA) == 0:
        print("Error: Param is null.")
        sys.exit(1)
    else:
        if 'parameters' in DATA:
            # URL传参，KOAL_CERT_CN/KOAL_CLIENT_IP/X-Forward-Host根据实际情况修改，forwardHost可返回空
            result = {
                "cn":DATA['parameters']['KOAL_CERT_CN'],
                "ip":DATA['parameters']['KOAL_CLIENT_IP'],
                "forwardHost":DATA['parameters']['X-Forward-Host']
            }
        elif 'headers' in DATA:
            # URL传参，同上
            result = {
                "cn":DATA['headers']['KOAL_CERT_CN'],
                "ip":DATA['headers']['KOAL_CLIENT_IP'],
                "forwardHost":DATA['headers']['X-Forward-Host']
            }
        elif 'cookies' in DATA:
            # cookie传参，同上
            result = {
                "cn":DATA['cookies']['KOAL_CERT_CN'],
                "ip":DATA['cookies']['KOAL_CLIENT_IP'],
                "forwardHost":DATA['cookies']['X-Forward-Host']
            }
        else:
            # 未传合法参数
            print("Error: Param is null.")
            sys.exit(1)
    # 输出解析结果
    print(json.dumps(result))
    sys.exit(0)  


if __name__ == '__main__':
    main()
