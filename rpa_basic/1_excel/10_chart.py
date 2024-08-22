from openpyxl import load_workbook
wb = load_workbook("rpa_basic/1_excel/sample.xlsx")

ws = wb.active

from openpyxl.chart import BarChart, Reference, LineChart

# ㅡㅡㅡㅡ bar 차트

# B2:C11 까지의 데이터를 => 차트로 생성! 
bar_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3) # min 끼리 B2 / max 끼리 C11 
bar_chart = BarChart() # 차트종류 설정 (Bar, Pie, Line, ...)
bar_chart.add_data(bar_value) # 연결작업 !!! = 차트 생성은 됏고 

ws.add_chart(bar_chart, "E1") # 엑셀에 차트를 추가 / 차트 넣을 위치 정의

# 결과 : min_row2 부터라 제목 포함안되서 - 제목이 계열1, 계열2 로 나옴 


# ㅡㅡㅡㅡ Line 차트

# B2:C11 까지의 데이터를 => 차트로 생성! 
line_value = Reference(ws, min_row=1, max_row=11, min_col=2, max_col=3) # min 끼리 B2 / max 끼리 C11 
line_chart = LineChart()

# 막대 tag <- data에서 자동 가져오는법!!!! miss 
line_chart.add_data(line_value, titles_from_data=True) # 연결작업 !!! = 차트 생성은 됏고  / 계열 = 영어, 수학 제목에서 가져옴

line_chart.title = '성적표' #제목
line_chart.style = 10 # 미리 정의된 스타일 적용, 사용자가 개별지정 가능
line_chart.y_axis.title = '점수' # y축 제목 지정
line_chart.x_axis.title = '번호' # x축 제목 지정

ws.add_chart(line_chart, "E1") # 엑셀에 차트를 추가 / 차트 넣을 위치 정의

# # 결과 : min_row1 부터라 제목 포함 되서 - 제목이 영어, 수학 으로 나옴 

wb.save("rpa_basic/1_excel/sample_chart.xlsx")



'''
구글에 'openpyxl' 이라 검색하면
젤 상위 사이트에서 <- chart 메뉴 가면
더 많은 메소드 사용 가능!! 참고 **


'''