#coding=utf-8


student = [{'name': 'admin', 'sex': 'man', 'phone': '110'}, {'name': 'user1', 'sex': 'male', 'phone': '119'}, {'name': 'usr', 'sex': 'female', 'phone': '333'}]
def printMenu():
    print("*"*30)
    print("     Stutents System V6.8.1")
    print("1.Add new student")
    print("2.Delect student")
    print("3.change name")
    print("4.search name in student")
    print("Press q to quit")
    print("Note:You need to add info first to test this student_system.py")
    print("*"*30)


#add student Function
def addStu():
    userName = input("Please Enter the name you want to op:")
    newSex = input("Enter your Sex:")
    newPhone = input("Please enter you phone number:")
    info = {}
    info['name'] = userName
    info['sex'] = newSex
    info['phone'] = newPhone
    student.append(info)
def deleteStu():
    stuId = int(input("Plese Enter ID you wanan to DELETE:"))
    if stuId < int(len(student)):
        del student[stuId]
    else:
        print("ID incorrect!")

def changeStu():
    stuId = int(input("Please Enter ID you wanna to change:"))
    if stuId < len(student):
        userName = input("plese enter which name you wana to change:")
        newSex = input("Enter your Sex:")
        newPhone = input("Please enter you phone number:")
        student[stuId - 1]['name'] = userName
        student[stuId - 1]['sex'] = newSex
        student[stuId - 1]['phone'] = newPhone
    else:
        print("Your ID incorrect !")
def searchStu():
    print("You select for search function to find student")
    userName = input("plese enter the name you wana to search:")
    for x in student:
        if userName == x['name']:
            print("Found it! lists are %s" % x['name'])
            print(" Name    Sex    Phone")
            print("%s      %s      %s" % (x['name'], x['sex'], x['phone']))
            break
    if userName != x['name']:
        print("No Record!")
def ls_Stu_Info():
    # print("Student Lists:%s"%student)
    print("No    Name      Sex     Phone ")
    i = 1
    for allist in student:
        print("%d     %s        %s       %s" % (i, allist['name'], allist['sex'], allist['phone']))
        i += 1
