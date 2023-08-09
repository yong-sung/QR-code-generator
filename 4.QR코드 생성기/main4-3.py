import qrcode

file_path = r'4.QR코드 생성기\qr코드모음.txt' # r의 의미: \를 아무 의미 없는 문자형태로 인식하기 위해
with open(file_path,'rt',encoding='UTF8') as f: # UTF8의 의미: 파일이 한국어로 돼있기 때문에
    read_lines = f.readlines()
    
    for line in read_lines:
        line = line.strip()
        print(line)

        qr_date = line
        qr_img = qrcode.make(qr_date)
        
        save_path = '4.QR코드 생성기\\' + qr_date + '.png'
        qr_img.save(save_path)

