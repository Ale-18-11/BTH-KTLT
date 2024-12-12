print("Sinh vien: Le Thai An")
print("MSSV: 235752021610024")
print("##################################################################################")
###########################################################################################

#[1]
#n1=int(input("enter n1 value"))
#n2=int(input("enter n2 value"))
#if n1>n2:
#    print("n1 is big")
#else:
#    print("n2 is big")


#[2]
#import math;
#x1=int(input("Enter x1--->"))
#y1=int(input("Enter y1--->"))
#
#x2=int(input("Enter x2--->"))
#y2=int(input("Enter y2--->"))
#
#d1=(x2-x1)*(x2-x1) ;
#d2=(y2-y1)*(y2-y1) ;
#res = math.sqrt(d1+d2)
#print ("Distance between two points:",res);


#[3]
#n = int(input("Enter a number---->"))
#if n % 2 == 0:
#    print ("EVEN Number");
#else:
#    print ("ODD Number");


#[4]
#i=1;
#for j in range (2,10):
#    print("i:",i,"j:",j)
#    print(i,"/",j)
#    print (i/j);


#[5]
#n = int(input("Enter A Number--->"));
#while n >=0:
#    print (n);
#    n=n-1;


#[6]
#j =[]
#for i in range (2000, 3201):
#    if ( i%7==0) and (i%5!=0) :
#        j.append(str(i))
#    print (','.join(j))


#[7]
#n = int(input("Nhập vào một số:"))
#d=dict()
#for i in range (1, n + 1):
#        d[i] =i*i
#
#print (d)


#[8]
#a, b = 1, 2
#total = 0
#print(a,end="")
#while (a <= 4000000 - 1 ):
#    if a%2==0:
#        total += a
#    a, b = b, a+b
#    print(a,end="")
#print("\n sum of prime numbers term in fibonacci series: ",total)


#[9]
#str=input ("Enter a String:")
#dict = {}
#for n in str:
#    keys = dict.keys()
#    if n in keys:
#        dict[n] += 1
#    else:
#        dict [n] = 1
#print (dict)


#[10]
#a = "hi i am python programmer"
#b = a.split()
#print (b)
#c = " ".join(b)
#print (c)


#[11]
#l =[1 , 'python',4,7]
#k = ['cse', 2, 'guntur',8]
#m =[]
#m.append(l);
#m.append(k);
#print (m)
#d={1:1,2:k, 'combine list':m}
#print (d)


#[12]
#import re
#value = []
#items=[x for x in input("Nhập mật khẩu: ").split(',')]
#for p in items:
#    if len(p)<6 or len(p)>12:
#        continue
#    else:
#        pass
#    if not re.search("[a-z]",p):
#        continue
#    elif not re.search("[0-9]",p):
#        continue
#    elif not re.search("[A-Z]",p):
#        continue
#    elif not re.search("[$#@]",p):
#        continue
#    elif re.search("\s",p):
#        continue
#    else:
#        pass
#    value.append(p)
#print


#[13]
import math
a = float(input("Nhập hệ số a: "))
while True:
    if a == 0:
        a = float(input("Số a phải khác 0. Nhập lại số a: "))
    else:
        break
b = float(input("Nhập hệ số b: "))
while True:
    if b == 0:
        b = float(input("Số b phải khác 0. Nhập lại số b: "))
    else:
        break
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4*a*c;
if delta > 0:
    x1 = (-(b) + math.sqrt(delta))/(2*a);
    x2 = (-(b) - math.sqrt(delta))/(2*a);
    print("Phương trình có 2 nghiệm phân biệt: ", x1, x2)
elif delta == 0:
    x = (-b)/(2*a);
    print("Phương trình có nghiệm kép: ", x)
elif delta < 0:
    print("Phương trình vô nghiệm")
