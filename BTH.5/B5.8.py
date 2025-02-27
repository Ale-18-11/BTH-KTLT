from search_module import Sequential_Search

print("Le Thai An")
print("Msv:235752021610024")

# Nhập số phần tử của danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị cho danh sách
dlist = []
for i in range(n):
    value = input(f"Nhập giá trị cho phần tử thứ {i+1}: ")
    dlist.append(value)

# Nhập phần tử cần tìm
item = input("Nhập phần tử cần tìm: ")

# Tìm kiếm phần tử bằng hàm Sequential_Search
index = Sequential_Search(dlist, item)

# In kết quả
if index != -1:
    print(f"Phần tử '{item}' được tìm thấy tại vị trí: {index}")
else:
    print(f"Phần tử '{item}' không có trong danh sách.")

