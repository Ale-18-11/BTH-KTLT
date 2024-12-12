# main.py
from search_module import binary_search
print("Le Thai An")
print("Msv:235752021610024")
# Nhập số phần tử của danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị cho danh sách
lst = []
for i in range(n):
    value = int(input(f"Nhập giá trị cho phần tử thứ {i+1}: "))
    lst.append(value)

# Sắp xếp danh sách
lst.sort()
print("Danh sách đã sắp xếp:", lst)

# Nhập phần tử cần tìm
value = int(input("Nhập giá trị cần tìm: "))

# Tìm kiếm phần tử bằng hàm binary_search
found = binary_search(lst, value)

# In kết quả
if found:
    print(f"Phần tử {value} có trong danh sách.")
else:
    print(f"Phần tử {value} không có trong danh sách.")
