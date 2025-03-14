import math 
from math import cos, acos, sqrt, cbrt, pi, e, log
################################################################################################################################
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
## Các nghiệm không có giá trị sẽ được đánh dấu bằng kí tự "x"  
################################################################################################################################
#Phép cộng
def Phep_Cong(num_1: float, num_2: float): 
    """
    Hàm thực hiện phép cộng 
    """
    return num_1 + num_2
#Đoạn code này có vai trò thực hiện phép tính cộng. Trong đoạn code có sử dụng Try-Except để báo ta nhập lại sau khi nhập sai.
#Break dùng để dừng vòng lặp lại.
#Sau khi ra kết qu, nếu muốn thực hiện tính toán tiếp thì gõ bất kì phím gì, nếu không thì gõ 'không'

#phép trừ
def Phep_Tru(num_1: float, num_2: float):
    """
    Hàm thực hiện phép trừ 
    """
    return num_2 - num_1
#Đoạn code này có vai trò thực hien phép tiính trừ. cấu trúc đoạn code thì giống như trên

#phép nhân
def Phep_Nhan(num_1: float, num_2: float):
    """
    Hàm thực hiện phép nhân 
    """
    return num_1 * num_2
#Đoạn code này có vai trò thực hiện phép tính nhân, cấu trúc đoạn code tương tự như trên

#phép chia
def Phep_Chia(num_1, num_2):
    try: 
        return num_1 / num_2 
    except ZeroDivisionError:
        return "Invalid method"
#Đoạn code này có vai trò thực hiện phép tính chia, cấu trúc đoạn code tương tự như trên

#Binh phuong
def Binh_Phuong(num):
    """
    Hàm thực hiện tính bình phương 1 số 
    """
    return num**2 
#Đoạn code này có vai trò thực hiện phép tính bình phương, cấu trúc đoạn code tương tự như trên

#căn bậc 2
def Can_Bac_2(num):
    """
    Tính căn bậc 2 một số 
    """
    result = math.sqrt(num)
    return result
#Đoạn code này có vai trò thực hiện phép tính căn bậc 2, cấu trúc đoạn code nhìn chung tương tự như trên.
#Có điều lần này ta cần thêm điều kiện so<0 vì căn bậc 2 không âm. Với lại ta cũng thêm hàm sqrt() trong thư viện math để thực hiện phép tính


# trị tuyệt đôi
def Tri_Tuyet_Doi(num):
    return math.fabs(num)
#Đoạn code này có vai trò thực hiện phép tính trị tuyệt đối, cấu trúc đoạn code tương tự như trên, ta cung thêm hàm abs có sẵn trong python để thực hiện phép tính trị tuyệt đối.

#UCLN
def ucln(num_1, num_2):
    #đoạn code có vai trò tính ước chung lớn nhất của 2 số, sử dụng hàm gcd trong thư viện math để tính.
    return math.gcd(num_1, num_2)

#BCNN
def bcnn(num_1, num_2):
    #Đoạn code có vai trò tính BCNN. Do thư viện math không có hàm tính BCNN nên ta sẽ tính bằng cách nhân 2 số lại rồi chia UCLN. UCLN thì làm như trên.
    so_1 = num_1
    so_2 = num_2
    # Tính UCLN để tính BCNN
    ucln = math.gcd(so_1, so_2)
    bcnn = abs(so_1 * so_2) // ucln  # Công thức tính BCNN
    return bcnn 

def PhanTichThuaSoNguyenTo(number):
    '''
    Đầu tiên ta lập hàm để tính các thừa số nguyen tố, bắt đầu với i=2 vì đây là snt nhỏ nhất. Ta sẽ dùng vòng lặp while lồng vào nhau
    vòng lặp while thứ nhất là để kiểm soát giá trị của i, bắt đầu từ số 2 và sau đó tăng dâần lên. Còn vòng lặp thứ 2 là để kiểm tra 
    xem n có chia hết i nhiều lần hay không.
    ví dụ n=2024, n%2==0 nên in ra 2(đây là tsnt đầu tiên), sau đó 2024//2=1012. Tiếp tục ta thấy 1012%2==0 nên in ra 2(tsnt tiếp theo), 1012//2=506
    cứ làm như vậy cho tới khi phân tích ra các số là 2,2,2,11,23
    '''
    #Đoạn code có vai trò tính các thừa số nguyên tố của một số bất kì
    i = 2
    thua_so = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            thua_so.append(i)
    if number > 1:
        thua_so.append(number)
    return thua_so

def to_hop(n, k):
    '''
    Đoạn code này có vai trò tính toán tổ hợp. Trong đoạn code này có sử dụng hàm factorial từ thư viện math để tính giai thừa cho
    công thức tổ hợp.
    '''
    if k > n:
        return 'không tồn tại'  # Tổ hợp không tồn tại nếu k lớn hơn n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k)) #Sử dụng thư viện math để tạo phép tính giai thừa

def chinh_hop(n, k):
    if k > n:
        return 'Không tồn tại'  # Chỉnh hợp không tồn tại nếu k lớn hơn n
    return math.factorial(n) // math.factorial(n - k)

#Hàm tính hoán vị
def hoan_vi(n):
    return math.factorial(n)

### ---------- Hàm tính giai thừa ---------- ###
def Giaithua(a):
    b = 1
    i = 1
    while i <= a:
        b = i * b
        i = i + 1
    return b

### ---------- Giải phương trình 1 ẩn ---------- ###
##-----Hàm giảỉ phương trình bậc 1, 1 ẩn theo dạng ax+b=c-----##
def PTBN(a, b):
    if a == 0:
        if b == 0:
            SoNghiem = 'Vô số nghiệm'
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
def PTBH(a, b, c):
    # Kiểm tra xem gía trị a có bằng 0 hay không, nếu bằng thì yêu cầu nhập lại cho đến khi a khác 0
    if a == 0: 
        return PTBN(b, c)
    else: 
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
def PTBB(a, b, c, d):
    # Case: Third-degree polynomial (a ≠ 0)
    if a != 0:
        delta = b**2 - 3 * a * c
        k = ((9 * a * b * c) - (2 * b**3) - (27 * a**2 * d)) / (2 * sqrt(abs(delta)**3)) if delta != 0 else 0
        m = b**2 - 27 * a**2 * d

        if delta == 0:
            if m == 0:
                x = -b / (3 * a)
                return "Phương trình có nghiệm bội: x = {}".format(x)
            else:
                x = (-b + cbrt(m)) / (3 * a)
                return (f"Phương trình có 1 nghiệm: x = {x}")
        elif delta < 0:
            x = (sqrt(abs(delta)) / (3 * a)) * ((cbrt(k + sqrt(k**2 + 1))) + (cbrt(k - sqrt(k**2 + 1)))) - (b / (3 * a))
            return (f"Phương trình có 1 nghiệm: x = {x}")
        else:
            if abs(k) > 1:
                x = ((sqrt(delta) * abs(k)) / (3 * a * k)) * ((cbrt(abs(k) + sqrt(k**2 - 1))) + (cbrt(abs(k) - sqrt(k**2 - 1)))) - (b / (3 * a))
                return (f"Phương trình có 1 nghiệm: x = {x}")
            else:
                x1 = (2 * sqrt(delta) * cos(acos(k) / 3) - b) / (3 * a)
                x2 = (2 * sqrt(delta) * cos((acos(k) / 3) - (2 * pi / 3)) - b) / (3 * a)
                x3 = (2 * sqrt(delta) * cos((acos(k) / 3) + (2 * pi / 3)) - b) / (3 * a)
                return (f"Phương trình có 3 nghiệm: x1 = {x1}, x2 = {x2}, x3 = {x3}")
    # Case: Second-degree polynomial or lower if a == 0
    else:
        # Check if it's a second-degree equation
        if b != 0:
            delta = c**2 - 4 * b * d
            if delta == 0:
                x = -c / (2 * b)
                return (f"Nghiệm kép: x = {x}")
            elif delta < 0:
                return ("Phương trình vô nghiệm")
            else:
                x1 = (-c - sqrt(delta)) / (2 * b)
                x2 = (-c + sqrt(delta)) / (2 * b)
                return (f"2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
        # Linear equation if b == 0
        elif c != 0:
            x = -d / c
            return (f"Nghiệm của phương trình bậc nhất: x = {x}")
        else:
            # Handle case for d == 0 as a special case with infinite solutions
            if d == 0:
                return ("Phương trình có vô số nghiệm")
            else:
                return ("Phương trình vô nghiệm")

###---------- Tính tổng giá trị của phương trình (Summation) ----------###
def Summation(start, end):
    PT = input('Nhập phương trình:')
    xBD = start
    xKT = end
    # Cho các giá trị của x vào 1 dãy
    PhamVi = range(xBD,xKT+1)
    # Lần lượt thay giá trị của x vào phương trình và cộng tổng các giá trị vào biến 'Tong'
    Tong = sum(eval(PT) for x in PhamVi)
    return Tong

def main_program():
    while True: 
        print("Các chương trình tính")
        print("*"*15)
        print("1. Cộng")
        print("2. Trừ")
        print("3. Nhân")
        print("4. Chia")
        print("5. Bình phương")
        print("6. Căn bặc 2")
        print("7. Trị tuyệt đối")
        print("8. Tìm ước chung lớn nhất")
        print("9. Bội chung nhỏ nhất")
        print("10. Phân tích thừa số nguyên tố")
        print("11. Tính tổ hợp")
        print("12. Tính chỉnh hợp")
        print("13. Tính hoán vị")
        print("14. Tính giai thừa")
        print("15. Tính Phương trình bậc nhất")
        print("16. Tính Phương trình bậc hai")
        print("17. Tính Phương trình bậc ba")
        print("18. Tính tổng dãy số")

        phep_tinh = int(input("Mời chọn phương trình tính"))
        while phep_tinh <= 0 or phep_tinh > 18: 
            print("Không hợp lệ, mời chọn lại!!")
            phep_tinh = int(input("Mời nhập chương trình tính: "))
        
        if phep_tinh == 1: 
            num_1 = float(input("Nhập số 1: "))
            num_2 = float(input("Nhập số 2: "))
            print("Kết quả: ",Phep_Cong(num_1, num_2))
        elif phep_tinh == 2: 
            num_1 = float(input("Nhập số 1: "))
            num_2 = float(input("Nhập số 2: "))
            print("Kết quả: ",Phep_Tru(num_1, num_2))
        elif phep_tinh == 3: 
            num_1 = float(input("Nhập số 1: "))
            num_2 = float(input("Nhập số 2: "))
            print("Kết quả: ",Phep_Nhan(num_1, num_2))
        elif phep_tinh == 4: 
            num_1 = float(input("Nhập số 1: "))
            num_2 = float(input("Nhập số 2: "))
            print("Kết quả: ",Phep_Chia(num_1, num_2))
        elif phep_tinh == 5: 
            num = float(input("Nhập số: "))
            print("Kết quả: ", Binh_Phuong(num))
        elif phep_tinh == 6: 
            num = float(input("Nhập số: "))
            print("Kết quả: ", Can_Bac_2(num))
        elif phep_tinh == 7: 
            num = float(input("Nhập số: "))
            print("Kết quả: ", Tri_Tuyet_Doi(num))
        elif phep_tinh == 7: 
            num = float(input("Nhập số: "))
            print("Kết quả: ", Tri_Tuyet_Doi(num))
        elif phep_tinh == 8: 
            num_1 = float(input("Nhập số 1: "))
            num_2 = float(input("Nhập số 2: "))
            print("Kết quả: ", ucln(num_1, num_2))
        elif phep_tinh == 9: 
            num_1 = float(input("Nhập số 1: "))
            num_2 = float(input("Nhập số 2: "))
            print("Kết quả: ", bcnn(num_1, num_2))
        elif phep_tinh == 10: 
            num = float(input("Nhập số: "))
            print("Kết quả: ", PhanTichThuaSoNguyenTo(num))
        elif phep_tinh == 11: 
            n = int(input("Nhập n: "))
            k = int(input("Nhập k: "))
            print("Kết quả: ", to_hop(n, k))
        elif phep_tinh == 12: 
            n = int(input("Nhập n: "))
            k = int(input("Nhập k: "))
            print("Kết quả: ", chinh_hop(n, k))
        elif phep_tinh == 13: 
            num = float(input("Nhập số: "))
            print("Kết quả: ", hoan_vi(num))
        elif phep_tinh == 14: 
            num = float(input("Nhập số: "))
            print("Kết quả: ", Giaithua(num))
        elif phep_tinh == 15: 
            a = float(input("Nhập hệ số 1: "))
            b = float(input("Nhập hệ số 2: "))
            print("Kết quả: ", PTBN(a,b))
        elif phep_tinh == 16: 
            a = float(input("Nhập hệ số 1: "))
            b = float(input("Nhập hệ số 2: "))
            c = float(input("Nhập hệ số 3: "))
            print("Kết quả: ", PTBH(a,b, c))    
        elif phep_tinh == 16: 
            a = float(input("Nhập hệ số 1: "))
            b = float(input("Nhập hệ số 2: "))
            c = float(input("Nhập hệ số 3: "))
            d = float(input("Nhập hệ số 3: "))
            print("Kết quả: ", PTBB(a,b, c, d)) 
        else: 
            start = float(input("Điểm bắt đầu: "))
            end = float(input("Điểm kết thúc: "))
            print("Kết quả: ", Summation(start, end))
        
        hoi = input("Continue? (y/n)")
        if hoi == 'n':
            print("Cảm ơn đã sử dụng")
            break 
        