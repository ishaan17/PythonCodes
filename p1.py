from scipy import stats
import matplotlib.pyplot as plt
Population=[1000,200,400,300,150,220,2000,1500,400,300,150,100,1560,300,351,100,300,1000,234,351,234,102,290]
Cities=["Agra","MuzaffarNagar","Merrut","Shamli","Khatauli","Saharanpur","a","n","b","b","mh"}
Population.sort()
tv=int(0.1*len(Population))
Population=Population[tv:]
Population=Population[:len(Population)-tv]
for i in range(len(Population)):
    y.append(5)
plt.plot(Population,Cities,"g^")
