# portal-jg_cascade_protection_scripts

#### 介绍
多瑙管理平台（Donau Portal）支持通过安全认证网关和CAS统一认证中心登录，对接安全认证网关和CAS统一认证中心时，用户需要参照当前提供的样例脚本定制自己所需的信息解析脚本。

#### 软件架构
Shell/Python2/Python3


#### 操作教程

1. 从网址 https://gitee.com/openeuler/portal-application-license-monitor/tree/jg_cascade_protection_scripts 下载压缩包, 解压至{INSTALL_PATH}/huawei/portal/ac/scripts/auth/目录下；

   注：INSTALL_PATH为Donau Portal安装目录

   <table> <tr> <td style='color:#fff;background:black'><pre>[root@hpc13554 auth]# pwd</pre>
   <pre>/opt/huawei/portal/ac/scripts/auth</pre>
   <pre>[root@hpc13554 auth]# ll</pre>
   <pre>total 32</pre>
   <pre>-rw-r--r-- 1 root root 655 May  5 17:15 cas_login_parser.py</pre>
   <pre>-rw-r--r-- 1 root root 92 May  5 17:15 cas_login_parser.sh</pre>
   <pre>-rw-r--r-- 1 root root 655 May  5 17:15 cas_logout_parser.py</pre>
   <pre>-rw-r--r-- 1 root root 93 May  5 17:15 cas_logout_parser.sh</pre>
   <pre>-rw-r--r-- 1 root root 477 May  5 17:15 cas_token_parser.py</pre>
   <pre>-rw-r--r-- 1 root root 421 May  5 17:15 cas_token_parser.sh</pre>
   <pre>-rw-r--r-- 1 root root 1448 May  5 17:15 gateway_token_parser.py</pre>
   <pre>-rw-r--r-- 1 root root 135 May  5 17:15 gateway_token_parser.sh</pre>
   [root@hpc13554 auth]# </td> </tr> </table>

2. 更改脚本的属主为Donau Portal安装用户，权限为500

   <table> <tr> <td style='color:#fff;background:black'><pre>[root@hpc13554 auth]# chown ccp_master: *</pre>
   <pre>[root@hpc13554 auth]# chmod 500 *</pre>
   <pre>[root@hpc13554 auth]# ll</pre>
   <pre>total 32</pre>
   <pre>-r-x------ 1 ccp_master ccs_master 655 May  5 17:15 cas_login_parser.py</pre>
   <pre>-r-x------ 1 ccp_master ccs_master 92 May  5 17:15 cas_login_parser.sh</pre>
   <pre>-r-x------ 1 ccp_master ccs_master 655 May  5 17:15 cas_logout_parser.py</pre>
   <pre>-r-x------ 1 ccp_master ccs_master 93 May  5 17:15 cas_logout_parser.sh</pre>
   <pre>-r-x------ 1 ccp_master ccs_master 477 May  5 17:15 cas_token_parser.py</pre>
   <pre>-r-x------ 1 ccp_master ccs_master 421 May  5 17:15 cas_token_parser.sh</pre>
   <pre>-r-x------ 1 ccp_master ccs_master 1448 May  5 17:15 gateway_token_parser.py</pre>
   <pre>-r-x------ 1 ccp_master ccs_master 135 May  5 17:15 gateway_token_parser.sh</pre>
   [root@hpc13554 auth]# </td> </tr> </table>

3. 修改脚本文件的fileformat文件格式为unix（如果安装了dos2unix，可以使用dos2unix filename1 filename2 filename3转换多个文件，若未安装dos2unix，可按照下面步骤修改文件格式）

   a) vim filename

   b) 输入:set ff=unix，然后回车

   c) :wq!保存文件

#### 注意事项

1. 当前脚本适配是针对HPC_23.0.0及之后的版本；

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
