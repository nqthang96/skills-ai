# Hướng dẫn sử dụng file tài nguyên (Resource Guide)

* **Khi nào sử dụng:** Sử dụng file này khi cần đề xuất các chi tiết trang trí nhỏ (Micro-patterns) để tạo chiều sâu giao diện (như hào quang, kính mờ, đổ bóng, layout chồng lấp, avatar group, stat card...) cho từng phần của trang đích.
* **Cách sử dụng hiệu quả:**
  * Căn cứ lựa chọn: Dựa vào cấu trúc bố cục (Layout Pattern) đã chọn và các thành phần UI (Components) của section để bổ sung hiệu ứng tương tác hoặc trang trí tương ứng.
---

**MICRO-PATTERNS**

Agent chọn và kết hợp phù hợp với từng section.

| Micro-pattern | Đặc điểm | Dùng khi |
|---|---|---|
| Floating Elements | Card hoặc badge nổi ra khỏi container chính, dùng negative margin hoặc absolute positioning | Section có stat card nổi, About section có số liệu floating, section cần tạo cảm giác 3D |
| Overlapping | Hai element chồng lên nhau, tạo chiều sâu | Ảnh chồng lên background shape, card chồng lên ảnh, section transition giữa 2 màu nền |
| Background Shape / Blob | Dùng SVG shape hoặc CSS gradient làm background decorative phía sau content | Hero section, CTA section, section cần tạo điểm nhấn mà không có ảnh thật |
| Badge / Label | Pill nhỏ đặt phía trên heading, ghi tên section hoặc keyword ngắn | Hầu hết các section có heading chính, giúp người đọc định hướng nhanh |
| Highlight Text | Một từ hoặc cụm từ trong heading được tô màu primary hoặc có underline decoration | Heading H1/H2 cần nhấn mạnh keyword quan trọng nhất |
| Divider / Separator | Đường kẻ ngang hoặc khoảng trắng lớn phân tách các block nội dung | Section có nhiều sub-block, cần phân tách rõ mà không dùng màu nền khác |
| Icon + Text Pattern | Icon nhỏ đặt cạnh text | Danh sách tính năng, danh sách lợi ích, checklist |
| Avatar Group | Nhiều avatar xếp chồng nhau một phần, thường kèm số lượng | Social proof, "X+ người đã sử dụng", team nhỏ |
| Stat Card | Card nhỏ hiển thị 1 con số lớn + label mô tả | Section có số liệu thống kê nổi bật cần highlight riêng |
| Quote Block | Text quote lớn, thường kèm dấu ngoặc kép decorative và thông tin tác giả | Testimonial, founder quote, mission statement |
