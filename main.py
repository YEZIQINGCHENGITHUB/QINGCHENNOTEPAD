from tkinter import *
import sys,os,easygui
import tkinter.filedialog as tg
#导入轮子
def Hello():
    
    #定义Hello函数
    def main():
        #定义main函数
        def save():
            #定义保存函数
            get=b.get("1.0","end")
            #得到文本框文字
            a=easygui.filesavebox(default='新建文本文档.txt')
            #询问保存路径
            w=open(a,"w")
            w.write(get)
            #写入文件
            w.close()
            a+1
        def dakai():
            #定义打开函数
            g=easygui.fileopenbox(default='*.txt')
            #询问文件路径
            h=open(g,encoding=None)
            i=h.read()
            #读取文件
            b.insert("end",i)
            h.close()
        def quit_ask():
            #定义关闭询问函数
            sa=easygui.buttonbox("关闭选项（点击右上角的X会自动关闭）","清晨记事本",choices=('保存','不保存','取消','关闭'))
            #询问是否保存
            if sa=="取消":
                pass
            #如果点击“取消”则跳过
            if sa=="不保存"or"关闭":
                WINDOWS.destroy()
                #如果点击“不保存”则关闭窗口
            
            if sa=="保存":
                save()
            #如果点击“保存”则执行保存函数
            
            
        def new_window():
            WINDOW=Tk()
            #初始化窗口
            WINDOW.title("清晨记事本")
            WINDOW.geometry('460x300')
            #定义标题和大小
            b=Text(WINDOW,width=600,height=50)
            b.place(x=0,y=0)
            b.pack()
            #初始化Text窗口
            ha=Button(WINDOW,text="保存",command=save)
            op=Button(WINDOW,text='打开',command=dakai)
            ne=Button(WINDOW,text="新窗口",command=new_window)
            ha.pack()
            op.pack()
            ne.pack()
            def made():
                sa=easygui.buttonbox("关闭选项（点击右上角的X会自动关闭）","清晨记事本",choices=('保存','不保存','取消','关闭'))
                #询问是否保存
                if sa=="取消":
                    pass
                #如果点击“取消”则跳过
                if sa=="不保存"or"关闭":
                    WINDOW.destroy()
                    #如果点击“不保存”则关闭窗口
                
                if sa=="保存":
                    save()
            #定义两个按钮
            WINDOW.protocol("WM_DELETE_WINDOW",made)
            #执行关闭询问函数
            WINDOW.mainloop()
            
        
                
#################################################################################################################
        
        WINDOWS=Tk()
        #初始化窗口
        WINDOWS.title("清晨记事本")
        WINDOWS.geometry('460x300')
        #定义标题和大小
        b=Text(width=600,height=50)
        B=Text(width=600,height=50)
        B,b=b,B
        
        
        b.place(x=0,y=0)
        b.pack()
        #初始化Text窗口
        ha=Button(WINDOWS,text="保存",command=save)
        op=Button(WINDOWS,text='打开',command=dakai)
        ne=Button(WINDOWS,text="新窗口",command=new_window)
        ha.pack()
        op.pack()
        ne.pack()
        #定义两个按钮
        WINDOWS.protocol("WM_DELETE_WINDOW",quit_ask)
        #执行关闭询问函数
        WINDOWS.mainloop()
        #重复执行
    main()
    #执行main函数
Hello()
#执行Hello函数
