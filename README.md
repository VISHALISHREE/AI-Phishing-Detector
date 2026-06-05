# AI Phishing URL Detector

## Overview

AI Phishing URL Detector is a machine learning-based web application that identifies whether a URL is legitimate or potentially malicious. The system analyzes URL characteristics using TF-IDF feature extraction and a trained machine learning model to classify URLs into different categories.

This project was developed as an academic and portfolio project to demonstrate the application of Machine Learning in Cybersecurity.

---

## Features

* Real-time URL phishing detection
* Machine Learning based classification
* TF-IDF feature extraction
* User-friendly web interface
* Scan history tracking using SQLite
* Analytics dashboard
* Threat intelligence visualization
* Responsive UI design

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite

### Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Joblib

---

## Project Structure

AI-Phishing-Detector

├── app.py

├── database.py

├── feature_extraction.py

├── train_tfidf_model.py

├── predict_tfidf.py

├── templates/

├── static/

├── dataset/

├── project_screenshots/

└── README.md

---

## Machine Learning Model

The project uses:

* TF-IDF Vectorization
* Supervised Machine Learning Classification

### Performance

Accuracy Achieved:

94.29%

Classification Categories:

* Benign
* Phishing
* Malware
* Defacement

---

## Screenshots

## Screenshots

### Home Page

![Home Page](./project_screenshots/scanner_homepage.png)

### Dashboard

![Dashboard](./project_screenshots/dashboard_page.png)

### Analytics

![Analytics](./project_screenshots/analytics_page.png)

### Search History

![Search History](./project_screenshots/search_history.png)

### About Page

![About Page](./project_screenshots/about_page\(1\).png)

### Phishing Detection Example

![Phishing Detection](./project_screenshots/negative_result.png)

### Safe URL Detection Example

![Safe URL Detection](./project_screenshots/positive%20result.png)

---

## Installation

### Clone Repository

git clone https://github.com/VISHALISHREE/AI-Phishing-Detector.git

### Move into Project Folder

cd AI-Phishing-Detector

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Application

python app.py

---

## Future Enhancements

* Deep Learning based phishing detection
* Real-time URL reputation checking
* Browser extension integration
* Threat intelligence API integration
* Improved phishing detection accuracy

---

## Author

Vishalishree

Department of Information Technology

SRM Institute of Science and Technology

