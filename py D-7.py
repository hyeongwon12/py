# import numpy as np
# import pandas as pd
# pot = []
# for i in range(45):
#     pot.append(i+1)
# print(pot)

# pot = list(range(1,46))
# print(pot)

# 리스트 축약
# pot = [n for n in range(1,46)]
# jackpot = []
# import random
# import time

# for n in range (1,7):
#  random.shuffle(pot)
#  num= pot.pop()
#  print(num)
#  jackpot.append(num)
#  time.sleep(2) #2초간 멈춤
# jackpot.sort()
# print(f'이번 당첨번호는 {jackpot}입니다.')

# import random
# import time
# import math
# print('updown게임을 시작합니다.')

# start = time.time()
# answer = random.randint(1,100)
# while True:
#  no = int(input('어떤 값일까요?>>>'))
#  if answer == no:
#     print('정답입니다.')
#     break
#  elif no < answer:
#     print('up')
#  else:
#     print('down')

# end = time.time()

# print(f" {math.floor(end - start)}초 안에 출력했습니다.")


# file = open('myfile.txt','wt')
# print('파일이 생성되었습니다')
# file.close()

# with open('myfile2.txt','wt') as file:
#     print('파일이 생성되었습니다')

# file = open('hello.txt','wt')

# file.write('해우')
# file.write('\n')
# file.write('반갑습니다')
# file.write('\n')

# print('파일 생성 끝')
# file.close


# file = open('hello.txt','at')

# file.write('hello.\n')
# file.write('n t m y.\n')
# print('내용추가성공')
# file.close


# student_list=[]

# with open('학생명단.csv','rt') as file:
#     file.readline()
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         student = line.split(',')
#         student_list.append(student)
# print(student_list)

# import pandas as pd

# data = pd.read_csv('customer.csv')
# print(data)

################################################################

# 클래스와 객체 class & object

# def student_info(name, department, professor, phone, address, grade ):
#     print(name)
#     print(department)
#     print(professor)
#     print(phone)
#     print(address)
#     print(grade)
# student_info('emily','computer engineering','james', '010-1234-5678','seoul','A')

# class WaffleMachine:
#     pass


# waffle = WaffleMachine()

# 클래스는 변수와 매서드(함수)로 구성된다.

# class Person:

#     def who_am_i(self, name, age, tel, address):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         self.address = address
        
# boy = Person()
# boy.who_am_i('john', 15, '1234-6789','toronto')
# print(boy.name)
# print(boy.age)
# girl = Person()
# girl.who_am_i('alice', 18,'4321,7654','la')
# print(girl.name)
# print(girl.age)

# class Book:
#     def print_info(self,제목,저자):
#         self.제목 = 제목
#         self.저자 = 저자
# book1 = Book()
# book2 = Book()
# book1.print_info('파이썬','민경태')
# book2.print_info('어린왕자','생텍쥐페리')
# a = []
# a.insert(book1,book2)
# print(a)

# class Watch:

#     def set_time(self):
#         now = input('시간을 입력하세요 >>> ')
#         hms = now.split(':')
#         self.hour = int(hms[0])
#         self.minute = int(hms[1])
#         self.second = int(hms[2])

#     def add_hour(self, hour):
#         if hour <= 0:
#             return
#         self.hour += hour
#         self.hour %= 24

#     def add_minute(self, minute):
#         if minute <= 0:
#             return
#         self.minute += minute
#         self.add_hour(self.minute // 60)
#         self.minute %= 60

#     def add_second(self, second):
#         if second <= 0:
#             return
#         self.second += second
#         self.add_minute(self.second // 60)
#         self.second %= 60

#     def see(self):
#         print('계산된 시간은 {}시 {}분 {}초입니다.'.format(self.hour, self.minute, self.second))


# watch = Watch()
# watch.set_time()
# watch.add_hour(int(input('계산할 시간을 입력하세요 >>> ')))
# watch.add_minute(int(input('계산할 분을 입력하세요 >>> ')))
# watch.add_second(int(input('계산할 초를 입력하세요 >>> ')))
# watch.see()

     