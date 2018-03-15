#coding=utf-8
import os
import functions
#1.打印提示功能
#os.system('clear')
#主体代码开始

#定义一个默认学生数据列表
while True:
    functions.printMenu()
    userInput =input("Please Enter Command to Continue (Q quit) :")
    errorInfo ="Check you name again,No Found!!!"
    if  userInput=="1":
        functions.addStu()

    #DELETE
    elif userInput == "2":
        functions.deleteStu()

    #Change
    elif    userInput=="3":
           functions.changeStu()
    #search
    elif    userInput=="4":
           functions.searchStu()
    #advanced all lists
    elif    userInput=="ls":
           functions.ls_Stu_Info()
    #Quit
    elif    userInput=="q":
            exit()
    elif    userInput=="cls":
        os.system('clear')

    else:
        print("Error Command!!!")
