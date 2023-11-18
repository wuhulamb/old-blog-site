# C:\Users\xsy\AppData\Local\Programs\Python\Python38\python.exe
# -*- Coding: UTF-8 -*-
# CreateDate: 2023-10-18 12:53
# Author: wuhulamb
import datetime
import pandas as pd

# 一些重要的默认值
crtyear = 2023                       # 当前的年份
week1m, week1d, week1y = 9, 3, 2023  # 当前学期的第一周的第一天

m, d, y = datetime.date.today().strftime('%m-%d-%Y').split('-')
m, d, y = int(m), int(d), int(y)
# m, d, y = 10, 10, 2023                           # 正式投入使用时请注释本行|与星期需匹配

data = {}
data["序号"] = []
data["课程名称"] = []
data["开课院系"] = []
data["课程号"] = []
data["选课人数"] = []
data["选课属性"] = []
data["主讲教师姓名"] = []
data["主讲教师所在院系"] = []
data["合讲教师"] = []
data["合班"] = []
data["周次分布"] = []
data["具体日期"] = []
data["星期"] = []
data["节次"] = []
data["教室"] = []
data["教师是否正常到课"] = []
data["学生是否正常到课"] = []
data["备注"] = []
hdr_data = {}
yesterdayNum = 0
todayNum = 0

def tozero(m: int, d: int, y: int):
    """
    计算输入日期到数学0年（公元元年1月1日前一天）的天数
    """
    normal_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    # 闰年 四年一闰 百年不闰 四百年一闰 1900不是闰年 2000是闰年 2020是闰年
    n = (y - 1) // 100
    q = (y - 1) // 4 - (n - (n // 4))  # 从输入日期的前一年到数学0年的闰年数
    a = q * 366 + (y - 1 - q) * 365    # 从输入日期的前一年到数学0年的天数
    if m > 1:  # 对月的情况进行讨论
        if (y % 100 != 0 and y % 4 == 0) or (y % 100 == 0 and y % 400 == 0):  # 闰年的情况
            b = sum([leap_year[z] for z in range(1, m)])                      # b是m之前月份的天数和
        else:                                                                 # 平年的情况
            b = sum([normal_year[z] for z in range(1, m)])
    else:
        b = 0
    return a + b + d

def yesterday(m: int, d: int, y: int):
    """
    返回输入日期前一天是几月几号
    """
    normal_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if m > 1:  # 对月的情况进行讨论
        lastm = m - 1
        lasty = y
        if (y % 100 != 0 and y % 4 == 0) or (y % 100 == 0 and y % 400 == 0):  # 闰年的情况
            lastd = leap_year[lastm]
        else:                                                                 # 平年的情况
            lastd = normal_year[lastm]
    else:
        lastm = 12
        lastd = 31
        lasty = y - 1
    if d > 1:
        return (m, d - 1, y)
    else:
        return (lastm, lastd, lasty)

# t % 7 {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
def weekday(m: int, d: int, y: int):
    """
    返回输入日期是星期几
    """
    return tozero(m, d, y) % 7

# 计算第几周
def whichweek(m: int, d: int, y: int, week1m=week1m, week1d=week1d, week1y=week1y):  # week1m, week1d为第一周的第一天（礼拜一的前一天————周日）
    """
    返回输入日期所在周次（如第一周）
    """
    t = tozero(m, d, y) - tozero(week1m, week1d, week1y)
    return t // 7 + 1

if __name__ == '__main__':
    
    print(r'''       
                    _                    _                     
         ___  _ _ _| |_ ___ ._ _ _  ___ | |__ ___     ___  _ _ 
        <_> || '_> | | |___|| ' ' |<_> || / // ._> _ | . \| | |
        <___||_|   |_|      |_|_|_|<___||_\_\\___.<_>|  _/`_. |
                                                     |_|  <___'
                  
                                 _        _           
             _ __ ___   __ _  __| | ___  | |__  _   _ 
            | '_ ` _ \ / _` |/ _` |/ _ \ | '_ \| | | |
            | | | | | | (_| | (_| |  __/ | |_) | |_| |
            |_| |_| |_|\__,_|\__,_|\___| |_.__/ \__, |
                                                |___/ 

                    __               ___                        __        
                   /\ \             /\_ \                      /\ \       
 __  __  __  __  __\ \ \___   __  __\//\ \      __      ___ ___\ \ \____  
/\ \/\ \/\ \/\ \/\ \\ \  _ `\/\ \/\ \ \ \ \   /'__`\  /' __` __`\ \ '__`\ 
\ \ \_/ \_/ \ \ \_\ \\ \ \ \ \ \ \_\ \ \_\ \_/\ \L\.\_/\ \/\ \/\ \ \ \L\ \
 \ \___x___/'\ \____/ \ \_\ \_\ \____/ /\____\ \__/.\_\ \_\ \_\ \_\ \_,__/
  \/__//__/   \/___/   \/_/\/_/\/___/  \/____/\/__/\/_/\/_/\/_/\/_/\/___/ 
                                                                          
    
    ''')
    
    print('''
    [NOTICE]
     * 原始到课数据的条数一定要保证无误
     * 办公室助理异常表需删除上周五的课程（保证全是本周课程）
     * 文件路径输入不能有引号、空格
     * 按Ctrl+C即可中断程序
    ''')
    check_pth = input('请输入闻韶楼数据表（表头+内容）：')
    office_pth = input('请输入办公室助理的异常表：')
    save_pth = input(r'请输入生成文件路径（eg. D:\xxx\xxx，按回车直接生成在当前工作路径）：')

    check_pth = '/'.join(check_pth.split('\\'))
    office_pth = '/'.join(office_pth.split('\\'))

    lastm, lastd, lasty = yesterday(m, d, y)
    weekToday = weekday(m, d, y)
    weekYesterday = weekday(lastm, lastd, lasty)

    #if weekToday == 5:
    #    classNumber = '1-11节'
    #else:
    #    classNumber = '1-8节'

    print('\n到课率表：\n')
    # print("【出现报错】（problem['教室情况（详细阐述）'].append(info_data.strip())）\n则数据表里查课同学无备注but异常表办公室助理有备注\n")
    wb_check = pd.read_excel(check_pth, header=None)     # 表头+当天需要处理的数据
    wb_office = pd.read_excel(office_pth, header=None)
    issue = {}
    hdr_issue = {}
    for k, foo in enumerate(wb_office.values[1]):
        if k < 14:
            hdr_issue[k] = foo
            issue[foo] = []
    for i in wb_office.values[2:]:
        for k, j in enumerate(i):
            if k < 14:
                issue[hdr_issue[k]].append(str(j))
    issue_df = pd.DataFrame(issue)

    for k, foo in enumerate(wb_check.values[0]):
        hdr_data[k] = foo
    for i in wb_check.values[1:]:
        # 从一行数据中逐个提取需要的信息
        for k, j in enumerate(i):
            if hdr_data[k] == '选课人数':            # int
                selhum = int(j)
                data[hdr_data[k]].append(selhum)
            if hdr_data[k] == '星期':                # str
                week_data = str(j)
                data[hdr_data[k]].append(week_data)
            if hdr_data[k] == '节次':                # str
                classNum_data = j
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '教室':                # str
                classroom_data = j
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '合班':                # str/nan
                stu_class = j
                data[hdr_data[k]].append(j)
            # 不做处理的信息
            if hdr_data[k] == '课程名称':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '开课院系':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '课程号':
                data[hdr_data[k]].append(str(j))
            if hdr_data[k] == '选课属性':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '主讲教师姓名':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '主讲教师所在院系':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '合讲教师':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '周次分布':
                data[hdr_data[k]].append(j)
        
        # 根据星期计算具体日期并填入，同时填入序号
        if week_data == str(weekYesterday):
            yesterdayNum += 1
            data['具体日期'].append('%.2d.%.2d' %(lastm, lastd))
            data['序号'].append(yesterdayNum)
        elif week_data == str(weekToday):
            todayNum += 1
            data['具体日期'].append('%.2d.%.2d' %(m, d))
            data['序号'].append(todayNum)
        else:
            print('日期与星期不匹配')
        
        # 写入异常情况备注
        for bar in issue_df[(issue_df['星期'] == str(weekYesterday)) | (issue_df['星期'] == str(weekToday))].values:
            # 从一行数据中依次提取相关信息
            for k, foo in enumerate(bar):
                if hdr_issue[k] == '星期':     # str
                    week_iss = foo.strip()     # 去前后空格，减少人为错误导致程序出现error
                if hdr_issue[k] == '节次':     # str
                    classNum_iss = foo.strip()
                if hdr_issue[k] == '教室':     # str
                    classroom_iss = foo.strip()
                if hdr_issue[k] == '备注信息':  # str
                    info_iss = foo.strip()
            if '闻韶楼' in classroom_iss or '美术' in classroom_iss or '音乐' in classroom_iss:
                if '闻韶楼' in classroom_iss:
                    classroom_iss = classroom_iss[3:].upper()
                else:
                    classroom_iss = classroom_iss.upper()
                # print(f'{week_data} == {week_iss} & {classNum_data} == {classNum_iss} & {classroom_data} == {classroom_iss}')
                if week_data == week_iss and classNum_data == classNum_iss and classroom_data == classroom_iss:
                    comment = info_iss
                    print(f'【闻韶楼到课异常（备注已写入到课表）】星期{week_data} {classNum_data} {classroom_data} 课程：{data["课程名称"][-1]} 备注：{comment}\n')
                    break
        else:
            comment = ''                      # 办公室助理无备注
        if comment == '':
            data['教师是否正常到课'].append('Y')
            data['学生是否正常到课'].append('Y')
        else:
            data['教师是否正常到课'].append('N')
            data['学生是否正常到课'].append('N')

        data['备注'].append(comment)

    # 提取待做数据的各时间段及教室，为后续遍历找到合班做准备
    data_df = pd.DataFrame(data)
    if save_pth == '':
        data_df.to_excel('闻韶楼%d月%d日学生到课情况统计表.xlsx' %(m, d), index=False)
    else:
        save_pth = '/'.join(save_pth.split('\\'))
        data_df.to_excel('%s/闻韶楼%d月%d日学生到课情况统计表.xlsx' %(save_pth, m, d), index=False)
    
    print('只是打印输出昨天、今天的闻韶楼异常以作检查之用：')
    for bar in issue_df[(issue_df['星期'] == str(weekYesterday)) | (issue_df['星期'] == str(weekToday))].values:
        # 从一行数据中依次提取相关信息
        for k, foo in enumerate(bar):
            if hdr_issue[k] == '星期':     # str
                week_iss = foo.strip()     # 去前后空格，减少人为错误导致程序出现error
            if hdr_issue[k] == '节次':     # str
                classNum_iss = foo.strip()
            if hdr_issue[k] == '教室':     # str
                classroom_iss = foo.strip()
            if hdr_issue[k] == '备注信息':  # str
                info_iss = foo.strip()
            if hdr_issue[k] == '课程名称':  # str
                name = foo.strip()
        if '闻韶楼' in classroom_iss or '美术' in classroom_iss or '音乐' in classroom_iss:    # 异常表中找到闻韶楼
            print(f'【闻韶楼到课异常】星期{week_iss} {classNum_iss} {classroom_iss} 课程：{name} 备注：{info_iss}\n')
    weekNum2Str = {1: "第一周", 2: "第二周", 3: "第三周", 4: "第四周", 5: "第五周", 6: "第六周", 7: "第七周", 8: "第八周", 9: "第九周", 10: "第十周", 11: "第十一周", 12: "第十二周", 13: "第十三周", 14: "第十四周", 15: "第十五周", 16: "第十六周", 17: "第十七周", 18: "第十八周", 19: "第十九周", 20: "第二十周",}               
    print(f'''
    【到课表注意事项】
    1. 调课至不同时段的备注需改成具体日期（其他备注也根据需要进行调整，如删除nan）
    2. 添加：X月X日闻韶楼第X-X节到课情况统计表（{weekNum2Str[whichweek(m, d, y)]}周X）
    3. 无师生的情况标黄
    4. 字体、字号、行高、列宽、边框
    5. 添加最后一行的备注说明
    ''')

