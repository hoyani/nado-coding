from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로x세로 +x좌표 +y좌표

listbox = Listbox(root, selectmode=EXTENDED, height=0) # extend 중복선택, single 한개만선택 / height 0 이면 전체다, 숫자3는 3만큼 창+드래그나머지 
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():    
        
    # 삭제
    #listbox.delete(END) #맨 뒤에 항목 삭제
    #listbox.delete(0) #맨 앞 항목 삭제
    
    
    # 갯수 확인
    #print('리스트에는', listbox.size(), '개가 있어요')
    
    # 항목 확인
    #print('1번쨰~3번째까지 항목', listbox.get(0,2)) #시작index, 끝index
    
    # 선택된 항목 확인 (index로 반환)
    print('선택된 항목 : ', listbox.curselection())
    
    
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 해줌 ㅇ

