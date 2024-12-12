print("Le Thai An")
print("Msv:235752021610024")
full_name = input("Nhập tên người: ")
parts = full_name.split()
if len(parts) >= 2:
    ho = parts[0]  # Phần họ
    ten_rieng = parts[-1]  # Tên riêng
    print(f"Họ: {ho}")
    print(f"Tên riêng: {ten_rieng}")
