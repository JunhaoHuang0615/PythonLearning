# import easygui
# easygui.msgbox("nihao")
import easygui as eas   #重命名导入
import sys
eas.msgbox("nihao")

while (True):
    eas.msgbox("This is a short game")

    msg = "What would you like to learn?"
    title = "こんにちは"
    choices = ["Live2D","Ps","AE","Git","Unity"]

    choice = eas.choicebox(msg,title,choices)
    #这个会生成一个choice的窗口，根据选择会把选项存在choice中，str类型的
    #这个地方会等待用户选择
    eas.msgbox("你的选择是"+ choice,'结果')

    msg = '重新开始吗？'
    title = '请选择'

    if(eas.ccbox(msg,title)):
        pass
    else:
        sys.exit(0) #User choice cancel
