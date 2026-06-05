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

<img width="1599" height="727" alt="scanner_homepage" src="https://github.com/user-attachments/assets/4a9cb365-e4bf-4833-933c-5c3a1e344b80" />

### Dashboard

<img width="1598" height="728" alt="dashboard_page" src="https://github.com/user-attachments/assets/c2666d22-a07d-4305-8851-ce1b3ce1d24c" />

### Analytics

<img width="1599" height="729" alt="analytics_page" src="https://github.com/user-attachments/assets/af5361d3-ec31-4fe5-a293-32e484099d3d" />

### Search History

<img width="1599" height="729" alt="search_history" src="https://github.com/user-attachments/assets/16bbc2cd-50bb-44ca-8ab1-9a0b5b086adb" />

### About Page

<img width="1599" height="728" alt="about_page(1)" src="https://github.com/user-attachments/assets/3ad1124a-87ea-4ede-b809-f55192f68c90" />
<img width="1599" height="726" alt="about_page(2)" src="https://github.com/user-attachments/assets/6c80321a-b849-4bb0-be94-2cc016b0eec8" />

### Phishing Detection Example

<img width="1599" height="724" alt="negative_result" src="https://github.com/user-attachments/assets/878c568d-db5f-44a2-b445-1708aeec49cb" />

### Safe URL Detection Example

<img width="1600" height="900" alt="positive result" src="https://github.com/user-attachments/assets/aecd315c-4aa4-47f0-98a1-a6bad5cefd6d" />

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

