import math   # 수학 관련 모듈

print(math.pi) # 3.14~~~~~~~~

print(math.ceil(1.1)) # 올림


import random   #난수 관련 모듈


#정수로 난수 하나 발생
print(random.randint(1,10)) #난수 발생 1~10

#정수로 특정 범위내에 난수 발생
print(random.randrange(10)) # 0생략 0~10미만
print(random.randrange(1,10)) # 1~10미만
print(random.randrange(1,10,2))#1부터 10미만 2씩증가

# random() 0이상 1미만에서의 임의의 실수로 난수 발생 %난수 표현

print(random.random())

# choice() 요소들중 하나를 랜덤 선택

season = ['spring','summer','fall','winter']

print(random.choice(season))

