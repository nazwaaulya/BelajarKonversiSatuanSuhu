#konverensi satuan temperatur 

print("/nPROGRAM KONVERENSI TEMPERATURE\n")

print("======Celcius======")
#celcius
celcius = float(input('Masukkan Suhu dalam Celcius : '))
print("suhu adalah", celcius, "Celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah : ", reamur, "Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah : ",fahrenheit, "Fahrenheit")

#Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah : ", kelvin, "Kelvin")

print("======Reamur======")
reamur = float(input('Masukkan suhu dalam Reamur : '))
print("suhu dalam reamur adalah : ", reamur, "Reamur")

#celcius
celcius = (5/4) * reamur
print("Suhu dalam celcius adalah: ", celcius , "celcius")

#fahrenheit
fahrenheit = ((9/4) * reamur ) + 32
print("Suhu dalam fahrenheit adalah: ", fahrenheit , "fahrenheit")

#kelvin
kelvin = ((5/4) * reamur ) + 273
print("Suhu dalamm kelvin adalah: ", kelvin , "kelvin")

print("======Fahrenheit======")
fahrenheit = float(input('Masukkan suhu dalam fahrenheit : '))
print("Suhu dalam fahrenheit adalah : ", fahrenheit, "fahrenheit")

#celcius
celcius = 5/9 * (fahrenheit - 32)
print("Suhu dalam celcius adalah: ", celcius , "celcius")

#reamur
reamur = 4/9 * (fahrenheit - 32)
print("Suhu dalam reamur adalah: ", reamur , "reamur")

#kelvin
celcius = 5/9 * (fahrenheit - 32)
kelvin = celcius + 273
print("Suhu dalam kelvin adalah : ", kelvin, "kelvin")

print("======Kelvin======")
kelvin = float(input('Masukkan suhu dalam kelvin : '))  # Ubah input menjadi float
print("Suhu dalam kelvin adalah:", kelvin, "kelvin")

# Celcius
celcius = kelvin - 273.15  
#Dalam skala Celsius, nol mutlak setara dengan -273.15 °C.
#Oleh karena itu, kita menggunakan angka 273.15 untuk mengkoreksi perbedaan antara skala Kelvin dan skala Celsius.
print("Suhu dalam celcius adalah:", celcius, "celcius")

# Reamur
reamur = 4/5 * celcius  # Gunakan variabel celcius yang sudah dihitung sebelumnya
print("Suhu dalam reamur adalah:", reamur, "reamur")

# Fahrenheit
fahrenheit = (9/5 * celcius) + 32  # Gunakan variabel celcius yang sudah dihitung sebelumnya
print("Suhu dalam fahrenheit adalah:", fahrenheit, "fahrenheit")
