# Integrated Security Framework for Canara Bank

## Overview

This Flask-based web application enhances security measures for Canara Bank's operations. It features a dual-layer security mechanism with Real-Time Fraud Detection and Multi-Factor Authentication (MFA) for call authentication.

## Features

- **Real-Time Fraud Detection**: Employs machine learning models to identify and alert on fraudulent transactions instantly.
- **Multi-Factor Authentication (MFA) for Calls**: Generates unique codes for call authentication between bank representatives and customers.

## Project Structure

- `app.py`: Flask application initialization and route definitions.
- `requirements.txt`: Dependencies required for the project.
- `best_model.pkl`: Serialized machine learning model for fraud detection.
- `static/`: Frontend static files like CSS and JavaScript.
  - `bank_cust.css`: Styles for the bank customer interface.
  - `bank_cust.js`: Client-side logic for the bank customer interface.
  - `style.css`: General styling.
- `templates/`: HTML templates for the application.
  - `bank_cust.html`: Bank customer interface.
  - `index.html`: Landing page.

## Machine Learning Approach
Development of the machine learning model using historical transaction data. The model employs various algorithms for anomaly detection to predict fraudulent activities.

### Running the Application

Clone the repository and navigate to the directory:

```sh
git clone https://github.com/pritiyadav888/canara.git
cd canara 

## Install dependencies

```sh
pip install -r requirements.txt

### Start the Flask app
flask run
# or
python app.py

### Usage
- Access the application at `http://127.0.0.1:5000/`.
- Use `/predict` for fraud detection.
- Use `/request-code` for MFA during calls.
- Interactive ML model demo at `/model`.

### Contributing

Contributions are encouraged. Please fork the repo, make changes, and submit a pull request.

### Contact

- **Priti Yadav**
- LinkedIn: [Priti Yadav](https://www.linkedin.com/in/priti-yadavml/)
- Email: [pritiyadav888@gmail.com](mailto:pritiyadav888@gmail.com)
- Project: [GitHub Repository](https://github.com/pritiyadav888/canara)
