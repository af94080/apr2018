# Here is the challenge, Titanic–
# Machine Learning from Disaster 
# from Kaggle 
# https://www.kaggle.com/c/titanic

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df = pd.read_csv('/home/asif/titanic_data.csv')
# /Users/arulfrancis/Documents/books/karim_tf/train.csv
df = pd.read_csv('/Users/arulfrancis/Documents/books/karim_tf/train.csv')

# specify the parameters for the graph:

fig = plt.figure(figsize=(18,6), dpi=1600) 
alpha=alpha_scatterplot = 0.2 
alpha_bar_chart = 0.55
fig = plt.figure()
ax = fig.add_subplot(111)

# Draw a bar diagram for showing who survived versus who did not:

ax1 = plt.subplot2grid((2,3),(0,0))
ax1.set_xlim(-1, 2)             
df.Survived.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
plt.title("Survival distribution: 1 = survived")

# Plot a graph showing survival by Age

plt.subplot2grid((2,3),(0,1))
plt.scatter(df.Survived, df.Age, alpha=alpha_scatterplot)
plt.ylabel("Age")                       
plt.grid(b=True, which='major', axis='y')  
plt.title("Survival by Age: 1 = survived")

# Plot a graph showing distribution of the passengers classes:

ax3 = plt.subplot2grid((2,3),(0,2))
df.Pclass.value_counts().plot(kind="barh", alpha=alpha_bar_chart)
ax3.set_ylim(-1, len(df.Pclass.value_counts()))
plt.title("Class dist. of the passengers")

# Plot a kernel density estimate of the subset of the 1st class passengers' age:

plt.subplot2grid((2,3),(1,0), colspan=2)
df.Age[df.Pclass == 1].plot(kind='kde')    
df.Age[df.Pclass == 2].plot(kind='kde')
df.Age[df.Pclass == 3].plot(kind='kde')
plt.xlabel("Age")    
plt.title("Age dist. within class")
plt.legend(('1st Class', '2nd Class','3rd Class'),loc='best')

# Plot a graph showing passengers per boarding location:

ax5 = plt.subplot2grid((2,3),(1,2))
df.Embarked.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
ax5.set_xlim(-1, len(df.Embarked.value_counts()))
plt.title("Passengers per boarding location")

# Finally, we show all the subplots together:

plt.show()

