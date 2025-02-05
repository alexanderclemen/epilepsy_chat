import pandas as pd
import sys
sys.path.append("..")

import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.constants import TO_DATA

data = pd.read_csv(f'{TO_DATA}cwe_data.csv', sep=';')

predictors = ['repetition', 
          'retraction', 
          'unfilled_pause', 
          'unfilled_pause_longer', 
        #   'unfilled_pause_longest', # only 1 datapoint, correlated with 'unfilled_pause_longer'
        #   'nonword', 'filled_pause', # do not exist
          'error', 
          'nr_lines', 
          'nr_words', 
          'nr_words_per_line', 
          'age_months', 
          #'gender' #TODO: Code gender in 0 and 1
          ]

X = data[predictors] # Features
y = data['cwe_sick'] # Labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# get the feature importances
feature_importances = rf_model.feature_importances_

# plot the feature importances
plt.figure(figsize=(10, 6))
plt.barh(predictors, feature_importances, color='skyblue')
plt.xlabel('Feature Importance')
plt.title('Feature Importance in Random Forest')
plt.show()

# Print feature importances for each predictor
for feature, importance in zip(predictors, feature_importances):
    print(f'{feature}: {importance:.4f}')