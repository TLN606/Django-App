# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack
Django 6 template (server-rendered HTML), CSS riêng viết tay, bỏ Bootstrap (người dùng xác nhận). Không dùng React hay framework JS. PostgreSQL. Đồ án nhóm 3 người, nộp 2/11/2026.

## Users
Sinh viên và dân văn phòng đặt bữa trưa: thường dùng điện thoại giữa giờ nghỉ, muốn chọn món nhanh, thấy rõ giá và tổng tiền, đặt xong là yên tâm.

## Product Purpose
FoodNow là web đặt đồ ăn trực tuyến cho một quán đồ ăn Việt bình dân (cơm, bún, phở, ăn vặt, đồ uống). Khách xem thực đơn, bỏ món vào giỏ, đặt hàng, theo dõi trạng thái đơn. Thành công là một khách mới đặt xong đơn đầu tiên không cần hướng dẫn.

## Positioning
Một quán, một thực đơn rõ ràng, giá niêm yết sẵn bằng đồng, đặt trong vài lần chạm. Không phải sàn nhiều quán. Chưa có điểm khác biệt nào khác được xác nhận.

## Operating Context
Khách đặt trên điện thoại hoặc máy tính trong giờ nghỉ trưa. Quản lý món và đơn qua Django Admin. Giỏ hàng lưu trong session. Đơn có trạng thái: chờ xử lý, đang làm, đang giao, hoàn tất, đã hủy.

## Capabilities and Constraints
- Có: tài khoản (đăng ký, đăng nhập, đăng xuất, hồ sơ), danh mục, món ăn, đánh giá (model sẵn), giỏ hàng và đơn hàng (model sẵn).
- Chưa quyết định: thanh toán thật (dự kiến chỉ giả lập), deploy (dự kiến Render), tìm kiếm và lọc.
- Một quán duy nhất, không đa nhà hàng.
- Tên thương hiệu giữ là FoodNow.

## Brand Commitments
Tên: FoodNow. Ngôn ngữ giao diện: tiếng Việt, tiền tệ đồng (đ). Chưa có logo, địa chỉ hay câu chuyện thương hiệu nào được xác nhận.

## Evidence on Hand
- 13 món mẫu trong 4 danh mục (Cơm, Bún - Phở, Ăn vặt, Đồ uống), có tên và giá, **chưa có ảnh món**. Dữ liệu tạo bằng `python manage.py seed_menu`.
- Không có ảnh chụp thật, đánh giá khách hàng, địa chỉ quán, giờ mở cửa hay số liệu kinh doanh. Không được bịa các thứ này.

## Product Principles
1. Giá và tổng tiền luôn nhìn thấy trước khi khách bấm đặt.
2. Đặt món phải xong trong vài lần chạm trên điện thoại.
3. Chỉ nói điều có thật: món, giá, trạng thái đơn. Không bịa đánh giá hay con số.
4. Mọi thành viên nhóm sửa được giao diện bằng file CSS và template, không cần công cụ build.
