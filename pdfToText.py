import PyPDF2
import os

def extract_text_from_pdf(pdf_path, output_text_file):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        
        extracted_text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()
    
    with open(output_text_file, 'w', encoding='utf-8') as output_file:
        output_file.write(extracted_text)

while True:
    pdf_path = input("PDFファイルのパスを入力してください（終了するには q を入力）: ")
    if pdf_path.lower() == 'q':
        break
    
    if not os.path.exists(pdf_path):
        print("指定されたパスが存在しません。")
        continue
    
    if not pdf_path.lower().endswith('.pdf'):
        print("指定されたファイルはPDFファイルではありません。")
        continue
    
    output_text_file = input("出力テキストファイルのパスを入力してください: ")
    
    extract_text_from_pdf(pdf_path, output_text_file)
    print("テキストを抽出して出力しました。")
