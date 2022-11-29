nilai =int(input("Masukkan nilai Anda = "))
if(nilai <=100):
    if(nilai >85):
        print("Huruf mutu Anda adalah A.")
    elif(nilai >75):
        print("Huruf mutu Anda adalah B.")
    elif(nilai >65):
        print("Huruf mutu Anda adalah C.")
    elif(nilai >55):
        print("Huruf mutu Anda adalah D.")
    elif(nilai <=55):
        print("Huruf mutu Anda adalah E.")
else:
    print("Nilai di luar jangkauan.")
'''
Struktur kendali pada Python
ada if, else, elif
Tingkatannya
if -> elif -> elif
Elif akan dicek jika if salah
else akan dicek jika elif ataupun if salah
digunakan indentasi tab, dengan memperhatikan kesejajaran posisi dari setiap kata kunci struktur kendali
'''