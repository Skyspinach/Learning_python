#!/usr/bin/python3
'''
System-user-mangement(系统用户管理系统)
'''


import msvcrt
import system_student_ma
import function_Student
import json
import os

class User(object):
    def __init__(self):
        self.path_json_config = 'config.json'
        self.path_json_data = 'sytemdata.json'
        self.root = "admin"
        self.rootpassword = "admin"
        #self.user = [{'id': '2', 'password': '123456'}, {'id': '1', 'password': '654321'}]
        self.user = []
        self.guest = ""
        self.Student_info = []



    def userconfrim(self,passname):#用户确认函数
        flag = 0
        for use in self.user:
            #print(self.user)
            if (use['id'] == passname):
                print("当前是用户操作请输入密码：(输入 0 返回上一步) ")
                # print(use)
                password = input(">>> ")
                if (password == use['password']):
                    print("\n***********当前是操作用户界面*******\n")
                    if (self.userfunc() == False):
                        continue
                    break
                elif (password == "0"):
                    break
                else:
                    print("密码错误")
                    break
                return True
            else:
                flag += 1
        if (flag == len(self.user)):
            return False


    def pwd_input(self):
        chars = []
        while True:
            try:
                newChar = msvcrt.getch().decode(encoding="utf-8")
            except:
                return input("你很可能不是在cmd命令行下运行，密码输入将不能隐藏:")
            if newChar in '\r\n':  # 如果是换行，则输入结束
                break
            elif newChar == '\b':  # 如果是退格，则删除密码末尾一位并且删除一个星号
                if chars:
                    del chars[-1]
                    msvcrt.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格
                    msvcrt.putch(' '.encode(encoding='utf-8'))  # 输出一个空格覆盖原来的星号
                    msvcrt.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格准备接受新的输入
            else:
                chars.append(newChar)
                msvcrt.putch('*'.encode(encoding='utf-8'))  # 显示为星号
        return (''.join(chars))


    def userdisplay(self):#注册用户显示函数
        for use in self.user:
            print(use)


    def useadd(self):#用户添加函数
        while True:
                print("当前为用户添加操作 \n请输入您的用户名 ： (输入ESC返回上一步)")
                passname = input(">>>  ")
                if (passname == "ESC"):
                    break
                else:
                    print(" 请输入您的密码 ：")
                    password = input(">>>")
                    # print(passname)
                    # print(password)
                    dict = {}
                    dict['id'] = passname
                    dict['password'] = password
                    self.user.append(dict)
                    #self.userdisplay()


    def usedelete(self):  # 用户删除函数
        while True:
                print("当前为用户删除操作 \n当前注册用户如下 ： (输入ESC返回上一步)")
                self.userdisplay()
                passname = input("请输入你需要删除的用户名 \n>>> ")
                if (passname == "ESC"):
                    break
                else:
                    flag = 0  # 列表项计数
                    for use in self.user:
                        flag += 1
                        # print(flag)
                        if use['id'] == passname:
                            print("查找到 用户：", "(", use['id'], ")")
                            pd = input("是否删除？ (y/n)  >>>")
                            if pd == "y":
                                use.clear()
                                self.user.pop(flag - 1)
                                print("\n操作完成\n\n当前学生信息：")

                            elif pd == "n":
                                break
                            else:
                                print("没有这个操作")
                    if (flag == len(self.user)):
                        print("无此人")

    def rootfunc(self):#root用户管理模式
        while True:
            print("=" * 50)
            print("          当前为ROOT用户管理模式 \n")
            print("             1.添加用户")
            print("             2.删除注册用户信息")
            print("             3.查看全部用户信息")
            print("             4.打开学生信息管理系统")
            print("             5.系统自爆")
            print("             0.保存退出")
            print("=" * 50)
            option = input("  请输入操作;")
            if option == "1":
                print("你选择的操作是 1 ")
                self.useadd()
            elif option == "2":
                print("你选择的操作是 2 ")
                self.usedelete()
            elif option == "3":
                print("你选择的操作是 3 ")
                self.userdisplay()
            elif option == "4":
                print("你选择的操作是 4 ")
                system_student_ma.system_student_root(self.Student_info)
            elif option == "5":
                pass
            elif option == "0":
                return False
                break
            else:
                print("没有这个操作请检查！！！")


    def userfunc(self):#普通用户管理模式
        while True:
            print("=" * 50)
            print("            当前为  普通用户  管理模式 \n")
            print("             1.打开学生信息管理系统")
            print("             0.保存退出")
            print("=" * 50)
            option = input("  请输入操作;")
            if option == "1":
                print("你选择的操作是 1 ")
                system_student_ma.system_student_user(self.Student_info)
            elif option == "0":
                return False
                break
            else:
                print("没有这个操作请检查！！！")

    def guestfunc(self):#游客模式
        while True:
            print("=" * 50)
            print("            当前为   游客   模式 \n")
            print("             1.打开学生信息管理系统（仅有查看功能）")
            print("             0.保存退出")
            print("=" * 50)
            option = input("  请输入操作;")
            if option == "1":
                print("你选择的操作是 1 ")
                system_student_ma.system_student_guest(self.Student_info)
            elif option == "0":
                return False
                break
            else:
                print("没有这个操作请检查！！！")



    def loginUI(self, Student_info):#登录界面函数
        while True:
                print("=" * 50)
                print("            欢迎使用系统管理 \n")
                print("             1.登录用户")
                print("             2.用户注册")
                print("             0.保存退出")
                print("=" * 50)
                pd = input("您的操作选项：  \n>>>")
                if(pd == "1"):
                    passname = input("请输入登录用户: (回车进入游客模式) \n   >>>")
                    if (passname == self.root):  # 系统用户界面
                        print("当前是系统用户请输入密码：(输入 0 返回上一步) ")
                        password = input(">>> ")
                        if (password == self.rootpassword):
                            print("\n当前是系统用户界面\n")
                            if (self.rootfunc() == False):
                                continue
                        elif (password == "0"):
                            continue
                        else:
                            print("密码错误")
                        break
                    elif (self.userconfrim(passname) == True):  # 用户访问)
                        pass
                    elif (passname == self.guest):  # 游客访问
                        #print("当前是游客访问 （仅有查看功能） ")
                        #print("\n当前是游客界面\n")
                        if (self.guestfunc() == False):
                            continue

                    elif (self.userconfrim(passname) == False):
                        print("\n无此用户\n")
                        continue
                elif (pd == "2"):
                    self.useadd()
                elif (pd == "0"):
                    print("所有操作结束，3秒后保存数据并退出")
                    function_Student.savedata_json(self.user, self.path_json_config)
                    function_Student.progress_bar(0.01)
                    break
                else:
                    print("无此操作")

    def confrim(self, isExists_config,isExists_data):  # 存储路径检测
        # ba = System_user_mangement.User()
        #  print(ba.rootpassword)
        if (isExists_data and isExists_config == True) :
            print("检测到配置文件存在")
            pd = input("是否导入： (Y/N) \n>>>")
            if (pd == "Y"):
                with open(self.path_json_config, 'r') as f:
                      if(f.read() == ""):# 调用系统命令行来创建文件
                          self.user = []
                      else:
                          self.user = function_Student.readdata_json(self.path_json_config)
                with open(self.path_json_data, 'r') as f:
                      if(f.read() == ""):# 调用系统命令行来创建文件
                          self.Student_info = []
                      else:
                          self.Student_info = function_Student.readdata_json(self.path_json_data)
                function_Student.progress_bar(0.005)
                print("配置文件导入完成")
                self.loginUI(self.Student_info)
            elif (pd == "N"):
                print("欢迎使用系统管理\n    管理员\n用户名：admin\n密码：  admin\n\n    本内容仅在重置后出现")
                Student_info_empty = []
                self.loginUI(Student_info_empty)
            else:
                print("没有这个操作")
        elif (isExists_data and isExists_config == False):
            if not os.path.exists(self.path_json_config):
                with open(self.path_json_config, 'w') as f:
                      f.write("")# 调用系统命令行来创建文件
            if not os.path.exists(self.path_json_data):
                with open(self.path_json_data, 'w') as f:
                      f.write("")# 调用系统命令行来创建文件
            Student_info_empty = []
            print("欢迎使用系统管理\n    管理员\n用户名：admin\n密码：admin\n\n    本内容仅在重置后出现")
            self.loginUI(Student_info_empty)

        else:
            if not os.path.exists(self.path_json_config):
                    with open(self.path_json_config, 'w') as f:
                        f.write("")  # 调用系统命令行来创建文件
            if not os.path.exists(self.path_json_data):
                with open(self.path_json_data, 'w') as f:
                    f.write("")  # 调用系统命令行来创建文件
            Student_info_empty = []
            print("欢迎使用系统管理\n    管理员\n用户名：admin\n密码：admin\n\n    本内容仅在重置后出现")
            self.loginUI(Student_info_empty)


    def login(self):  # 登录函数
        isExists_config = function_Student.pathconfrim(self.path_json_config)
        isExists_data = function_Student.pathconfrim(self.path_json_data)
        function_Student.progress_bar(0.01)
        self.confrim(isExists_config, isExists_data)







# while True:
#     ba.rootfunc()



