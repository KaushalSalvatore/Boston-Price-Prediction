## Boston Price Prediction Using machine learning algorithm

This is machine learning web app that use to predict Boston house price accroding to given paramenter in data set.

## Click the following link for view the deployed project:
- https://boston-price-prediction.onrender.com/

## Webview screenshots
![page_1](https://github.com/KaushalSalvatore/Boston-Price-Prediction/assets/50286592/a86240c5-a381-413d-aeb9-dc2c628c9f9f)
![page_2](https://github.com/KaushalSalvatore/Boston-Price-Prediction/assets/50286592/4d4be79f-2db7-4d1c-8713-b3ccf7ec2313)


## ML Project lifeCycle Stp by Step

- Data Collection
- Data Analysis
- Data Visualization
- Feature Engineering
- Feature Selection
- Model Building
- Model Evalution
- Hyper Parameter Tunning
- Creating Pickle file
- Web App using Flask
- Deployment

#### Data set
```bash
    from sklearn.datasets import load_boston
```

#### Data Set Characteristics:
- Number of Instances: 506 
- Number of Attributes: 13 numeric/categorical predictive.

#### Data Attribute Information

- **CRIM:** per capita crime rate by town
- **ZN:** proportion of residential land zoned for lots over 25,000 sq.ft.
- **INDUS:** proportion of non-retail business acres per town
- **CHAS:** Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- **NOX:** nitric oxides concentration (parts per 10 million)
- **RM:** average number of rooms per dwelling
- **AGE:** proportion of owner-occupied units built prior to 1940
- **DIS:** weighted distances to five Boston employment centres
- **RAD:** index of accessibility to radial highways
- **TAX:** full-value property-tax rate per $10,000
- **PTRATIO:** pupil-teacher ratio by town
- **B:** 1000(Bk - 0.63)^2 where Bk is the proportion of black people by town
- **LSTAT:** % lower status of the population

## Use Technologies

**python packages:** Pandas, Numpy, Scikit-learn, matplotlib ,seaborn

**ML Algorithms:** LinearRegression

**Framework:** Flask

**frontend:** Html, CSS

## Run Locally

Clone the project

```bash
  git clone https://github.com/KaushalSalvatore/Boston-Price-Prediction.git
```
Install dependencies

```bash
  pip install -r requirements. txt
```

Start the local server

```bash
  Python index.py or index.py
```
## Deploy on a Github

To deploy this project on github use this following command in the project folder.

Initializing a new repository
```bash
  git init
```

A gitignore file specifies intentionally untracked files that Git should ignore.
```bash
  touch .gitignore
```
Add all the files 
```bash
  git add .
```
Check file status 
```bash
  git status
```
Commit all the file on git
```bash
  git commit -m "your message"
```
Push all the code on github
```bash
  git push <your_branch_name>
```
Push code
```bash
  git push -u origin <your_branch_name>
```
Push code forcefully 
```bash
  git push origin <your_branch_name> --force
```
## Create Docker Image
- **Dockerfile:** first create a docker file that is a text document that contains all the commands a user could call on the command line to assemble an image.
- **FROM** python:3.8.17 (to create a blank base image)
- **COPY** . /app (allows us to copy a file or folder from the host system into the docker image)
- **WORKDIR** /app (define the working directory of a Docker container at any given time)
- **RUN** pip install -r requirements.txt (execute any commands in a new layer on top of the current image and commit the results)
- **EXPOSE** 8000 (tells Docker that a container listens for traffic on the specified port.)
- **CMD** python index.py (specifies the instruction that is to be executed when a Docker container starts.)


## command for create and Deploy docker image in a Docker hub
```bash
  Create a docker image 
  docker build -t kaushalpandey/boston-price-prediction .
```
```bash
  run docker image  
  docker run -p 8000:8000 boston-price-prediction	
```
```bash
  docker login
  docker build -t boston-price-prediction .
```
```bash
  push to docker hub
  docker push kaushalpandey/flask-helloworld:latest
```
```bash
  pull docker image
  docker pull kaushalpandey/boston-price-prediction:latest
```



## Important Definition :
- **LinearRegression**
- **coefficients**
- **intercept**
- **Assumptions**
- **mean squared error**
- **Mean absolute error**
- **R square**
- **Adjusted r square**





## Feedback

if you have any suggetion and feedback and need any kind of project related help reach me out at
[linkedin](https://www.linkedin.com/in/kaushal-pandey-067898165/)

#### Thank You 