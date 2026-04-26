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

header_height = 80
footer_height = 80

full_text = ''

for page in doc:
    rect = page.rect # 페이지 크기 가져오기

    header = page.get_text(clip=(0, 0, rect.width, header_height))
    footer = page.get_text(clip=(0, rect.height - footer_height, rect.width, rect.height))
    text = page.get_text(clip=(0, header_height, rect.width, rect.height - footer_height))

    full_text += text + '\n--------------------------------------------------------------\n'

# 파일명만 추출
pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0] # 확장자 제거

txt_file_path = f"output/{pdf_file_name}_with_preprocessing.txt"

with open(txt_file_path, 'w', encoding = 'utf-8') as f:
    f.write(full_text)