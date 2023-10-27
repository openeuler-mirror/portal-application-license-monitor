# portal-application-license-monitor

#### Description
user can log in Donau Portal through the security authentication gateway and CAS. When connecting to the security authentication gateway and CAS, you need to customize the required information parsing script based on the provided sample script.

#### Software Architecture
Shell/Python2/Python3

#### Operation

1. Download the compressed package from  https://gitee.com/openeuler/portal-application-license-monitor/tree/jg_cascade_protection_scripts and decompress it to the {INSTALL_PATH}/huawei/portal/ac/scripts/auth/ directory.

   Note: INSTALL_PATH is the installation directory of Donau Portal.

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

2. Change the owner of the script to the Donau Portal installation user with permission 500.

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

4. Modify the fileformat file format of the script file to unix (if dos2unix is installed, you can use dos2unix filename1 filename2 filename3 to convert multiple files, if dos2unix is not installed, you can follow the steps below to modify the file format.)

   a)     vim filename

   b)     Input:set ff=unix，then press Enter

   c)     :wq!Save the file.

#### Precautions

1.  This script adaptation is for versions after HPC_23.0.0;

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
