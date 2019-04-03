import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import numpy as np

height = np.array([170,180,160,185,167])
weight = np.array([80,100,65,105,73])
# 몸무게와 키의 도표
# plt.plot(weight,height,"ro")
# plt.xlim(0,110)
# plt.ylim(100,200)
# plt.show()
# x 의 범위가 -10에서 10일때 x의 제곱값을 챠트로 그려 주세요plt.xlim(-10,10)
# x = np.arange(-10,10)
# plt.plot(x,x **2,"x")
# plt.xlim(-10,10)
# plt.show()

t1 = np.arange(0,5,0.1)    #0부터 5까지 스탭이 0.1씩
t2 = np.arange(0,5,0.02)   #0부터 5까지 스탭이 0.02씩
# print(t1)
# print(t2)
# plt.figure(1)
# plt.plot(t1,"ro")
#
# plt.figure(2)
# plt.plot(t2,"x")
# plt.show()

# plt.subplot(211)          #2행 1열로 도화지를 나누어 1번째에
# plt.plot(t1)
# plt.subplot(212)          #2행 1열로 나눈 도화지에 2번째에
# plt.plot(t2,"k")
# plt.show()

# print(   np.exp(2)   )      #지수 함수
# print(   np.log(2)   )      #로그 함수

#0.01에서 0.01씩 증가 하여 2까지의 수들에 대한 지수값과 로그값을 하나의 화면에 챠트로 그려보세요.
#2개를 ㅣ챠트를 가로로 나타내 봅니다.
# t1 = np.arange(0.01,2,0.01)
# t2 = np.exp(t1)
# print(t2)
# t3 = np.log(t1)
# print(t3)
# plt.subplot(121)
# plt.plot(t2,"bx")
#
# plt.subplot(122)
# plt.plot(t3,"ko")
# plt.show()
path = "C:\Windows\Fonts\malgun.ttf"
#fontprop = font_manager.FontProperties(fname=path, size=18)
fontprop = font_manager.FontProperties(fname=path).get_name()
rc('font',family=fontprop)
qty = [10,20,10,30,50]
plt.bar(range(5),qty,0.4)
plt.title("요일별 과일 판매량", fontproperties=fontprop)
plt.show()