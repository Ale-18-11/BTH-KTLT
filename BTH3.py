print("Sinh vien: Le Thai An")
print("MSSV: 235752021610024")
print("####################################################################")
#############################################################################

#[1]
#def sum(a,b):
#    print("sum = "+str(a+b))
# tinh tong 2 so 4,5
#sum(4,5)
# tinh tong 2 so 3,7
#sum(3,7)


#[2]
#def sum(a, b):
#    return a+ b
#c = sum(4, 5);
#print("Tong cua 4 va 5 = " + str(c))


#[3]
#a = "Hello"
#def say_hello(a):
#    print(a)
#print(a)


#[4]
#a = "Hello Guy!"
#def say(a):
#    a = "Vinh University"
#    print(a)
#say(a)
#print(a)


#[5]
#a = "Hello Guy!"
#def say():
#    global a
#    a = " Vinh University "
#    print(a)
#say()
#print(a)


#[6]
#def get_sum(*num):
#    tmp = 0
#    # duyet cac tham so
#    for i in num:
#        tmp += i
#    return tmp
#result = get_sum(1, 2, 3, 4, 5)
#print(result)


#[7]
#def checkValue(n):
#    if n%2 == 0:
#        print ("Đây là một số chẵn")
#    else:
#        print ("Đây là một số lẻ")
#checkValue(7)


#[8]
#import math
#pos = [0,0] # Tọa độ x, y
#while True:
#    s = input()
#    if not s:
#        break
#    movement = s.split(" ") # split: tách chuỗi
#    direction = movement[0] # movement[0]: lấy phần tử đầu tiên
#    steps = int(movement[1]) # movement[1]: lấy phần tử thứ 2
#    if direction == "UP":
#        pos[0] += steps
#    elif direction == "DOWN":
#        pos[0] -= steps
#    elif direction == "LEFT":
#        pos[1] -= steps
#    elif direction == "RIGHT":
#        pos[1] += steps
#    else:
#        pass # Nếu hướng không hợp lệ, lệnh pass sẽ bỏ qua mà không làm gì
#################################
#print(int(round(math.sqrt(pos[1]**2 + pos[0]**2)))) # round(...): Làm tròn kết quả


#[9]
#""" Program make a simple calculator that can add, subtract, multiply and divide using functions"""
# This function adds two numbers
#def add(x, y):
#    return x + y
# This function subtracts two numbers
#def subtract(x, y):
#    return x - y
# This function multiplies two numbers
#def multiply(x, y):
#    return x * y
# This function divides two numbers
#def divide(x, y):
#    return x / y
#print("Select operation.")
#print("1.Add")
#print("2.Subtract")
#print("3.Multiply")
#print("4.Divide")
# Take input from the user
#choice = input("Enter choice((1/2/3/4): ")
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))
#
#if choice =='1':
#    print(num1,"+",num2,"=", add(num1,num2))
#elif choice =='2':
#    print(num1,"-",num2,"=", subtract(num1,num2))
#elif choice =='3':
#    print(num1,"*",num2,"=", multiply(num1, num2))
#elif choice =='4':
#    print(num1,"/",num2,"=", divide(num1,num2))
#else:
#    print("Invalid input")


#[10]
#import math
#def Tinh1(R):
#    return math.pi*2*R
#def Tinh2(R):
#    return math.pi*R**2
#def Tinh(R):
#    ket_qua1 = Tinh1(R)
#    ket_qua2 = Tinh2(R)
#    return ket_qua1 , ket_qua2
#print("Chu vi va dien tich hinh tron lan luot la: ", Tinh(5))


#[11]
import math
def benefit(t,n,k):
    return n*t*k
so_von=int(input("Số vốn ban đầu: "))
lai_suat=float(input("Lãi suất tiết kiệm: "))
so_thang=int(input("Số tháng gửi tiết kiệm: "))

print(so_von,"*",lai_suat,"*",so_thang,"=", benefit(so_von,lai_suat,so_thang))
