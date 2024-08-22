from openpyxl import load_workbook
wb = load_workbook("rpa_basic/1_excel/sample.xlsx")

ws = wb.active


# ㅡㅡㅡㅡ 줄 삭제

ws.delete_rows(8) #8번째 줄의 7번학생 데이터 삭제 
ws.delete_rows(8,3) #8번째 줄부터 총 3줄 삭제

wb.save("rpa_basic/1_excel/sample_delete_row.xlsx")

# ㅡㅡㅡㅡ 열 삭제


#ws.delete_cols(2) #2번째 열 삭제
ws.delete_cols(2,2) #2번째 열부터 총 2개열 삭제 

wb.save("rpa_basic/1_excel/sample_delete_col.xlsx")