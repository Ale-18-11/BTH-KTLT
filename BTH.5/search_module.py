def binary_search(lst, value):
    """
    Hàm tìm kiếm nhị phân trong danh sách đã sắp xếp.

    Args:
        lst (list): Danh sách đã sắp xếp.
        value: Phần tử cần tìm kiếm.

    Returns:
        bool: True nếu tìm thấy, False nếu không tìm thấy.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2  # Tìm chỉ số giữa
        if lst[mid] == value:
            return True  # Tìm thấy phần tử
        elif lst[mid] < value:
            left = mid + 1  # Tìm ở nửa phải
        else:
            right = mid - 1  # Tìm ở nửa trái

    return False  # Không tìm thấy
