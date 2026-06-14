# Hướng dẫn sử dụng file tài nguyên (Resource Guide)

* **Khi nào sử dụng:** Sử dụng file này khi cần rà soát, tinh chỉnh hoặc tối ưu hóa phân cấp thị giác (Visual Hierarchy) cho giao diện của các section, nhằm tạo luồng đọc dễ chịu và tập trung sự chú ý vào các thông điệp/CTA chính.
* **Cách sử dụng hiệu quả:**
  * Căn cứ lựa chọn: Dựa vào cấu trúc các component, nội dung trong section và thứ tự ưu tiên đọc thông tin mà bạn muốn dẫn dắt mắt người dùng đi qua.

---

**VISUAL HIERARCHY**

Agent áp dụng kết hợp các kỹ thuật sau để tạo thứ tự đọc rõ ràng trong mỗi section.

| Kỹ thuật | Đặc điểm | Dùng khi |
|---|---|---|
| Size Hierarchy | Element quan trọng hơn → font size lớn hơn hoặc component lớn hơn. Thứ tự chuẩn: H1/H2 → Subtitle → Body → Caption. Không dùng 2 text cùng size và weight cạnh nhau nếu vai trò khác nhau | Luôn áp dụng cho mọi section |
| Weight Hierarchy | Chỉ dùng 3 mức: 400 → 600 → 700/800. Không nhảy cấp | Luôn áp dụng cho mọi section |
| Color Hierarchy | Neutral-900 (heading) → Neutral-700 (body) → Neutral-400 (caption). Primary color cho CTA và keyword quan trọng nhất | Luôn áp dụng cho mọi section |
| Contrast Hierarchy | Element cần chú ý nhất → contrast cao nhất so với background. Tối thiểu 4.5:1 cho text thường, 3:1 cho text lớn >24px bold | CTA button luôn là element có contrast cao nhất trong section |
| Spacing Hierarchy | Element liên quan → khoảng cách nhỏ. Element khác group → khoảng cách lớn hơn. Khoảng cách heading → subtitle nhỏ hơn subtitle → body | Luôn áp dụng, đặc biệt section có nhiều group nội dung |
| Alignment Hierarchy | Căn trái tạo cảm giác tự nhiên, dễ đọc. Căn giữa tạo cảm giác trang trọng, nhấn mạnh. Không trộn lẫn căn trái và căn giữa trong cùng 1 group | Section full-width dùng căn giữa, section split dùng căn trái |
| Depth Hierarchy | Tạo cảm giác không gian 3 lớp: background → mid-ground (card, container) → foreground (text, CTA). Dùng shadow và z-index để phân tầng | Section có floating element, overlapping, card nổi |
| Repetition & Consistency | Các element cùng vai trò phải có cùng style xuyên suốt toàn trang. Tạo rhythm thị giác giúp người đọc nhận ra pattern nhanh | Luôn áp dụng, đặc biệt với button, card, icon |
| Isolation | Đặt 1 element quan trọng tách biệt, xung quanh nhiều whitespace | CTA chính, số liệu nổi bật, quote ngắn cần gây ấn tượng mạnh |
| Direction & Flow | Dùng hình dạng, mũi tên, hoặc bố cục để dẫn hướng mắt người đọc theo luồng mong muốn | Hero section, How it works, quy trình nhiều bước |
| Texture & Pattern | Dùng subtle texture hoặc pattern làm background để tạo chiều sâu mà không gây rối | Section cần tạo điểm khác biệt, tránh flat design quá đơn điệu |
