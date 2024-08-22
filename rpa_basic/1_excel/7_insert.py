from openpyxl import load_workbook
wb = load_workbook("rpa_basic/1_excel/sample.xlsx")
ws = wb.active


# ㅡㅡㅡㅡ 줄을 삽입

# ws.insert_rows(8) #8번쨰 줄이 비워지고 1줄 추가
# ws.insert_rows(8,5) # 8번줄에, 5줄 빈줄을 추가 
# wb.save("sample_insert_rows.xlsx")


# ㅡㅡㅡㅡ 열을 삽입


#ws.insert_cols(2) #2번째 비워지고 1열 추가
ws.insert_cols(2,3) # 2번열에, 3개 빈 열을 추가 
wb.save("rpa_basic/1_excel/sample_insert_cols.xlsx")