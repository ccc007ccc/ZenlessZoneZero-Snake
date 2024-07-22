# 绝区零蛇对蛇全自动刷分脚本

此Python脚本通过模拟键盘输入来自动控制贪吃蛇游戏中的蛇进行刷分。脚本会让蛇以原地转圈的方式移动并在失败后自动重新开始，从而实现全自动刷分(很难刷到千万分以上).

## 脚本说明

### 必需模块

脚本依赖于 `keyboard pyautogui` 库。你可以使用以下命令安装：

```sh
pip install keyboard pyautogui
```

## 使用方法

1. 确保你已经安装了好了库
2. 将start.py保存到你的电脑上
3. 以管理员权限打开终端(右键任务栏Windows图标->点击终端管理员)
4. 输入python + 脚本路径 如 `python "C:\xxx\start.py"`
5. 在贪吃蛇游戏中，按下 `F10` 键开始自动刷分(不用操控,脚本会自动将蛇移动到角落)。
6. 按下 `F11` 键暂停刷分。

## 注意事项

- 运行此脚本时，请确保游戏窗口处于活动状态。
- 该脚本模拟键盘操作，因此在运行期间请勿手动干预蛇的移动，以避免冲突。

## 常见问题

- 如果游戏失败后不会自动重新开始，请将游戏结束界面此处截图并替换/img/image.png文件。![image](doc/img/1.png)

## 免责声明

此脚本仅供学习和娱乐使用，请勿用于破坏游戏平衡或其他不正当行为。使用此脚本的风险由用户自行承担。