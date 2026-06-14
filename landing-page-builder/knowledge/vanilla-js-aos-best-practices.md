# Thực hành kỹ thuật tốt nhất (Vanilla JS, AOS, CSS Best Practices)
 
Tài liệu này định nghĩa các tiêu chuẩn lập trình frontend mà Agent phải tuân thủ khi sinh mã nguồn Vanilla HTML/CSS/JS cho Landing Page ở Bước 6.
 
---
 
## 1. Cấu trúc và Tổ chức Dự án
* **HTML5 Semantic:** Sử dụng đầy đủ các thẻ semantic như `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<aside>`.
* **CSS Bố cục:** Sử dụng các class tiện ích của Tailwind CSS cho toàn bộ bố cục (Flexbox, Grid, spacing). Hạn chế tối đa viết CSS thủ công trong `styles.css`.
* **Nội dung nhúng (Embedded Content):** Dữ liệu chữ, số lượng đếm ngược và nhãn nút phải được viết trực tiếp trong tệp `index.html`. Không cần tạo tệp dữ liệu trung gian.
 
---
 
## 2. Tích hợp AOS (Animate On Scroll)
AOS được khuyên dùng để tạo hiệu ứng xuất hiện khi cuộn trang vì tính ổn định cao, nhẹ và dễ bảo trì.
* **Cú pháp chuẩn hóa:**
  - Nhúng stylesheet AOS CSS trong thẻ `<head>`:
    ```html
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    ```
  - Nhúng script AOS JS ngay trước thẻ đóng `</body>`:
    ```html
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    ```
  - Khởi tạo thư viện trong `app.js` sau khi DOM tải xong:
    ```javascript
    document.addEventListener("DOMContentLoaded", () => {
        if (typeof AOS !== 'undefined') {
            AOS.init({
                duration: 800,       // Thời gian chạy hiệu ứng (ms)
                once: true,          // Hiệu ứng chỉ chạy một lần khi cuộn qua
                easing: 'ease-out-quad', // Kiểu chuyển động mượt mà
                offset: 120          // Khoảng cách kích hoạt hiệu ứng trước khi phần tử xuất hiện (px)
            });
        }
    });
    ```
* **Sử dụng trong HTML:**
  - Gán thuộc tính `data-aos` trực tiếp lên thẻ HTML cần hiệu ứng (Ví dụ: `fade-up`, `fade-in`, `slide-right`...).
  - Thiết lập thời gian trễ cho các phần tử nối tiếp nhau (stagger) bằng thuộc tính `data-aos-delay` (Ví dụ: `100`, `200`, `300`...).
 
---
 
## 3. Tích hợp SwiperJS (Cho Slider/Carousel)
Nếu dự án yêu cầu Slider (ví dụ: Testimonials hoặc hình ảnh sản phẩm), sử dụng **SwiperJS** thay vì tự viết logic JS phức tạp.
* **Liên kết CDN:**
  ```html
  <!-- Head -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
  <!-- Body Close -->
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  ```
* **Khởi tạo cơ bản:**
  ```javascript
  const swiper = new Swiper('.swiper-container', {
      loop: true,
      autoplay: { delay: 5000 },
      pagination: { el: '.swiper-pagination', clickable: true },
      navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
  });
  ```
 
---
 
## 4. Xử lý Form và gửi dữ liệu về Google Sheets
Để thu thập thông tin đăng ký tư vấn/mua hàng và lưu vào Google Sheets, tuân thủ các quy tắc sau:
* **Sử dụng Fetch API (JS thuần):** Gửi dữ liệu không đồng bộ để tránh tải lại trang web, nâng cao trải nghiệm người dùng.
* **Trạng thái UI trực quan:**
  - Khi đang gửi: Vô hiệu hóa nút Submit (`disabled`), thay đổi text thành "ĐANG XỬ LÝ..." hoặc hiển thị loader.
  - Khi thành công: Hiển thị thông báo thành công dạng hộp thoại/nền xanh kèm icon check, reset form.
  - Khi gặp lỗi: Hiển thị thông báo lỗi rõ ràng để người dùng thử lại.
* **Mẫu Code gửi AJAX:**
  ```javascript
  const form = document.getElementById("order-form");
  const statusMsg = document.getElementById("status-message");
  const submitBtn = document.getElementById("submit-btn");
 
  if (form) {
      form.addEventListener("submit", (e) => {
          e.preventDefault();
          const formData = new FormData(form);
          
          // Trạng thái Loading
          submitBtn.disabled = true;
          submitBtn.textContent = "ĐANG GỬI...";
          statusMsg.className = "status-message loading";
          statusMsg.textContent = "Vui lòng chờ giây lát...";
 
          fetch(form.action, {
              method: "POST",
              body: formData,
              mode: "no-cors" // Google Apps Script yêu cầu no-cors để thực thi direct
          })
          .then(() => {
              submitBtn.disabled = false;
              submitBtn.textContent = "ĐĂNG KÝ NGAY";
              statusMsg.className = "status-message success";
              statusMsg.textContent = "Đăng ký thành công! Chuyên gia sẽ liên hệ với bạn sớm nhất.";
              form.reset();
          })
          .catch((error) => {
              console.error("Form error:", error);
              submitBtn.disabled = false;
              submitBtn.textContent = "ĐĂNG KÝ NGAY";
              statusMsg.className = "status-message error";
              statusMsg.textContent = "Gửi thông tin thất bại. Vui lòng kiểm tra lại mạng.";
          });
      });
  }
  ```
 
---
 
## 5. Quản lý Theme động bằng Tailwind Config
* Định nghĩa màu sắc, font chữ, bo góc của dự án trong đối tượng `tailwind.config` inline trực tiếp trong HTML:
  ```html
  <script>
      tailwind.config = {
          theme: {
              extend: {
                  colors: {
                      primary: {
                          DEFAULT: '#029695',
                          hover: '#016a69',
                      },
                      secondary: {
                          DEFAULT: '#ea580c',
                      }
                  },
                  borderRadius: {
                      'card': '20px',
                  }
              }
          }
      }
  </script>
  ```
* Sử dụng các cấu hình này trực tiếp qua các class Tailwind: `bg-primary`, `hover:bg-primary-hover`, `text-secondary`, `rounded-card`.
 
---
 
## 6. Tải Icons hiệu quả
* **Lucide Icons via CDN:** Nhúng script CDN Lucide trong file HTML:
  ```html
  <script src="https://unpkg.com/lucide@latest"></script>
  ```
* **Khởi tạo Icons:** Sau khi HTML tải xong, gọi hàm khởi tạo trong `app.js` để render các icon tự động thông qua thuộc tính `data-lucide`:
  ```javascript
  document.addEventListener("DOMContentLoaded", () => {
    lucide.createIcons();
  });
  ```
