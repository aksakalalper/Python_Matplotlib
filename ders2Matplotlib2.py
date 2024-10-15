import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,2,100) #1 ile 2 arasini 100 esit parcaya boler
plt.plot(x,x,label="x=x",color="red",linestyle="dashed") 
plt.plot(x,x**2,label="x=x**2",color="blue",linestyle="dashed")
plt.plot(x,x**3,label="x=x**3",color="orange",linestyle="dashed")
plt.title("x ve usleri") #graifk adi verildi
plt.xlabel("x ekseni") #x eksen etiketi.
plt.ylabel("y ekseni") #y eksen etiketi
plt.legend() #her grafik ogesinin etiket bilgisi yazdirildi.
plt.show() #graifk gosterildi.

