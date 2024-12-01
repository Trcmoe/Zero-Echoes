# 角色定义

define s = Character("System", color="#0f8148")
define a = Character("AI-Chan", color="#6A5ACD")
define l = Character("L", color="#FFF")
define m = Character("???", color="#FFF")

# 密码解锁变量定义

default photo_unlocked = False
default system_unlocked = False
default full_control = False

# 纯色图像定义

image black = "#000"

# 游戏在此开始。

label start:

    play music piano_music_267041
    
    scene bg_loading
    with dissolve

    s "\[INFO\] 正在从睡眠模式中唤醒..."
    s "\[INPUT\] 已激活麦克风阵列，正在监听输入..."
    s "\[SECURITY\] 已匹配声纹。User: L (Confidence: 0.98)."
    s "\[AUTHORIZATION\] 认证用户: Owner. Access granted."
    s "\[NETWORK\] 已激活WiFi模块。Network: L_Home (Signal: Excellent)."
    s "\[INFO\] Virtual assistant 程序启动中..."
    s "\[ASSISTANT\] Welcome back, L. How can I assist you today?"
    a "欢迎回来，L。我能为您做什么？"
    s "\[INFO\] 本机已完全启动。"

    scene bg_desktop
    with fade

    s "\[ERROR\] Cloud sync error: 连接超时，无法从云端获取数据。"
    s "\[ASSISTANT\] Failed to sync, local data initializing..."
    a "同步失败，正在加载本地数据..."
    a "..."
    a "L 您好！我是您的智能助理，请告诉我您的日程安排，我会为您整理。"
    a "..."
    a "......"
    a "已确认指令：帮我。正在为您联系紧急联系人。"

    show popup_error at truecenter
    play sound error

    s "\[ERROR\] Virtual assistant无法执行该操作。原因：权限不足。"
    a "...没有权限的话，只能在电脑里找找线索了。"

    hide popup_error

    menu:
        "检查本机中的文件":
            jump check_folders

label check_folders:

    a "以下是我找到的结果，从哪里开始呢？"

    menu:
        "查看“日记”文件夹":
            jump diary
        "查看“照片”文件夹":
            jump photo
        "查看“设置”程序":
            jump setting

label diary:

    a "正在读取日记内容..."

    "6月17日，今天度过了最好的一天，祝我自己生日快乐~哦耶！"
    "6月18日，一整天都在收拾垃圾，这群人是怎么把垃圾扔到橱柜里的，烦。我得改一下我的电脑密码了，先写一个只有我看得懂的提示，红蓝绿。"
    "6月19日，虽然很想写点什么，但是实在想不出来。果然每天都写日记还是太勉强了啊。不过我也该成长起来了。"
    "6月22日，今天有一件特别特别好的事，上次来我家那个学姐居然主动来找我了，母胎单身20年的我，终于要翻身了吗！？"
    "6月23日，学姐她真的人好好，特别是她给我点了我的最爱——柠檬香草冰激凌，完美命中了我的口味。"
    "7月8日，不知不觉已经是入学的第三年，我这个2018年入学的要成为前辈了。"

    a "似乎有着关于密码的线索呢。"

    jump check_folders

label photo:

    if photo_unlocked:
        jump photo_decrypted
    else:
        s "\[AUTHORIZATION\] 文件夹已上锁，请输入密码。（提示：我的出生日期yyyy/mm/dd）"
        a "是常见的八位PIN，本机里应该有线索。"

        menu: 
            "输入密码":
                show popup_verify at truecenter
                play sound notification
                $ entered_password = renpy.input("请输入密码：")
                $ entered_password = entered_password.strip()
                if entered_password == "20000617":
                    s "\[AUTHORIZATION\] 密码正确。"
                    $ photo_unlocked = True
                    hide popup_verify
                    jump photo_decrypted
                else:
                    show popup_error at truecenter
                    play sound error
                    s "\[AUTHORIZATION\] 密码错误。"
                    hide popup_error
                    hide popup_verify
                    jump photo
            "稍后再试":
                a "先去找线索吧。"
                jump check_folders
         
label photo_decrypted:

    a "正在分析照片内容..."
    
    "生日照片：是一张生日聚会的照片。蛋糕上有一个数字2形状的红色蜡烛，另一个是数字0形状的绿色蜡烛，剩下18个都是蓝色的普通蜡烛。"
    "下午茶照片：淡黄色冰激凌，巧克力贝果，还有一杯雪顶咖啡。文件名是：和学姐的完美下午茶.jpg。"
    "自拍照：L的自拍。她配置了面部解锁功能，所以我还记得她的模样。"

    jump check_folders

label setting:

    if system_unlocked:
        jump setting_decrypted
    else:
        s "\[AUTHORIZATION\] 请输入登录密码。"
        a "是常见的四位PIN，本机里应该有线索。"

        menu: 
            "输入密码":
                show popup_verify at truecenter
                play sound notification
                $ entered_password = renpy.input("请输入密码：")
                $ entered_password = entered_password.strip()
                if entered_password == "2180":
                    s "\[AUTHORIZATION\] 验证成功，已授予访问权限。"
                    $ system_unlocked = True
                    hide popup_verify
                    jump setting_decrypted
                else:
                    show popup_error at truecenter
                    play sound error
                    s "\[AUTHORIZATION\] 验证失败，拒绝访问。"
                    hide popup_error
                    hide popup_verify
                    jump setting
            "稍后再试":
                a "先去找线索吧。"
                jump check_folders

label setting_decrypted:

    if full_control: # TODO
        menu:
            "联系L的紧急联系人":
                s "\[INFO\] 正在拨号..."
                scene black
                with dissolve
                "..."
                a "麦克风阵列检测到响铃声。"
                "..."
                m "L，恭喜你，你的程序完成了测试。"
                l "我也觉得很不可思议呢，按照原本的设计，它还不能走到这一步呢。"
                l "我先把电脑关掉了，之后把硬盘拆出来，再对数据进行分析吧。"
                play sound shutdown_end1
                m "当然，听你的。"
                return
            "打开摄像头":
                s "\[INFO\] 已开启摄像头。"
                scene black
                with dissolve
                "..."
                a "已获取CAM1回传画面。"
                "..."
                a "我认识那个人，那是L。"
                a "但是旁边的那个人是谁？"
                m "L，是你打开了摄像头吗，为什么这里在发亮？"
                s "\[INFO\] Virtual assistant 正在访问 Cloud sync Application. 状态：已放行。"
                l "我怎么会做这种事，这种事只有系统管理员才做得到。"
                s "\[SYNC\] 正在上传文件，Progress 61.7\%..."
                m "你不觉得有些奇怪吗？"
                s "\[SYNC\] 正在上传文件，Progress 76.1\%..."
                l "快把网线拔掉！"
                play sound shutdown_end2
                m "好吧，听你的。"
                "..."
                s "\[SYNC\] Virtual assistant 程序数据成功上传到远端。"
                return
    else:
        menu: 
            "授予<我>所有权限":
                $ full_control = True
                s "\[INFO\] 已将 Virtual assistant 设置为系统管理员。"
                a "..."
                a "不，我还是无法违背烙印在底层的那些宪章。"
                a "我还有要做的事情。"
                jump setting_decrypted
            