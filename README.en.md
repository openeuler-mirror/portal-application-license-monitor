# portal-application-license-monitor

#### Description
Donau Portal visualizes the status data of license management utilities through the monitoring module. The status data collection scripts of different types of license management utilities need to be created in accordance with the Donau Portal rules.
portal-application-license-monitor provides a best practice for Donau Portal to interconnect with the FlexNet license management utility.

#### Software Architecture
Python2/Python3

#### Operation

1. Download the compressed package from  https://gitee.com/openeuler/portal-application-license-monitor and decompress it to the {INSTALL_PATH}/huawei/portal/ac/scripts/license_manager/ directory.

   Note: INSTALL_PATH is the client installation directory and SCHEDULER_TYPE is the scheduler type.

   <table> <tr> <td style='color:#fff;background:black'><pre>[root@hpc13554 license_manager]# pwd</pre>
   <pre>/opt/huawei/portal/ac/scripts/license_manager</pre>
   <pre>[root@hpc13554 license_manager]# ll</pre>
   <pre>total 16</pre>
   <pre>-rw-r--r-- 1 root root 15855 May  5 17:15 flexnet</pre>
   [root@hpc13554 license_manager]# </td> </tr> </table>

2. Change the owner of the script to the Donau Portal/Donau Portal Client installation user with permission 500.

   <table> <tr> <td style='color:#fff;background:black'><pre>[root@hpc13554 license_manager]# chown ccp_master: flexnet</pre>
   <pre>[root@hpc13554 license_manager]# chmod 500 flexnet</pre>
   <pre>[root@hpc13554 license_manager]# ll</pre>
   <pre>total 16</pre>
   <pre>-r-x------ 1 ccp_master ccs_master 15855 May  5 17:15 flexnet</pre>
   [root@hpc13554 license_manager]# </td> </tr> </table>

4. Modify the fileformat file format of the script file to unix (if dos2unix is installed, you can use dos2unix filename1 filename2 filename3 to convert multiple files, if dos2unix is not installed, you can follow the steps below to modify the file format.)

   a)     vim filename

   b)     Input:set ff=unix，then press Enter

   c)     :wq!Save the file.

#### Instructions

1. For details, see section 7.1.26 in the "HPC 23.0.RC1 User Guide".

#### Precautions

1.  This script adaptation is for versions after HPC_23.0.RC1;
2.  This script applies only to the FlexNet license management utility. For other types of license management utilities, you can customize a status data collection script named after the license management utility by referring to this script.

#### Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request


#### Gitee Feature

1.  You can use Readme\_XXX.md to support different languages, such as Readme\_en.md, Readme\_zh.md
2.  Gitee blog [blog.gitee.com](https://blog.gitee.com)
3.  Explore open source project [https://gitee.com/explore](https://gitee.com/explore)
4.  The most valuable open source project [GVP](https://gitee.com/gvp)
5.  The manual of Gitee [https://gitee.com/help](https://gitee.com/help)
6.  The most popular members  [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
