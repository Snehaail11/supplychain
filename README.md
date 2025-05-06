---

## 📦 Supply Chain Demand Forecasting

This project forecasts retail product demand using machine learning and visualizes the results in Power BI. It combines data engineering, model building, and business intelligence.

---

### 🧠 Project Objective

Predict future product demand across different warehouses using historical retail data, and visualize insights to support inventory and logistics decisions.

---

### ⚙️ Tech Stack

* **Python** (pandas, scikit-learn, SQLAlchemy)
* **PostgreSQL** (data storage)
* **Power BI** (reporting and visualization)
* **Random Forest Regressor** (forecasting model)

---

### 🗃️ Data Source

Table: `retail_orders` (PostgreSQL)

Columns used:

* `product_code`
* `warehouse`
* `product_category`
* `date`
* `order_demand`
* `open`, `promo`, `stateholiday`, `schoolholiday`, `petrol_price`

---

### 📈 Steps Performed

1. **Connect to PostgreSQL** and fetch data.
2. **Clean data** (handle negative demand, parse dates).
3. **Encode categorical features**.
4. **Split data** into train/test sets.
5. **Train a Random Forest** regression model.
6. **Predict future demand** and evaluate with R² and RMSE.
7. **Save predictions** to a new PostgreSQL table: `demand_predictions`.
8. **Visualize in Power BI**:

   * Forecast accuracy by product or category.
   * Actual vs predicted demand.

---

### 🖥️ How to Run

1. Start PostgreSQL and ensure `supply_chain_db` is running.
2. Run the script:

```bash
python supply_chain_forecast.py
```

3. Open Power BI, connect to PostgreSQL → table `demand_predictions`.
4. Build visuals like:

   * Bar charts for accuracy
   * Line charts for predicted vs actual demand

---

### 📊 Power BI Tips

* Use `SUM` of `Actual_Demand` and `Predicted_Demand` for aggregation.
* Create calculated columns like `ForecastAccuracy = 1 - ABS(Predicted - Actual) / Actual`.
* Use `product_code` or `warehouse` on the axis.

---

### ✅ Result

* RMSE and R² scores printed in console
* Clean predictions in PostgreSQL
* Interactive dashboard in Power BI

---
