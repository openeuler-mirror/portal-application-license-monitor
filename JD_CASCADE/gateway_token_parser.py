#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) Huawei Technologies Co., Ltd. 2023-2023. All rights reserved.
import sys
import json

PARAM = sys.argv[1]
DATA = json.loads(PARAM)
cn = ''
ip = ''
forwardHost = ''
result=''

def main():
    if len(DATA) == 0:
        print("Error: Param is null.")
        sys.exit(1)
    else:
        if 'parameters' in DATA:
            # URL传参，koal_cert_cn/koal_client_ip/x-forwarded-host根据实际情况修改
	    for key in DATA['parameters']:
		if key.lower() == 'koal_cert_cn':
		    cn=DATA['parameters']['koal_cert_cn']
		elif key.lower() == 'koal_client_ip':
		    ip=DATA['parameters']['koal_client_ip']
		elif key.lower() == 'x-forwarded-host':
		    forwardHost=DATA['parameters']['x-forwarded-host']
		else:
		    continue
        if 'headers' in DATA:
            # URL传参，同上
	    for key in DATA['headers']:
                if key.lower() == 'koal_cert_cn':
                    cn=DATA['headers']['koal_cert_cn']
                elif key.lower() == 'koal_client_ip':
                    ip=DATA['headers']['koal_client_ip']
                elif key.lower() == 'x-forwarded-host':
                    forwardHost=DATA['headers']['x-forwarded-host']
		else:
                    continue
        if 'cookies' in DATA:
            # cookie传参，同上
	    for key in DATA['cookies']:   
                if key.lower() == 'koal_cert_cn':
                    cn=DATA['cookies']['koal_cert_cn']
                elif key.lower() == 'koal_client_ip':
                    ip=DATA['cookies']['koal_client_ip']
                elif key.lower() == 'x-forwarded-host':
                    forwardHost=DATA['cookies']['x-forwarded-host']
		else:
                    continue
    result = {
                "cn":cn,
                "ip":ip,
                "forwardHost":'https://' + forwardHost
            }
    # 输出解析结果
    print(json.dumps(result))
    sys.exit(0)  


if __name__ == '__main__':
    main()
