import qrcode

qr_date = 'www.naver.com'
qr_img = qrcode.make()

save_path = '4.QR코드 생성기\\' + qr_date + '.png'
qr_img.save(save_path)