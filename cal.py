class Calc:
    def add(self,a,b):
        return a + b

    def subs(self,a,b):
        return a - b

    def mult(self,a,b):
        return a * b

    def divi(self,a,b):
        return a / b











'''
a = 1
b = 2

sum = 4

c = Calc()
s = c.add(a,b)

if s == sum:
    print(a,",",b,"用例通过！")
else:
    # 把错误信息写到日志文件中
    f = open("a.log","w+",encoding="utf-8")
    f.write(str(a)+"," + str(b) + "执行add方法时用例不通过！")
'''