import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv(r'C:\Users\HP\Downloads\house_prices_dataset.csv')
print(df.head())
z=df.shape
print(z)
x=df[['square_feet','distance_to_city(km)','num_rooms']]
y=df['price']
model = LinearRegression()
model.fit(x, y)
new=pd.DataFrame([[2248,22,3]], columns=['square_feet','distance_to_city(km)','num_rooms'])
prediction = model.predict(new)
print(prediction)

