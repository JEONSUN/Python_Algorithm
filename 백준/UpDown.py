#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


        
def solution() :
    result = random.randint(1,100)
    d_list = []
    
    while 1 :
        try :
            print("-" * 50)

            x = int(input("숫자를 입력하시오 : "))
            print(f'입력 값 : {x}')
            if x < 100 :
                if result > x :
                    print("Up")
        
                elif result < x : 
                    print("Down")
            
                elif result == x :
                    print(f"정답입니다 : {result}")
                    break
            
        
            else :
                print("범위를 벗어났습니다.")
            
            if x in d_list :
                print("이미 눌렀습니다.")
            else :
                d_list.append(x)
            
        except ValueError:
            print("어허 다시입력하세요")


        
        