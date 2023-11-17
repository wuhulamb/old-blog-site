---
title: 每日到课率整理@Python
author: wuhulamb
date: 2023-11-02 18:53
place: 兰大，榆中，教室
---
一个整理每日到课率程序的使用说明
<!--more-->

## 写给谁

- 需要使用该程序进行数据处理的人
- ~~想要了解技术实现思路的人（先留一个坑，以后有空再填）~~

## 功能

- 制作每日到课率表
- 制作异常情况表+截图重命名

## 代码下载
- [nor-make.py](/media/download/nor-make.py)
- [art-make.py](/media/download/art-make.py)

## 开始使用

### 1. 数据准备

#### （1）查课同学
只保留**小表头** + **今天要处理的数据**（eg. 周二9-11+周三1-8），建议**按行复制**，不要遗漏备注

![original-data.png](/media/image/2023/11/original-data.png)
*此处以秦岭堂为例，天山堂、闻韶楼同理*

#### （2）办公室助理
如果有**上周周5**异常课程的记录，**需删除**（删除后序号无需调整），保证记录的异常情况都是本周的,其余不变

![office.png](/media/image/2023/11/office.png)

#### （3）截图
截图路径示例（注意：截图存放在**第7周**，不是第七周）

    F:\到课情况原始数据\20231017\天山堂   #「第7周」文件夹上一级

![data-env2.png](/media/image/2023/11/data-env2.png "environment")

### 2. 运行程序

#### （1）打开cmd
![cmd.png](/media/image/2023/11/cmd.png "cmd")

#### （2）运行python程序
    python D:\xxx\xxx\nor-make.py  # 运行程序（后面为nor-make.py文件所在路径）

![nor-make-start.png](/media/image/2023/11/nor-make-start.png "start")
*此处以nor-make.py为例，art-make.py同理*

### 3. 输入选项

#### （1）输入示例
- 第一项：数据地点（art-make.py默认闻韶楼，无需输入）
- 第二项：原始查课数据路径（**小表头** + **今天待做数据**）【详见[数据准备（1）](#1查课同学)】
- 第三项：异常到课数据路径【详见[数据准备（2）](#2办公室助理)】
- 第四项：截图文件夹路径【详见[数据准备（3）](#3截图)】
- 第五项：生成文件路径，即文件输出位置

![nor-make-input.png](/media/image/2023/11/nor-make-input.png "input")
*输入概览*

#### （2）示例环境
![data-env1.png](/media/image/2023/11/data-env1.png "environment")
*总环境*

![data-env2.png](/media/image/2023/11/data-env2.png "environment")
*天山堂环境*

![data-env3.png](/media/image/2023/11/data-env3.png "environment")
*周次文件夹需命名为**第7周**，而不是第七周*

![data-env4.png](/media/image/2023/11/data-env4.png "environment")
*周二各节次文件夹*

![data-env5.png](/media/image/2023/11/data-env5.png "environment")
*7-8节问题教室截图*


### 4. 打印输出（用作检查）
![nor-make-report1.png](/media/image/2023/11/nor-make-report1.png "report")
*输出*

![nor-make-report2.png](/media/image/2023/11/nor-make-report2.png "report")
*and another 输出*

### 5. 见证奇迹
![result1.png](/media/image/2023/11/result1.png "result")
*生成文件夹*

![result2.png](/media/image/2023/11/result2.png "result")
*每日到课率表+异常情况截图*

![result3.png](/media/image/2023/11/result3.png "result")
*每日到课率表*

![result4.png](/media/image/2023/11/result4.png "result")
*截图 + 异常情况表*

![result5.png](/media/image/2023/11/result5.png "result")
*异常情况表*
