# Integrated Security Framework for Canara Bank

Hi! ![waving hand](https://user-images.githubusercontent.com/18350557/176309783-0785949b-9127-417c-8b55-ab5a4333674e.gif) Welcome to this project

This Flask-based web application enhances security measures for any Bank's operations. It features a dual-layer security mechanism with Real-Time Fraud Detection and Multi-Factor Authentication (MFA) for call authentication.

--------------------------------------------------

### Demo 
* https://youtu.be/0ZrVQ9q6HkM

## Features

Project is deployed here -- https://hack-canara-85be2294d386.herokuapp.com/

<ul>
<li><b>Real-Time Fraud Detection</b>: Employs machine learning models to identify and alert on fraudulent transactions instantly.</li>
<li><b>Multi-Factor Authentication (MFA) for Calls</b>: Generates unique codes for call authentication between bank representatives and customers.</li>
</ul>

## Project Structure


- `app.py`: Flask application initialization and route definitions.
- `requirements.txt`: Dependencies required for the project.
- `best_model.pkl`: Serialized machine learning model for fraud detection.
- `best_fraud_detection_model.h5`: Serialized deep learning model for fraud detection.
- `static/`: Frontend static files like CSS and JavaScript.
  - `bank_cust.css`: Styles for the bank customer interface.
  - `bank_cust.js`: Client-side logic for the bank customer interface.
  - `style.css`: General styling.
- `templates/`: HTML templates for the application.
  - `bank_cust.html`: Bank customer interface.
  - `index.html`: Landing page.
  - `Report.html`: Data Insights.

## Machine Learning Approach

Development of the machine learning model using historical transaction data. The model employs various algorithms for anomaly detection to predict fraudulent activities.

### Running the Application

#### Clone the repository and navigate to the directory

* git clone https://github.com/pritiyadav888/canara.git

#### Setting Up a Virtual Environment
  For Mac/Linux Systems:
    * python3 -m venv venv
    * source venv/bin/activate
    * pip install -r requirements.txt

  For Windows Systems: 
    * python -m venv venv
    * venv\Scripts\activate
    * pip install -r requirements.txt
   
* flask run or python app.py
* Access the application at `http://127.0.0.1:5000/`.
* Use `/predict` for fraud detection.
* Use `/request-code` for MFA during calls.
* Interactive ML model demo at `/model`.

### About ML_notebooks 
* Use of TPOT and Tomek Links (mathematics-11-02862.pdf):

* TPOT: The first notebook employs TPOT (Tree-based Pipeline Optimization Tool), an automated machine learning tool that uses genetic algorithms to optimize machine learning pipelines. TPOT is particularly effective in selecting and tuning models and preprocessing methods, which is invaluable in scenarios like fraud detection where the selection of the right model and its hyperparameters can significantly impact performance.
Tomek Links: To address the class imbalance prevalent in credit card transaction data, the notebook utilizes Tomek links. This technique helps in rebalancing the dataset by removing certain instances from the majority class, thereby making the dataset more balanced and improving the model's ability to detect fraud, which is typically the rare class in such datasets.
* Dataset Characteristics: The dataset, comprising 284,807 transactions with only 492 fraudulent cases, presents a significant challenge due to this imbalance. The application of Tomek links is critical in enhancing the model's sensitivity to fraudulent transactions.
Transition to LightGBM due to Computational Constraints:

* Computational Intensity: While TPOT and Tomek links are effective, they can be computationally intensive, especially in cases of large datasets like those involving credit card transactions. This computational demand can make the process time-consuming and resource-intensive, which might not be feasible in all environments.
LightGBM: In the second notebook, the focus shifts to using LightGBM (Light Gradient Boosting Machine), a gradient boosting framework that uses tree-based learning algorithms. LightGBM is known for its efficiency in terms of speed and memory usage, making it a more practical choice for large datasets. It is particularly adept at handling large amounts of data and provides a good balance between model performance and computational efficiency.
Feature Importance Visualization: The notebook includes a feature importance graph generated by LightGBM. This graph is instrumental in identifying which features are most predictive of fraudulent transactions. For instance, features like V17, V14, and V12 are shown to be particularly important. Such insights are valuable for understanding the underlying patterns in the data and can inform further feature engineering and model refinement.
Integration of Multi-Factor Authentication (MFA) and Machine Learning in Fraud Detection:

### MFA Implementation 

* MFA Implementation: The system leverages the pyotp library to generate Time-based One-Time Passwords (TOTP), adding a layer of security in customer-bank interactions. This real-time code generation and verification, facilitated by Flask-SocketIO, play a crucial role in preventing phishing and similar fraudulent activities.
Machine Learning for Transaction Analysis: Alongside MFA, the system incorporates a machine learning model to analyze transaction data and predict potential fraud, issuing alerts when necessary. This dual approach of MFA for immediate transaction security and machine learning for pattern recognition and prediction forms a robust defense against fraud.
### Contributing

Contributions are encouraged. Please fork the repo, make changes, and submit a pull request.

### Contact

* **Priti Yadav**
* 🖥️ Connect on [Linkedin](http://www.linkedin.com/in/priti-yadavml/)
* ✉️  You can contact the team at [pritiyadav888@gmail.com](mailto:pritiyadav888@gmail.com)
* Project: [GitHub Repository](https://github.com/pritiyadav888/canara)





