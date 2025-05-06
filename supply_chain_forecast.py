import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Step 1: Connect to PostgreSQL
engine = create_engine("postgresql://postgres:123456@localhost:5432/supply_chain_db")

# Step 2: Load data from PostgreSQL
df = pd.read_sql("SELECT * FROM retail_orders", con=engine)
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

# Step 3: Basic data cleanup
df['order_demand'] = df['order_demand'].astype(str).str.replace('(', '-').str.replace(')', '').astype(float)
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Step 4: Label encoding for categorical columns
categorical_cols = ['product_code', 'warehouse', 'product_category', 'open', 'promo', 'stateholiday', 'schoolholiday']

le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col].astype(str))




# Step 5: Features and target
features = ['product_code', 'warehouse', 'product_category', 'day', 'month', 'year', 'open', 'promo', 'stateholiday', 'schoolholiday', 'petrol_price']

X = df[features]
target = 'order_demand'
y = df[target]

print("\nFeature Data Types:")
print(df[features].dtypes)


# Step 6: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 8: Predict and evaluate
y_pred = model.predict(X_test)
print("\nModel Evaluation:")
print("R^2 Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Step 9: Save predictions for Power BI
X_test['Predicted_Demand'] = y_pred
X_test['Actual_Demand'] = y_test.values

# Save to PostgreSQL
X_test.to_sql("demand_predictions", con=engine, index=False, if_exists="replace")
print("\n✅ Forecasted demand saved to 'demand_predictions' table.")
