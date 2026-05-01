[app]
# 应用标题
title = My Pygame App
# 包名 (必须是小写字母和数字)
package.name = mypygameapp
# 域名
package.domain = org.test

# 源码目录
source.dir = .
# 包含的文件类型
source.include_exts = py,png,jpg,kv,atlas

# 版本号
version = 0.1

# --- 重点修改这里 ---
# 1. 必须加上 hostpython3，否则编译报错
# 2. 暂时去掉 pgs4a，只保留 pygame。
#    注意：Pygame 在安卓上支持有限，如果这个不行，后面必须换 Kivy。
requirements = python3,hostpython3,pygame,sdl2

# 权限
android.permissions = INTERNET,VIBRATE

# 屏幕方向 (建议先设为竖屏 portrait，方便测试)
android.orientation = portrait

# --- 建议加上这个，指定 NDK 版本，避免版本不兼容 ---
android.ndk = 17c
