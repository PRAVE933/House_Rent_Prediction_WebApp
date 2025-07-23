import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Step 1: Load the dataset
df = pd.read_csv("House_Rent_Dataset.csv")

# Step 2: Drop unwanted columns
df.drop(['Posted On', 'Floor', 'Area Locality', 'Point of Contact'], axis=1, inplace=True)

# Step 3: Encode categorical columns
le = LabelEncoder()
df['Area Type'] = le.fit_transform(df['Area Type'])
df['City'] = le.fit_transform(df['City'])
df['Furnishing Status'] = le.fit_transform(df['Furnishing Status'])
df['Tenant Preferred'] = le.fit_transform(df['Tenant Preferred'])

# Step 4: Define input features and target
X = df[['BHK', 'Size', 'Bathroom', 'Area Type', 'City', 'Furnishing Status', 'Tenant Preferred']]
y = df['Rent']

# Step 5: Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Save the model
joblib.dump(model, "rent_model.pkl")

print("✅ Model trained and saved as 'rent_model.pkl'")
