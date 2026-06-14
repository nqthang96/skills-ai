# Nguyên tắc thiết kế Landing Page (Design Principles)

Tài liệu này chứa các nguyên tắc cốt lõi về mặt thẩm mỹ và bố cục mà Agent phải áp dụng trong suốt quá trình xác định layout và sinh mã nguồn cho Landing Page.

---

## 1. Phân cấp thị giác (Visual Hierarchy)
Phân cấp thị giác giúp dẫn dắt mắt người đọc đi qua các thông tin theo thứ tự quan trọng giảm dần.
* **Kích thước & Trọng lượng (Size & Weight):** Tiêu đề chính (`h1`, `h2`) phải lớn hơn rõ rệt so với tiêu đề phụ (`h3`) và nội dung chi tiết. Các từ khóa quan trọng hoặc con số thống kê cần được bôi đậm hoặc tăng font-size để tạo điểm nhấn.
* **Màu sắc & Độ tương phản (Color & Contrast):** Các nút hành động chính (Primary CTA) phải sử dụng màu có độ tương phản cao nhất so với nền. Text phụ (subtitle, caption) nên giảm opacity (ví dụ: `text-slate-400` trên nền tối) để giảm bớt độ nổi bật.
* **Khoảng trắng (Negative Space):** Tạo không gian thở cho mắt người dùng. Khoảng cách giữa các phần tử nhỏ trong một nhóm nên từ `8px` đến `24px`, khoảng cách giữa các nhóm lớn từ `32px` đến `64px`, và khoảng cách giữa các section lớn phải từ `80px` đến `120px`.

---

## 2. Nhịp điệu thị giác (Pacing & Rhythm)
Nhịp điệu giao diện giúp người dùng không cảm thấy nhàm chán hoặc mệt mỏi khi cuộn trang dài.
* **Nguyên tắc đan xen Layout:** KHÔNG sử dụng cùng một loại cấu trúc bố cục (Layout Pattern) cho 3 section liên tiếp.
  * *Ví dụ vi phạm:* Section 3 dùng Split (Chữ bên trái - Ảnh bên phải), Section 4 dùng Split (Chữ bên trái - Ảnh bên phải), Section 5 dùng Split.
  * *Cách giải quyết tốt:* Đan xen giữa các khối **Dày** (như Bento Grid, Mosaic Grid, Multi-column Card) và khối **Thoáng** (như Hero banner tối giản, Split layout 2 cột rộng, Center layout 1 cột).
* **Đan xen màu nền (Background Alternation):** Không dùng cùng một màu nền cho 2 section liên tiếp.
  * *Ví dụ:* Nếu Section 1 dùng màu nền sáng trắng, Section 2 nên dùng màu nền xám nhẹ hoặc tối màu để phân định rõ ranh giới giữa các phần của trang web.

---

## 3. Quy tắc Zig-zag (Alternating Layouts)
Quy tắc này giúp cân bằng thị giác và giữ cho mắt người dùng di chuyển liên tục theo đường zig-zag tự nhiên khi cuộn trang.
* **Áp dụng:** Khi có 2 section dạng Split (chia đôi màn hình: 1 bên chữ, 1 bên ảnh) nằm liên tiếp nhau hoặc cách nhau 1 section nhẹ, bạn bắt buộc phải đảo ngược vị trí hiển thị của chúng.
  * *Section A:* [Văn bản] ở cột Trái | [Hình ảnh/Mockup] ở cột Phải.
  * *Section B:* [Hình ảnh/Mockup] ở cột Trái | [Văn bản] ở cột Phải.

---

## 4. Quy tắc Khoảng cách gần (Proximity Rule)
* **Khái niệm:** Các phần tử có liên quan chặt chẽ về mặt nội dung phải được đặt gần nhau để người dùng hiểu rằng chúng thuộc cùng một nhóm thông tin. Các phần tử không liên quan phải có khoảng cách đủ xa để tránh hiểu lầm.
* **Áp dụng:**
  * Khoảng cách giữa Badge và Primary Title: `8px` - `12px`.
  * Khoảng cách giữa Primary Title và Subtitle: `12px` - `16px`.
  * Khoảng cách từ cụm Tiêu đề đến nút CTA: `24px` - `32px`.
  * Khoảng cách từ CTA đến các thông tin bổ sung phía dưới (ví dụ: "Không cần thẻ tín dụng"): `8px` - `12px`.

---

## 5. Hệ lưới 12 cột (12-Column Grid System)
* Đối với giao diện Desktop, toàn bộ bố cục của các section phải được dựng dựa trên hệ lưới 12 cột chuẩn.
* Cách phân bổ cột phổ biến:
  * Layout 2 cột bằng nhau: `col-span-6` và `col-span-6`.
  * Layout Split lệch (tập trung nội dung): `col-span-7` (chữ) và `col-span-5` (ảnh) hoặc ngược lại.
  * Layout 3 thẻ thông tin: 3 thẻ, mỗi thẻ chiếm `col-span-4`.
  * Layout 4 thẻ dịch vụ: 4 thẻ, mỗi thẻ chiếm `col-span-3`.
  * Layout Bento Grid: Kết hợp linh hoạt các ô có độ rộng khác nhau (ví dụ: 1 ô `col-span-8` và 1 ô `col-span-4`).
