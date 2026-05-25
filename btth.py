raw_data = "   nGuyen vaN aN  ;  2004   "

while True:
    print("===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")

    choice = int(input("Nhập lựa chọn của bạn (1-4): "))

    match choice:
        case 1:
            print(f"Chuỗi dữ liệu gốc hiện tại: {raw_data}")

        case 2:
            info = raw_data.split(";")
            full_name = info[0].strip().title()
            birth_year = int(info[1].strip())
            age = 2026 - birth_year

            print("[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]")
            print(f"- Họ và tên: {full_name}")
            print(f"- Tuổi hiện tại: {age} tuổi")

        case 3:
            info = raw_data.split(";")
            full_name = info[0].strip().title()
            birth_year = info[1].strip()
            name_part = full_name.split()

            first_name = name_part[0]
            middle_name = name_part[1]
            last_name = name_part[-1]

            email = (first_name[0] + middle_name[0] + last_name).lower() + "@company.com"
            member_id = last_name.upper() + birth_year[-2:]

            print("==============================")
            print("      THẺ THÀNH VIÊN MỚI")
            print("==============================")
            print(f"Họ và tên: {full_name}")
            print(f"Mã ID: {member_id}")
            print(f"Email: {email}")
            print("==============================")

        case 4:
            print("Chương trình đã dừng!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")