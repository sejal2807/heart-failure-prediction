# heart-failure-prediction

Predicting Mortality of Heart Failure Patients with ML

This dataset contains the medical records of 299 patients who had heart failure, collected during their follow-up period, where each patient profile has 13 clinical features.

Data Source -
https://archive.ics.uci.edu/ml/datasets/Heart+failure+clinical+records

The dataset is first preprocessed and libraries that are used to analyze and visualize the data are pandas, numpy, matplotlib, seaborn. Seaborn's boxplot is used for outlier detection and feature engineering is done for removing outliers in dataset. For feature selection, selectkbest and chisquare are used. Got the accuracy 76% from logistic regression, 72% from KNN, 73% from DecisionTree. Lime for model interpretation and confusion matrix for evaluation are plotted.

And deployed the model on heroku using flask as backend and html and css as frontend.

https://heartfailurepatient-prediction.herokuapp.com/

