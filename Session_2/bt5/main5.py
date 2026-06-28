# PHẦN 1: BẢNG THIẾT KẾ ROUTING (8 ENDPOINTS)MethodEndpointMục đíchGET/productsLấy danh sách tất cả sản phẩmGET/products/detailXem chi tiết thông tin sản phẩmPOST/productsThêm sản phẩm mới vào khoPUT/products/updateCập nhật thông tin sản phẩmDELETE/products/deleteXóa một sản phẩm khỏi hệ thốngGET/products/statsXem thống kê tổng quan (số lượng, giá trị kho)GET/products/on-sale(Mở rộng) Lấy danh sách sản phẩm đang giảm giáGET/products/top-rated(Mở rộng) Lấy danh sách sản phẩm được đánh giá cao nhất

from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_all_products():
    return {"message": "Danh sách tất cả sản phẩm"}

@app.get("/products/detail")
def get_product_detail():
    return {"message": "Thông tin chi tiết của sản phẩm"}

@app.post("/products")
def create_product():
    return {"message": "Sản phẩm mới đã được thêm thành công"}

@app.put("/products/update")
def update_product():
    return {"message": "Thông tin sản phẩm đã được cập nhật"}

@app.delete("/products/delete")
def delete_product():
    return {"message": "Sản phẩm đã bị xóa khỏi hệ thống"}

@app.get("/products/stats")
def get_product_stats():
    return {"message": "Thống kê kho hàng: 100 sản phẩm, tổng giá trị 500 triệu"}

@app.get("/products/on-sale")
def get_sale_products():
    return {"message": "Danh sách sản phẩm đang khuyến mãi giảm giá"}

@app.get("/products/top-rated")
def get_top_rated_products():
    return {"message": "Danh sách các sản phẩm được khách hàng đánh giá 5 sao"}