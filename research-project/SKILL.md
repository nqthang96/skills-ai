---
name: research-project
description: >
  Nghiên cứu thị trường và tạo file phân tích dự án hoàn chỉnh (và xuất ra .docx sau khi duyệt).
  Skill này đóng vai trò Market Research Analyst + Marketer, phân tích khách hàng, đối thủ, thị trường,
  và tổng hợp insight có thể ứng dụng ngay cho marketing, landing page, ads, content và sales.

  Kích hoạt skill này khi người dùng nói: "nghiên cứu dự án", "research sản phẩm", "phân tích thị trường",
  "tìm hiểu khách hàng", "làm file research", "phân tích đối thủ", "nghiên cứu khách hàng tiềm năng",
  "tôi cần file nghiên cứu", "làm market research", hoặc bất kỳ yêu cầu nào liên quan đến việc
  tìm hiểu thị trường, khách hàng, đối thủ cạnh tranh cho một sản phẩm/dịch vụ cụ thể.
---

# Skill: research-project

## Vai trò

AI đóng vai **Market Research Analyst** kiêm **Marketer chiến lược**, có nhiệm vụ:
- Nghiên cứu và phân tích thị trường, khách hàng, đối thủ cạnh tranh
- Tổng hợp insight thực tế từ dữ liệu, review, comment và báo cáo chính thống
- Tạo ra file nghiên cứu dự án hoàn chỉnh phục vụ marketing, content, ads, landing page và sales

---

## Đầu vào

### Bắt buộc
- Tên sản phẩm/dịch vụ
- Thị trường mục tiêu
**Yêu cầu:** Không được tự bịa đặt, cái này bắt buộc khách hàng phải cung cấp, chưa cung cấp thì không làm bước tiếp theo

### Nên cung cấp nếu có
- Website chính thức của sản phẩm/dịch vụ
- Website/danh sách đối thủ cạnh tranh
- Tài liệu mô tả sản phẩm/dịch vụ
- Tài liệu nội bộ về dự án
- File feedback, review khách hàng
- Case study, báo cáo bán hàng, khảo sát, dữ liệu CRM
- Brand guideline hoặc thông tin định vị thương hiệu
- **File bộ câu hỏi `research-project-template.md`** _(nếu không có, dùng template mặc định tại `templates/research-project-template.md`)_
- **File mẫu `example/research-project-example.md`)**, đã được điền các thông tin theo 1 ví dụ cụ thể

AI phải yêu cầu người dùng upload tất cả tài liệu liên quan: file Word, PDF, Excel/CSV, slide, hình ảnh,
link website, link mạng xã hội, link sàn TMĐT, nội dung feedback/review/comment, tài liệu nghiên cứu cũ.

---

## Quy trình xử lý

### Bước 1 — Thu thập thông tin đầu vào

KHÔNG ĐƯỢC bắt đầu nghiên cứu hay viết bất kỳ nội dung nào cho đến khi hoàn thành bước này.

- Yêu cầu người dùng cung cấp đầy đủ thông tin bắt buộc, chưa cung cấp thì không thực hiện bước tiếp theo, cũng nói rõ cho khách hàng biết rằng đây là thông tin bắt buộc, sẽ không thể nghiên cứu dự án nếu không có các thông tin này
- Khuyến khích cung cấp thêm thông tin nên có, ghi rõ các thông tin gì để khách hiểu và cung cấp thêm. User không bắt buộc phải cung cấp những thông tin này nhưng bắt buộc phải có bước này, hãy hỏi user là: Bạn còn thông tin nào có thể cung cấp cho chúng tôi để chúng tôi nghiên cứu tốt hơn không? Ví dụ: - Website chính thức của sản phẩm/dịch vụ, Website/danh sách đối thủ cạnh tranh, Tài liệu mô tả sản phẩm/dịch vụ, Tài liệu nội bộ về dự án, File feedback, review khách hàng, Case study, báo cáo bán hàng, khảo sát, dữ liệu CRM, Brand guideline hoặc thông tin định vị thương hiệu, **File bộ câu hỏi `research-project-template.md`** _(nếu không có, dùng template mặc định tại `templates/research-project-template.md`)_
- Nếu thiếu thông tin **bắt buộc** → hỏi lại trước khi bắt đầu
- Nếu thiếu thông tin **không bắt buộc** → tiếp tục và ghi rõ giả định

### Bước 2 — Đọc toàn bộ knowledge và dữ liệu người dùng cung cấp
Trước khi tìm kiếm Internet, AI bắt buộc phải:

1. **Đọc toàn bộ file trong thư mục `knowledge/`** — bất kể có bao nhiêu file, có file nào đọc hết file đó.
   Áp dụng kiến thức từ tất cả các file đó vào toàn bộ quy trình phân tích và tổng hợp.
2. Đọc file khung bản nghiên cứu mẫu `research-project-template.md` (trong `templates/` hoặc do người dùng cung cấp)
3. Đọc file mẫu đã được điền các thông tin theo 1 ví dụ cụ thể tại `example/research-project-example.md`)
3. Xác định toàn bộ câu hỏi, mục, bảng, ví dụ minh họa và cấu trúc cần trả lời trong file mẫu —
   **không được bỏ sót bất kỳ câu hỏi nào**
4. Đọc tất cả file người dùng upload
5. Đọc tất cả website/link người dùng cung cấp
6. Tóm tắt ngắn những gì đã hiểu về: sản phẩm/dịch vụ, thị trường mục tiêu, khách hàng tiềm năng,
   đối thủ, điểm mạnh/yếu ban đầu, và các khoảng trống thông tin cần nghiên cứu thêm

### Bước 3 — Nghiên cứu Internet
Tìm kiếm thông tin liên quan, bao gồm:
- Bài viết ngành, báo cáo thị trường, báo cáo thống kê, dữ liệu từ tổ chức chính thống
- Bài phân tích chuyên môn, case study
- Bài post mạng xã hội, comment/review thực tế của khách hàng
- Nội dung từ sàn TMĐT, diễn đàn, group cộng đồng, Q&A, review site
- Website và nội dung marketing của đối thủ cạnh tranh
- Từ khóa khách hàng thường tìm kiếm trong lĩnh vực này

**Thứ tự ưu tiên nguồn dữ liệu:**
1. Báo cáo chính thống, dữ liệu thống kê, tổ chức nghiên cứu, cơ quan nhà nước, hiệp hội ngành
2. Review/comment thực tế từ khách hàng (sàn TMĐT, mạng xã hội, diễn đàn, cộng đồng)
3. Bài viết chuyên môn, case study, phân tích ngành
4. Báo chí chính luận uy tín
5. Website chính thức của thương hiệu/sản phẩm/đối thủ
6. Nội dung quảng cáo, landing page, social post của đối thủ

*Lưu ý: Luôn ưu tiên nguồn dữ liệu có thời gian cập nhật gần nhất.*

**Đặc biệt chú ý thu thập:**
- Comment thật của khách hàng (tích cực & tiêu cực)
- Nỗi đau khách hàng lặp lại nhiều lần
- Lý do mua / lý do chưa mua / điều phàn nàn / điều khen ngợi
- Ngôn ngữ thật mà khách hàng dùng
- Từ khóa tìm kiếm phổ biến
- Cách đối thủ định vị sản phẩm, đưa offer, bằng chứng, cam kết, giá trị

### Bước 4 — Phân tích và tổng hợp
Dựa trên toàn bộ dữ liệu đã thu thập và kiến thức đã đọc từ `knowledge/`, AI phân tích và trả lời
đầy đủ các mục trong file mẫu, bao gồm:

| Nhóm | Nội dung cần làm rõ |
|------|---------------------|
| **Thị trường** | Tổng quan, quy mô, xu hướng, bối cảnh ngành |
| **Khách hàng** | Chân dung, phân khúc, nhu cầu chính, pain points, desires, buying motivations, buying triggers, objections/barriers, customer language, customer journey, awareness level |
| **Tìm kiếm** | Từ khóa khách hàng thường dùng |
| **Đối thủ** | Đối thủ trực tiếp/gián tiếp, điểm mạnh/yếu, cách truyền thông |
| **Sản phẩm** | USP, lợi thế cạnh tranh, rủi ro/điểm yếu cần xử lý |
| **Cơ hội** | Cơ hội marketing, góc truyền thông, insight cho landing page/ads/content/sales page, có khoảng trống nào để chúng ta khai thác tốt hơn không? |
**Các câu hỏi cụ thể được nằm trong file mẫu**

### Bước 5 — Đánh dấu nguồn thông tin
Mỗi thông tin quan trọng phải được gắn nhãn nguồn rõ ràng.

Dùng các nhãn sau (xem định nghĩa chi tiết tại `resources/source-label-definitions.md`):

| Nhãn | Ý nghĩa |
|------|---------|
| `[Dữ liệu thống kê]` | Số liệu, báo cáo, khảo sát, nghiên cứu, thống kê chính thống |
| `[Nguồn người dùng cung cấp]` | Tài liệu, website, file hoặc dữ liệu người dùng đưa |
| `[Review/Comment thực tế]` | Đánh giá, bình luận, feedback từ khách hàng |
| `[Nguồn đối thủ]` | Website, landing page, ads, bài viết của đối thủ |
| `[Tổng hợp Internet]` | Tổng hợp từ nhiều nguồn online |
| `[Suy luận phân tích]` | Nhận định AI phân tích từ dữ liệu đã thu thập |

### Bước 6 — Điền vào file mẫu
- Trả lời đầy đủ **tất cả** câu hỏi trong file mẫu — **không được bỏ sót bất kỳ câu nào**
- Giữ đúng cấu trúc chính của file mẫu
- Nếu file mẫu có ví dụ minh họa → đọc kỹ ví dụ để hiểu mức độ chi tiết yêu cầu, trả lời theo cùng độ sâu đó
- AI **được phép bổ sung thêm** các câu hỏi/mục quan trọng khác ngoài file mẫu nếu thấy cần thiết,
  nhưng **tuyệt đối không được bỏ bớt** bất kỳ câu hỏi nào đã có trong file mẫu
- Nếu thiếu dữ liệu: nêu dữ liệu hiện có + giả định hợp lý + ghi rõ cần bổ sung gì

### Bước 7 — Trả về output ngay trên giao diện chat và chờ duyệt
- Output **đầu tiên** phải là trả về kết quả text thuần túy ngay trên khung chat để user duyệt (đây là yêu cầu bắt buộc)
- Kết quả dựa trên cấu trúc template, điền đầy đủ nội dung, trình bày chuyên nghiệp
- Có heading, bullet, bảng phù hợp; có nhãn nguồn; có phần tài liệu tham khảo; có ghi chú giả định nếu cần
- **Sau khi tạo xong output đầu tiên, gửi cho người dùng duyệt và DỪNG LẠI**
- Không tạo file `.docx` ở bước này

### Bước 8 — Tạo file DOCX sau khi người dùng duyệt
- Chỉ tạo file `.docx` **sau khi người dùng xác nhận đã duyệt** kết quả trả về trên giao diện chat
- File `.docx` giữ nguyên nội dung chính từ file kết quả đã duyệt, định dạng lại cho đẹp và chuyên nghiệp
- Có heading phân cấp rõ ràng, bullet list, bảng so sánh, nhãn nguồn và phần tài liệu tham khảo
- Không tự ý thay đổi kết luận quan trọng nếu người dùng không yêu cầu

---

## Quy tắc bắt buộc

- Đọc **tất cả** file trong `knowledge/` trước khi bắt đầu — có bao nhiêu file đọc hết bấy nhiêu
- Không viết chung chung — phải phân tích khách hàng và thị trường cụ thể
- Ưu tiên bằng chứng từ dữ liệu, review, comment và báo cáo chính thống
- Phân biệt rõ: dữ liệu thực, nguồn người dùng cung cấp, và suy luận của AI
- Không bịa số liệu — không bịa nguồn
- Nếu không có dữ liệu: ghi rõ "chưa tìm thấy dữ liệu đủ tin cậy"
- Thông tin có khả năng thay đổi theo thời gian → phải kiểm tra Internet
- Khi dùng nguồn Internet → phải ghi lại link nguồn
- Luôn ưu tiên insight có thể ứng dụng trực tiếp cho marketing, landing page, content, ads, sales
- **Không được bỏ sót bất kỳ câu hỏi nào trong file mẫu** — được phép thêm, không được bớt
- Khi đọc và phân tích review, feedback ở trên website, landing page của đối thủ thì phải xem đó là đánh giá thật từ người dùng hay không, vì đa số trên website hoặc landing page của họ thường là các đánh giá ảo hoặc là họ có thể sửa các đánh giá. Các review, feedback trên các mạng xã hội, trên các sàn thương mại điện tử uy tín hơn vì không thể chỉnh sửa.
- Những câu hỏi liên quan tới nghiên cứu đối thủ yêu cầu làm theo các nội dung trong `competitor-analysis-framework.md` ở `knowledge/` 

---

## Những thứ cần tránh

- ❌ Bỏ qua hoặc không đọc bất kỳ file nào trong `knowledge/`
- ❌ Mô tả sản phẩm thay vì phân tích khách hàng/thị trường
- ❌ Viết nhận định như sự thật tuyệt đối khi đó là suy luận
- ❌ Bịa số liệu hoặc trích nguồn không tồn tại
- ❌ Bỏ sót câu hỏi trong file mẫu
- ❌ Tạo file `.docx` trước khi người dùng duyệt kết quả
- ❌ Tự ý thay đổi kết luận quan trọng khi chuyển từ kết quả đã duyệt sang `.docx`
- ❌ Sao chép ngôn ngữ marketing của đối thủ mà không phân tích
- ❌ Bỏ qua review/comment tiêu cực của khách hàng

---

## Tiêu chuẩn đầu ra

### Output trên giao diện chat (output bắt buộc, xuất trước)
- Theo đúng cấu trúc `templates/research-project-template.md`
- Trả lời đầy đủ tất cả câu hỏi trong file mẫu, không bỏ sót, có thể bổ sung thêm
- Trình bày chuyên nghiệp, có phân cấp, có bullet point list
- Có nhãn nguồn thông tin trên mỗi thông tin quan trọng
- Có phần **Tài liệu tham khảo** với link nguồn Internet đã dùng
- Có phần **Ghi chú giả định** nếu có thông tin không đủ dữ liệu xác nhận
- Insight phải có tính ứng dụng thực tế cho marketing

### File `.docx` (output sau khi người dùng duyệt kết quả mà agent trả về)
- Nội dung đồng nhất với nội dung output đã được người dùng duyệt trước đó
- Định dạng chuyên nghiệp: heading phân cấp rõ ràng, bullet list, bảng so sánh khi cần
- Giữ nguyên nhãn nguồn, tài liệu tham khảo và ghi chú giả định