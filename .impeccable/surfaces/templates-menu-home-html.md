---
version: 1
slug: "templates-menu-home-html"
primary_target: "templates/menu/home.html"
related_targets: ["templates/base.html"]
---

# Surface brief: trang chủ và thực đơn FoodNow

Mode: Persuade (trang chủ, thực đơn). Giỏ hàng, đơn hàng và hồ sơ kế thừa cùng thế giới nhưng làm theo Operate.

Audience và việc cần làm: sinh viên, dân văn phòng đặt bữa trưa trên điện thoại. Việc: chọn món, thấy giá, bỏ vào giỏ trong vài lần chạm.

Chứng cứ có sẵn: 13 món mẫu với tên và giá, 4 danh mục. Không có ảnh món, không có đánh giá, địa chỉ hay giờ mở cửa; không được bịa.

Ràng buộc: Django template, CSS riêng, không Bootstrap, font tự host, tiếng Việt, tiền đồng. Còn phải tuân thủ luật nhà của skill design-taste-frontend: không eyebrow, không monospace, không viền mảnh, không gradient, không đổ bóng, không thẻ icon.

Chưa quyết: ảnh món thật (nhóm tự chụp sau); logo.

## Direction contract

THESIS: Thực đơn là chồng tô sứ men trắng vẽ chàm: mỗi danh mục là một chiếc tô vẽ chàm, các món là hàng chữ lớn với giá viết cạnh bên. Từ chối lưới thẻ ảnh món kèm nút cam của mọi web đặt đồ ăn.

OWN-WORLD: nền sứ trắng ngả lạnh #F4F6F8, mảng chàm đặc #1C3C8C phủ cả vùng lớn, mực chàm tối #0F1F4D cho chữ, đỏ ớt #D0102A (đổi từ #D9381E vì bộ dò màu của luật nhà coi #D9381E là nâu cam; #D0102A vẫn đạt tương phản 5.5:1 với chữ trắng) chỉ dành cho giá và hành động chính. Hình món ăn là tô tròn vẽ bằng SVG nét chàm phẳng, không bóng. Chữ tiêu đề Bricolage Grotesque đậm, thân chữ Be Vietnam Pro, cả hai tự host. Nút bo tròn hoàn toàn như miệng tô. Không viền mảnh, không đổ bóng, không gradient.

STORY: Khách hiểu trong vài giây đây là quán cơm trưa có giá rõ ràng, thấy món, tin giá niêm yết, bấm Thêm và đặt đơn mà không cần hướng dẫn.

FIRST VIEWPORT: Bảy phần mười bề rộng là mảng chàm đặc; trong đó tiêu đề h1 cỡ lớn "Đặt bữa trưa trong một phút" (rút gọn từ "Bữa trưa nóng, đặt trong một phút" để vừa hai dòng), một câu bổ nghĩa ngay dưới và nút tròn đỏ ớt "Xem thực đơn". Ba phần mười còn lại là một chiếc tô vẽ chàm khổng lồ cắt tràn mép phải. Trên điện thoại mảng chàm xếp trên, tô xếp dưới, nút vẫn nằm trong màn hình đầu.

FORM: Tô sứ hoa lam, vị trí 4 trong danh sách hướng của mình, seed:e28dba446f9c4c72.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
