
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('churn_data.csv')

X = df[['tenure','monthly_charges']]
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = LogisticRegression()
model.fit(X_train,y_train)

print("Model Accuracy:", model.score(X_test,y_test))
