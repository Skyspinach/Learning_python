#!/usr/bin/python3
'''
function(学生信息管理系统操作函数)
'''
import pickle
import json
import System_user_mangement
import os


def display(Student_info): #显示函数
    for student in Student_info:
         print(student)
    return

def insert(Student_info):#添加函数
    dict = {}
    name = input("请输入学生姓名：")
    schoolnum = input("请输入学生学号：")
    phone = input("请输入学生电话：")
    dict['姓名'] = name
    dict['学号'] = schoolnum
    dict['电话'] = phone
    Student_info.append(dict)
    print("当前学生信息：", dict)
    return

####################################################################
#查找函数


def searchbyname(Student_info):#按名查找函数
    print("")
    flag = 0
    name = input("请输入需要查询的学生姓名：")
    for student in Student_info:
        if student['姓名'] == name:
           print(student)
           break
        else:
           flag+=1
    # print(flag)
    # print(len(Student_info))
    if(flag == len(Student_info)):
        print("无此人")
    return

def searchbyschoolnum(Student_info):#按学号查找函数
    print("")
    flag = 0
    schoolnum = input("请输入需要查询的学生学号：")
    for student in Student_info:
        if student['学号'] == schoolnum:
            print(student)
            break
        else:
            flag += 1
            # print(flag)
            # print(len(Student_info))
    if (flag == len(Student_info)):
         print("无此人")
    return

def searchbyphone(Student_info):#按电话查找函数
    print("")
    flag = 0
    phone = input("请输入需要查询的学生学号：")
    for student in Student_info:
        if student['电话'] == phone:
            print(student)
            break
        else:
            flag += 1
            # print(flag)
            # print(len(Student_info))
    if (flag == len(Student_info)):
        print("无此人")
    return


def search(Student_info):#查找主函数界面
    while True:
        print("z" * 50)
        print("       欢迎使用  学生信息查询    \n")
        print("             1.通过名字查询")
        print("             2.通过学号查询")
        print("             3.通过电话查询")
        print("             0.退出")
        print("z" * 50)
        option_search = input("  请输入操作;")
        if option_search == "1":
            print("你选择的操作是 1 ")
            searchbyname(Student_info)
        elif option_search == "2":
            print("你选择的操作是 2 ")
            searchbyschoolnum(Student_info)
        elif option_search == "3":
            print("你选择的操作是 3 ")
            searchbyphone(Student_info)
        elif option_search == "0":
            print("你选择的操作是 0 ")
            break
        else:
            print("没有这个操作请检查！！！")



###################################################################


def delete(Student_info):#删除函数
    #print(Student_info)
    print("当前全部学生名字信息：")
    for student in Student_info:
        print(student)
    name = input("请输入需要删除的学生的姓名：")
    flag = 0 #列表项计数
    for student_d in Student_info:
        flag += 1
        #print(flag)
        if student_d['姓名'] == name:
            print("查找到", "(", student_d['姓名'], ")")
            pd = input("是否删除？ (y/n)  >>>")
            if pd == "y":
                student_d.clear()
                Student_info.pop(flag - 1)
                print("\n操作完成\n\n当前学生信息：")
                for student in Student_info:
                    print(student)
            elif pd == "n":
                break
            else:
                print("没有这个操作")
    return






def modify(Student_info):#修改函数
    #print(Student_info)
    print("当前全部学生名字信息：")
    for student in Student_info:
        print(student)
    name = input("请输入需要修改信息的学生的姓名：")
    flag = 0 #列表项计数
    for student_d in Student_info:
        flag += 1
        #print(flag)
        if student_d['姓名'] == name:
            print("查找到", "(", student_d, ")")
            pd = input('''请选择修改的对象？ 
        1.姓名
        2.学号
        3.电话
        >>>''')
            if pd == "1":
                con = input("请输入修改的姓名： ")
                student_d['姓名'] = con
                print("修改完成")
                print("修改后\n", "(", student_d, ")")
                break
            elif pd == "2":
                con = input("请输入修改的学号： ")
                student_d['学号'] = con
                print("修改完成")
                print("修改后\n", "(", student_d, ")")
                break
            elif pd == "3":
                con = input("请输入修改的电话： ")
                student_d['电话'] = con
                print("修改完成")
                print("修改后\n", "(", student_d, ")")
                break
            else:
                print("没有这个操作")
            break
    if (flag == len(Student_info)):
        print("无此人")
    return



def progress_bar(num):#进度条
    import time
    import sys
    for i in range(101):
        sys.stdout.write('\r')
        sys.stdout.write("%s%% | %s" % (int(i % 101), int(i % 101) * '>'))
        sys.stdout.flush()
        time.sleep(num)
    sys.stdout.write('\n')





######################################################
#序列化保存,读取数据

def savedata_pickle(Student_info,path):#序列化保存数据，（仅限python3读取）
    with open(path, 'wb') as f:
        pickle.dump(Student_info, f)

def readdata_pickle(path):  # 读取序列化数据，（仅限python3读取）
    with open(path, 'rb') as f:
        Student_info_re = pickle.load(f)
        #print(Student_info_re)
        #display(Student_info_re)
        print("   本地数据读取成功\n")
    return Student_info_re

######################################################


######################################################
#序列化json保存,读取数据

def savedata_json(Content,path):#序列化json保存数据，
    with open(path, 'w', encoding='UTF-8') as f:
        json.dump(Content, f)

def readdata_json(path):  # 读取序列化json数据，
    with open(path, 'r') as f:
        Student_info_re = json.load(f)
        #print(Student_info_re)
        #display(Student_info_re)
        print("   本地数据读取成功\n")
    return Student_info_re

######################################################

def pathconfrim(path): #存储路径检测
    isExists = os.path.exists(path)
    if (isExists == True):
        return True
    elif(isExists == False):
        return False













