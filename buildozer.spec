[app]

# (str) 应用标题
title = My Pygame App

# (str) 包名
package.name = mypygameapp

# (str) 包域名
package.domain = org.test

# (list) 源码目录
source.dir = .

# (list) 包含的文件扩展名
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) 版本号
version = 0.1

# --- 关键修复点 ---
# 1. 使用稳定版 pygame (2.4.0)
# 2. 移除非法字符和 -dev 包
requirements = python3,pygame==2.4.0

# (str) 图标 (如果有的话，取消注释)
# icon.filename = %(source.dir)s/icon.png

# (list) Android 权限
android.permissions = INTERNET,VIBRATE

# (str) 屏幕方向
# portrait (竖屏) 或 landscape (横屏)
android.orientation = landscape

# --- 2026 年兼容性配置 ---
# 使用稳定版 NDK (r23.2) 而不是 r25b
android.ndk = 23.2.8568313

# Android API 级别
android.api = 34
android.minapi = 21
android.ndk_api = 21

# 强制使用 develop 分支的 python-for-android
p4a.branch = develop

[buildozer]

# (int) 日志级别 (0 = error, 1 = warning, 2 = info, 3 = debug)
log_level = 2

# (str) 设置编译目标目录
bin_dir = bin

# (list) 额外的构建参数
# android.add_compile_options = 
