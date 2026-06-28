# PHẦN 1: PHÂN TÍCH LỖI
# Endpoint hiện tại: /student (tên đơn, số ít).

# Vì sao gọi /students bị lỗi 404? FastAPI là một hệ thống "định hướng chính xác". Khi bạn khai báo @app.get("/student") nhưng lại gọi /students (thêm chữ 's'), hệ thống không tìm thấy route nào khớp hoàn toàn nên báo 404 Not Found.

# Vì sao tên /student không phù hợp? Trong quy chuẩn RESTful, endpoint trả về danh sách phải là danh từ số nhiều (/students). Tên /student (số ít) thường dành cho việc thao tác với một sinh viên cụ thể (thường đi kèm với ID).

# Vì sao return students[0] sai? Yêu cầu nghiệp vụ là trả về toàn bộ danh sách, nhưng lệnh này chỉ lấy ra phần tử đầu tiên (index 0).

# Đường dẫn đúng: Theo yêu cầu khách hàng, đường dẫn phải là /students.

from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"},
]

@app.get("/students")
def get_all_students():
    return students