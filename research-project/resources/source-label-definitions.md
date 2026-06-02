# Source Label Definitions — Định nghĩa Nhãn Nguồn Thông tin

## Mục đích

Mỗi thông tin quan trọng trong file nghiên cứu **bắt buộc** phải được gắn nhãn nguồn.
Nhãn giúp người đọc biết ngay mức độ tin cậy và xuất xứ của từng thông tin,
phân biệt rõ dữ liệu thực tế với suy luận của AI.

---

## Danh sách nhãn

### `[Dữ liệu thống kê]`
**Dùng khi:** Thông tin dựa trên số liệu, báo cáo, khảo sát, nghiên cứu hoặc thống kê từ tổ chức chính thống.

**Ví dụ nguồn:** Nielsen, Statista, Tổng cục Thống kê, World Bank, McKinsey, báo cáo ngành có tên tổ chức rõ ràng.

**Yêu cầu kèm theo:** Phải ghi tên tổ chức + năm công bố + link nguồn (nếu có).

**Ví dụ sử dụng:**
> Thị trường TMĐT Việt Nam đạt 20,5 tỷ USD năm 2023, tăng 25% so với năm trước. `[Dữ liệu thống kê]`
> *(Nguồn: e-Conomy SEA 2023 — Google, Temasek, Bain & Company)*

---

### `[Nguồn người dùng cung cấp]`
**Dùng khi:** Thông tin lấy từ tài liệu, website, file hoặc dữ liệu do người dùng (client) cung cấp trực tiếp.

**Ví dụ nguồn:** File Word/PDF nội bộ, website sản phẩm, slide giới thiệu, dữ liệu CRM, báo cáo bán hàng nội bộ.

**Yêu cầu kèm theo:** Ghi rõ tên file hoặc loại tài liệu đã dùng.

**Ví dụ sử dụng:**
> Sản phẩm hiện đang phục vụ hơn 5.000 khách hàng doanh nghiệp vừa và nhỏ. `[Nguồn người dùng cung cấp]`
> *(Nguồn: File pitch deck "Company Overview Q1 2024" do client cung cấp)*

---

### `[Review/Comment thực tế]`
**Dùng khi:** Thông tin lấy từ đánh giá, bình luận, feedback thực tế của khách hàng trên các nền tảng công khai.

**Ví dụ nguồn:** Review Shopee/Tiki/Lazada, comment Facebook/TikTok/YouTube, đánh giá Google Maps, App Store, diễn đàn, group cộng đồng.

**Yêu cầu kèm theo:** Ghi rõ nền tảng và thời gian (nếu biết).

**Ví dụ sử dụng:**
> Khách hàng thường khen sản phẩm về tốc độ giao hàng nhanh và đóng gói cẩn thận. `[Review/Comment thực tế]`
> *(Tổng hợp từ ~200 review trên Shopee, tháng 1–3/2024)*

---

### `[Nguồn đối thủ]`
**Dùng khi:** Thông tin lấy từ website, landing page, quảng cáo, bài viết hoặc tài liệu marketing của đối thủ cạnh tranh.

**Ví dụ nguồn:** Website đối thủ, Facebook Ad Library, TikTok ads, email marketing của đối thủ, landing page campaign.

**Yêu cầu kèm theo:** Ghi rõ tên đối thủ và nguồn cụ thể.

**Ví dụ sử dụng:**
> Đối thủ X đang định vị sản phẩm theo góc "tiết kiệm thời gian" với headline "Hoàn thành trong 10 phút". `[Nguồn đối thủ]`
> *(Nguồn: Landing page chính của đối thủ X, truy cập tháng 4/2024)*

---

### `[Tổng hợp Internet]`
**Dùng khi:** Thông tin được tổng hợp từ nhiều nguồn online, không phải một nguồn duy nhất cụ thể, hoặc từ bài viết chuyên môn/báo chí chung.

**Ví dụ nguồn:** Bài viết phân tích ngành trên báo kinh tế, blog chuyên ngành, tổng hợp từ nhiều diễn đàn.

**Yêu cầu kèm theo:** Nếu có thể, ghi ít nhất 1-2 link nguồn đại diện.

**Ví dụ sử dụng:**
> Xu hướng mua sắm theo livestream đang tăng mạnh tại Việt Nam, đặc biệt với nhóm 18-35 tuổi ở đô thị. `[Tổng hợp Internet]`
> *(Tham khảo: VnExpress, CafeF, Brands Vietnam)*

---

### `[Suy luận phân tích]`
**Dùng khi:** Thông tin là nhận định, kết luận hoặc đề xuất do AI phân tích và suy luận từ các dữ liệu đã thu thập — không phải dữ liệu trực tiếp từ nguồn nào.

**Yêu cầu kèm theo:** Ghi rõ dựa trên những dữ liệu nào để suy ra kết luận đó.

**Ví dụ sử dụng:**
> Phân khúc khách hàng 25-35 tuổi tại TP.HCM có khả năng là nhóm có tỷ lệ chuyển đổi cao nhất,
> do kết hợp giữa khả năng chi trả và mức độ nhận thức vấn đề cao. `[Suy luận phân tích]`
> *(Dựa trên: dữ liệu nhân khẩu học [Dữ liệu thống kê] + review người mua thực tế [Review/Comment thực tế])*

---

## Quy tắc gắn nhãn

1. **Mỗi thông tin quan trọng phải có nhãn** — đặc biệt là số liệu, nhận định về khách hàng, kết luận về đối thủ
2. **Nhãn đặt ngay sau câu/đoạn** áp dụng nhãn đó
3. **Một thông tin có thể có nhiều nhãn** nếu kết hợp nhiều nguồn (ví dụ: `[Dữ liệu thống kê]` + `[Suy luận phân tích]`)
4. **Suy luận không được trình bày như sự thật tuyệt đối** — dùng ngôn ngữ có độ bất định: "có thể", "khả năng cao", "dựa trên dữ liệu hiện có"
5. **Không được bịa nguồn** — nếu không nhớ nguồn chính xác, gắn `[Tổng hợp Internet]` và cố gắng tìm lại link