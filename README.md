# 🛡️ Phishing URL Detection using Machine Learning

## 🚀 About the Project

Phishing attacks often begin with something as simple as a suspicious-looking URL. This project explores how machine learning can be used to identify potentially malicious URLs by analyzing their structural characteristics.

The system extracts meaningful features from a submitted URL and passes them to a trained **Random Forest Classifier**. The model then estimates the probability that the URL belongs to the phishing class and converts that probability into an easy-to-understand risk level.

The project combines **machine learning, feature engineering, and a Flask-based web application** to create an end-to-end phishing URL detection system.

## 🔍 How It Works

The system follows a straightforward pipeline. A user provides a URL, which is first processed by the feature extraction module. The extractor analyzes different aspects of the URL, such as its length, domain structure, number of subdomains, suspicious keywords, and other characteristics.

These extracted features are then mapped to the feature format expected by the trained model. The Random Forest classifier processes the resulting feature vector and produces a probability for the prediction.

Finally, the application converts this probability into a phishing score and presents the result as **Low Risk, Medium Risk, or High Risk**, making the prediction easier to interpret.

## 🧠 Machine Learning

The classification model used in this project is a **Random Forest Classifier** implemented with Scikit-learn. The model is trained using the supplied phishing URL dataset, with 80% of the data used for training and 20% reserved for testing.

The Random Forest consists of **100 decision trees**, and the trained model is saved using Joblib as `phishing_model.pkl`. This allows the Flask application to load the already-trained model and perform predictions without retraining it every time the application starts.

The training script also calculates feature importance, making it possible to examine which URL characteristics contribute most strongly to the model's decisions.

## 🧩 Features Extracted

Rather than relying only on the complete URL as text, the system converts it into a set of numerical and boolean characteristics.

The feature extractor looks at properties such as **URL length, domain length, number of dots, number of hyphens, number of subdomains, presence of an IP address, presence of an `@` symbol, suspicious URL patterns, HTTPS usage, suspicious keywords, and suspicious TLDs**.
The system also checks for keywords commonly associated with phishing attempts, including terms such as `login`, `verify`, `update`, `secure`, `bank`, `account`, `confirm`, and `password`. It additionally checks for several potentially suspicious TLD strings such as `.xyz`, `.tk`, `.ml`, `.ga`, and `.top`.

## ⚡ Risk Scoring

The prediction returned by the Random Forest is converted into a percentage-based phishing score.

| Phishing Score | Risk Level     |
| -------------: | -------------- |
|   **0–39.99%** | 🟢 Low Risk    |
|  **40–69.99%** | 🟠 Medium Risk |
|    **70–100%** | 🔴 High Risk   |

These thresholds are defined in the Flask application and are used to determine the risk category returned to the frontend.

## 🌐 Web Application

The project uses **Flask** to provide the web application and prediction API. When a URL is submitted, the backend receives it through a `POST` request to the `/predict` endpoint, extracts its features, sends them to the trained model, and returns the prediction as JSON.

The response contains the submitted URL, phishing score, risk level, display color, and the extracted URL features, allowing the result to be presented in a user-friendly way.

## ⚙️ Installation

Clone the repository and install the required Python dependencies:

```bash
pip install flask pandas scikit-learn joblib
```

Make sure the phishing dataset is available before training the model.

## 🏋️ Train the Model

Run the training script:

```bash
python train_model.py
```

The script loads the dataset, splits it into training and testing data, trains the Random Forest classifier, evaluates its performance, and saves the trained model as:

```text
phishing_model.pkl
```

The training process also displays the dataset dimensions, the number of training and testing samples, the achieved accuracy, and the most important features identified by the model.

## ▶️ Run the Application

After training the model, start the Flask application:

```bash
python app.py
```

The application loads the saved model and starts the Flask development server. The web interface is served from the root route `/`.

Open the local Flask URL shown in the terminal to access the application.

## 🧪 Example

A URL such as:

```text
https://www.google.com/search?q=python
```

will be analyzed based on its structural characteristics.

On the other hand, a URL containing characteristics such as an IP address, suspicious keywords, multiple unusual subdomains, or suspicious domain patterns may produce a higher phishing score.

The feature extractor includes example URLs for testing, including both legitimate and intentionally suspicious examples.

## 📊 Why This Approach?

The goal of this project is not simply to create a collection of manually defined phishing rules. Instead, the URL characteristics are converted into features that can be learned by a machine-learning model.

This allows the classifier to identify combinations of characteristics that may be associated with phishing URLs rather than depending entirely on a single rule, keyword, or domain pattern.

## 🔮 Future Improvements

The current system focuses primarily on URL-based characteristics, which leaves several interesting directions for further development.

Future versions could incorporate additional information such as **DNS characteristics, domain age, certificate information, URL entropy, redirect behavior, webpage content, HTML features, and external domain reputation**. More advanced models could also be explored and compared using metrics such as precision, recall, F1-score, ROC-AUC, and confusion matrices.

The project could eventually evolve from a URL-only detector into a broader phishing detection system capable of combining multiple sources of evidence.

## ⚠️ Limitations

This system analyzes the characteristics of a URL and does not inspect the actual webpage, its HTML, JavaScript, visual appearance, DNS history, or external reputation services.

Therefore, the prediction should be treated as an **ML-based risk estimate rather than a definitive statement that a website is malicious or safe**.

The performance of the system also depends heavily on the quality and distribution of the dataset used to train the model.

## 🛠️ Technologies

**Python · Scikit-learn · Pandas · Flask · Joblib · Machine Learning**

## 📌 Disclaimer

This project is intended for **educational and research purposes**. The prediction generated by the model should not be considered a guaranteed determination of whether a URL is safe or malicious. Always verify suspicious links through trusted sources before entering sensitive information.

---

### ⭐ Built to explore how Machine Learning can be applied to real-world cybersecurity problems.
