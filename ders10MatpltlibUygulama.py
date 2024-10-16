import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini oku
df = pd.read_csv('StudentPerformanceFactors.csv')

# Temel istatistikleri hesapla
print("Veri Seti Bilgileri:")
print(df.info())
print("\nTemel İstatistikler:")
print(df.describe())

# Eksik değerleri kontrol et
print("\nEksik Değerler:")
print(df.isnull().sum())

# Basit bir görselleştirme (örneğin, histogram)
df.hist(figsize=(10, 8))
plt.suptitle("Veri Seti Histogramları")
plt.show()

# Sadece sayısal sütunları seç
numerical_df = df.select_dtypes(include=['float64', 'int64'])

# Korelasyon matrisi oluştur
corr_matrix = numerical_df.corr()

# Korelasyon matrisini yazdır
print("\nKorelasyon Matrisi:")
print(corr_matrix)

# Isı haritası ile korelasyon matrisi görselleştirme
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Korelasyon Matrisi Isı Haritası")

# Isı haritası ile korelasyon matrisi görselleştirme
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Korelasyon Matrisi Isı Haritası")
plt.show()
