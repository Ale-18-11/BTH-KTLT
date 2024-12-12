print("Le Thai An")
print("Msv:235752021610024")
S = input("Nhập chuỗi: ")
for ch in S:
    if ch not in [' ', '\t']:  # Bỏ qua các ký tự không nhìn thấy
        print(ch)
