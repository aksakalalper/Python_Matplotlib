import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file="StudentPerformanceFactors.csv"
data=pd.read_csv(file)
df=pd.DataFrame(data=data)
print(df.nunique(),df.info())

# Her benzersiz öğenin adını ve sayısını bul
unique_counts = df['Hours_Studied'].value_counts()

# Sonuçları iki ayrı diziye sakla
items = unique_counts.index.tolist() # Benzersiz öğelerin adları
counts = unique_counts.values.tolist() # Her öğenin sayıları

# Birleşik veri seti
labels = items
sizes = counts

# Pasta grafiği oluşturma
plt.pie(sizes, labels=labels, autopct="%0.3f%%")
plt.title('Birleşik Veri Seti')
plt.show()





