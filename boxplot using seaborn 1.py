
import seaborn

    

tip = seaborn.load_dataset('titanic')
  
seaborn.boxplot(x ='survived', y ='age', data = tip)

#use violinplot or histplot instead of boxplot