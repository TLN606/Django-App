---
name: FoodNow
description: Quán cơm trưa Việt, thực đơn như chồng tô sứ men trắng vẽ hoa lam.
colors:
  porcelain: "#F4F6F8"
  white: "#FFFFFF"
  mist: "#E4EAF6"
  cobalt: "#1C3C8C"
  ink: "#0F1F4D"
  chili: "#D0102A"
  chili-deep: "#A80D22"
  on-cobalt-soft: "#C9D4F0"
typography:
  display:
    fontFamily: "Bricolage Grotesque, Be Vietnam Pro, system-ui, sans-serif"
    fontSize: "clamp(2.5rem, 7vw, 6rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "Bricolage Grotesque, Be Vietnam Pro, system-ui, sans-serif"
    fontSize: "clamp(2rem, 4.5vw, 3.5rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Be Vietnam Pro, system-ui, sans-serif"
    fontSize: "clamp(1.25rem, 2.4vw, 1.625rem)"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  price:
    fontFamily: "Bricolage Grotesque, Be Vietnam Pro, system-ui, sans-serif"
    fontSize: "clamp(1.5rem, 3vw, 2rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.02em"
  lead:
    fontFamily: "Be Vietnam Pro, system-ui, sans-serif"
    fontSize: "clamp(1.125rem, 1.6vw, 1.375rem)"
    fontWeight: 400
    lineHeight: 1.6
  body:
    fontFamily: "Be Vietnam Pro, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Be Vietnam Pro, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 600
    lineHeight: 1
rounded:
  field: "12px"
  pill: "999px"
  round: "50%"
spacing:
  gutter: "clamp(16px, 4vw, 48px)"
  section-gap: "clamp(72px, 10vw, 160px)"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
components:
  button-primary:
    backgroundColor: "{colors.chili}"
    textColor: "{colors.white}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: "0 32px"
    height: "52px"
  button-primary-hover:
    backgroundColor: "{colors.chili-deep}"
  button-cobalt:
    backgroundColor: "{colors.cobalt}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "0 32px"
    height: "52px"
  button-cobalt-hover:
    backgroundColor: "{colors.ink}"
  nav:
    backgroundColor: "{colors.cobalt}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    height: "68px"
  input:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    height: "52px"
    padding: "0 16px"
  message-error:
    backgroundColor: "{colors.chili}"
    textColor: "{colors.white}"
    padding: "16px 48px"
---

# Design System: FoodNow

## Overview

**Creative North Star: "Tô sứ hoa lam"**

Thực đơn là chồng tô sứ men trắng vẽ chàm: nền sứ trắng ngả lạnh (porcelain), mảng chàm đặc (cobalt) phủ nguyên vùng lớn, chữ mực chàm tối (ink). Mỗi danh mục là một vùng nền riêng, không phải lưới thẻ; mỗi món là một dòng chữ có giá viết ngay bên phải. Hình minh họa là chiếc tô, ly vẽ bằng SVG nét chàm phẳng.

Giọng điệu: thẳng, ấm, rõ giá. Bố cục để chữ đặc và mảng màu làm việc, không trang trí thừa. Khối lớn, chữ tiêu đề rất đậm, khoảng thở rộng giữa các vùng.

**Key Characteristics:**
- Hai mảng màu lớn: chàm đặc (đầu trang, thanh điều hướng, chân trang) xen kẽ sứ trắng và mist.
- Đỏ ớt chỉ dành cho giá, nút hành động chính, lỗi và vòng focus.
- Phẳng hoàn toàn: không bóng, không gradient, không viền mảnh.
- Nút tròn hẳn như miệng tô; ô nhập bo 12px.
- Hai font tự host (Bricolage Grotesque, Be Vietnam Pro) có bản tiếng Việt.

## Colors

Bảng màu lạnh một tông chàm trên nền sứ, với một điểm nhấn đỏ ớt duy nhất.

### Primary
- **Chàm hoa lam** (cobalt, #1C3C8C): mảng nền thanh điều hướng, hero, chân trang; chữ tiêu đề danh mục; liên kết; mô tả món; nét vẽ của mọi chiếc tô.

### Secondary
- **Đỏ ớt** (chili, #D0102A): giá món, nút chính (`.btn`), thông báo lỗi, vòng focus toàn cục. Đậm hơn khi hover (chili-deep, #A80D22).

### Neutral
- **Sứ trắng lạnh** (porcelain, #F4F6F8): nền trang.
- **Trắng men** (white, #FFFFFF): ruột tô, nền ô nhập, chữ trên chàm.
- **Sương chàm** (mist, #E4EAF6): nền các danh mục chẵn xen kẽ, thông báo thường.
- **Mực chàm** (ink, #0F1F4D): chữ thân; hover của nút chàm.
- **Chàm nhạt trên nền chàm** (on-cobalt-soft, #C9D4F0): câu bổ nghĩa hero và dòng chân trang.

### Named Rules
**The One Chili Rule.** Đỏ ớt chỉ đi với giá và hành động; không dùng làm nền vùng lớn hay trang trí.
**The Cobalt Field Rule.** Chàm xuất hiện như mảng đặc phủ cả vùng, không như đường viền hay nét kẻ.

## Typography

**Display Font:** Bricolage Grotesque 800 (fallback Be Vietnam Pro, system-ui)
**Body Font:** Be Vietnam Pro 400 và 600 (fallback system-ui)

**Character:** Tiêu đề đặc, nén chặt (letter-spacing âm), đối lập với thân chữ tròn, dễ đọc, đủ dấu tiếng Việt.

### Hierarchy
- **Display** (800, clamp(2.5rem, 7vw, 6rem), 1): h1 hero. Chân trang dùng cùng font ở cỡ clamp(3.5rem, 18vw, 14rem), line-height 0.9, letter-spacing -0.05em cho tên quán.
- **Headline** (800, clamp(2rem, 4.5vw, 3.5rem), 1.02): h2 danh mục, h1 trang tài khoản.
- **Title** (600 Be Vietnam Pro, clamp(1.25rem, 2.4vw, 1.625rem), 1.25): tên món.
- **Price** (800 display, clamp(1.5rem, 3vw, 2rem), 1): giá, màu chili, không xuống dòng.
- **Lead** (400, clamp(1.125rem, 1.6vw, 1.375rem)): câu bổ nghĩa hero, giới hạn 36ch.
- **Body** (400, 1.0625rem, 1.6): mô tả món giới hạn 52ch.
- **Label** (600, 0.9375rem): liên kết, nút trong thanh điều hướng.

### Named Rules
**The Heavy Headline Rule.** Chỉ h1, h2, h3 hệ display dùng weight 800; mọi chữ còn lại dùng 400 hoặc 600.

## Layout

Vùng chứa `.wrap` rộng tối đa 1320px, lề `--gutter` clamp(16px, 4vw, 48px). Nhịp dọc giữa các vùng là `--section-gap` clamp(72px, 10vw, 160px). Khoảng cách nội bộ dùng bước 8, 16, 24, 32px.

Hero: một cột trên điện thoại (chữ trên, tô dưới); từ 900px chia 7fr/5fr, tô rộng 130% tràn mép phải. Danh mục: một cột trên điện thoại; từ 700px chia 5fr/7fr, phần đầu danh mục (tô và tiêu đề) dính trên (sticky, top 32px) trong khi danh sách món cuộn. Mỗi món là lưới hai cột: tên và mô tả bên trái, giá bên phải, đệm dọc 20px. Dưới 520px, mục "Thực đơn" trên thanh điều hướng ẩn.

## Elevation & Depth

Hoàn toàn phẳng. Độ sâu đến từ đổi mảng màu (cobalt, porcelain, mist) và từ chồng hình tô lên nền, không có `box-shadow` nào trong stylesheet. Trạng thái dùng dịch chuyển và đổi màu, không dùng bóng.

### Named Rules
**The Flat Bowl Rule.** Không bóng, không gradient, không viền mảnh; ranh giới là đổi màu nền.

## Shapes

Hai ngôn ngữ hình: tròn hẳn (nút 999px, ảnh món 50%, hình tô) và bo vừa 12px cho ô nhập. Không có thẻ viền. Tô vẽ nét chàm dày 6px (ly 6px, ống hút 9px) tô đặc trắng, họa tiết chàm đặc bên trong, cắt theo `clipPath`.

## Components

### Buttons
- **Shape:** viên thuốc tròn hẳn (999px), cao tối thiểu 52px, đệm ngang 32px, chữ 600 1.0625rem.
- **Primary (`.btn`):** nền chili, chữ trắng. Hover chili-deep (#A80D22); nhấn thu nhỏ `scale(0.97)`; chuyển 0.25s `--ease-out`.
- **Cobalt (`.btn-ink`):** nền cobalt, hover ink.

### Navigation
Thanh chàm đặc cao tối thiểu 68px; tên quán "FoodNow" 800 1.5rem trắng bên trái, liên kết 600 0.9375rem trắng bên phải. Hover gạch chân dưới (offset 0.35em), không đổi màu. Nút Đăng xuất là `button` trông như liên kết.

### Dish row (món)
Dòng chữ không thẻ: tên (title), giá (price, chili) cùng hàng, mô tả (cobalt) bên dưới. Không có hiệu ứng hover vì dòng chưa bấm được; khi có nút "Thêm" thì nút mới có trạng thái hover. Ảnh món, khi có, là hình tròn 96px.

### Bowl illustration (hình tô)
Bốn `symbol` SVG dùng chung (`bowl-com` cánh sen, `bowl-bun` sóng nước, `bowl-anvat` chấm tròn, `bowl-douong` ly ống hút), chọn theo `category.glyph`. Hero dùng `bowl-com` cỡ lớn, trượt vào và xoay nhẹ một lần khi vào trang (settle), sau đó đứng yên.

### Inputs / Fields
Nền trắng, không viền, bo 12px, cao 52px, đệm ngang 16px. Focus: vòng `outline` 3px màu cobalt (nhãn 600 phía trên). Lỗi: danh sách chili 600. Form rộng tối đa 460px.

### Messages
Dải ngang toàn bề rộng, nền mist chữ ink 600; lỗi nền chili chữ trắng.

### Motion
Easing `--ease-out` cubic-bezier(0.16, 1, 0.3, 1). Hero nhập theo bậc `rise` (0.8s, trễ 0.08s/0.16s); `.reveal` hiện dần khi cuộn, chỉ ẩn trước khi hiện nếu có lớp `.js`. `prefers-reduced-motion` tắt mọi animation và transition.

## Do's and Don'ts

### Do:
- **Do** để giá luôn viết bằng Bricolage 800 màu chili, định dạng `12.000đ`.
- **Do** dùng mảng nền đặc (cobalt, mist) để chia vùng thay vì đường kẻ.
- **Do** vẽ minh họa món bằng nét chàm 6px trên men trắng, phẳng.
- **Do** giữ vòng focus 3px, offset 3px trên mọi phần tử tương tác.
- **Do** chạy mọi chuyển động qua `--ease-out` và tôn trọng reduced-motion.

### Don't:
- **Don't** dùng chili làm nền vùng lớn hoặc cho chữ không phải giá, hành động, lỗi.
- **Don't** thêm bóng, gradient, hoặc viền mảnh quanh thẻ; không dựng lưới thẻ món.
- **Don't** thêm màu thứ hai ngoài họ chàm và chili.
- **Don't** đặt weight 800 cho chữ thân hoặc nhãn.
