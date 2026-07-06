# Student Placement Prediction

A Machine Learning based web application that predicts whether a student is likely to get placed based on academic and skill-related parameters.

## Features

- Predicts student placement chances
- User-friendly web interface using Flask
- Machine Learning model using Random Forest
- Fast and simple prediction
- Clean HTML and CSS design

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML
- CSS

## Project Structure

```
Student-Placement-Prediction/
│── app.py
│── train_model.py
│── dataset.csv
│── placement_model.pkl
│── requirements.txt
│── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Input Parameters

- CGPA
- IQ Score
- Profile Score
- Internship (0/1)
- Communication Score
- Projects
- Aptitude Score

## Output

The application predicts whether the student is:

- Likely to Get Placed
- Not Likely to Get Placed

## Installation

Clone the repository

```bash
git clone https://github.com/varshukavi479-oss/Student-Placement-Prediction.git
```

Go to project folder

```bash
cd Student-Placement-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train_model.py
```

Run the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

## Future Improvements

- Better UI Design
- Multiple ML Algorithms Comparison
- Deployment using Render
- User Login System
- Database Integration

## Author

**Varshini**


---
⭐ If you found this project useful, please give it a Star.
