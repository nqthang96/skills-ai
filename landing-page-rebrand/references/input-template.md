# Chỉnh sửa Landing Page Có Sẵn — Mẫu Input Bắt Buộc

Điền các mục dưới đây trước khi chỉnh sửa. Nếu mục nào không áp dụng, ghi rõ `Không áp dụng` hoặc `Không có`, đặc biệt là trạng thái bonus. Không được để trống một dữ kiện có thể ảnh hưởng đến giá, offer, asset hoặc phạm vi chỉnh sửa.

## 1. Dự án và file

- Folder/repository landing page:
- File/page chính xác được phép sửa:
- File hoặc folder nào không được đụng tới:
- Có `AGENTS.md` hoặc quy định riêng không:
- Có thay đổi đang tồn tại cần giữ nguyên không:

## 2. Tên sản phẩm và nguồn chính thức

- Tên sản phẩm cũ:
- Các biến thể tên cũ cần thay:
- Tên sản phẩm mới hiển thị chính xác:
- Sale page/product page chính thức:
- Brief hoặc tài liệu chính thức bổ sung:
- Ngôn ngữ và tone copy:

## 3. Affiliate và CTA

- Affiliate/CTA URL mới:
- CTA nào phải dùng URL này: tất cả / chỉ định rõ:
- Link nào phải giữ nguyên:
- CTA label nào phải giữ nguyên:
- Heading hoặc badge nào phải giữ nguyên tuyệt đối:

## 4. Thương hiệu và asset

- Màu thương hiệu mới:
- Có đổi các biến thể trực tiếp của màu thương hiệu không: gradient / highlight / hover / active / tint / glow / border / shadow / badge / CTA:
- File logo mới:
- File favicon mới:
- Ảnh Hero mới:
- Ảnh Independent Buyer Insight/Review:
- Các ảnh thay thế khác và vị trí tương ứng:
- Nếu được phép chọn ảnh bất kỳ cho logo/favicon, xác nhận rõ ảnh nào được chọn cho vai trò nào:

## 5. Dữ kiện offer chính thức

- Giá hiện tại/giá launch:
- Giá gốc hoặc giá tham chiếu:
- Hình thức thanh toán:
- Thời hạn hoàn tiền:
- Wording hoặc điều kiện scarcity/expiry/launch:
- Claim pháp lý hoặc điều kiện cần giữ đúng:

### Promotion Inventory — toàn bộ ưu đãi và khuyến mại

- Có promotion ngoài bonus không: `Có` / `Không` / `Chưa xác định`:
- `promotion_count`:
- Promotion cần được phân bổ vào: `Exclusive Launch Advantage` / `Early Bird Special Promotion` / `Important Notice For Today’s Visitors`:
- Promotion 1:
  - Loại: coupon / discount / launch deal / bundle / free resource / ưu đãi khác:
  - Tên promotion:
  - Coupon code, giữ nguyên hoa thường:
  - Giá trị giảm hoặc lợi ích:
  - Giá/offer áp dụng:
  - Điều kiện sử dụng:
  - Đối tượng áp dụng:
  - Thời hạn hoặc giới hạn:
  - Nội dung chính thức từ nguồn:
  - URL hoặc vị trí trong nguồn:
  - Section cần hiển thị:
- Promotion 2:
  - Loại:
  - Tên promotion:
  - Coupon code:
  - Giá trị giảm hoặc lợi ích:
  - Giá/offer áp dụng:
  - Điều kiện sử dụng:
  - Đối tượng áp dụng:
  - Thời hạn hoặc giới hạn:
  - Nội dung chính thức từ nguồn:
  - URL hoặc vị trí trong nguồn:
  - Section cần hiển thị:
- Các promotion khác (liệt kê đủ nếu có):

Mỗi promotion chính thức phải xuất hiện ít nhất một lần trong ba vùng offer. Không tự tính giá cuối cùng hoặc điều kiện mới nếu nguồn không công bố.

## 6. Trạng thái bonus bắt buộc

- Bonus: `Có bonus` / `Không có bonus`:
- `bonus_count`:
- Nếu có bonus, danh sách chính xác:
  1. Tên bonus — giá trị:
  2. Tên bonus — giá trị:
  3. Tên bonus — giá trị:
  4. Tên bonus — giá trị:
- Tổng giá trị bonus:
- Included resources/tài nguyên đi kèm (nếu khác bonus):
- Tổng giá trị included resources nếu nguồn công bố:
- Có được dùng lợi ích sản phẩm thay cho bonus ở các slot được prompt gốc cho phép không:

Nếu không có bonus, phải ghi `bonus_count = 0`. Không dùng giá trị bonus cũ, không gọi included resources là bonus và không tự ước tính giá trị chưa được công bố.

## 7. Phạm vi mặc định theo từng section

Nếu dùng đúng prompt gốc, xác nhận: `Dùng bảng phạm vi mặc định của skill`.

- Toàn trang: đổi tên sản phẩm, màu thương hiệu, asset được mapping và CTA URL; giữ nguyên phần còn lại.
- Hero: đổi logo/ảnh Hero, đoạn mô tả công dụng được chỉ rõ và toàn bộ offer trong `Exclusive Launch Advantage`, gồm giá, discount, coupon, bonus, resource và điều kiện chính thức; giữ heading, badge, CTA label và copy khác.
- Automated 7-Agent Architecture: được viết lại toàn bộ nội dung sản phẩm trong section; giữ layout, class/ID, card style, icon system, responsive và section order; card count theo sản phẩm.
- Independent Buyer Insight: đổi đúng 3 card, `Best Suited For` và ảnh; giữ heading, copy chung, dòng user/result, rating, star, CTA, testimonial và phần khác.
- Early Bird Special Promotion: đổi giá, discount, coupon, điều kiện promotion, số ngày hoàn tiền, bonus và token giá trị bonus trong CTA; giữ heading, badge, CTA wording xung quanh, guarantee và urgency wording.
- Important Notice For Today’s Visitors: đưa vào hoặc cập nhật các promotion quan trọng, coupon/discount và bonus trong vùng offer; nếu không có bonus thì xóa đúng phần bonus; giữ nguyên mọi thứ khác.
- Các section khác: giữ nguyên tuyệt đối.

## 8. Ngoại lệ nếu có

- Section nào được phép thay ngoài bảng mặc định:
- Câu/heading/badge/CTA/rating/testimonial/guarantee nào được phép đổi thêm:
- Section nào chỉ được thay token hoặc giá trị:
- Section nào tuyệt đối không được đụng tới:
- Có promotion nào bắt buộc phải lặp lại ở cả ba vùng offer không:
- Yêu cầu khác:

Nếu không có ngoại lệ, ghi `Không có`. Nếu nguồn chính thức mâu thuẫn với nội dung phải giữ nguyên, phải hỏi lại trước khi sửa phần mâu thuẫn.
