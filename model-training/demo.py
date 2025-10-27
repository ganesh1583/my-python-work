# ==========================
# House Price Prediction ML
# ==========================

# Import required libraries
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Step 1: Prepare the data
# --------------------------
# Training data (house size in sq ft vs price in $)
X = np.array([[500], [1000], [1500], [2000], [2500]])   # Input feature
y = np.array([150000, 300000, 450000, 600000, 750000])  # Target (output)

# --------------------------
# Step 2: Create the model
# --------------------------
model = LinearRegression()

# --------------------------
# Step 3: Train the model
# --------------------------
model.fit(X, y)

# --------------------------
# Step 4: Check learned parameters
# --------------------------
print("Model learned:")
print(f"  Weight (slope): {model.coef_[0]:.2f}")
print(f"  Bias (intercept): {model.intercept_:.2f}")

# --------------------------
# Step 5: Make a prediction
# --------------------------
size = int(input("Enter size : "))  # example input
pred_price = model.predict([[size]])
print(f"\nPredicted price for a {size} sq ft house: ${pred_price[0]:.2f}")

# --------------------------
# Step 6: Visualize the result
# --------------------------
plt.scatter(X, y, color="blue", label="Training Data")
plt.plot(X, model.predict(X), color="red", label="Model Prediction")
plt.scatter(size, pred_price, color="green", s=100, label="Predicted Point")
plt.xlabel("House Size (sq ft)")
plt.ylabel("Price ($)")
plt.title("House Price Prediction using Linear Regression")
plt.legend()
plt.show()

