import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x=np.linspace(-10,9,20)
y=x**3
z=x**2
figure=plt.figure()

'''
axes=figure.add_axes([0.1,0.1,0.8,0.8]) #kenardan bosluk olusturuldu. ilk 2 degisken alttan ve soldan boslugu belirtir.
axes.plot(x,y,"red") 
axes.set_ylabel("y ekseni")
axes.set_xlabel("x ekseni") 
axes2=figure.add_axes([0.2,0.6,0.25,0.25]) 
axes2.plot(x,z,"blue") 
axes2.set_ylabel("y ekseni")
axes2.set_xlabel("x ekseni")
plt.show() 

axes=figure.add_axes([0,0,1,1]) #iki grafik ortak eksende birlestirildi.
axes.plot(x,y,color="red",label="grafik1") 
axes.plot(x,z,color="blue",label="grafik2")
axes.legend(loc=1) 
plt.show()

'''
fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(10,10)) #subplot ile birden fazla grafik eklenir.
axes[0].plot(x,y)
axes[0].set_title("küpü")
axes[1].plot(x,z)
axes[1].set_title("karesi")
plt.tight_layout()
fig.savefig("figure.png")
plt.show()
