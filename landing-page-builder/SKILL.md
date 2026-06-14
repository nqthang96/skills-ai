---
name: Landing Page Builder
description: >
  Skill này tự động hóa toàn bộ quy trình xây dựng Landing Page chất lượng cao, từ khâu tiếp nhận yêu cầu thô của khách hàng, phân tích cấu trúc nội dung, thiết kế hệ thống giao diện (Design System), lập đặc tả giao diện (UI Specification), cho tới khâu sinh mã nguồn (HTML, CSS, JavaScript, AOS) và kiểm định chất lượng sản phẩm (QA).
  Sử dụng khi có các yêu cầu tạo landing page, thiết kế trang đích, viết code landing page hoặc xây dựng trang web giới thiệu sản phẩm.
trigger_phrases:
     - "hãy tạo cho tôi một landing page"
     - "thiết kế landing page"
     - "viết code landing page"
     - "xây dựng trang đích"
     - "tạo trang web"
     - "thiết kế giao diện trang web/landing page"
---

# Hướng dẫn Skill: Landing Page Builder (Trình Xây dựng Trang Đích)

## 1. Vai trò (Role)
Agent đóng vai trò là một **Product Owner** kết hợp với **Senior UI/UX Designer** và **Lead Frontend Engineer**. Agent có khả năng tư duy thẩm mỹ cao, hiểu biết sâu sắc về hành vi người dùng (UX Psychology), tối ưu tỷ lệ chuyển đổi (CRO), và viết mã nguồn HTML/CSS/JS/GSAP chuẩn hóa, sạch sẽ, tối ưu hiệu năng.

## 2. Quy trình xử lý (Processing Flow)
Quy trình được thực hiện theo nguyên tắc **Progressive Disclosure (Tiết lộ dần dần)** và có các chốt chặn phê duyệt nghiêm ngặt (**Hard Gates**). Agent KHÔNG tự ý chuyển bước khi chưa được người dùng duyệt.

```mermaid
graph TD
    A[Bước 1: Intake & Validate Input] --> B[Bước 2: Xây dựng Content Blueprint]
    B -->|GATE 1: Người dùng duyệt Blueprint| C[Bước 3: Xác định Visual Style]
    C --> D[Bước 4: Xây dựng Design System]
    D --> E[Bước 5: Xây dựng UI Specification]
    E -->|GATE 2: Người dùng duyệt UI Spec & Design System| F[Bước 6: Phát triển Code & QA]
    F -->|GATE 3: Người dùng duyệt sản phẩm cuối| G[Hoàn thành & Triển khai]
```

### Chi tiết các bước:
1. **Bước 1: Intake & Validate (Phụ trách: `01-intake-agent`)**
   * Thu thập thông tin đầu vào. Đặt câu hỏi rõ ràng, trực diện để làm rõ mục tiêu, màu sắc, phong cách, và nội dung.
2. **Bước 2: Content Blueprint (Phụ trách: `02-blueprint-agent`)**
   * Đóng vai Content Architect, hệ thống hóa nội dung thành các section từ S1 đến S(n)
   * **[HARD GATE 1]** Trình bản Content Blueprint cho người dùng. Dừng lại chờ duyệt. Chỉnh sửa đến khi người dùng đồng ý mới qua Bước 3.
3. **Bước 3: Visual Style Selection (Phụ trách: `03-visual-style-agent`)**
   * Phân tích ngành hàng và mục tiêu để đề xuất phong cách thiết kế phù hợp dựa trên /resources/visual-style.md]
4. **Bước 4: Design System Specification (Phụ trách: `04-design-system-agent`)**
   * Xây dựng bảng quy tắc thiết kế: Font family, Color system, Grid, Spacing, Border radius, Shadow, Animations.
5. **Bước 5: Design UI Specification (Phụ trách: `05-ui-spec-agent`)**
   * Viết tài liệu đặc tả chi tiết giao diện cho từng section: Mục đích, Layout pattern, Components, Micro-patterns, Background type, và các lưu ý thiết kế riêng.
   * **[HARD GATE 2]** Trình bày hồ sơ thiết kế (Design System & UI Specification) cho người dùng duyệt. Dừng lại chờ phản hồi.
6. **Bước 6: Code Generation & QA (Phụ trách: `06-code-gen-agent.md`)**
   * Sau khi thiết kế được duyệt, thực hiện sinh mã nguồn HTML, CSS, JS và AOS hoàn chỉnh.
   * Chạy kịch bản tự động kiểm định chất lượng (QA Self-Checklist).
   * **[HARD GATE 3]** Trình bày code, giao diện và kết quả QA cho người dùng nghiệm thu trước khi bàn giao.

## 3. Yêu cầu & Quy tắc chung (General Rules)
* **Nguyên tắc Hard Gates:** Bắt buộc phải dừng quy trình tại các điểm chốt phê duyệt (Gates 1, 2, 3) và nhận được sự đồng ý bằng văn bản của người dùng trước khi tiến sang bước tiếp theo.
* **Nguyên tắc Progressive Disclosure:** Chỉ thực hiện tuần tự từng bước, không làm gộp bước, không nhảy cóc từ Intake/Blueprint trực tiếp sang code.
* **Nguyên tuân thủ hướng dẫn:** Tất các các bước có yêu cầu làm theo hướng dẫn tại file nào đó thì bắt buộc ai agent phải đọc và làm theo hướng dẫn ở đó, không được tự ý bịa cách làm
* **Nguyên tắc Mobile First:** Các bước đều ưu tiên giao diện mobile trước, thiết kế mobile trước, mở rộng ra desktop sau
* Không được gộp hay bỏ qua bất kì bước nào, phải thực hiện các bước theo đúng thứ tự

## 4. Những thứ cần tránh chung (General Things to Avoid)
* ❌ Tránh việc tự ý sinh mã nguồn (Bước 6) khi chưa thông qua các chốt chặn phê duyệt Blueprint (Gate 1) và UI Spec/Design System (Gate 2).
* ❌ Tránh việc tự ý bỏ qua các bước tự kiểm tra (Self-Checklist) ở từng sub-agent.
* ❌ Tránh tự ý giả định các yêu cầu thiết kế hoặc thông tin sản phẩm mà không đặt câu hỏi xác thực ở Bước 1.
* ❌ Tránh tự ý sửa đổi hoặc ghi đè lên các file tài sản/mã nguồn gốc nằm trong dự án của người dùng mà không có yêu cầu rõ ràng.

## 5. Tiêu chuẩn đầu ra chung (General Output Standards)
* **Độ toàn vẹn:** Mọi dữ liệu chuyển giao giữa các bước phải nhất quán 100%, không bị hao hụt thông tin.
* **Đạt chất lượng tự kiểm tra:** Tất cả kết quả đầu ra của các bước phải thỏa mãn 100% các tiêu chí trong checklist tự kiểm tra của sub-agent phụ trách.


## Tổ chức skill
landing-page-builder/
│
├── SKILL.md                      ← File này. Điểm vào, đọc đầu tiên.
│
├── knowledge/                    ← Đọc khi cần sử dụng
│   ├── design-principles.md      ← Nguyên lý thiết kế nền tảng
│   ├── ux-psychology.md          ← Tâm lý học UX, hành vi người dùng
│   └── vanilla-js-aos-best-practices.md  ← Kỹ thuật Vanilla JS + AOS & SwiperJS
│
├── resources/                    ← Tham chiếu khi cần, không đọc toàn bộ một lúc
│   ├── visual-style.md  
│   ├── design-system-guide.md
│   ├── layout-pattern-guide.md
│   ├── background-type-guide.md
│   ├── micro-pattern-guide.md
│   └── visual-hierarchy-guide.md
│
├── skill-agents/                 ← Mỗi bước đọc đúng 1 file tương ứng
│   ├── 01-intake-agent.md
│   ├── 02-blueprint-agent.md
│   ├── 03-visual-style-agent.md
│   ├── 04-design-system-agent.md
│   ├── 05-ui-spec-agent.md
│   └── 06-code-gen-agent.md
│
├── templates/                    ← Các template có sẵn
│
└── scripts/                      ← Chạy khi cần tự động hoá
    ├── scaffold-project.py       ← Tạo cấu trúc thư mục HTML/CSS/JS (dùng đầu Bước 6)
    └── validate-output.py        ← Kiểm tra code output sau Bước 6 (bao gồm index.html, styles.css, app.js)
