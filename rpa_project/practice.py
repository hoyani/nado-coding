from openpyxl import Workbook
from random import *

wb = Workbook()
ws = wb.active
ws.title = 'Practice'


# ========== 1줄씩 data 넣기
ws.append(["학번", "출석", "퀴즈1","퀴즈2", "중간고사", "기말고사", "프로젝트", "총점(SUM)", "성적"])

for i in range(1,11): #10개 데이터 넣기 
    ws.append([i,randint(0,100), randint(0,100)])
    



wb.save("practice.xlsx")