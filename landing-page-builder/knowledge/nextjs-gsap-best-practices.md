# Thực hành kỹ thuật tốt nhất (Next.js, GSAP, Tailwind Best Practices)

Tài liệu này định nghĩa các tiêu chuẩn lập trình frontend mà Agent phải tuân thủ khi sinh mã nguồn Next.js cho Landing Page ở Bước 6.

---

## 1. Cấu trúc Component trong Next.js
* **Tính độc lập & Tái sử dụng:** Mỗi section ($S_1 \rightarrow S_n$) nên được tách thành một component riêng biệt nằm trong thư mục `components/sections/` (Ví dụ: `components/sections/Hero.js`, `components/sections/Features.js`).
* **Dữ liệu tách biệt (Clean Separation of Concerns):**
  * Tuyệt đối không hardcode text trực tiếp vào các file component.
  * Mọi nội dung text, link ảnh, nhãn nút (CTA label), và biểu tượng (icon key) phải được đọc từ file tập trung `data/contentData.json`.
  * Điều này cho phép dễ dàng thay đổi ngôn ngữ, nội dung mà không cần can thiệp vào cấu trúc code React.

---

## 2. Tối ưu hóa GSAP và ScrollTrigger
GSAP ScrollTrigger rất mạnh mẽ nhưng nếu không được tối ưu sẽ dễ gây giật lag (jank) hoặc rò rỉ bộ nhớ (memory leaks).
* **Khởi tạo đúng cách trong React:**
  * Luôn sử dụng `useRef` để tham chiếu đến các phần tử DOM cần chuyển động. Không dùng bộ chọn query selector toàn cục (`document.querySelector`).
  * Sử dụng hook `useIsomorphicLayoutEffect` (hoặc `useEffect` thông thường nếu chạy Client-side) kết hợp với `gsap.context()` để gom nhóm các hiệu ứng và dọn dẹp (clean up) bộ nhớ khi component bị unmount.
* **Cú pháp chuẩn hóa:**
  ```javascript
  import { useEffect, useRef } from 'react';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/dist/ScrollTrigger';

  gsap.registerPlugin(ScrollTrigger);

  export default function FeatureSection({ data }) {
    const containerRef = useRef(null);

    useEffect(() => {
      let ctx = gsap.context(() => {
        gsap.from(".animate-item", {
          opacity: 0,
          y: 50,
          stagger: 0.1,
          duration: 0.8,
          ease: "power2.out",
          scrollTrigger: {
            trigger: containerRef.current,
            start: "top 80%", // Kích hoạt khi đỉnh của container chạm 80% chiều cao viewport
            toggleActions: "play none none reverse"
          }
        });
      }, containerRef); // Scopes selectors to containerRef

      return () => ctx.revert(); // Dọn dẹp sạch sẽ chuyển động khi unmount
    }, []);

    return (
      <section ref={containerRef} className="py-24">
        <h2 className="animate-item">{data.title}</h2>
        <p className="animate-item">{data.subtitle}</p>
      </section>
    );
  }
  ```
* **Lưu ý hiệu năng:**
  * Tránh chuyển động các thuộc tính gây tính toán lại bố cục (layout reflow) như `width`, `height`, `top`, `left`, `margin`.
  * Chỉ nên chuyển động các thuộc tính được tối ưu hóa phần cứng (GPU accelerated) như `transform` (`x`, `y`, `scale`, `rotation`) và `opacity`.

---

## 3. Tailwind CSS & Inline Style cho CSS Variables
* **Kết hợp linh hoạt:** Sử dụng Tailwind CSS cho các thuộc tính layout, spacing, flexbox, grid cơ bản. 
* **Quản lý Theme động:** Đối với các giá trị màu sắc chủ đạo được cấu hình động bởi người dùng (ở Design System), sử dụng inline style để gán CSS Variables ở cấp thẻ bọc ngoài cùng (wrapper), sau đó dùng Tailwind class tương tác với các biến đó.
  * *Ví dụ:*
    ```javascript
    // Component wrapper
    const themeStyles = {
      '--color-primary': designSystem.colors.primary,
      '--color-primary-hover': designSystem.colors.primaryHover,
      '--radius-button': designSystem.borderRadius.button,
    };

    return (
      <div style={themeStyles} className="theme-wrapper">
        <button className="bg-[var(--color-primary)] hover:bg-[var(--color-primary-hover)] rounded-[var(--radius-button)] px-6 py-3 text-white transition-colors">
          Click Me
        </button>
      </div>
    );
    ```

---

## 4. Tải Icons và Assets hiệu quả
* **Lucide Icons qua CDN hoặc Import:** Nếu dự án dùng Next.js thông thường, khuyến khích import trực tiếp từ package `lucide-react`. Nếu yêu cầu tải động thông qua CDN, hãy đảm bảo cơ chế fallback hiển thị mượt mà, không bị nhấp nháy giao diện khi chưa tải xong thư viện.
* **Tải trước hình ảnh quan trọng (Preloading):** Đối với các ảnh nền hoặc ảnh banner chính trong vùng Above the fold (Hero section), hãy sử dụng thẻ `<Image priority />` của Next.js để tải trước hình ảnh, tránh gây ảnh hưởng xấu đến điểm số LCP (Largest Contentful Paint).
