import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Titanic = pd.read_csv("titanic.csv")

Titanic.head()
Titanic.columns
Titanic.shape
Titanic.isnull().sum()
plt.figure(figsize=(10, 6))

sns.heatmap(Titanic.isnull(), cmap="spring")

plt.show()
Titanic.drop("Cabin", axis=1, inplace=True)
Titanic.head()
Titanic.dropna(inplace=True)

Titanic.isnull().sum()
plt.figure(figsize=(10, 6))

sns.heatmap(Titanic.isnull(), cmap=False)

plt.show()

pd.set_dummies(Titanic["Sex"]).head()

sex = pd.set_dummies(Titanic["Sex"], drop_first=True)

sex.head(4)

pd.get_dummies(Titanic["Embarked"]).head(4)
embarked = pd.get_dummies(
    Titanic["Embarked"],
    drop_first=True
)

embarked.head(4)
pclass = pd.get_dummies(
    Titanic["Pclass"],
    drop_first=True
)

pclass.head(4)

Titanic = pd.concat(
    [Titanic, sex, embarked, pclass],
    axis=1
)
Titanic.head()
