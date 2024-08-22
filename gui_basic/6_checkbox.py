from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로x세로 +x좌표 +y좌표


chkvar = IntVar() #chkvar 에 int형으로 값 저장 
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
#chkbox.select() # 자동 선택처리 
#chkbox.deselect() #선택 해제 처리
chkbox.pack()


chkvar2 = IntVar() 
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():    
    print(chkvar.get()) # 체크해제 : 0출력 / 체크 : 1출력 
    print(chkvar2.get())
    print('------')
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 해줌 ㅇ

