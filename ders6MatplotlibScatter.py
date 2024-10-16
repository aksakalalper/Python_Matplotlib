import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyası oku
file="engine_data.csv"
data=pd.read_csv(file) 
df=pd.DataFrame(data=data)

# Birinci veri seti
x1 = df["Engine rpm"]
y1 = df["Lub oil pressure"]

# İkinci veri seti
x2 = df["Engine rpm"]
y2 = df["Fuel pressure"]

# Grafik oluşturma
plt.scatter(x1, y1, label='Yağ basıncı',s=1,color="red")
plt.scatter(x2, y2, label='Yakıt basıncı',s=1,color="blue")

# Başlık ve etiketler
plt.title('Motor devir analizi')
plt.xlabel('Motor deviri')
plt.ylabel('Yağ basıncı/Yakıt basıncı')

# Lejandı göster
plt.legend()

# Grafiği göster
plt.show()

