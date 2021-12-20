# 1.1字符串的拼接
str1 = input("请输入一个人的名字：")
str2 = input("请输入一个地点：")
print("世界这么大，{}想去{}看看。".format(str1,str2))
# 1.2整数序列求和
n = input("请输入一个整数N：")
sum = 0
for i in range(int(n)):#或者调和函数eval(n)
   print(i,end = ' ')
   sum = sum + i+1
print("1到N求和结果为：",sum)
# 1.3 9*9乘法表
# 版本一
for i in range(1,10):
   for m in range(1,i+1):
       sum = i*m
       if m < i:
           if sum < 10:
               print(m,'*',i,"= {}".format(sum),end = '  ')
           else:
               print(m,'*',i,'=',sum,end = ' ')
       else:
           print(m,'*',i,'=',sum)
# 版本二
for i in range(1,10):
   for j in range(1,i+1):
       print("{} * {} = {:2}".format(j,i,i*j),end = ' ')
   print('')
# ---------1.4 计算1+2!+3!+4!+...+10!------------#
sum,tmp = 0,1
for i in range(1,11):
   tmp *= i
   sum += tmp
print("1+2!+3!+4!+...+10!=",sum)
# ---------1.5 猴子吃桃问题 ----------------------#
# list(range(5,0,-1)) -----  [5, 4, 3, 2, 1]
n = 1
for i in range(5,0,-1):
   n = (n+1)*2  #n = (n+1)<<1 左移一位乘以2
print(n)
# --------1.6 健康食谱输出 ------------------------#
diet = ['西红柿','土豆','鸡蛋','黄瓜','青菜']
for i in range(5):
   for j in range(5):
       if (i != j):
           print(diet[i],diet[j],sep = '炒')
# --------1.7 绘制五角星 --------------------------#
from turtle import *
##fillcolor("red")
color('red','yellow') #color('线条颜色','填充颜色')
begin_fill()
while True:
   forward(200)
   right(144)
   if abs(pos()) < 1:
       break
end_fill()
# ------1.8 太阳花的绘制 --------------------------#
from turtle import *
color('red','yellow')
begin_fill()
while True:
   forward(200)
   left(170)
   if abs(pos()) <1:
       break
end_fill()
done()