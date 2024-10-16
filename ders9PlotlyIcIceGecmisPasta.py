import pandas as pd
import plotly.express as px

# Örnek veri seti oluştur
data = {
    'Kategori': ['Gıda', 'Gıda', 'Gıda', 'İçecek', 'İçecek', 'Giyim', 'Giyim'],
    'Alt Kategori': ['Meyve', 'Sebze', 'Tahıl', 'Sıcak', 'Soğuk', 'Kadın', 'Erkek'],
    'Değer': [500, 300, 200, 150, 250, 350, 150]
}

df = pd.DataFrame(data)

# Sunburst chart oluştur
fig = px.sunburst(
    df,
    path=['Kategori', 'Alt Kategori'],
    values='Değer',
    title='Kategori ve Alt Kategorilere Göre Değerler'
)

# Yüzdelikleri göstermek için customdata kullan
fig.update_traces(textinfo='label+percent entry', texttemplate='%{label}: %{percentEntry:.2%}')

# Grafiği göster
fig.show()
