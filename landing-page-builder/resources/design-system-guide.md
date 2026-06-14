# Hướng dẫn sử dụng file tài nguyên (Resource Guide)

* **Khi nào sử dụng:** Sử dụng file này khi cần thiết lập, tính toán hoặc kiểm tra toàn bộ các tham số quy chuẩn thiết kế chung (Design System) của dự án.
* **Cách sử dụng hiệu quả:**
  * Căn cứ lựa chọn: Dựa vào ngôn ngữ nội dung của landing page (tiếng Việt/tiếng Anh), ngành hàng sản phẩm, màu sắc nhận diện thương hiệu của khách hàng (Primary color), cảm xúc muốn truyền tải, visual style
  * Phương pháp đọc: **Agent bắt buộc phải đọc kỹ toàn bộ tài liệu này** (từ mục 1 đến 12) vì các thông số như kích thước Scale, khoảng cách Gap, bo góc Radius, Shadow, và các cấp độ CSS variables có tính liên kết chặt chẽ và phải được tính toán chính xác tuyệt đối để gán vào mã nguồn.

---

**DESIGN SYSTEM**

---

**1. FONT FAMILY**

Xác định ngôn ngữ nội dung trước:
- Tiếng Việt → Body font: **Be Vietnam Pro**
- Tiếng Anh → Body font: **Inter**
- Song ngữ → **Be Vietnam Pro** (hỗ trợ cả hai)

Sau khi xác định body font, chọn thêm 1 display font kết hợp dựa trên cảm giác cần truyền:

| Cảm giác | Body font | Display font kết hợp |
|---|---|---|
| Hiện đại, chuyên nghiệp | Be Vietnam Pro / Inter | Syne, Space Grotesk |
| Thân thiện, gần gũi | Be Vietnam Pro / Inter | Plus Jakarta Sans, Nunito |
| Sang trọng, cao cấp | Be Vietnam Pro / Inter | DM Serif Display, Playfair Display |
| Sáng tạo, cá tính | Be Vietnam Pro / Inter | Clash Display, Cabinet Grotesk |
| Đáng tin, truyền thống | Be Vietnam Pro / Inter | Merriweather, Lora |

Display font dùng cho H1, H2. Body font dùng cho H3 trở xuống, paragraph, UI.

---

**2. SIZE SCALE**


Base font size mặc định: **16px** (người dùng có thể chỉ định giá trị khác).

Toàn bộ scale tính theo tỉ lệ nhân từ base, dùng CSS variable `--font-base`:

| Token | Tỉ lệ | Công thức | Mặc định (base=16px) | Dùng cho |
|---|---|---|---|---|
| xs | ×0.75 | base × 0.75 | 12px | Caption, label nhỏ |
| sm | ×0.875 | base × 0.875 | 14px | Secondary text |
| base | ×1 | base | 16px | Body text |
| lg | ×1.125 | base × 1.125 | 18px | Lead paragraph |
| xl | ×1.5 | base × 1.5 | 24px | H4, H3 |
| 2xl | ×2 | base × 2 | 32px | H2 nhỏ |
| 3xl | ×3 | base × 3 | 48px | H2 chính |
| 4xl | ×4 | base × 4 | 64px | H1 hero |

Khi người dùng đổi base thành 18px thì toàn bộ scale tự cập nhật theo, không cần chỉnh từng giá trị.

---

**3. LINE HEIGHT**

| Font size | Hệ số |
|---|---|
| >=20px | 1.25 |
| < 20px | 1.5 |

**Letter Spacing:** Cố định 0px cho tất cả, không ngoại lệ.

---

**4. COLOR SYSTEM**

Input cần có: 1 màu chủ đạo (primary). Nếu không có, chọn theo ngành (bảng bên dưới).

Từ primary, tự động xây color palette theo nguyên tắc màu kinh điển:

| Nguyên tắc | Khi nào dùng | Cách tạo |
|---|---|---|
| Monochromatic | Brand mạnh, muốn nhất quán | Chỉ dùng primary, tạo các tint/shade (10%, 20%, 40%, 60%, 80%) |
| Complementary | Cần 1 accent nổi bật cho CTA | Xoay 180° trên color wheel |
| Analogous | Cảm giác hài hòa, tự nhiên | Lấy 2 màu liền kề ±30° trên color wheel |
| Triadic | Creative, cá tính, đa dạng | Lấy 2 màu cách đều 120° |

Ngoài primary palette, luôn cần thêm:
- **Neutral scale:** 5 mức — 900 (text chính), 700 (text phụ), 400 (placeholder), 100 (border), 50 (surface)
- **Semantic:** Success #10B981, Warning #F59E0B, Error #EF4444 — cố định, không đổi theo ngành

Nếu không có primary color từ input, chọn theo ngành:

| Ngành | Primary gợi ý |
|---|---|
| SaaS / Tech | #6366F1 |
| Health / Medical | #10B981 |
| Finance / Legal | #2563EB |
| Beauty / Lifestyle | #F43F5E |
| Education | #3B82F6 |
| Food / Restaurant | #F97316 |
| Real Estate | #059669 |
| Creative / Agency | #8B5CF6 |

---

**5. GRID SYSTEM**

Cố định 12-column grid.

| Breakpoint | Container width | Gutter |
|---|---|---|
| Mobile < 768px | 100%, padding 16px | 16px |
| Tablet 768–1024px | 100%, padding 32px | 24px |
| Desktop > 1024px | max-width 1280px, auto margin | 32px |

---

**6. SPACING — GAP SYSTEM**

Base unit 4px, phát triển theo dãy tăng dần:

| Value | Dùng cho |
|---|---|
| 4px | Khoảng cách tối thiểu, icon + label inline |
| 8px | Padding nhỏ trong component (badge, tag) |
| 12px | Khoảng cách giữa các form field |
| 16px | Padding trong component (button, input) |
| 24px | Gap giữa các element trong cùng 1 group |
| 32px | Gap giữa các component khác nhau, Card padding nhỏ |
| 36px | Card padding chuẩn |
| 48px | Gap giữa các sub-section |
| 60px | Gap giữa các section lớn, display gap |

---

**7. SECTION PADDING**

| Device | Padding top/bottom |
|---|---|
| Desktop | 30px – 80px (hero và CTA section dùng 80px, section thông thường 48–64px) |
| Mobile | 30px – 50px |

**Section Spacing — khoảng cách dọc giữa các content block lớn:** cố định 40px–60px.

---

**8. BORDER RADIUS**

Thang cố định, áp dụng theo loại thành phần:

| Value | Dùng cho |
|---|---|
| 0px | Standard input |
| 3px | Divider, tag nhỏ |
| 3.75px | Badge, chip |
| 15px | Rounded input, Secondary button |
| 20px | Service card, Primary button |
| 25px | Default container, featured card |
| 40px | Large decorative container |
| 50% | Avatar, icon tròn |
| 100px | Pill button, tag lớn |

---

**9. BUTTON STYLE**

| Loại | Border radius | Kích thước tham chiếu |
|---|---|---|
| Primary | 20px | height 48–56px, padding 16–24px |
| Secondary | 15px | height 44–48px, padding 14–20px |
| Ghost / tròn | 50%, width = height = 60px | icon centered |

---

**10. CARD STYLE**

- Border radius: 20px (service card) hoặc 25px (featured/default container)
- Không dùng border
- Padding nội bộ: 32px–36px
- Shadow: Elevation 2 (xem mục 11)

---

**11. SHADOW — 4 CẤP ELEVATION**

| Cấp | CSS | Dùng cho |
|---|---|---|
| Elevation 1 | 0 2px 8px rgba(0,0,0,0.06) | Nút nổi, badge |
| Elevation 2 | 0 4px 16px rgba(0,0,0,0.08) | Card mặc định |
| Elevation 3 | 0 8px 28px rgba(0,0,0,0.12) | Card hover |
| Elevation 4 | 0 16px 48px rgba(0,0,0,0.16) | Dropdown, modal |

---

**12. ANIMATION**

Dùng **AOS (Animate On Scroll)** cho tất cả animation scroll-based. Nguyên tắc:

| Loại | Class/Attribute | Giá trị khuyên dùng |
|---|---|---|
| Entrance (fade + slide up) | `data-aos="fade-up"` | `data-aos-duration="600" data-aos-easing="ease-out"` |
| Hover transition (CSS) | - | `150ms ease` |
| Section reveal | `data-aos="fade-in"` | `data-aos-duration="800" data-aos-easing="ease-out"` |

Stagger các element trong cùng 1 group: Sử dụng thuộc tính `data-aos-delay="50"`, `data-aos-delay="100"`, `data-aos-delay="150"`... giữa các item.
