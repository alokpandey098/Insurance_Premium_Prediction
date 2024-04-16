<div id="top"></div>

# Insurance Premium Prediction Projecct
Build a solution that should able to predict the premium of the personal for health insurance.

![alt text](image.png)

### About Dataset
The insurance.csv dataset contains 1338 observations (rows) and 7 features (columns). The dataset contains 4 numerical features (age, bmi, children and expenses) and 3 nominal features (sex, smoker and region) that were converted into factors with numerical value designated for each level.

### Please check the link below:
Streamlit Deployment - *[Current Live Link]*: 
<b>[Streamlit-app*](https://insurancepremiumprediction-2gdje8hzyaeepigzb5rgq4.streamlit.app/)</b>
<br><br>

<br>
Elastic Beanstalk:
[*Deployment Link Live-Beanstalk*](http://insurance-env-1.eba-ztjhym2p.ap-south-1.elasticbeanstalk.com/)

### Documentation:

[High Level Design](https://github.com/alokpandey098/Insurance_Premium_Prediction/blob/main/Documentation/High%20Level%20Document.pdf)

[Low Level Design](https://github.com/alokpandey098/Insurance_Premium_Prediction/blob/main/Documentation/Low%20Level%20Document.pdf)

[Project Architecture](https://github.com/alokpandey098/Insurance_Premium_Prediction/blob/main/Documentation/Project%20Architecture.pdf)

[Project Wireframe:](https://github.com/alokpandey098/Insurance_Premium_Prediction/blob/main/Documentation/Project%20Wireframe.pdf)

[Detailed Project Report](https://github.com/alokpandey098/Insurance_Premium_Prediction/blob/main/Documentation/Detailed%20Project%20Report.pdf)


<p align="right">(<a href="#top">back to top</a>)</p> 

### Steps Taken:
* Installed Python, VS Code and Git.
* Created an account on Atlas MongoDB.
* Download the source dataset from [Kaggle Repository](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction).
* For Regression Problem algorithm decided to predict the feature `expenses`.
* Deployed on AWS-EC2.

### Data Cleaning:
* Data was cleaned which has an header issue, missing values, misplaced values and outliers.

### EDA and Feature Engineering:
* In this step, we will apply Exploratory Data Analysis (EDA) to extract insights from the data set to know which features have contributed more in predicting Forest fire by performing Data Analysis using Pandas and Data visualization using Matplotlib & Seaborn.
* Done Feature scaling by Standard Scaler in which data lies between -1 and +1.

### Model Building 
* For Regression Problem algorithm decided to predict the feature `expenses`.
* Models used : **Linear regression, Random forest, Decision tree, Ada-boost and Grad-boost.**

<p align="right">(<a href="#top">back to top</a>)</p> 

### Model Selection
* HyperParameter Tuning with Gridsearch CV is done for both Regression.
* For Regression: Metrics are r2 score, adjusted r2 and mean absolute error.

### Flask, Docker and  AWS Deployment:
* Build a Flask App with Docker file.
* Deployed on AWS-EC2 with CI/CD pipeline through Github actions.

### ML-Flow and DVC [facilitate collaboration ml-lifecycle]:
- Used MLflow for experiment tracking, logging metrics, parameters, and artifacts during model training.
- Used DVC to version control and manage your large datasets efficiently.
- By integrating MLflow and DVC, we can create a more robust and reproducible machine learning workflow that addresses both code and data versioning concerns.

<p align="right">(<a href="#top">back to top</a>)</p> 


#### Prediction Screen:

![Screenshot_predict](https://github.com/alokpandey098/Insurance_Premium_Prediction/blob/main/Img/Screenshot%202024-04-15%20205952.png)

### **Technologies used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)


### **Tools used**
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![AWS-EC2](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

## Contact
[![Alok Kumar|LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)][reach_linkedin]
[![Alok Kumar|G-Mail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)][reach_gmail]

<p align="right">(<a href="#top">back to top</a>)</p> 


<!-- Reach Contact -->
[reach_linkedin]: https://www.linkedin.com/in/alok-kumar087
[reach_gmail]: mailto:kalok0575@gmail.com?subject=Github


