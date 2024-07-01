#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 로또 번호 생성기
import time
t = input('타이머 입력:')
for i in range(int(t)) :
    print(i)
    time.sleep(1)



import random

lotto = []
num = []
nums = range(1,46)

for i in range(5) :
    lotto = random.sample(nums, 6)
    lotto.sort()
    list = str(lotto)
    print(i+1,'번째줄 : ', list[1:-1]) # 괄호 제거
    
    lotto = [] #초기화

p = input('0이면 종료')
while p == 0 :
    break


# In[ ]:




