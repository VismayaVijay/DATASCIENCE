
#creating dataframe from student list


import pandas as pd1
data1 = [['Shreya',20],['Rakshit',22],['Srijan',18]]

df1 =pd1.DataFrame(data1,columns=['Name', 'Age'])

print(df1)