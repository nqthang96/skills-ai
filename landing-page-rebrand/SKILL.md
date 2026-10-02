---
name: landing-page-rebrand
description: "Chuyển landing page affiliate HTML/CSS/JavaScript có sẵn sang sản phẩm mới bằng template cố định: chỉ điền nội dung trong [ ], giữ nguyên mọi nội dung ngoài [ ] và đưa đủ offer, promotion, bonus theo nguồn chính thức."
---

# Chỉnh sửa Landing Page Theo Template Cố Định

Dùng skill này khi chuyển một landing page affiliate/bridge page sang sản phẩm mới. Landing page hiện tại là template đã tối ưu; không tự ý viết lại hoặc cải tiến ngoài phạm vi template và yêu cầu rõ ràng của người dùng.

## Quy tắc duy nhất của template

Trước khi sửa, phải đọc toàn bộ template được người dùng chỉ định. Bản reference mặc định là [references/template-landing-page-google-ads.md](references/template-landing-page-google-ads.md); nếu request có file template khác thì dùng file đó làm nguồn ưu tiên.

- Giữ nguyên section, thứ tự, cấu trúc, field, câu chữ, dấu câu, badge, heading, CTA label, rating, guarantee, urgency, footer và legal text của template.
- Mọi nội dung nằm trong placeholder `[ ... ]` là vùng phải điền/thay bằng dữ kiện sản phẩm mới.
- Mọi nội dung ngoài placeholder `[ ... ]` là nội dung cố định, không được dịch, sửa, rút gọn, viết lại, xóa, di chuyển hoặc thay bằng nội dung mới.
- Các câu mô tả nhiệm vụ trong template như “Đưa ra các công dụng...” hoặc “Trường hợp sản phẩm không có bonuses...” là hướng dẫn điền slot, không phải câu được tự ý đưa vào landing page.
- Giá trị ví dụ bên trong placeholder như `$37`, `$832`, `6`, `SAVE10`, `2026` chỉ là ví dụ; không dùng nếu nguồn chính thức không xác nhận.
- Không thay toàn bộ landing page bằng file template và không tự tạo section. Nếu landing page thực tế khác section, field hoặc cấu trúc template, phải hỏi trước khi thêm, xóa, di chuyển hoặc tái cấu trúc.

Nếu người dùng yêu cầu thay đổi ngoài placeholder, chỉ thực hiện đúng phần được nêu trong request. Nếu không được yêu cầu, mặc định giữ nguyên.

## Ba thay đổi toàn trang bắt buộc khi prompt yêu cầu

Ba yêu cầu dưới đây là ngoại lệ toàn trang được phép thực hiện, nhưng không mở rộng quyền sửa các nội dung khác:

1. **Màu thương hiệu:** thay đúng màu thương hiệu sản phẩm cũ sang màu thương hiệu sản phẩm mới ở mọi nơi màu đó được dùng trong HTML, CSS, JavaScript, inline style và SVG/vector asset.
   - **Bắt buộc đồng bộ trọn gói hệ sinh thái màu (Palette Ecosystem):** Scan cả CSS variable, background, text, border, gradient, highlight, hover/active, glow và shadow là biến thể trực tiếp của màu thương hiệu. Ví dụ cụ thể:
     - Nền nhạt/tint: các biến `--color-primary-light`, `--color-primary-tint`, `--color-bg-primary-tint` phải đổi sang tone màu nhạt tương ứng của màu mới (ví dụ: tím nhạt sang vàng nhạt/kem ấm), không được giữ màu nền của thương hiệu cũ.
     - Nền Dark Theme: kiểm tra các màu nền tối (`--color-bg-dark-hero`, `--color-bg-dark-slate`, v.v.). Nếu nền tối bị ám sắc thái màu cũ (như tím than), phải chuyển sang màu than đá trung tính (Neutral Charcoal `#0b0d12`, `#0f1218`) hoặc màu tối của thương hiệu mới.
     - Gradient, Shimmer & Glow: dải gradient phát sáng (`--gradient-text-shimmer`, glow filter, orbital mesh) phải đổi sang tone màu mới, không để sót các điểm phát sáng của màu cũ.
     - Tên Class & Selectors: quét và đổi các class HTML/CSS mang tên màu cũ (như `highlight-text--bright-purple`, `bento-card__icon-wrap--purple`) sang class màu mới tương ứng.
   - Không đổi màu ngữ nghĩa không liên quan như success/warning. Không chỉnh pixel trong ảnh raster nếu chưa được yêu cầu.
   - **Bước đối soát bắt buộc:** Sau khi sửa, phải chạy lệnh quét toàn bộ file CSS, HTML, JS tìm các mã màu hex, rgb/rgba và từ khóa tên màu của thương hiệu cũ để xác nhận số lượng còn sót lại bằng `0`.
2. **Logo và favicon:** thay thật file/logo source và link rel="icon" bằng asset người dùng cung cấp; nếu người dùng cho phép chọn ảnh bất kỳ thì ghi rõ asset được chọn. Không chỉ đổi alt text hoặc tên file. Kiểm tra mọi vị trí logo và favicon đều tải đúng asset mới.
3. **Affiliate/CTA link:** thay href của toàn bộ nút/link CTA trong Sticky Bar, Hero, các CTA giữa trang, Early Bird và Final Notice, cùng single source of truth trong JavaScript nếu có, bằng đúng URL người dùng gửi. Giữ nguyên CTA label và câu chữ nếu không được yêu cầu đổi; kiểm tra không còn CTA URL cũ.

Các thay đổi trên phải được ghi vào change map và kiểm tra riêng sau khi sửa. Nếu người dùng không cung cấp màu, asset hoặc affiliate URL bắt buộc, phải hỏi lại trước khi chỉnh.

## Input bắt buộc

Chưa được chỉnh sửa file khi thiếu input cốt lõi. Phải hỏi người dùng bằng checklist ngắn nếu thiếu:

1. Folder và file/page chính xác được phép sửa; quy định `AGENTS.md` nếu có.
2. File template cần dùng hoặc xác nhận dùng reference mặc định.
3. Tên sản phẩm cũ, các biến thể tên cũ và tên sản phẩm mới.
4. Sale page/product page hoặc brief chính thức.
5. Affiliate/CTA URL và CTA nào dùng URL đó.
6. Màu thương hiệu mới, phạm vi đổi gradient/highlight/glow/shadow/badge/CTA.
7. Asset mapping: logo, favicon, Hero, Insight/Review và ảnh khác; quyền chọn ảnh bất kỳ nếu có.
8. Offer và promotion chính thức: giá, giá gốc, discount, coupon code, giá trị giảm, điều kiện, thời hạn, payment, refund và các ưu đãi khác. Người dùng không cung cấp thì tự lấy thông tin ở trong trang sale page
9. `promotion_count`: số promotion ngoài bonus; nếu không có ghi `0`.
10. `bonus_count`: số bonus; nếu không có ghi `0`. Nếu có, ghi tên, mô tả, giá trị từng bonus và tổng giá trị.
11. Ngôn ngữ/tone và ngoại lệ phạm vi nếu có.

Không suy đoán giá, coupon, discount, điều kiện, thời hạn, bonus, tổng giá trị hoặc claim sản phẩm. Nếu nguồn không nói rõ, hỏi lại.

## Offer, promotion và bonus

- Phải lập `Promotion Inventory` từ nguồn chính thức, gồm mọi coupon, discount, launch deal, bundle, free resource, điều kiện và thời hạn.
- Mọi promotion chính thức phải được điền vào placeholder offer phù hợp trong một hoặc nhiều vùng: `Exclusive Launch Advantage`, `Early Bird Special Promotion`, `Important Notice For Today’s Visitors`.
- Coupon phải giữ nguyên hoa thường, ký tự, giá trị giảm và điều kiện. Không tự tính giá cuối cùng nếu nguồn không công bố.
- Nếu template không có đủ placeholder để đưa một promotion chính thức lên trang, phải hỏi người dùng trước khi thêm placeholder hoặc thay đổi cấu trúc.
- `bonus_count` và `promotion_count` độc lập. Coupon/discount không được tính là bonus.
- Nếu `bonus_count = 0`, không giữ bonus cũ, không tạo bonus mới và không dùng giá trị bonus cũ. Với slot có hướng dẫn fallback, chỉ điền lợi ích/công dụng chính thức của sản phẩm; nếu không có slot fallback thì xóa đúng phần bonus khi người dùng cho phép.
- Nếu `bonus_count > 0`, điền đúng danh sách chính thức; không thêm item để đủ số lượng cũ. Included resources phải gọi đúng là tài nguyên đi kèm, không tự gọi là bonus.
- Số lượng card công dụng/framework và item bonus/promotion thay đổi theo dữ liệu nguồn, không mặc định 7 card hoặc 6 bonus; vẫn giữ style, grid, numbering và responsive của template.

## Quy trình

1. Đọc `AGENTS.md`, template, file HTML/CSS/JavaScript và asset hiện tại; kiểm tra worktree, giữ nguyên thay đổi có sẵn.
2. Thu thập dữ kiện sản phẩm và lưu fact sheet Markdown trong folder hỗ trợ trước khi sửa landing page. Ghi rõ dữ kiện nguồn, suy luận và copy đề xuất.
3. Lập bảng placeholder: nội dung trước, dữ kiện sẽ điền và nguồn. Đánh dấu nội dung ngoài `[ ]` là vùng khóa.
4. Chỉ sửa file trong đúng folder landing page. Dùng `apply_patch`; giữ CSS source of truth, CSS variable, class/ID, layout, icon system và interaction hiện có. Không hardcode tùy ý, override hoặc `!important`.
5. Thay asset và CTA URL đúng mapping; không tự generate, crop hoặc retouch nếu chưa được phép.

## Rà soát ngữ pháp và cổng phê duyệt

Sau khi điền mọi placeholder và trước khi bàn giao, phải đọc lại toàn bộ nội dung tiếng Anh đã render như người dùng nhìn thấy. Đặc biệt kiểm tra điểm nối giữa nội dung cố định và placeholder có nhiều promotion, coupon, bonus hoặc danh sách dài: mạo từ, số ít/số nhiều, chủ-vị, dấu câu, giới từ, thứ tự từ và câu có tự nhiên không.

- Nếu không có lỗi, báo rõ đã rà soát và không phát hiện vấn đề ngữ pháp đáng chú ý.

- Nếu có câu sai, cụt, gượng hoặc dễ hiểu nhầm: tuyệt đối không tự sửa, kể cả khi có thể sửa trong placeholder.

- Báo cáo phải gồm section/vị trí, câu hiện tại, phần gây vấn đề, lý do và một hoặc vài phương án tiếng Anh đề xuất.

- Dừng mọi thay đổi liên quan đến câu đó và hỏi người dùng có duyệt phương án nào không. Chỉ sau khi người dùng duyệt rõ ràng mới được sửa, và chỉ sửa tối thiểu đúng phần đã duyệt.

- Nếu lỗi nằm ở nội dung cố định ngoài placeholder, phải nói rõ đó là nội dung khóa và chỉ sửa khi người dùng cho phép ngoại lệ.
  
  ## Kiểm tra trước khi bàn giao

- Đọc diff: không có nội dung ngoài placeholder hoặc ngoại lệ được người dùng cho phép bị thay đổi.

- Không còn placeholder sản phẩm chưa được điền và không còn tên, giá, offer, bonus hoặc promotion cũ trong vùng phải thay.

- Đối chiếu toàn bộ `Promotion Inventory`, `promotion_count`, `bonus_count`, giá trị, coupon, điều kiện và thời hạn với fact sheet.

- Xác nhận `bonus_count = 0` không còn bonus cũ và không có bonus/promotion tự bịa.

- Kiểm tra CTA href, asset, favicon, màu thương hiệu, HTML/CSS/JavaScript; chạy `node --check` và `git diff --check` khi phù hợp.

- **Nghiệm thu màu sắc (Color Audit Gate):** Chạy script/lệnh tìm kiếm các mã màu hex, rgb, rgba và tên màu của thương hiệu cũ trên toàn bộ dự án (`index.html`, `style.css`, `script.js`). Bắt buộc kết quả trả về phải bằng 0 match trước khi bàn giao.

- Khi có thể, kiểm tra local page desktop/mobile, ảnh, CTA sau binding JavaScript và console errors.

Báo cáo file đã sửa, fact sheet, placeholder đã điền, promotion/bonus đã xử lý, nội dung được giữ nguyên và các mâu thuẫn còn lại.
