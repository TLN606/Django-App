# FoodNow

Web đặt đồ ăn trực tuyến — đồ án môn **Công nghệ Lập trình Hiện đại**.

Django 6 + Django REST Framework + PostgreSQL, giao diện bằng Django template.

## Yêu cầu
- Python 3.12
- PostgreSQL 15+ (cài local, dùng pgAdmin để quản lý)

## Cài đặt lần đầu
```bash
git clone https://github.com/TLN606/Django-App.git
cd Django-App
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
cp .env.example .env            # rồi sửa SECRET_KEY và DATABASE_URL
```

Tạo database (một lần): trong pgAdmin, chuột phải **Databases → Create → Database…**, đặt tên `django_app`.
Hoặc dùng lệnh: `psql -U postgres -c "CREATE DATABASE django_app;"`

Trong `.env`, điền mật khẩu user `postgres` (mật khẩu bạn đặt lúc cài PostgreSQL) vào `DATABASE_URL`.

Chạy:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Biến môi trường (`.env`, KHÔNG commit)
| Biến | Ý nghĩa |
|---|---|
| `SECRET_KEY` | Khóa bí mật của Django (ký session, token). Mỗi môi trường một khóa riêng. |
| `DEBUG` | `True` khi dev, `False` khi deploy. |
| `ALLOWED_HOSTS` | Danh sách host, cách nhau bằng dấu phẩy. |
| `DATABASE_URL` | `postgres://USER:PASSWORD@HOST:PORT/DBNAME` |

Tạo SECRET_KEY mới:
```bash
python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
```

## Cấu trúc
- `config/` — settings, urls của project
- `core/` — app chính (thêm app mới: `python manage.py startapp <tên>` rồi khai báo trong `INSTALLED_APPS`)

## Workflow nhóm
Nhánh:
- `main`: bản ổn định, dùng để nộp bài. Chỉ nhận merge từ `develop`.
- `develop`: nhánh tích hợp, mọi tính năng merge vào đây.
- `feature/<tên>` / `fix/<tên>`: nhánh làm việc, tạo từ `develop`.

Quy trình:
1. `git checkout develop && git pull`, rồi `git checkout -b feature/<tên-ngắn>`.
2. Commit nhỏ, rõ nghĩa. Có thay đổi model thì commit kèm file migration.
3. Push nhánh, mở Pull Request **vào `develop`** (mẫu PR có sẵn), nhờ ít nhất 1 bạn review.
4. CI (`.github/workflows/ci.yml`) tự chạy `check`, kiểm tra thiếu migration và `test` trên PostgreSQL thật. CI đỏ thì chưa merge.
5. Merge xong thì xóa nhánh cũ. Khi `develop` ổn định, mở PR `develop` → `main`.
6. Thêm thư viện: `pip install <gói>` rồi `pip freeze > requirements.txt` và commit.
7. Trước khi mở PR chạy local: `python manage.py test`.
