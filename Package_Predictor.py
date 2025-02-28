import pandas as pd
import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("placement-dataset.csv")
X = data[["cgpa"]]
y = data["package"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Function to predict LPA
def predict_lpa():
    try:
        cgpa = float(entry.get())
        predicted_lpa = model.predict([[cgpa]])[0]
        result_label.config(text=f"🎯 Estimated LPA: {predicted_lpa:.2f} LPA", fg="blue")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid CGPA.")

# GUI Setup
root = tk.Tk()
root.title("Package Predictor")
root.geometry("450x300")
root.configure(bg="#f4f4f4")

# Outer Frame (Box Effect)
frame = tk.Frame(root, bg="white", bd=3, relief="solid", padx=20, pady=20)
frame.pack(pady=30)

# Title Label
tk.Label(frame, text="📦 Package Predictor", font=("Arial", 14, "bold"), fg="#333", bg="white").pack(pady=5)

# CGPA Input Label
tk.Label(frame, text="📚 Enter CGPA:", font=("Arial", 12), bg="white").pack(pady=5)
entry = tk.Entry(frame, font=("Arial", 14), width=10, justify="center", bd=2, relief="solid")
entry.pack(pady=5)

# Predict Button
predict_btn = tk.Button(frame, text="🔍 Predict LPA", font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", command=predict_lpa)
predict_btn.pack(pady=10)

# Result Label
result_label = tk.Label(frame, text="", font=("Arial", 14, "bold"), bg="white", fg="black")
result_label.pack(pady=10)

root.mainloop()
