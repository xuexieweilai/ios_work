# 第一部分
## 一 、前提准备条件
1. MacOs
2. Xcode（建议更新为最新版本）
3. npm
4. carthage

###### 安装npm和Carthage
```
# 安装 node
brew install node
# 查看npm版本
npm -v

6.2.0
  # 安装Carthage:
brew install Carthage

# 如果只是更新请输入
brew upgrade carthage
```
###### 注：如果用brew安装十分的慢，采用国内镜像
```
# 长期替换(建议使用此项配置)  
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles'>>   ~/.bash_profile   

#执行.bash_profile脚本让配置即时生效
source ~/.bash_profile
```
######从github中克隆WebDriverAgent项目
[WebDriverAgent](https://github.com/facebook/WebDriverAgent)
```
git clone https://github.com/facebook/WebDriverAgent
```
*运行初始化脚本
```
# 进入到WDA 根目录
cd WebDriverAgent/

# 运行初始化脚本
./Scripts/bootstrap.sh
```
```
Fetching dependencies
Please update to the latest Carthage version: 0.31.1. You currently are on 0.30.1
*** Checking out RoutingHTTPServer at "v1.0.1"
*** Cloning RoutingHTTPServer
*** xcodebuild output can be found in /var/folders/gf/jjhn56c97293xtjvtwlnwr8h0000gp/T/carthage-xcodebuild.RROZOv.log
*** Downloading RoutingHTTPServer.framework binary at "v1.0.1"
Building Inspector
Creating bundle directory...
Fetching Inspector dependencies...
npm WARN deprecated css-list@0.1.3: Deprecated.
npm WARN deprecated minimatch@2.0.10: Please update to minimatch 3.0.2 or higher to avoid a RegExp DoS issue
npm WARN deprecated browserslist@0.4.0: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.

> fsevents@1.2.4 install /Users/zhan/Desktop/mine/Stu资料/Git/WebDriverAgent/Inspector/node_modules/fsevents
> node install

[fsevents] Success: "/Users/zhan/Desktop/mine/Stu资料/Git/WebDriverAgent/Inspector/node_modules/fsevents/lib/binding/Release/node-v64-darwin-x64/fse.node" already installed
Pass --update-binary to reinstall or --build-from-source to recompile
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN react-dom@15.6.2 requires a peer of react@^15.6.2 but none is installed. You must install peer dependencies yourself.
npm WARN web-driver-inspector@1.0.0 No repository field.

added 759 packages from 536 contributors and audited 2620 packages in 69.318s
found 9 vulnerabilities (4 low, 4 high, 1 critical)
  run `npm audit fix` to fix them, or `npm audit` for details
Validating Inspector
Building Inspector...

> web-driver-inspector@1.0.0 build /Users/zhan/Desktop/mine/Stu资料/Git/WebDriverAgent/Inspector
> webpack --progress --colors

Hash: 0acdc7e8b3b0d143afc5  
Version: webpack 1.15.0
Time: 7085ms
       Asset    Size  Chunks             Chunk Names
inspector.js  862 kB       0  [emitted]  main
   [0] multi main 28 bytes {0} [built]
    + 226 hidden modules
Done
```
# 二、证书配置
1、Xcode打开WebDriverAgent目录下的WebDriverAgent.xcodeproj文件。
(1)按照下面图的步骤依次执行点击，先配置**WebDriverAgentLib**：
![image](https://upload-images.jianshu.io/upload_images/16098398-cd356c46b57ad439.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](https://upload-images.jianshu.io/upload_images/16098398-bbb017ab860eacd9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
(2)按照下面图的步骤依次执行点击，再配置WebDriverAgentRunner：
![image](https://upload-images.jianshu.io/upload_images/16098398-baffaaec9e0ef64d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
但是会提示问题：
*The app ID "com.facebook.WebDriverAgentRunner" cannot be registered to your development team. Change your bundle identifier to a unique string to try again.*

请进入**WebDriverAgentRunner -> Build Settings**设置中，找到Packaging中的选项，将其内容修改为唯一识别的字符串，如下图所示
![image](https://upload-images.jianshu.io/upload_images/16098398-4bb3eca8a0f9af25.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
不报错了：
![image](https://upload-images.jianshu.io/upload_images/16098398-993eda25cad05f43.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 三、运行与测试
1、iphone手机连接Mac，并添加信任
         设置=》通用=》设备管理=》开发者应用=》验证应用

2、选择**Product->Destination->你的设备**
![image](https://upload-images.jianshu.io/upload_images/16098398-123820f9e60a3d0c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3、选择**Product->Scheme->WebDriverAgentRunner**
![image](https://upload-images.jianshu.io/upload_images/16098398-2f5d050521370ef4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

 4、然后进行运行，Product中选择test（快捷键command+ U）
![image](https://upload-images.jianshu.io/upload_images/16098398-972247eeff1edd64.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
 运行后会提示输入密码：
![image](https://upload-images.jianshu.io/upload_images/16098398-29ed0694bfdef402.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**注意：一直输入密码，直到它不提示为止，此密码应该为登录密码。**

但是，运行后创建成功，但是证书有问题。
![image](https://upload-images.jianshu.io/upload_images/16098398-b31285358ee8232f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
*The certificate used to sign "WebDriverAgentRunner-Runner" has either expired or has been revoked. An updated certificate is required to sign and install the application.*

用于签署“WebDriverAgentRunner Runner”的证书已过期或被撤销。需要更新的证书来签署和安装应用程序。

 打开“钥匙串访问”，查看【我的证书】得知，原来是证书过期了。
![image](https://upload-images.jianshu.io/upload_images/16098398-333abdb81b30ac74.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
 右键删除此证书。
![image](https://upload-images.jianshu.io/upload_images/16098398-8ab6f1efe485cc8a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
删除证书后 ，再重新添加，如下图
![image](https://upload-images.jianshu.io/upload_images/16098398-dcdcf7882fb61ebd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

 再次运行Xcode，先删除之前的运行的，**Product->Clean Build Folder**

此时，不出意外 WDA在手机中安装成功，并且下面控制台输出下面的效果。
打开控制台方法：选择view->Debug Area->Activate console打开底部控制台。
![image](https://upload-images.jianshu.io/upload_images/16098398-333abac45eeee95b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
 然后控制台会输出IP地址和端口，例如：http://192.168.0.0:8100/status,输入在浏览器中，

确认WDA是否运行成功。如果出现一串JSON输出，说明WDA安装成功了。
# 四、端口转发
但是可能页面刷新出不来：
```
 使用--HEAD安装最新版本
$ brew install libimobiledevice --HEAD
$ iproxy 8100 8100
```
ps :记录一次安装libimobiledevice的坑：
错误：
1. 断开连接 brew unlinked libimobiledevice
2.l连接： brew linked libimobiledevice
断开之后会报错：
```
==> ./autogen.sh
Last 15 lines from /Users/n/Library/Logs/Homebrew/libimobiledevice/01.autogen.sh:
checking dynamic linker characteristics... darwin18.0.0 dyld
checking how to hardcode library paths into programs... immediate
checking for pkg-config... /usr/local/opt/pkg-config/bin/pkg-config
checking pkg-config is at least version 0.9.0... yes
checking for libusbmuxd >= 1.1.0... no
configure: error: Package requirements (libusbmuxd >= 1.1.0) were not met:

Requested 'libusbmuxd >= 1.1.0' but version of libusbmuxd is 1.0.10

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables libusbmuxd_CFLAGS
and libusbmuxd_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
```
解决办法：
```
brew update
brew uninstall --ignore-dependencies libimobiledevice
brew uninstall --ignore-dependencies usbmuxd
brew install --HEAD usbmuxd
brew unlink usbmuxd
brew link usbmuxd
brew install --HEAD libimobiledevice
```
[解决办法参考]([https://github.com/flutter/flutter/issues/22595](https://github.com/flutter/flutter/issues/22595)
)
end ps

 但是会提示你需要更新：
```
Warning: libimobiledevice HEAD-26373b3_2 is already installed and up-to-date
To reinstall HEAD_3, run `brew reinstall libimobiledevice`
$ brew reinstall libimobiledevice
```
更新后：
**关键**
注意： 项目运行，启动程序的时候是不能让这个命令运行的，会报端口占用的错误。
```
# 运行命令后会显示如下：
$ iproxy 8100 8100
waiting for connection
```
此时浏览器输入：http://localhost:8100/status ，确认WDA是否运行成功。


![image](https://upload-images.jianshu.io/upload_images/16098398-1420f0ec5f8c6c55.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
 而inspector的地址是http://localhost:8100/inspector， inspector是用来查看UI的图层，方便写测试脚本用的
![image](https://upload-images.jianshu.io/upload_images/16098398-27532da2f3228cca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


原文地址：
[[【Mac + Python3.6 + ATX基于facebook-wda】之IOS自动化（一）：WebDriverAgent安装](https://www.cnblogs.com/Owen-ET/p/9792146.html)
]([https://www.cnblogs.com/Owen-ET/p/9792146.html](https://www.cnblogs.com/Owen-ET/p/9792146.html)
)

# 第二部分  记录Macaca和app-inspectoer的使用
##一、环境配置
1. node.js : 版本要求需要9以上
```
# 查看node版本
node -v
# 安装node.js
brew install node
```
2. 安装usbmuxd，一个可以通过USB控制连接，让电脑控制手机的工具
```
brew install usbmuxd
```
3. 安装ideviceinstaller
```
brew install ideviceinstaller
```
4. 应用中如含有 WebView，请安装 [ios-webkit-debug-proxy](https://github.com/google/ios-webkit-debug-proxy)
```
$ brew install ios-webkit-debug-proxy
```
5. 请安装 [macaca-ios](https://github.com/macacajs/macaca-ios) 驱动（安装方法二选一）
```
# 本地安装
$ npm i macaca-ios --save-dev
# 全局安装
$ npm i macaca-ios -g
```
*   在运行的过程中，如果发现问题， 可以在macaca 启动时设置 --verbose 参数， 运行的日志中会显示XCTestWD的[诊断日志信息](https://github.com/macacajs/XCTestWD/blob/master/#43-debug-info).
## ios真机
首先要明白两个概念：

*   Macaca 依赖 `macaca-ios`，而 `macaca-ios` 依赖安装到真机的 `XCTestWD`，所以要确保 Macaca 最终调用的 `XCTestWD` 是安装到真机上的 `XCTestWD`。
*   iOS 真机上的 `XCTestWD` 需要签名(`TEAM_ID`)，且和被测试的app一样。

### [#](https://macacajs.github.io/zh/guide/environment-setup.html#%E9%80%9A%E8%BF%87%E5%AE%89%E8%A3%85-macaca-ios-%E8%87%AA%E5%8A%A8%E9%85%8D%E7%BD%AE-xctestwd%EF%BC%88%E6%8E%A8%E8%8D%90%EF%BC%89)通过安装 macaca-ios 自动配置 XCTestWD（推荐）
```
# 卸载之前安装的 macaca-ios
$ npm uninstall -g macaca-ios

# 安装有 TEAM_ID 的 macaca-ios
$ DEVELOPMENT_TEAM_ID=TEAM_ID npm i macaca-ios -g
```
如果真机中有相应的测试app，参数中app 可不填

######关于 TEAM_ID
如果你不知道你的 TEAM_ID，可以在 XCode 你的项目里设置或找到 TEAM_ID（需要登录Apple账号）。在设置 Development Team 下拉列表里点击Other即可查看当前 TEAM_ID。
![image](https://upload-images.jianshu.io/upload_images/16098398-d426f3e768d688de.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## Android环境
* [安装 JDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)，要求 1.8 （不支持Java 9）
-  配置 JAVA_HOME，根据你所使用的 shell 工具修改不同的文件，比如 ~/.bashrc, ~/.bash_profile, ~/.zshrc
```
# 例如
export JAVA_HOME=path/to/your/Java/Home
# 或
export JAVA_HOME="$(/usr/libexec/java_home -v 1.8)"
```
+ 安装 18-25 版本中的任一 Android SDK 和 Android Support Repository
+ shell 环境设置 ANDROID_HOME，根据你所使用的Terminal修改不同的文件，比如 ~/.bashrc, ~/.bash_profile, ~/.zshrc
```
# 例如
export ANDROID_HOME = /usr/local/opt/android-sdk
# 或
export ANDROID_HOME="/Users/<UserName>/Library/Android/sdk"
```
- 请安装 [gradle](https://gradle.org/) 来构建 [UIAutomatorWD](https://github.com/macacajs/UIAutomatorWD) 和其它依赖包。 ( gradle时更新电脑内全部的的东西，很耗时)
- 可以设置Maven源地址获取更快的安装速度。
```
MAVEN_MIRROR_URL=http://maven.aliyun.com/nexus/content/groups/public/ npm i macaca-android -g
```
请安装 [macaca-android](https://github.com/macacajs/macaca-android) 驱动
```
# 本地安装
npm i macaca-android --save-dev
# 全局安装
npm i macaca-android -g
```
- 准备 App 包：如需要测试 Android 应用，请使用 .apk 格式的包。
- 如果在运行 npm i macaca-android -g 的过程中出现 [You have not accepted the license agreements of the following SDK components]，请执行如下命令(该命令将同意所有的AndroidSDK 协议)后再次执行安装。
```
$ yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses
```
## Desktop 环境
- 如需要测试 Chrome 环境，请安装 [macaca-chrome](https://github.com/macacajs/macaca-chrome) 驱动
```
# 本地安装
npm i macaca-chrome --save-dev
# 全局安装
npm i macaca-chrome -g
```
### 命令行工具

###[#](https://macacajs.github.io/zh/guide/environment-setup.html#%E5%85%A8%E5%B1%80%E5%AE%89%E8%A3%85)全局安装
```
$ npm i -g macaca-cli
```
如果看到如下可爱的🐒，那恭喜你安装成功啦！重新安装则会覆盖更新。
![image](https://upload-images.jianshu.io/upload_images/16098398-c110318d173b3b38.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 环境检查
通过 macaca doctor 可以检查环境是否配置成功
```
 macaca doctor
```
如下图所示则表示环境均配置正常，如果有标红提示，则需要对应处理。
![image](https://upload-images.jianshu.io/upload_images/16098398-08e3e90fd6a0a46e.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 记录一次错误
![image](https://upload-images.jianshu.io/upload_images/16098398-1feb7d13803cdd58.png!large?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 解决方法：
-- 找到环境变量中ANDROID_HOME
```
which android
```
-- 创建license
```
$ mkdir "/Users/.../Library/Android/sdk/licenses"
$ echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > "/Users/.../Library/Android/sdk/licenses/android-sdk-license"
$ echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" > "/Users/.../Library/Android/sdk/licenses/android-sdk-preview-license"
```
## 命令行执行 app-inspector
```
app-inspector -u [udid] --verbose
```
出现下图代表成功了
![image](https://upload-images.jianshu.io/upload_images/2358191-376e5aed90ca7fb3.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)
- 错误二
安装XCTestWD时，XCTestWD会安装到手机上，当时无论怎样都安装不上，最后用
```
# 卸载之前安装的 macaca-ios
$ npm uninstall -g macaca-ios

# 安装有 TEAM_ID 的 macaca-ios
$ DEVELOPMENT_TEAM_ID=TEAM_ID npm i macaca-ios -g
```
重装一遍就好了
- 错误三
输入命令app-inspector -u [udid] --verbose ，浏览器中无法获取手机画面
- 解决办法：
1. 多试几次或者重启终端和手机
2. 出现如图所示，表示启动成功
![屏幕快照 2019-12-11 下午3.28.53.png](https://upload-images.jianshu.io/upload_images/16098398-52af6e812640981d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 错误四
下载的Macaca命令不好使，是因为没有配置环境变量，配置一下环境变量就好了，不知道为什么，下载的默认路径和别人的不一样，找的配环境和找的时候点事情。
```
# 环境变量配置文件
vim .bash_profile
# 修改之后保存并退出，然后执行
source ~/.bash_profile
```
###### 参考文章
- 配置环境变量相关：
[Mac 配置环境变量]([https://www.jianshu.com/p/7e30b7b7ee48](https://www.jianshu.com/p/7e30b7b7ee48)
)
- 配置Macaca环境相关
[Macaca环境配置官方中文文档]([https://macacajs.github.io/zh/guide/environment-setup.html#%E5%AE%89%E8%A3%85-node-js](https://macacajs.github.io/zh/guide/environment-setup.html#%E5%AE%89%E8%A3%85-node-js)
)
[Mac下配置Macaca + APP inspector]([https://www.jianshu.com/p/28d87ef66477](https://www.jianshu.com/p/28d87ef66477)
)
[Macaca搭建中遇到的坑]([https://testerhome.com/topics/12278](https://testerhome.com/topics/12278)
)
# 第三部分 libimobiledevice的安装和常用命令
####1.介绍
libimobiledevice 是一个跨平台的软件库，支持 iPhone®, iPod Touch®, iPad® and Apple TV® 等设备的通讯协议。不依赖任何已有的私有库，不需要越狱。应用软件可以通过这个开发包轻松访问设备的文件系统、获取设备信息，备份和恢复设备，管理 SpringBoard 图标，管理已安装应用，获取通讯录、日程、备注和书签等信息，使用 libgpod 同步音乐和视频。
#### 2.安装方式
```
brew install -HEAD libimobiledevice 
brew install ideviceinstaller  
```
#### 3.常用命令
##### 3.1 查看当前所连接的设备
```
MacBookPro:~ lemon$ idevice_id -l # 显示当前所连接的设备[udid]，包括 usb、WiFi 连接
********c06e788b2d8dc60004a7015ce5dad782
********9a816a4089bd28f4f2e63c57a8138c63

instruments -s devices      # 列出设备包括模拟器、真机及 mac 电脑本身
ideviceinstaller -u [udid] -U [bundleId] # 给指定连接的设备卸载应用
ideviceinstaller -u [udid] -l                   # 指定设备，查看安装的第三方应用
ideviceinstaller -u [udid] -l -o list_user      # 指定设备，查看安装的第三方应用
ideviceinstaller -u [udid] -l -o list_system    # 指定设备，查看安装的系统应用
ideviceinstaller -u [udid] -l -o list_all       # 指定设备，查看安装的系统应用和第三方应用
ideviceinfo -u [udid]                       # 指定设备，获取设备信息
ideviceinfo -u [udid] -k DeviceName         # 指定设备，获取设备名称：iPhone6s
idevicename -u [udid]                       # 指定设备，获取设备名称：iPhone6s
ideviceinfo -u [udid] -k ProductVersion     # 指定设备，获取设备版本：10.3.1
ideviceinfo -u [udid] -k ProductType        # 指定设备，获取设备类型：iPhone8,1
ideviceinfo -u [udid] -k ProductName        # 指定设备，获取设备系统名称：iPhone OS
```
原文：
[libimobiledevice安装和常用命令]([https://www.jianshu.com/p/746f3ddded1f](https://www.jianshu.com/p/746f3ddded1f)
)
