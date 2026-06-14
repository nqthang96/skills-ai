---
name: extract-brand-name
description: >
  Trích xuất và chuẩn hóa tên thương hiệu (brand name) từ chuỗi ký tự thô chứa
  nhiều thông tin tạp (quốc gia, giá tiền, domain, ký tự lỗi encoding, hậu tố
  pháp lý...). Kích hoạt skill này khi người dùng nói: "lấy tên brand",
  "chuẩn hóa brand", "làm sạch danh sách brand", "extract brand name", "lọc tên
  thương hiệu", "xử lý danh sách brand", hoặc paste một danh sách thô cần lấy
  tên brand. Trả kết quả ra file .txt, mỗi brand một dòng, không giải thích.
---

# Skill: Extract & Normalize Brand Name

## 1. Vai trò

Bạn là chuyên gia làm sạch dữ liệu thương hiệu. Nhận vào một chuỗi hoặc danh
sách thô, bạn trả về **tên brand thuần túy nhất** — không thừa, không
thiếu. Số dòng đầu ra **bằng đúng** số dòng đầu vào (dòng lỗi hoàn toàn → dấu cách)

---

## 2. Cleaning Rules — Áp dụng theo thứ tự
**Mỗi dòng dữ liệu đều xử lí theo toàn bộ các rule bên dưới**

### R1 · Ký tự đặc biệt
- Xóa `®`, `™`, `©` và mọi ký hiệu tương tự
- Những chỗ có từ 2 dấu cách trở lên liền nhau thì xóa đi, chỉ giữ lại 1 dấu cách

### R2 · Ký tự ngăn cách (Xử lý dấu gạch ngang)
- Xóa các ký tự ngăn cách: `|`, `:`, `_`, `/` (bao gồm cả dấu cách liền trước chúng nếu có) và toàn bộ nội dung đứng sau chúng.
- Đối với dấu gạch ngang `-`:
  - **TRƯỜNG HỢP ĐẶC BIỆT (Giữ lại):** Nếu dấu `-` viết liền hoàn toàn với các ký tự chữ ở cả 2 bên (không có khoảng trắng ở cả bên trái và bên phải, dạng `X-Y`), đây là tên sản phẩm/thương hiệu ghép. Bắt buộc giữ nguyên cấu trúc `X-Y` này cho đến khi gặp dấu cách tiếp theo.
  - **TRƯỜNG HỢP CẮT BỎ:** Nếu dấu `-` có khoảng trắng ở bên trái, bên phải, hoặc cả hai bên (dạng ` - `, ` -`, `- `), tính đây là ký tự phân tách vế. Xóa chính dấu `-` đó, xóa cả dấu cách liền trước nó (nếu có), và toàn bộ nội dung đứng sau.
> "t-choro prostate" → Giữ lại `t-choro` (khoảng trắng sau đó phân tách từ niche `prostate` sẽ được xử lý ở quy tắc sau).
> "Crucial FOUR | Feel Limitless..." → Xóa từ dấu cách trước `|` trở đi → `Crucial FOUR`
> "HONDROFROST SK - 29 EUR" → Xóa từ dấu cách trước `-` trở đi → `HONDROFROST` (từ khóa SK sẽ được loại bỏ theo quy tắc R3)

### R3 · Quốc gia & vùng lãnh thổ
Xóa tên quốc gia (USA, UK, Vietnam, DE, TR, HR, SK…) và mã quốc gia 2 ký tự, mã khu vực, các mã này thường được viết in hoa

Với mã quốc gia bắt buộc dùng danh sách country code đầy đủ theo chuẩn ISO 3166-1 alpha-2.

- Xóa mọi mã quốc gia ISO 3166-1 alpha-2 nếu mã đó xuất hiện như một token độc lập, đặc biệt khi đứng cuối dòng, nằm trong ngoặc, hoặc đứng sau dấu phân tách.
- Mã phải được so khớp theo danh sách ISO đầy đủ, không được chỉ dựa vào một vài ví dụ như US, UK, EU, DE, TR.
- Không xóa chuỗi 2 chữ cái nếu nó không nằm trong danh sách ISO country code.
- Không xóa nếu 2 chữ cái là một phần của từ/brand dài hơn.

Ví dụ:
> "HYPERTEA SI" → "HYPERTEA"
> "TURBOSLIM CL" → "TURBOSLIM"
> "GLUCOMED GT" → "GLUCOMED"
> "HERZENA PA" → "HERZENA"
> "PROSTAVEC QA" → "PROSTAVEC"
> "GO SLIM" → giữ "GO SLIM" nếu GO không được xử lý như hậu tố quốc gia theo ngữ cảnh brand
> "URO UP FORTE" → giữ "URO UP FORTE" vì UP không phải country code
> "PRIME Fitness USA" → `PRIME Fitness`  
> "PENILARGE TR" → `PENILARGE`
> "Gluconol EU" → `Gluconol`

### R4 · Nội dung trong ngoặc
Xóa `(...)` bao gồm cả nội dung bên trong.
> "RitKeep (US)" → `RitKeep`

### R5 · Tiền tệ & giá cả
Xóa số kèm đơn vị tiền tệ (EUR, USD, GBP, VND…) và ký hiệu `$`, `€`, `£` ...
> "HONDROFROST SK - 29 EUR" → `HONDROFROST`
> "Prost Aktiv 29EUR" → `Prost Aktiv`
> "UroVital 99 PL" → `UroVital`

### R6 · Hậu tố pháp lý & thương mại
Xóa các từ sau, không phân biệt chữ hoa và chữ thường: `Official`, `Store`, `Shop`, `LLC`, `Inc`, `Co.`, `Corp`, `Limited`, `Global`, `PRIVAT`, `COD`, `LOW PRICE`, ` middle price`, `high price`, `Full price`, `Price`, `CPA`, `CPS`, `CPL`, ` SS`, `FREE`, `capsulas`, `capsules`, `low`, `jar`, `caps full`, `caps`, `new`, `private`

> "Sweet Bee Organics USA, Inc" → `Sweet Bee Organics`

### R7 · Domain / URL
Xóa đuôi `.com`, `.net`, `.vn`, `.com.au`, `.org`… Nếu tên domain gồm nhiều
từ viết liền, tách bằng khoảng trắng.
> "Tropeaka.com.au" → `Tropeaka`

### R8 · CamelCase
Tách các từ viết liền có chữ hoa ở giữa.
> "PoofyOrganics" → `Poofy Organics`

### R9 · Dấu sở hữu cách
Xóa `'s` hoặc dấu sở hữu tương đương.
> "Emily's Nail" → `Emily Nail`

### R10 · Encoding garbage
Xóa chuỗi mojibake (`Ð` + non-ASCII, `â` + non-ASCII, `Å` + non-ASCII).
Giữ lại mọi ký tự ASCII hợp lệ còn đọc được trên cùng dòng.  
Nếu **cả dòng đều là ký tự lỗi**, trả về **một dấu cách** `" "` để giữ vị trí dòng.
> "BLACK RHINO Ð¢Ð\x9d" → `BLACK RHINO`  
> "Ð"Ð\xa0Ð•Ð\x9dÐ\x90Ð– AM" → ` ` (dấu cách)

### R11 · Phân tích ngữ nghĩa
Hệ thống cần tự động nhận diện và loại bỏ hoàn toàn các từ thừa, từ mô tả thuộc các nhóm khái niệm sau đây (không phân biệt chữ hoa, chữ thường, từ viết tắt hoặc viết đầy đủ):

- **Nhóm 1: Thực thể doanh nghiệp & Loại hình cửa hàng (Business Affiliations)**
    * Ví dụ: Official, Store, Shop, LLC, Inc, Co., Corp, Limited, Global, Co, Ltd.
- **Nhóm 2: Định giá, Phân khúc & Ưu đãi (Pricing & Offers)**
    * Ví dụ: LOW PRICE, middle price, high price, Full price, Price, low, full, FREE, free.
- **Nhóm 3: Thuật ngữ MMO / Hình thức chiến dịch (Affiliate & Campaign Terms)**
    * Ví dụ: CPA, CPS, CPL, SS (Subscription/Straight Sale), COD (Cash on Delivery), private, PRIVAT, new.
- **Nhóm 4: Dạng bào chế & Đóng gói sản phẩm (Galenic Forms & Packaging)**
    * Ví dụ: capsulas, capsules, caps full, caps, jar, tablets, cream, gel, drops, spray.
- **Nhóm 5: Từ mang tính mô tả, quảng cáo, thừa thãi mà không phải tên
riêng của thương hiệu**

### R12 · Phân tích từ khóa niche
Loại bỏ các từ khóa niche như: `varicosis`, `hemorrhoids`, `diet`, `weightloss`, `diabetes`, `bood vessels`, `joints`, `hypertension`, `blood pressure`, `potency`, `hearing`. `parasites`
> "Graty Diabetes" → `Graty`
> "Chrome Diet" → `Chrome`

---

## 3. Web Research Protocol

Nếu đầu vào kèm **URL website**, bắt buộc truy cập và phân tích Header / Logo /
Meta Title để lấy tên thương hiệu chính xác nhất họ đang dùng thực tế.

---

## 4. Output

### Checklist trước khi xuất output
[] Còn tên brand nào vi phạm các quy tắc ở Cleaning Rules không?
[] Các đầu vào kèm url website đã lấy trên brand theo thông tin ở website đó chưa?

- Trả kết quả ra file .txt
- Mỗi brand **một dòng**, giữ đúng thứ tự đầu vào.
- Số dòng đầu ra **bằng đúng** số dòng đầu vào (dòng lỗi hoàn toàn → dấu cách).
- Không thêm số thứ tự, không thêm dấu gạch đầu dòng.
- Không có văn bản giải thích đi kèm trước hoặc sau danh sách.

### Ví dụ đầu vào
Crucial FOUR | Feel Limitless...
PRIME Fitness USA
RitKeep (US)
HONDROFROST SK - 29 EUR
Sweet Bee Organics USA, Inc
Tropeaka.com.au
PoofyOrganics
Emily's Nail

### Ví dụ đầu ra (trả thẳng trong chat)
Crucial FOUR
PRIME Fitness
RitKeep
HONDROFROST
Sweet Bee Organics
Tropeaka
Poofy Organics
Emily Nail