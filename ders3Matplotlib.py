import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



''' alt alta grafik olusturuldu.
x=np.linspace(1,2,10) #1 ile 2 arasini 10 esit parcaya boler
fig,axs= plt.subplots(3) #3 tane alt eksene sahip bir figur olusturuldu.
axs[0].plot(x,x,color="red",marker="o") #eksen atamalari yapildi.
axs[0].set_title("grafik1") #grafik isimleri verildi.
axs[1].plot(x,x**2,color="blue",marker="*") #eksen atamalari yapildi.
axs[1].set_title("grafik2")
axs[2].plot(x,x**3,color="green",marker="x") #eksen atamalari yapildi.
axs[2].set_title("grafik3")
plt.tight_layout() #grafik yerlesimi birbiri icine girmeyecek sekilde ayarlandi.
plt.show()

'''

x=np.linspace(1,2,10) #1 ile 2 arasini 10 esit parcaya boler
fig,axs= plt.subplots(2,2) #2x2 matris seklinde figur olusturuldu.
fig.suptitle("grafikler")
axs[0,0].plot(x,x,color="red",marker="o") #eksen atamalari yapildi.
axs[0,0].set_title("grafik1") #grafik isimleri verildi.
axs[0,1].plot(x,x**2,color="blue",marker="*") #eksen atamalari yapildi.
axs[0,1].set_title("grafik2")
axs[1,0].plot(x,x**3,color="green",marker="x") #eksen atamalari yapildi.
axs[1,0].set_title("grafik3")
axs[1,1].plot(x,x**3,color="orange",marker="+") #eksen atamalari yapildi.
axs[1,1].set_title("grafik4")
plt.tight_layout()
plt.show()