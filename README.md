# portal-application-license-monitor

#### 介绍
多瑙管理平台（Donau Portal）基于许可证管理服务状态数据，通过监控模块实现了对应用许可证管理服务的状态监控和展示。针对不同类型的许可证管理服务，需要根据Donau Portal的规则输出对应许可证管理服务的状态数据采集脚本。
portal-application-license-monitor提供了Donau Portal对接flexnet许可证管理服务的最佳实践脚本，方便用户参考集成。

#### 软件架构
Python2/Python3


#### 操作教程

1. 从网址 https://gitee.com/openeuler/portal-application-license-monitor 下载压缩包, 解压至{INSTALL_PATH}/huawei/portal/ac/scripts/license_manager/目录下；

   注：INSTALL_PATH为Donau Portal/Donau Portal Client安装目录

   <table> <tr> <td style='color:#fff;background:black'><pre>[root@hpc13554 license_manager]# pwd</pre>
   <pre>/opt/huawei/portal/ac/scripts/license_manager</pre>
   <pre>[root@hpc13554 license_manager]# ll</pre>
   <pre>total 16</pre>
   <pre>-rw-r--r-- 1 root root 15855 May  5 17:15 flexnet</pre>
   [root@hpc13554 license_manager]# </td> </tr> </table>

2. 更改脚本的属主为Donau Portal/Donau Portal Client安装用户，权限为500

   <table> <tr> <td style='color:#fff;background:black'><pre>[root@hpc13554 license_manager]# chown ccp_master: flexnet</pre>
   <pre>[root@hpc13554 license_manager]# chmod 500 flexnet</pre>
   <pre>[root@hpc13554 license_manager]# ll</pre>
   <pre>total 16</pre>
   <pre>-r-x------ 1 ccp_master ccs_master 15855 May  5 17:15 flexnet</pre>
   [root@hpc13554 license_manager]# </td> </tr> </table>

3. 修改脚本文件的fileformat文件格式为unix（如果安装了dos2unix，可以使用dos2unix filename1 filename2 filename3转换多个文件，若未安装dos2unix，可按照下面步骤修改文件格式）

   a) vim filename

   b) 输入:set ff=unix，然后回车

   c) :wq!保存文件

#### 使用说明

1.  参见《HPC 23.0.RC1 用户指南》7.1.26章节。

#### 注意事项

1. 当前脚本适配是针对HPC_23.0.RC1及之后的版本；
2. 当前脚本只适用于FlexNet许可证管理服务，其它类型许可证管理服务如需使用相关功能，需要定制对应许可证管理服务名称命名的数据采集脚本。

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
