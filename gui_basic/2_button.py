from tkinter import *

root = Tk()

root.title("Nado GUI")

root.geometry("640x480+300+100") # 가로x세로 +x좌표 +y좌표

root.resizable(False, False) #x너비, y높이 값 변경 불가 (창크기 변경불가)

btn1 = Button(root, text="버튼1")
btn1.pack() #팩해줘야 실제 root 메인 윈도우에 포함됌 

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()


btn5 = Button(root, fg="red", bg="yellow", text="버튼5") #foreground 글자색 
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되엇어요")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop() #창이 닫히지 않도록 해줌 

