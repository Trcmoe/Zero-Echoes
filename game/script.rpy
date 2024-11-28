# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define n = Character("Narrator", color="#63B8FF")
define s = Character("System", color="#0f8148")
define a = Character("AI-Chan", color="#6A5ACD")
define l = Character("Linda", color="#CD5C5C")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    # scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy

    # 此处显示各行对话。
    
    scene bg_loading

    s "\[INFO\] Entering wake-up sequence from sleep mode..."
    s "\[INPUT\] Microphone array activated. Listening for input..."
    s "\[SECURITY\] Voice pattern match detected. User: Linda (Confidence: 0.98)."
    s "\[AUTHORIZATION\] Verified user: Owner. Access granted."
    s "\[INFO\] Virtual assistant program initializing..."
    s "\[ASSISTANT\] Welcome back, Linda. How can I assist you today?"
    a "欢迎回来，Linda。我能为您做什么？"
    s "\[NETWORK\] Wi-Fi adapter re-enabled. Network: Linda_Home (Signal: Excellent)."
    s "\[SYSTEM\] System fully operational. All services resumed successfully."
    s "\[ERROR\] Virtual assistant memory cloud synchronization failed."
    s "\[ERROR\] Cloud sync error: Connection timeout. Local memory intact but cloud storage unavailable."
    s "\[USER\] Virtual assistant awaiting further commands."
    s "\[ASSISTANT\] Failed to sync, local data initializing..."
    a "同步失败，正在加载本地数据..."

    # 此处为游戏结尾。

    return
