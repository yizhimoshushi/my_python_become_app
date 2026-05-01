[app]
# 应用标题
title = My Pygame App
# 包名 (必须是小写字母和数字，不能有空格)
package.name = mypygameapp
# 域名 (随意写，但要符合规范)
package.domain = org.test

# 源码目录 (就是当前目录)
source.dir = .
# 包含的文件类型
source.include_exts = py,png,jpg,kv,atlas

# 版本号
version = 0.1

# 核心配置：告诉 Buildozer 我们需要 pygame 和 pgs4a
# 注意：这里不是 kivy，而是 pygame
requirements = python3,pygame,pgs4a

# 权限 (比如震动、网络等，按需开启)
android.permissions = INTERNET,VIBRATE

# 屏幕方向
android.orientation = landscape
