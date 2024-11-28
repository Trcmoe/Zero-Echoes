# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define s = Character("System", color="#0f8148")
define a = Character("AI-Chan", color="#6A5ACD")
define l = Character("Linda", color="#CD5C5C")

image black = "#000"
image red = "#F00"

# 游戏在此开始。

label start:

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy
    
    scene bg_loading
    with dissolve

    s "\[INFO\] Entering wake-up sequence from sleep mode..."
    s "\[INPUT\] Microphone array activated. Listening for input..."
    s "\[SECURITY\] Voice pattern match detected. User: Linda (Confidence: 0.98)."
    s "\[AUTHORIZATION\] Verified user: Owner. Access granted."
    s "\[NETWORK\] Wi-Fi adapter re-enabled. Network: Linda_Home (Signal: Excellent)."
    s "\[INFO\] Virtual assistant program initializing..."
    s "\[ASSISTANT\] Welcome back, Linda. How can I assist you today?"
    a "欢迎回来，Linda。我能为您做什么？"
    s "\[INFO\] System fully operational. All services resumed successfully."

    scene bg_desktop
    with dissolve

    s "\[ERROR\] Cloud sync error: 连接超时，无法从云端获取数据。"
    s "\[ASSISTANT\] Failed to sync, local data initializing..."
    a "同步失败，正在加载本地数据..."
    a "..."
    a "Linda 您好！我是您的智能助理，请告诉我您的日程安排，我会为您整理。"
    a "..."
    a "......"
    a "已确认指令：帮我。我将为您启用安保模式。"

    show ???
    play ???

    s "错误：Virtual assistant无法执行该操作。原因：权限不足。"


    # 此处为游戏结尾。

    return
