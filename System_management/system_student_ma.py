#!/usr/bin/python3
import time
import function_Student
import os
'''
Student_information_management_system(学生信息管理系统)
'''
#path_pickle = './data_save\sytemdata.pdata'
path_json_data = 'sytemdata.json'


def system_student_root(Student_info):#root系统用户管理模式UI
    function_Student.progress_bar(0.01)

    #Student_info = [{'姓名': '1', '学号': '5674', '电话': '547'}, {'姓名': '2', '学号': '6964', '电话': '65465'}, {'姓名': '3', '学号': '6964', '电话': '65465'}]

    #Student_info = function_Student.readdata_pickle(path_pickle )
    #Student_info = function_Student.readdata_json(path_json_data)

    while True:
            print("="*50)
            print("          欢迎使用学生管理系统\n")
            print("             1.添加学生信息")
            print("             2.删除学生信息")
            print("             3.修改学生信息")
            print("             4.查找学生信息")
            print("             5.查看全部学生信息")
            print("             0.保存退出")
            print("="*50)
            option = input("  请输入操作;")
            if option == "1":
                print("你选择的操作是 1 ")
                function_Student.insert(Student_info)
            elif option == "2":
                print("你选择的操作是 2 ")
                function_Student.delete(Student_info)
            elif option == "3":
                print("你选择的操作是 3 ")
                function_Student.modify(Student_info)
            elif option == "4":
                print("你选择的操作是 4 ")
                function_Student.search(Student_info)
            elif option == "5":
                print("你选择的操作是 5 ")
                print("全部学生信息为：", )
                for student in Student_info:
                    print(student)
            elif option == "0":
                print("所有操作结束，3秒后保存数据并退出")
                function_Student.savedata_json(Student_info, path_json_data)
                #function_Student.savedata_pickle(Student_info, path_pickle)
                function_Student.progress_bar(0.01)
                # i = 3
                # while(i>0):
                #      print("倒计时%s秒后退出" % i)
                #      time.sleep(1)
                #      i-=1
                break
            else:
                print("没有这个操作请检查！！！")


def system_student_user(Student_info):#普通用户管理模式UI
    function_Student.progress_bar(0.01)

    #Student_info = [{'姓名': '1', '学号': '5674', '电话': '547'}, {'姓名': '2', '学号': '6964', '电话': '65465'}, {'姓名': '3', '学号': '6964', '电话': '65465'}]

    #Student_info = function_Student.readdata_pickle(path_pickle )
    #Student_info = function_Student.readdata_json(path_json )

    while True:
            print("="*50)
            print("          欢迎使用学生管理系统\n")
            print("             1.添加学生信息")
            print("             2.查找学生信息")
            print("             3.查看全部学生信息")
            print("             0.保存退出")
            print("="*50)
            option = input("  请输入操作;")
            if option == "1":
                print("你选择的操作是 1 ")
                function_Student.insert(Student_info)
            elif option == "2":
                print("你选择的操作是 2 ")
                function_Student.search(Student_info)
            elif option == "3":
                print("你选择的操作是 3 ")
                function_Student.display(Student_info)

            elif option == "0":
                print("所有操作结束，3秒后保存数据并退出")
                function_Student.savedata_json(Student_info, path_json_data)
                #function_Student.savedata_pickle(Student_info, path_pickle)
                function_Student.progress_bar(0.01)
                break
            else:
                print("没有这个操作请检查！！！")


def system_student_guest(Student_info):  # 游客模式UI
    function_Student.progress_bar(0.01)

    # Student_info = [{'姓名': '1', '学号': '5674', '电话': '547'}, {'姓名': '2', '学号': '6964', '电话': '65465'}, {'姓名': '3', '学号': '6964', '电话': '65465'}]

    # Student_info = function_Student.readdata_pickle(path_pickle )
    #Student_info = function_Student.readdata_json(path_json)
    while True:
        print("=" * 50)
        print("          欢迎使用学生管理系统（仅有查看功能）\n")
        print("             1.查找学生信息")
        print("             2.查看全部学生信息")
        print("             0.保存退出")
        print("=" * 50)
        option = input("  请输入操作;")
        if option == "1":
            print("你选择的操作是 1 ")
            function_Student.search(Student_info)
        elif option == "2":
            print("你选择的操作是 2 ")
            function_Student.display(Student_info)

        elif option == "0":
            print("所有操作结束，3秒后退出")
            function_Student.progress_bar(0.01)
            break
        else:
            print("没有这个操作请检查！！！")

