[app]
title = SuperTrader
package.name = supertrader
package.domain = com.supertrader.app
source.dir = .
version = 0.1
requirements = python3,kivy==2.3.0,Pillow
orientation = portrait

[buildozer]
log_level = 2

[app:android]
permissions = INTERNET
p4a.fork = kivy
p4a.branch = master
android.api = 33
android.minapi = 21
android.accept_sdk_license = True
android.ndk = 25b
