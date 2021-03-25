usia=19
x=int(input("Berapa Umur Anda :"))
if usia < x :
    print("Anda Cukup Umur.")
    y= input("Apakah Anda sudah lulus ujian kualifikasi (Y/T)")
    if y == "Y" :
        print("Anda dapat mendaftar di kursus")
    elif y == "T" :
        print("Anda tidak dapat mendaftar di kursus.")
else :
    print("Anda Belum Cukup Umur.")
