#导入 * 全部
import qrcode #专门生成二维码的
from tkinter import *
#定义二维码的名字和格式
file_name='二维码.jpg'
#这一步是创建窗口
def show():
 #创建窗口
 root=Tk()
 #创建画布width 宽  height高度 紫色普遍属性 bg就是背景颜色
 canvas=Canvas(root,width=800,height=800,bg="white")
 #加载图片
 img=PhotoImage(file=file_name)

 #将我们的图片放在画布 x数值越大越往右 y数值越大越往下走
 canvas.create_image(400,400,image=img)
 canvas.pack()
 #显示窗口
 root.mainloop()

def mk_qrcod(content):
    #改二维码的属性
 q=qrcode.QRCode()
 q.add_data(content)
 #True 真 False 假 生成二维码图片
 q.make(fit=True)
    #fill_color这是设置二维码颜色  back_color二维码背景色
 img=q.make_image(fill_color="green",back_color="white")
    #添加我们的二维码
 img.save(file_name)
#传输协议
Https="https://"
if __name__ == '__main__':
 while True:
     #输入
    result=input("请输入内容").strip()
    if result=="end":
        #结束
        break

    else:
        #拼接协议不让称为一个单纯的字符串而是一个网址 格式 https://www.baibu.com
        mk_qrcod(Https+result)
        #弹窗显示我们的二维码
        show()