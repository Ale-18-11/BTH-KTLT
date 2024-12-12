print("Le Thai An")
print("Msv:235752021610024")
# Nhập chuỗi các số nhị phân
chuoi_nhi_phan = input("Nhập chuỗi các số nhị phân cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số nhị phân
danh_sach_nhi_phan = chuoi_nhi_phan.split(',')

# In ra các số nhị phân đã nhập
for nhi_phan in danh_sach_nhi_phan:
    print(nhi_phan)
