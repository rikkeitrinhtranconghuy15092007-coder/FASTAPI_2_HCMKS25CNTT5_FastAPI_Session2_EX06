# Input: Danh sách students cho sẵn (dạng list of dictionaries).

# Output mong muốn: Một JSON object bao gồm message (chuỗi thông báo) và data (danh sách các sinh viên có status == "active").

# Điều kiện lọc: Sinh viên có thuộc tính status bằng chuỗi "active".

# Các bước xử lý:

# Bước 1: Khai báo endpoint @app.get("/students/active").

# Bước 2: Sử dụng một vòng lặp hoặc list comprehension để lọc danh sách students gốc, lấy ra các phần tử thỏa mãn status == "active".

# Bước 3: Kiểm tra xem danh sách đã lọc có phần tử nào không.

# Bước 4: Trả về kết quả JSON theo đúng cấu trúc {"message": "...", "data": [...]}.

from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Binh", "status": "inactive"},
    {"id": 3, "name": "Cuong", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"}
]

@app.get("/students/active")
def get_active_students():
    active_list = [s for s in students if s["status"] == "active"]
    
    if not active_list:
        return {
            "message": "Không có sinh viên đang học",
            "data": []
        }
    
    return {
        "message": "Danh sách sinh viên đang học",
        "data": active_list
    }