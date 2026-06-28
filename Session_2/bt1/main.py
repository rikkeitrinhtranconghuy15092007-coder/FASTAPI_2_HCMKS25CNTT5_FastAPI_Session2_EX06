   #Phân tích lỗi 
   # 1 Trace  luồng xuwrt lý khi người dùng mở cái http lên hàm set students() được kích hoạt và trả về một chuỗi string danh sách sinh viên 
#   Tại sao không nên trả về String? API JSON phải trả về đúng định dạng cấu trúc dữ liệu (Object hoặc Array). Khi trả về một chuỗi, Frontend không thể dùng hàm .map() hay các vòng lặp để hiển thị từng sinh viên mà phải dùng kỹ thuật cắt chuỗi (parsing) rất thủ công và dễ vỡ. FastAPI mặc định là Framework cho API, nó sinh ra để tự động chuyển list, dict của Python thành JSON chuẩn chỉnh.

# Lỗi về REST Endpoint Naming Convention:

# Tên endpoint /getStudents sử dụng động từ (get), điều này vi phạm chuẩn RESTful.

# Trong REST, endpoint nên là danh từ số nhiều chỉ tài nguyên, còn phương thức HTTP (GET, POST,...) mới là thứ quyết định hành động.

from fastapi import FastAPI

app = FastAPI()

students = ["An", "Binh", "Cuong"]

@app.get("/students")
def get_students():
    return students