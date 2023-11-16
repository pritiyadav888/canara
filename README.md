<h1 align="center">Integrated Security Framework for Canara Bank</h1>
Hi ![](https://user-images.githubusercontent.com/18350557/176309783-0785949b-9127-417c-8b55-ab5a4333674e.gif)Welcome to this project 
===================================================================================================================================

This Flask-based web application enhances security measures for Canara Bank's operations. It features a dual-layer security mechanism with Real-Time Fraud Detection and Multi-Factor Authentication (MFA) for call authentication.
--------------------------------------------------

## Features

<ul>
<li><b>Real-Time Fraud Detection</b>: Employs machine learning models to identify and alert on fraudulent transactions instantly.</li>
<li><b>Multi-Factor Authentication (MFA) for Calls</b>: Generates unique codes for call authentication between bank representatives and customers.</li>
</ul>

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

#### Clone the repository and navigate to the directory

* git clone https://github.com/pritiyadav888/canara.git
* cd canara
* pip install -r requirements.txt
* flask run
##### or
* python app.py
* Access the application at `http://127.0.0.1:5000/`.
* Use `/predict` for fraud detection.
* Use `/request-code` for MFA during calls.
* Interactive ML model demo at `/model`.


### Contributing

Contributions are encouraged. Please fork the repo, make changes, and submit a pull request.

### Contact

* **Priti Yadav**
* 🖥️ Connect on [Linkedin](http://www.linkedin.com/in/priti-yadavml/)
* ✉️  You can contact me at [pritiyadav888@gmail.com](mailto:pritiyadav888@gmail.com)
* Project: [GitHub Repository](https://github.com/pritiyadav888/canara)
