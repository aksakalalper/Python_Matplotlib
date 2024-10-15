import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''
yil=[2011,2012,2013,2014,2015]
oyuncu1=[8,10,12,7,9]
oyuncu2=[7,12,5,15,21]
oyuncu3=[18,20,22,10,3]

#stack plot // yigin grafikte her deger birbirinin ustune eklenir.
plt.plot([],[],color="red",label="oyuncu1")
plt.plot([],[],color="blue",label="oyuncu2")
plt.plot([],[],color="orange",label="oyuncu3")
plt.legend()
plt.title("gol sayilari")
plt.xlabel("yil")
plt.ylabel("gol sayisi")
plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["red","blue","orange"])
plt.show()


#pie chart // pasta grafigi seklinde grafik olusturuldu.
goalTypes="penalti","kaleden kaleye","serbest vurus"
goals=[12,35,7]
colors=["blue","red","orange"]
plt.pie(goals,labels=goalTypes,colors=colors)
plt.show()

#bar grafigi // 
plt.bar([1,2,3,4,5],[50,40,70,80,20],label="bmw",width=0.5)
plt.bar([1,2,3,4,5],[30,20,50,10,20],label="audi",width=0.5)
plt.xlabel("gun")
plt.ylabel("km")
plt.title("arac bilgileri")
plt.legend()
plt.show()

'''
yaslar=[10,22,23,14,55,60,45,34,78,75]
plt.hist(yaslar,histtype='bar',rwidth=0.8)
plt.xlabel("yas gruplari")
plt.ylabel("kisi sayisi")
plt.title("histogram grafigi")
plt.show()


