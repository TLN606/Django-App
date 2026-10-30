# Ghi chú tiến độ — FoodNow

Cập nhật lần cuối: 2026-10-30. Deadline: **2026-11-02**.

## Đã xong
- Dựng project Django 6 (`config/`) và app `core`, môi trường ảo `.venv`.
- Chuyển cấu hình sang `.env` (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL`) bằng `django-environ`; có `.env.example`.
- Kết nối PostgreSQL 18 trên máy; `migrate` và `test` chạy qua (1 test).
- Cài `djangorestframework` và `psycopg`, `requirements.txt` đã cập nhật.
- `README.md`: cài đặt, biến môi trường, quy trình nhóm (`feature/*` → `develop` → `main`).
- CI GitHub Actions (`.github/workflows/ci.yml`) chạy `check`, kiểm tra migration, `test` trên PostgreSQL. Xanh trên `main` và `develop`.
- Push commit đầu lên GitHub; tạo nhánh `develop`, đặt làm nhánh mặc định.
- Rule bảo vệ `main` và `develop`: bắt buộc PR, 1 người duyệt, check `test` xanh, cấm force push và xóa nhánh.
- Mẫu Pull Request, mẫu issue (Tính năng, Lỗi), nhãn `feature`/`bug`/`docs`/`urgent`.
- 10 issue chia việc (#1–#10); #1, #2, #10 đã gán cho TLN606.
- Gửi lời mời collaborator (quyền write) cho `nguyenlehaitrieu` và `QuangDuy0904`.

- Khung 3 app `accounts`, `menu`, `orders` (PR `feature/scaffold`): model `Category`/`Dish`/`Review`/`Order`/`OrderItem`, admin, `base.html` Bootstrap, trang chủ liệt kê món, cấu hình `MEDIA`, ngôn ngữ `vi`.
- Quyết định deploy: Render.

## Chưa xong
- Hai bạn chưa nhận lời mời, nên chưa gán được #3–#8 (dự kiến: `menu` → nguyenlehaitrieu, `orders` → QuangDuy0904).
- Dựng khung 3 app `accounts`, `menu`, `orders` (model, URL, `base.html` Bootstrap, trang chủ).
- Thêm 3 app vào `INSTALLED_APPS`; cấu hình `MEDIA_ROOT`/`MEDIA_URL` cho ảnh món ăn.
- Tính năng vòng 1: tài khoản, danh sách và chi tiết món, giỏ hàng, đặt hàng, lịch sử đơn.
- Tính năng vòng 2: tìm kiếm/lọc, đánh giá, thanh toán giả lập, deploy (Render).
- Test cho các luồng chính, dữ liệu mẫu, ảnh chụp màn hình trong README.
- CD / deploy: chưa có, chờ nhóm chọn nơi deploy.
- Chưa thử mở PR thật để kiểm tra rule bảo vệ nhánh chặn đúng.

## Đang vướng
**1. Hai bạn chưa nhận lời mời collaborator**
- Đã thử: gửi lời mời qua `gh api` (thành công, trạng thái pending).
- Chưa được: GitHub chỉ cho gán issue cho người đã nhận lời mời.
- Việc cần: hai bạn mở https://github.com/TLN606/Django-App/invitations và bấm Accept.

**2. Lệnh `gh` không chạy trong terminal bash của phiên**
- Đã thử: `gh auth login` → `gh: command not found`; gõ nhầm `git auth login` → `'auth' is not a git command`.
- Đã xử lý: gọi bằng đường dẫn đầy đủ `"/c/Program Files/GitHub CLI/gh.exe"` hoặc làm trong PowerShell sau khi nạp lại PATH.
- Còn lại: terminal mới (mở lại sau khi cài) sẽ nhận `gh` bình thường.

**3. Tạo ruleset bảo vệ nhánh bị lỗi `Problems parsing JSON` (HTTP 400)**
- Đã thử: truyền JSON bằng here-string qua pipe trong PowerShell 5.1 → lỗi (thêm ký tự BOM).
- Đã xử lý: ghi JSON ra file rồi dùng `gh api --input <file>` → thành công.

**4. Mời collaborator lần đầu không gửi được**
- Đã thử: dùng chuỗi `jq` có ký tự `->` trong PowerShell → bị tách thành cờ lệnh, lệnh lỗi.
- Đã xử lý: chạy lại với `--silent` và truy vấn `invitations` riêng → thành công.

**5. Đã gặp lỗi mật khẩu PostgreSQL (đã giải quyết)**
- Đã thử: `psql` không mật khẩu → `no password supplied`; `migrate` với mật khẩu mẫu → `password authentication failed`.
- Đã xử lý: sửa `DATABASE_URL` trong `.env` bằng mật khẩu thật.

**6. Email cá nhân đã nằm trong commit đầu tiên (repo public)**
- Chưa xử lý: viết lại lịch sử để gỡ là rủi ro, nên giữ nguyên.
- Nếu muốn che ở các commit sau: đặt `git config --global user.email` thành email noreply của GitHub.

**7. Rule yêu cầu 1 người duyệt nhưng nhóm mới có 1 người hoạt động**
- Tạm thời: admin được bypass khi merge PR, vẫn phải qua PR và CI xanh.
