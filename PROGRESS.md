# Ghi chú tiến độ — FoodNow

Cập nhật lần cuối: 2026-10-31. Deadline: **2026-11-02**.

## Đã xong
**Nền tảng**
- Project Django 6 (`config/`), cấu hình qua `.env` (`django-environ`), kết nối PostgreSQL 18; `.env.example`.
- CI GitHub Actions chạy `check`, kiểm tra migration, `test` trên PostgreSQL. Xanh trên `main`, `develop` và PR #14.
- `develop` là nhánh mặc định; rule bảo vệ `main` và `develop` (bắt buộc PR, 1 người duyệt, CI `test` xanh, cấm force push). Mẫu PR, mẫu issue, nhãn.
- README: cài đặt, biến môi trường, quy trình nhóm. `PRODUCT.md`, `DESIGN.md` (PR #14).

**Tính năng (đã merge vào `develop`)**
- #11 Khung 3 app `accounts`, `menu`, `orders` và model `Category`, `Dish`, `Review`, `Order`, `OrderItem`, đăng ký admin, cấu hình `MEDIA`.
- #12 Đăng ký (tự đăng nhập), đăng nhập, đăng xuất, hồ sơ, navbar theo trạng thái đăng nhập. Đóng issue #1, #2.
- #13 Lệnh `python manage.py seed_menu`: 4 danh mục, 13 món mẫu, chạy lại không trùng.

**Đang chờ merge**
- #14 Giao diện "Tô sứ hoa lam": CSS riêng (bỏ Bootstrap), font tự host, trang chủ + thực đơn theo danh mục, giá dạng `45.000đ`, trang tài khoản theo kiểu mới. CI xanh, test qua 8/8.

**Quyết định**
- Deploy bằng Render. Đa nhà hàng bỏ. Thanh toán chỉ giả lập.

## Chưa xong
- **Giỏ hàng và đặt hàng (#5, #6):** chưa có nút "Thêm" trên món nên khách chưa đặt được. Đây là việc lớn nhất còn thiếu.
- Danh sách/chi tiết món, tìm kiếm và lọc (#4). Model và admin của món (#3) đã có từ #11 nhưng issue còn mở.
- Đánh giá món (#7), thanh toán giả lập (#8), deploy Render (#9).
- Ảnh món ăn thật: nhóm tải qua `/admin/`, ảnh tự hiện. Địa chỉ, giờ mở cửa: đang ghi "sắp cập nhật".
- Test cho luồng giỏ hàng và đặt hàng, ảnh chụp màn hình trong README (#10).
- Hai bạn `nguyenlehaitrieu` và `QuangDuy0904` chưa nhận lời mời (kiểm tra 2026-10-31), nên #3–#8 chưa gán được.
- CD: chưa có, làm cùng #9.

## Đang vướng
**1. Hai bạn chưa nhận lời mời collaborator**
- Đã thử: gửi lời mời qua `gh api` (thành công, đang pending).
- Chưa được: GitHub chỉ cho gán issue cho người đã nhận lời mời.
- Việc cần: hai bạn mở https://github.com/TLN606/Django-App/invitations và bấm Accept.

**2. Rule cần 1 người duyệt nhưng mới có 1 người hoạt động**
- Đã thử: merge bình thường → nút Merge bị chặn ("Review required").
- Tạm thời: admin tích "Merge without waiting for requirements" (bypass); vẫn phải qua PR và CI xanh.

**3. Giá hiện `40000đ` thay vì `40.000đ`**
- Đã thử: filter `intcomma` (cài `django.contrib.humanize`), rồi `floatformat:"0g"` → đều không ngăn cách hàng nghìn, vì locale `vi` của Django không bật nhóm số.
- Đã xử lý: filter tự viết `vnd` trong `menu/templatetags/menu_extras.py`, có test.

**4. Server thử trả lỗi 500 sau khi thêm module mới**
- Nguyên nhân: thêm package `templatetags` mới thì phải khởi động lại `runserver`.
- Đã thử: tắt hết tiến trình Python → bị chặn (quá rộng, có thể ảnh hưởng chương trình khác); chạy server mới ở cổng khác → được.
- Việc cần: mỗi thành viên tắt và chạy lại `python manage.py runserver` sau khi `git pull`.

**5. Bộ kiểm tra giao diện báo "trang đứng yên" và "thiếu ảnh"**
- Đã thử: sửa CSS, chạy lại → vẫn báo. Tìm ra: Windows đang tắt "Show animations" nên trình duyệt báo `prefers-reduced-motion: reduce` và CSS đúng chuẩn đã tắt animation. Khi ép bật lại: 9 chuyển động chạy, 17/17 khối hiện đủ.
- "Thiếu ảnh": chưa có ảnh món thật; không dùng ảnh mạng vì sẽ trình bày sai món của quán.

**6. Đã gặp và đã xử lý (để nhớ)**
- `gh` không nhận trong terminal bash → gọi bằng đường dẫn đầy đủ hoặc PowerShell. Tạo ruleset lỗi `Problems parsing JSON` (BOM của PowerShell 5.1) → ghi JSON ra file rồi `--input`. Lệnh `jq` có `->` bị PowerShell tách cờ → chạy lại với `--silent`.
- Lỗi mật khẩu PostgreSQL → sửa `DATABASE_URL` trong `.env`.
- In tiếng Việt ra terminal bị `UnicodeEncodeError` (bảng mã cp1252) → đặt `PYTHONUTF8=1` (PowerShell: `$env:PYTHONUTF8=1`).

**7. Email cá nhân nằm trong commit đầu tiên (repo public)**
- Chưa xử lý: viết lại lịch sử là rủi ro nên giữ nguyên. Muốn che từ giờ: `git config --global user.email` thành email noreply của GitHub.
