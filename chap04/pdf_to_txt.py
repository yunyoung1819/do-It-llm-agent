import pymupdf
import os

pdf_file_path = r"C:\Users\user\do_it\chap04\data\20260418.pdf"
doc = pymupdf.open(pdf_file_path)

if doc.is_encrypted: 
    success = doc.authenticate("880418")
    if not success:
        print("비밀번호가 틀렸습니다.")
    else:
        print("인증 성공")

full_text = ''

for page in doc:    # 문서 페이지 반복
    text = page.get_text()  # 페이지 텍스트 추출
    full_text += text

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0]  # 확장자 제거

txt_file_path = f"output/{pdf_file_name}.txt"
with open(txt_file_path, 'w', encoding = 'utf-8') as f:
    f.write(full_text)