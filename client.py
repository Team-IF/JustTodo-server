import json
import os

import requests

link = "http://localhost:5000/"
username = "str"


def main():
    os.system("cls")
    print("1. 메모 확인하기")
    print("2. 메모 작성하기")
    print("3. 메모 수정하기")
    print("4. 클라이언트 종료")
    print()
    sel = input("번호를 입력해 주세요: ")
    return sel


# 메모 dict가 들어있는 list로 반환
def getmemo():
    os.system("cls")
    req = json.loads(requests.get(link).text)
    for i in req:
        if i.get("private") == 1 and i.get("author") != username: req.remove(i)
    return req


def postmemo():
    os.system("cls")
    pass


def editmemo():
    os.system("cls")
    pass


while True:
    os.system("pause>nul")
    sel = main()
    if sel == "1":
        for i in getmemo():
            print(i)
    elif sel == "2":
        postmemo()
    elif sel == "3":
        editmemo()
    elif sel == "4":
        exit()
