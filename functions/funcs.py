#Phép cộng
def Phep_cong():
    while True:
        try:
            so_1 = float(input("Nhập số thứ nhất: "))
            so_2 = float(input("Nhập số thứ hai: "))
            ket_qua = so_1 + so_2
            print(f"Kết quả của {so_1} + {so_2} = {ket_qua}")
            tiep_tuc = input("Bạn có muốn tiếp tục tính toán? (gõ 'không' để dừng, bất kỳ phím nào khác để tiếp tục): ")
            if tiep_tuc == 'không':
                print("Tạm biệt!")
                break
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
Phep_cong()
#Đoạn code này có vai trò thực hiện phép tính cộng. Trong đoạn code có sử dụng Try-Except để báo ta nhập lại sau khi nhập sai.
#Break dùng để dừng vòng lặp lại.
#Sau khi ra kết qu, nếu muốn thực hiện tính toán tiếp thì gõ bất kì phím gì, nếu không thì gõ 'không'

#phép trừ
def Phep_tru():
    while True:
        try:
            so_1 = float(input("Nhập số thứ nhất: "))
            so_2 = float(input("Nhập số thứ hai: "))
            ket_qua = so_1 - so_2
            print(f"Kết quả của {so_1} - {so_2} = {ket_qua}")
            tiep_tuc = input("Bạn có muốn tiếp tục tính toán? (gõ 'không' để dừng, bất kỳ phím nào khác để tiếp tục): ")
            if tiep_tuc == 'không':
                print("Tạm biệt!")
                break
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
Phep_tru()
#Đoạn code này có vai trò thực hien phép tiính trừ. cấu trúc đoạn code thì giống như trên

#phép nhân
def Phep_nhan():
    while True:
        try:
            so_1 = float(input("Nhập số thứ nhất: "))
            so_2 = float(input("Nhập số thứ hai: "))
            ket_qua = so_1 * so_2
            print(f"Kết quả của {so_1} * {so_2} = {ket_qua}")
            tiep_tuc = input("Bạn có muốn tiếp tục tính toán? (gõ 'không' để dừng, bất kỳ phím nào khác để tiếp tục): ")
            if tiep_tuc == 'không':
                print("Tạm biệt!")
                break
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
Phep_nhan()
#Đoạn code này có vai trò thực hiện phép tính nhân, cấu trúc đoạn code tương tự như trên

#phép chia
def Phep_chia():
    while True:
        try:
            so_1 = float(input("Nhập số thứ nhất: "))
            so_2 = float(input("Nhập số thứ hai: "))
            ket_qua = so_1 / so_2
            print(f"Kết quả của {so_1} / {so_2} = {ket_qua}")
            tiep_tuc = input("Bạn có muốn tiếp tục tính toán? (gõ 'không' để dừng, bất kỳ phím nào khác để tiếp tục): ")
            if tiep_tuc == 'không':
                print("Tạm biệt!")
                break
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
Phep_chia()
#Đoạn code này có vai trò thực hiện phép tính chia, cấu trúc đoạn code tương tự như trên

#Binh phuong
def binh_phuong():
    while True:
        try:
            so = float(input("Nhập một số: "))
            ket_qua = so ** 2
            print(f"Kết quả của {so}^2 = {ket_qua}")
            tiep_tuc = input("Bạn có muốn tiếp tục tính toán? (gõ 'không' để dừng, bất kỳ phím nào khác để tiếp tục): ")
            if tiep_tuc == 'không':
                print("Tạm biệt!")
                break
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
binh_phuong()
#Đoạn code này có vai trò thực hiện phép tính bình phương, cấu trúc đoạn code tương tự như trên

#căn bậc 2
import math  # Thư viện cung cấp hàm sqrt() để tính căn bậc 2
def can_bac_2():
    while True:
        try:
            so = float(input("Nhập một số: "))
            if so < 0:
                print("Không thể tính căn bậc 2 của số âm. Vui lòng nhập một số không âm.")
            else:
                ket_qua = math.sqrt(so)
                print(f"Căn bậc 2 của {so} = {ket_qua}")
            tiep_tuc = input("Bạn có muốn tiếp tục tính toán? (gõ 'không' để dừng, bất kỳ phím nào khác để tiếp tục): ")
            if tiep_tuc == 'không':
                print("Tạm biệt!")
                break
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")
can_bac_2()
#Đoạn code này có vai trò thực hiện phép tính căn bậc 2, cấu trúc đoạn code nhìn chung tương tự như trên.
#Có điều lần này ta cần thêm điều kiện so<0 vì căn bậc 2 không âm. Với lại ta cũng thêm hàm sqrt() trong thư viện math để thực hiện phép tính


# trị tuyệt đôi
def tri_tuyet_doi():
    while True:
        try:
            so = float(input("Nhập một số): "))
            ket_qua = abs(so)
            print(f"Trị tuyệt đối của {so} = {ket_qua}")
            tiep_tuc = input(
                "Bạn có muốn tiếp tục tính toán? (gõ 'không' để dừng, bất kỳ phím nào khác để tiếp tục): ")
            if tiep_tuc == 'không':
                print("Tạm biệt!")
                break
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")
tri_tuyet_doi()
#Đoạn code này có vai trò thực hiện phép tính trị tuyệt đối, cấu trúc đoạn code tương tự như trên, ta cung thêm hàm abs có sẵn trong python để thực hiện phép tính trị tuyệt đối.


#UCLN
import math
def ucln():
    while True:
        try:
            so_1 = int(input("Nhập số thứ nhất: "))
            so_2 = int(input("Nhập số thứ hai: "))
            ucln = math.gcd(so_1, so_2)
            print(f"Ước chung lớn nhất của {so_1} và {so_2} là: {ucln}")
            tiep_tuc = input("Bạn có muốn tiếp tục tính toán? (gõ 'không' để dừng, bất kỳ phím nào khác để tiếp tục): ")
            if tiep_tuc == 'không':
                print("Tạm biệt!")
                break
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")
ucln()
#đoạn code có vai trò tính ước chung lớn nhất của 2 số, sử dụng hàm gcd trong thư viện math để tính.

#BCNN
import math
def bcnn():
    while True:
        try:
            so_1 = int(input("Nhập số thứ nhất: "))
            so_2 = int(input("Nhập số thứ hai: "))
            # Tính UCLN để tính BCNN
            ucln = math.gcd(so_1, so_2)
            bcnn = abs(so_1 * so_2) // ucln  # Công thức tính BCNN
            print(f"Bội chung nhỏ nhất của {so_1} và {so_2} là: {bcnn}")
            tiep_tuc = input("Bạn có muốn tiếp tục tính toán? (gõ 'không' để dừng, bất kỳ phím nào khác để tiếp tục): ")
            if tiep_tuc == 'không':
                print("Tạm biệt!")
                break
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")
bcnn()
#Đoạn code có vai trò tính BCNN. Do thư viện math không có hàm tính BCNN nên ta sẽ tính bằng cách nhân 2 số lại rồi chia UCLN. UCLN thì làm như trên.


def phan_tich_thua_so_nguyen_to(n):
    i = 2  # Bắt đầu kiểm tra từ 2 (số nguyên tố nhỏ nhất)
    print(f"Các thừa số nguyên tố của {n} là: ", end="")
    while i <= n:
        while n % i == 0:
            print(i, end=" ")
            n //= i
        i += 1
    print()
'''
Đầu tiên ta lập hàm để tính các thừa số nguyen tố, bắt đầu với i=2 vì đây là snt nhỏ nhất. Ta sẽ dùng vòng lặp while lồng vào nhau
vòng lặp while thứ nhất là để kiểm soát giá trị của i, bắt đầu từ số 2 và sau đó tăng dâần lên. Còn vòng lặp thứ 2 là để kiểm tra 
xem n có chia hết i nhiều lần hay không.
ví dụ n=2024, n%2==0 nên in ra 2(đây là tsnt đầu tiên), sau đó 2024//2=1012. Tiếp tục ta thấy 1012%2==0 nên in ra 2(tsnt tiếp theo), 1012//2=506
cứ làm như vậy cho tới khi phân tích ra các số là 2,2,2,11,23
'''

def thua_so_nguyen_to():
    while True:
        try:
            so = int(input("Nhập một số nguyên dương để phân tích (hoặc gõ 'dừng' để kết thúc): "))
            if so <= 0:
                print("Vui lòng nhập một số nguyên dương!")
                continue
            # Gọi hàm phân tích thừa số nguyên tố
            phan_tich_thua_so_nguyen_to(so)
            # Hỏi người dùng có muốn tiếp tục hay không
            tiep_tuc = input("Bạn có muốn tiếp tục tính toán? (gõ 'không' để dừng, bất kỳ phím nào khác để tiếp tục): ")
            if tiep_tuc == 'không':
                print("Tạm biệt!")
                break
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")
#Bước này thì giống như các phép tính trên.
thua_so_nguyen_to()
#Đoạn code có vai trò tính các thừa số nguyên tố của một số bất kì

#Hàm tính tổ hợp
import math
def to_hop(n, k):
    if k > n:
        return 'không tồn tại'  # Tổ hợp không tồn tại nếu k lớn hơn n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k)) #Sử dụng thư viện math để tạo phép tính giai thừa
n = int(input("Nhập giá trị n: "))
k = int(input("Nhập giá trị k: "))
ket_qua = to_hop(n, k)
print(f"Tổ hợp C({n}, {k}) = {ket_qua}")
'''
Đoạn code này có vai trò tính toán tổ hợp. Trong đoạn code này có sử dụng hàm factorial từ thư viện math để tính giai thừa cho
công thức tổ hợp.
'''

#Hàm tính chỉnh hợp
import math
def chinh_hop(n, k):
    if k > n:
        return 'Không tồn tại'  # Chỉnh hợp không tồn tại nếu k lớn hơn n
    return math.factorial(n) // math.factorial(n - k)
n = int(input("Nhập giá trị n: "))
k = int(input("Nhập giá trị k: "))
ket_qua = chinh_hop(n, k)
print(f"Chỉnh hợp P({n}, {k}) = {ket_qua}")
#Đoạn code có vai trò tính chỉnh hợp của 2 giá trị bất kì

#Hàm tính hoán vị
import math
def hoan_vi(n):
    return math.factorial(n)
n = int(input("Nhập giá trị n: "))
ket_qua = hoan_vi(n)
print(f"Hoán vị ({n}) = {ket_qua}")
#Đoạn code có vai trò tính hoán vị


                    ###---------- Import các lệnh có sẵn từ thư viện math ----------###
from math import cos, acos, sqrt, cbrt, pi, e, log
    ##############################################################################################################################################
    ##      Giải thích: cos    : Dùng để tính cos                                                                                               ##
    ##                  acos   : Dùng để tính arcos                                                                                             ##
    ##                  sqrt   : Dùng để tính căn bậc 2                                                                                         ##
    ##                  cbrt   : Dùng để tính căn bậc 3                                                                                         ##
    ##                  pi     : Số pi, dùng để tính nghiệm phương trình bậc 3                                                                  ##
    ##                  e      : Giá trị số e                                                                                                   ##
    ##                  log    : Tính log của x theo cú pháp log(x,CoSo), nếu không có cơ số thì mặc định log theo cơ số e (Hay còn gọi là ln)  ##
    ## Một số lưu ý:                                                                                                                            ##
    ## Khi nhập các giá trị để giải phương trình, sử dụng hàm eval để người dùng có thể nhập các giá trị như pi, e, log...                      ##
    ## Sử dụng hàm float cho các giá trị nhập cho phép chương trình được nhập tính các nghiệm số lẻ                                             ##
    ## Sau khi tính các giá trị x của phương trình, cho các giá trị của x vào 1 list gọi là list Nghiem để tiện rút trích                       ##
    ## Các nghiệm không có giá trị sẽ được đánh dấu bằng kí tự "x"                                                                              ##
    ##############################################################################################################################################
                    ### ---------- Hàm tính giai thừa ---------- ###
def Giaithua():
    a = int(input('Nhập số a:'))
    b = 1
    i = 1
    while i <= a:
        b = i * b
        i = i + 1
    return b
                    ### ---------- Giải phương trình 1 ẩn ---------- ###
##-----Hàm giảỉ phương trình bậc 1, 1 ẩn theo dạng ax+b=c-----##
def PTBN():
    # Nhập các giá trị cần thiết
    a = float(eval(input('Nhập số a:')))
    b = float(eval(input('Nhập số b:')))
    # Nếu giá trị của a = 0 thì phương trình sẽ có vô số nghiệm nếu b = 0 và vô nghiệm nếu b khác 0
    if a == 0:
        if b == 0:
            SoNghiem = 'VSN'
            x = 'x'
        else:
            SoNghiem = 0
            x ='x'
    # Tính nghiệm x bằng cách chuyển vế đổi dấu
    else:
        SoNghiem = 1
        x = -b / a
    Nghiem = [x]
    return SoNghiem,Nghiem

##-----Hàm giải phương trình bậc 2, 1 ẩn theo dạng ax^2+bx+c=0-----##
def PTBH():
    # Nhập các giá trị cần thiết
    a = float(eval(input('Nhập số a (a khác 0):')))
    # Kiểm tra xem gía trị a có bằng 0 hay không, nếu bằng thì yêu cầu nhập lại cho đến khi a khác 0
    while a == 0:
        a = float(eval(input('Xin hãy nhập lại số a (a khác 0):')))
    b = float(eval(input('Nhập số b:')))
    c = float(eval(input('Nhập số c:')))
    # Tính delta
    delta = (b * b) - (4 * a * c)
    # Trường hợp delta nhỏ hơn 0 => Phương trình vô nghiệm
    if delta < 0:
        SoNghiem = 0
        x1 = 'x'
        x2 = 'x'
        NghiemBoi = False
    elif delta == 0:
        SoNghiem = 1
        x1= - b / (2 * a)
        x2= 'x'
        NghiemBoi = True
    # Trường hợp còn lạ: delta > 0 => Phương trình có 2 nghiệm phân biệt
    else:
        SoNghiem = 2
        x1 = (- b + sqrt(delta)) / (2 * a)
        x2 = (- b - sqrt(delta)) / (2 * a)
        NghiemBoi = False
    Nghiem = [x1, x2]
    return SoNghiem, Nghiem, NghiemBoi

##-----Hàm giải phương trình bậc 3, 1 ẩn theo dạng ax^3+bx^2+cx+d=0-----##
# Phương pháp sử dụng: Phương pháp tổng hợp và lượng giác áp dụng cho mọi trường hợp, có thể tham khảo trên Wikipedia
def PTBB():
    # Nhập các giá trị cần thiết
    a = float(eval(input('Nhập số a (a khác 0):')))
    # Kiểm tra xem gía trị a có bằng 0 hay không, nếu bằng thì yêu cầu nhập lại cho đến khi a khác 0
    while a == 0:
        a = float(eval(input('Xin hãy nhập lại số a (a khác 0):')))
    b = float(eval(input('Nhập số b:')))
    c = float(eval(input('Nhập số c:')))
    d = float(eval(input('Nhập số d:')))
    # Tính giá trị delta và giá trị k, m theo công thức
    delta = (b**2) - (3 * a * c)
    k = ((9 * a * b * c ) - (2 * (b**3)) - (27 * (a**2) * d)) / (2 * sqrt(abs(delta)**3))
    m = (b**2) - (27 * (a**2) * d)
    # Nếu delta = 0 => Xem xét giá trị của m
    if delta == 0:
        # m=0 => Phương trình có 1 nghiệm bội
        if m == 0:
            SoNghiem = 1
            x1= - b / (3 * a)
            x2= 'x'
            x3= 'x'
            NghiemBoi = True
        # m khác 0 => Phương trình có 1 nghiệm duy nhất
        else:
            SoNghiem = 1
            x1= (- b + cbrt(m)) / (3 * a)
            x2= 'x'
            x3= 'x'
            NghiemBoi = False
    # Trường hợp delta < 0 => Phương trình có 1 nghiệm
    elif delta < 0:
        SoNghiem = 1
        x1 = (sqrt(abs(delta)) / (3 * a)) * ((cbrt(k + sqrt(k**2 + 1))) + (cbrt(k - sqrt(k**2 + 1)))) - (b / (3 * a))
        x2 = 'x'
        x3 = 'x'
        NghiemBoi = False
    else:
        # Khi delta > 0 => Xem xét giá trị của k
        # |k| >1 => Phương trình có 1 nghiệm
        if abs(k) > 1:
            SoNghiem = 1
            # Áp dụng công thức tính giá trị nghiệm
            x1 = ((sqrt(delta) * abs(k)) / (3 * a * k)) * ((cbrt(abs(k) + sqrt(k**2 - 1))) + (cbrt(abs(k) - sqrt(k**2 - 1)))) - (b / (3 * a))
            x2 = 'x'
            x3 = 'x'
            NghiemBoi = False
        # |k| >= 1 => Phương trình có ít nhất 2 nghiệm phân biệt
        else:
            #Áp dụng công thức
            x1 = (2 * sqrt(delta) * cos(acos(k) / 3) - b)/(3 * a)
            x2 = (2 * sqrt(delta) * cos((acos(k) / 3)-((2 * pi) / 3)) - b)/(3 * a)
            x3 = (2 * sqrt(delta) * cos((acos(k) / 3)+((2 * pi) / 3)) - b)/(3 * a)
            # Kiểm tra xem trong 3 nghiệm có nghiệm bị trùng không
            if x1 == x2:
                SoNghiem = 2
                NghiemBoi = True
                x1 = x1
                x2 = x3
                x3 = 'x'
            elif x1==x3:
                SoNghiem = 2
                NghiemBoi = True
                x1 = x1
                x2 = x2
                x3 = 'x'
            elif x2 == x3:
                SoNghiem = 2
                NghiemBoi = True
                x1 = x1
                x2 = x2
                x3 = 'x'
            else:
                SoNghiem = 3
                NghiemBoi = False
    Nghiem = [x1,x2,x3]
    return SoNghiem, Nghiem, NghiemBoi

##----- In kết quả các nghiệm tính được -----##
def KetQuaPT():
    if SoNghiem == 0:
        print('Phương trình này vô nghiệm')
    elif SoNghiem == 'VSN':
        print('Phương trình này vô số nghiệm')
    else:
        for i in range (SoNghiem):
            print('Nghiệm thứ',i + 1,'là:',Nghiem[i])
            i = i + 1


                    ###---------- Tính tổng giá trị của phương trình (Summation) ----------###
def Summation():
    PT = input('Nhập phương trình:')
    xBD = int(input('Nhập giá trị bắt đầu của x:'))
    xKT = int(input('Nhập giá trị kết thúc của x:'))
    # Cho các giá trị của x vào 1 dãy
    PhamVi = range(xBD,xKT+1)
    # Lần lượt thay giá trị của x vào phương trình và cộng tổng các giá trị vào biến 'Tong'
    Tong = sum(eval(PT) for x in PhamVi)
    return Tong


                    ###---------- Chương trình ----------###
print('###################################################')
print('##                Nhập số để tính:               ##')
print('## [1]: Tính giá trị của giai thừa               ##')
print('## [2]: Tìm nghiệm của phương trình 1 ẩn         ##')
print('## [3]: Tính tổng phương trình (Summation)       ##')
print('###################################################')
BaiToan = int(input('Nhập số 1, 2 hoặc 3 để tiếp tục:'))
# Yêu cầu người dùng nhập lại nếu giá trị không đúng
while BaiToan !=1 and BaiToan !=2 and BaiToan !=3:
    BaiToan = int(input('Xin hãy nhập lại:'))
# Lần lượt kiểm tra giá trị của biến BaiToan để sử dụng hàm tính cho phù hợp
if BaiToan == 1:
    print('Tính giá trị của số giai thừa a!')
    KetQua = Giaithua()
    print('Kết quả cần tìm là:', KetQua)
elif BaiToan == 2:
    print('##############################################')
    print('##    Tìm nghiệm của phương trình 1 ẩn      ##')
    print('##############################################')
    print('##          Nhập số 1,2,3 để tính:          ##')
    print('## [1]: Phương trình bậc nhất               ##')
    print('## [2]: Phương trình bậc hai                ##')
    print('## [3]: Phương trình bâc ba                 ##')
    print('##############################################')
    GPT = int(input('Nhập số 1, 2 hoặc 3 để tiếp tục:'))
    # Mặc định cho giá trị của NghiemBoi = False, nếu trong quá trình giải phương trình cho ra nghiệm kép hoặc nghiệm bội thì giá trị của NghiemBoi sẽ trờ thành False
    NghiemBoi = False
    # Yêu cầu người dùng nhập lại nếu giá trị không đúng
    while GPT != 1 and GPT != 2 and GPT != 3:
        GPT = int(input('Xin hãy nhập lại:'))
    if GPT == 1:
        print('Giải phương trình bậc nhất ax+b=0')
        SoNghiem,Nghiem = PTBN()
    elif GPT == 2:
        print('Giải phương trình bậc hai ax^2+bx+c=0')
        SoNghiem, Nghiem = PTBH()
    elif GPT == 3:
        print('Giải phương trình bậc ba ax^3+bx^2+cx+d=0')
        SoNghiem, Nghiem = PTBB()
    # Sau khi giải phương trình, kiểm tra xem phương trình có nghiệm bội không
    if NghiemBoi == True:
        print('Phương trình có nghiệm bội')
    # In kết quả
    KetQuaPT()
elif BaiToan == 3:
    KetQua = Summation()
    print('Tổng cần tìm là:',KetQua)
print('----------Kết thúc----------')
input('Vui lòng nhấn Enter để thoát')