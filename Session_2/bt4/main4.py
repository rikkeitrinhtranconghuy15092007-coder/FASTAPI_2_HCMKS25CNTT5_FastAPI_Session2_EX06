#  Input: Danh sách books (List các Dictionary) chứa các thông tin id, title, và quantity.Output: Một JSON object bao gồm message (chuỗi thông báo) và data (danh sách các quyển sách thỏa mãn điều kiện).Điều kiện lọc: 0 <= quantity <= 5 (Sách phải có trường quantity và giá trị phải từ 0 đến 5).PHẦN 2: HAI GIẢI PHÁP ĐỀ XUẤTGiải pháp 1 (Vòng lặp for truyền thống): Khởi tạo một danh sách rỗng, duyệt qua từng cuốn sách bằng for, kiểm tra điều kiện (sử dụng if lồng nhau hoặc try-except để kiểm tra sự tồn tại của trường quantity), sau đó append vào danh sách kết quả.Giải pháp 2 (List Comprehension): Sử dụng cấu trúc lọc dữ liệu một dòng, kết hợp với các toán tử điều kiện để loại bỏ dữ liệu lỗi ngay trong quá trình duyệt.PHẦN 3: SO SÁNH VÀ LỰA CHỌNTiêu chíVòng lặp forList comprehensionĐộ dễ hiểuRất cao (rõ ràng từng bước)Trung bình (cần quen cú pháp)Độ ngắn gọnDàiRất ngắn gọnDễ xử lý bẫyDễ quản lý logic phức tạpHơi khó nếu logic lọc quá nhiều tầngDễ bảo trìCaoCao nếu viết vừa phảiLựa chọn: Tôi chọn Giải pháp 1 (Vòng lặp for).Lý do: Vì bài toán yêu cầu xử lý nhiều "bẫy" dữ liệu (thiếu trường, giá trị âm), vòng lặp for cho phép kiểm tra từng điều kiện một cách tường minh, giúp code dễ đọc và dễ bảo trì hơn đối với các lập trình viên khác khi nhìn vào phần logic xử lý lỗi.PHẦN 4: THIẾT KẾ CÁC BƯỚC XỬ LÝKhởi tạo FastAPI và danh sách books.Định nghĩa route GET /books/low-stock.Khởi tạo result_list = [].Duyệt qua từng cuốn sách trong books.Kiểm tra: Nếu quantity thiếu hoặc < 0 thì continue (bỏ qua).Nếu quantity <= 5 thì thêm vào result_list.Kiểm tra result_list: nếu rỗng thì trả về thông báo không có dữ liệu, ngược lại trả về kết quả.
from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "Python Basic", "quantity": 12},
    {"id": 2, "title": "FastAPI Beginner", "quantity": 3},
    {"id": 3, "title": "Clean Code", "quantity": 5},
    {"id": 4, "title": "Database Design", "quantity": 0},
    {"id": 5, "title": "Web API Design", "quantity": 20},
    {"id": 6, "title": "Java Basic"},
    {"id": 7, "title": "Spring Boot", "quantity": -2} 
]

@app.get("/books/12")
def get_low_stock_books():
    low_stock_list = []
    
    for book in books:
        qty = book.get("quantity")
        
        if qty is None or qty < 0:
            continue
            
        if qty <= 5:
            low_stock_list.append(book)
    
    if not low_stock_list:
        return {
            "message": "Không có sách nào sắp hết hàng",
            "data": []
        }
    
    return {
        "message": "Danh sách sách sắp hết hàng",
        "data": low_stock_list
    }