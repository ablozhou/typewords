import random
s = "abcdefghijklmnopqrstuvwxyz"#ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
count=0

while True:
    length = random.randint(1,4)
   # print("生成字符串长度为%d"%length)
    s1=""
    for i in range(0,length):
        s1 +=s[random.randint(0,len(s)-1)]
    s1+="\n"    
    ans = input(s1)
    
    if ans == "over":
        print("game over!!!")
        break
    
    if ans == s1[:-1]:
        count+=length
        print("wonderful %d\n"%count)
    else:
        count -=length
        print("do better %d\n"%count)
        if count <0 :
            print("您已没分game over!!!")
            break