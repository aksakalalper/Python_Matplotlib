import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# CSV dosyası oku
file="data.csv"
data=pd.read_csv(file) 
df=pd.DataFrame(data=data)
print(df.info())
print(df["Torque [Nm]"].nunique()) 

# Veri setleri
x = df["Rotational speed [rpm]"]
y = df["Torque [Nm]"]
y1=df.sort_values("Torque [Nm]",ascending=False)["Torque [Nm]"]

# Grafik oluşturma 
plt.pie(y1,autopct="%0.3f%%")

# Başlık ve etiketler
plt.title('Motor devir analizi')

# Lejandı göster
plt.legend()

# Grafiği göster
plt.tight_layout()
plt.show()
