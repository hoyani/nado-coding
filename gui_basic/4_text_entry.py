from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로x세로 +x좌표 +y좌표

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력 : ") #여러줄 입력용

e = Entry(root, width=30) #한줄 입력용 - id, pw 등
e.pack()
e.insert(0, "한줄만 입력")


def btncmd():
    
    #내용 등록 
    print(txt.get("1.0", END)) #라인1부터 0번쨰 컬럼위치 가져와라 
    print(e.get())
    
    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 해줌 ㅇ

