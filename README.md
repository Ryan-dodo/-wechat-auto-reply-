# 基于pyautogui的微信自动回复脚本

## 工作原理：

在电脑端登录微信客户端，保证微信左侧界面不受遮挡，利用pyautogui找到信息的红点标志，依次点击回复对象，文本框，输入内容，发送。没错，原理十分简单、暴力。效果稳定，基本可以避免错发消息。

## 调试方法：

刚开始可以用小号调试，可以替换image文件夹中的图片，更改好图片路径，pyautogui的图像识别十分严格，精确到像素。可以在次基础上给特定联系人，设定特定的回复文字，回复的消息只能是英文，可以发送表情包。

## 脚本效果：

![image](https://github.com/Ryan-dodo/-wechat-auto-reply-/blob/main/image/display.PNG)

回复的文字、表情包支持自定义，再说一遍，只能回复英文，或者自行复制中文粘贴来实现。

## 版本更新

暂无

