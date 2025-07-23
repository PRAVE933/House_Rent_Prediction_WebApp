🏡 House Rent Prediction Web App (Machine Learning + Streamlit)

This project is a user-friendly and interactive **web application** that predicts house rent based on user inputs such as BHK, area, location, and furnishing status.  
It combines **machine learning** and **Streamlit** to offer real-time rent prediction using a trained regression model.

📌 Features Included

🤖 1. Machine Learning Rent Predictor
- 📊 Accepts user input (BHK, size, location, etc.)
- 🧠 Predicts rent using a trained regression model
- ⚙️ Model built with `scikit-learn`, trained on real housing data
- 💾 Model saved and loaded using `joblib`

🌐 2. Interactive Web Interface**
- 🖥️ Built using Streamlit framework
- 🧩 Real-time prediction on form submission
- 🖱️ Easy-to-use and clean UI
- 📉 Model logic separated from interface for maintainability

 💾 Files Included

- `app.py` → Main Streamlit web application  
- `main.py` → Model training script  
- `rent_model.pkl` → Trained ML model file  
- `House_Rent_Dataset.csv` → Dataset used for training  
- `requirements.txt` → Required Python libraries  
- `README.md` → Project documentation (this file)

🛠️ Tools & Technologies Used

| Tool              | Purpose                          |
|-------------------|----------------------------------|
| Python            | Programming language             |
| Pandas & NumPy    | Data processing & handling       |
| scikit-learn      | Machine learning (regression)    |
| Joblib            | Save/load trained model          |
| Streamlit         | Build web interface              |
| Git & GitHub      | Version control & collaboration  |

 ⚙️ How to Use

1. ✅ Clone the Repository
bash
git clone https://github.com/PRAVE933/House_Rent_Prediction_WebApp.git
cd House_Rent_Prediction_WebApp

2. 📦 Install Dependencies
bash
pip install -r requirements.txt

3. ▶️ Run the Streamlit App
bash
streamlit run app.py

4. 🌐 Visit in Your Browser

Open the link shown in terminal, usually:
[http://localhost:8501](http://localhost:8501)

 🧠 About the Model

The model is trained on a **realistic housing dataset** containing features like:

* 🛏️ Number of bedrooms (BHK)
* 📐 Area in square feet
* 📍 Location
* 🛋️ Furnishing status

It uses a **regression algorithm** from `scikit-learn` to estimate rental price.

 📂 Project Structure

House_Rent_Prediction_WebApp/
├── app.py                  # Streamlit frontend
├── main.py                 # ML model training
├── rent_model.pkl          # Trained model file
├── House_Rent_Dataset.csv  # Training dataset
├── requirements.txt        # Dependencies
└── README.md               # Documentation

👩‍💻 Author
Jeeru Sowmya – Aspiring Data Analyst and AI Engineer
🔗 (https://www.linkedin.com/in/jeeru-sowmya-800603253)




