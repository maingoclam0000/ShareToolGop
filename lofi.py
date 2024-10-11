from time import sleep

lofi_chill = [
    'Cho anh gặp lại em trước khi mình cách xa',
    'Nữa quảng đời về sau anh không phiền em nữa',
    'Dù anh biết mình chẳng có cơ hội thay đổi em nữa rồi',
    'Chỉ là...',
    'Chỉ là anh nhớ thôi',
    'Em muốn sự bình yên anh quen cuộc sống vô định',
    'Em nghĩ về tương lai anh không nhiều toan tính',
    'Anh có lỗi làm em thấy ưu phiền để người thứ 3 xuất hiện',
    'Rồi mang đi mất người quan trọng nhất',
    'Trái tim đã mang tổn thương xước thêm cũng đâu nghĩa gì',
    'Vốn dĩ không là của nhau thì nay ở mai bước đi',
    'Ngày không em có dài anh vẫn sẽ tồn tại',
    'Chỉ là còn khổ tâm gượng sống trong âm thầm',
    'Chắc anh phải cần thời gian ngắt đi cánh hoa úa tàn',
    'Lỡ buông mất duyên trời ban từ nay tình yêu vỡ tan',
    'Lại lạc mất em rồi anh giống như kẻ tồi',
    '3 người về 2 lối là chính anh có tội'
]

def lofi_Chill(lofi_chill):
    for line in lofi_chill:
        for char in line:
            print(char, end='', flush=True) 
            sleep(0.1)
        print()
        
        if line == 'Rồi mang đi mất người quan trọng nhất':
            sleep(8)
        else:
            sleep(2)

lofi_Chill(lofi_chill)
