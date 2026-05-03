[app]

# 应用基本信息
title = Pygame Test
package.name = pygametest
package.domain = org.example

source.dir = .
source.include_exts = py

# 入口文件（非常重要）
requirements = python3,pygame==2.5.2

orientation = portrait
osx.python_version = 3

fullscreen = 1
show_status_bar = 0

# Android 专用
android.permissions = VIBRATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# 关闭不需要的功能（减少体积 & 报错）
p4a.branch = develop
p4a.local_recipes =

# SDL / pygame 设置
[buildozer]
log_level = 2
warn_on_root = 1
