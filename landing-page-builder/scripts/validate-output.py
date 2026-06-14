#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
validate-output.py
------------------
Kiểm định chất lượng mã nguồn đầu ra trước khi chuyển cho con người duyệt.
Kiểm tra cấu trúc tệp tin Vanilla (index.html, styles.css, app.js), các quy chuẩn đặt tên ảnh, SEO và các liên kết CDN cần thiết (GSAP, ScrollTrigger, Lucide).
"""

import os
import sys
import re

# Đảm bảo in ký tự Unicode tiếng Việt không bị lỗi trên terminal Windows
if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def check_seo_and_structure(project_dir):
    """Kiểm tra cấu trúc tệp tin và các tiêu chuẩn SEO/CDN cơ bản."""
    errors = []
    warnings = []
    
    # 1. Kiểm tra sự tồn tại của các tệp quan trọng
    critical_files = [
        "index.html",
        "styles.css",
        "app.js"
    ]
    
    for f in critical_files:
        path = os.path.join(project_dir, f)
        if not os.path.exists(path):
            errors.append(f"Thiếu file quan trọng: {f}")

    # 2. Quét file index.html để check SEO và các liên kết CDN/Script
    index_path = os.path.join(project_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Kiểm tra sự tồn tại của tiêu đề và meta
        if "<title>" not in html:
            warnings.append("Cảnh báo: Thiếu thẻ <title> thiết lập tiêu đề trang.")
        if 'name="description"' not in html and 'name=\'description\'' not in html:
            warnings.append("Cảnh báo: Thiếu thẻ meta description phục vụ SEO.")
            
        # Kiểm tra thẻ h1 (mỗi trang chỉ nên có duy nhất 1 thẻ h1)
        h1_count = len(re.findall(r"<h1[\s>]", html))
        if h1_count == 0:
            warnings.append("Cảnh báo: Không tìm thấy thẻ <h1> trên trang.")
        elif h1_count > 1:
            warnings.append(f"Cảnh báo: Phát hiện {h1_count} thẻ <h1>. Tiêu chuẩn SEO yêu cầu tối đa 1 thẻ <h1> mỗi trang.")

        # Kiểm tra liên kết stylesheet styles.css
        if "styles.css" not in html:
            errors.append("Lỗi: Chưa liên kết file styles.css trong index.html")
            
        # Kiểm tra liên kết app.js
        if "app.js" not in html:
            errors.append("Lỗi: Chưa liên kết file app.js trong index.html")

        # Kiểm tra CDN AOS
        if "aos" not in html.lower():
            warnings.append("Cảnh báo: Không tìm thấy liên kết stylesheet/script AOS (Cần thiết cho hiệu ứng).")
 
        # Kiểm tra CDN Tailwind CSS
        if "tailwindcss" not in html.lower():
            warnings.append("Cảnh báo: Không tìm thấy liên kết script CDN Tailwind CSS.")

        # Kiểm tra CDN Lucide
        if "lucide" not in html:
            warnings.append("Cảnh báo: Không tìm thấy liên kết script Lucide Icons (Cần thiết cho biểu tượng).")
    else:
        errors.append("Không tìm thấy trang chính: index.html")

    return errors, warnings

def check_images(project_dir):
    """Kiểm tra quy chuẩn đặt tên hình ảnh trong thư mục assets/images."""
    errors = []
    image_dir = os.path.join(project_dir, "assets/images")
    
    if os.path.exists(image_dir):
        files = os.listdir(image_dir)
        pattern = r"^s\d+_[a-z0-9_]+\.(jpg|jpeg|png|gif|svg|webp)$"
        for f in files:
            # Bỏ qua các file ẩn hệ thống
            if f.startswith('.'):
                continue
            if not re.match(pattern, f):
                errors.append(f"Tên file ảnh sai định dạng quy chuẩn: {f} (Yêu cầu dạng: s[section]_[name]_[index].[ext])")
    else:
        errors.append("Không tìm thấy thư mục lưu trữ ảnh: assets/images")
        
    return errors

def main():
    project_dir = sys.argv[1] if len(sys.argv) > 1 else "./vanilla-landing-page"
    project_dir = os.path.abspath(project_dir)

    print("==================================================")
    print(f"[*] ĐANG BẮT ĐẦU CHẠY KIỂM ĐỊNH QA DỰ ÁN TẠI:\n    {project_dir}")
    print("==================================================")

    if not os.path.exists(project_dir):
        print(f"[-] Lỗi: Thư mục dự án không tồn tại: {project_dir}")
        sys.exit(1)

    errors_seo, warnings_seo = check_seo_and_structure(project_dir)
    errors_img = check_images(project_dir)

    all_errors = errors_seo + errors_img
    all_warnings = warnings_seo

    # Xuất kết quả
    if all_warnings:
        print("\n[!] CÁC CẢNH BÁO PHÁT HIỆN:")
        for w in all_warnings:
            print(f"    ⚠️  {w}")

    if all_errors:
        print("\n[-] PHÁT HIỆN CÁC LỖI TIÊU CHUẨN (Cần sửa):")
        for e in all_errors:
            print(f"    ❌  {e}")
        print("\n[!] Kết luận: KIỂM ĐỊNH THẤT BẠI. Hãy sửa lỗi trên trước khi đưa cho con người duyệt.")
        sys.exit(1)
    else:
        print("\n[+] Kết luận: KIỂM ĐỊNH THÀNH CÔNG! Dự án đạt đủ các tiêu chuẩn chất lượng tự động.")
        sys.exit(0)

if __name__ == "__main__":
    main()
