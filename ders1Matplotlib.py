#veriler ile gorsellestirme ve grafik olsuturma islemleri yapilir.
import numpy as np
import matplotlib.pyplot as plt

y=np.arange(10,16)
x=np.arange(1,7) 
plt.plot(x,y,marker="o",linestyle="dashed") #x yatay ve y dikey sekilde grafik olusturuldu. cizgi ve nokta ozellikleri belirtildi.
plt.axis([1,8,10,17]) #eksen sinirlari olusturuldu.
plt.title("Grafik adi")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.show()

