###Soal Tes Dasa untuk menghitung jarak atau selisih huruf

abj = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
angk = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

def soal():    
    a1 = input("h 1: ")
    a2 = input("h 2: ")
    a3 = input("h 3: ")
    aa = [a1,a2,a3]

    aa.sort()

    if aa[0] in abj:
        ang1 = abj.index(aa[0])
        print(angk[ang1])

    if aa[1] in abj:
        ang2 = abj.index(aa[1])
        print(angk[ang2])

    if aa[2] in abj:
        ang3 = abj.index(aa[2])
        print(angk[ang3])

    print(aa)
    print(f"{angk[ang2]-angk[ang1]} <----> {angk[ang3]-angk[ang2]} ")

    if angk[ang2]-angk[ang1] < angk[ang3]-angk[ang2]:
        print("Jawaban :", a1)
    else:
        print("Jawaban :", a3)

start = True
wStop = 0    
while start:
    soal()
    wStop = input("Lanjut soal selanjutnya? (Y/N) : ")
    if(wStop == 'Y' or wStop == 'y'):
        continue
    else:
        break