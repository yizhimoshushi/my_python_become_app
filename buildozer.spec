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
# 1. 移除了 sdl2 和 hostpython3 (它们不是 pip 包，会导致参数解析错误)
# 2. 确保没有包含任何 -dev 或非法字符
requirements = python3, pygame

# (str) 图标 (如果有的话，取消注释)
# icon.filename = %(source.dir)s/icon.png

# (list) Android 权限
android.permissions = INTERNET,VIBRATE

# (str) 屏幕方向
# portrait (竖屏) 或 landscape (横屏)
android.orientation = landscape

# --- 2026 年兼容性配置 ---
# 使用较新的 NDK 版本 (25b) 以支持现代编译器
android.ndk = 25b

# Android API 级别
android.api = 34
android.minapi = 21

# (str) 语言区域
ios.kivy_ios_dir =
ios.multiarch_dirs =

# (list) KivyMD 等资源 (如果需要)
# kivy.deps = 

# (list) 额外的 Android 源文件
# android.add_src =

# (str) 资产目录 (如果需要将文件打包进 APK)
# android.add_assets =

# (list) 引导程序
# android.bootstrap = pygame

[buildozer]

# (int) 日志级别 (0 = error, 1 = warning, 2 = info, 3 = debug)
log_level = 2

# (str) 设置编译目标目录
bin_dir = 

[app]

# (str) 应用包分类
android.category = Game

# (list) Android 软件包依赖
# android.add_jar =
# android.add_aar =

# (str) Android NDK API (仅用于特定情况)
# android.ndk_api =
