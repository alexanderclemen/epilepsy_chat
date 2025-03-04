import pandas as pd
import argparse
import sys
sys.path.append("../")

import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.constants import TO_DATA
from src.rf_predictors import predictors


def main(input_file):
  
  print(f'{input_file}')
  
  # read in data
  df = pd.read_csv(f'{TO_DATA}{input_file}', sep=';')
  X = df[predictors] # Features
  y = df['cwe_sick'] # Labels
  
  print(f'Predictors: {predictors}')

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=666)

  # create the model with 100 trees, 
  rf_model = RandomForestClassifier(n_estimators=100,
                                    random_state=666)
  
  # min_samples_split: This controls the minimum number of samples required to split an internal node. A larger value would prevent the tree from splitting too often and reduce complexity.
  
  # min_samples_leaf: This controls the minimum number of samples required to be at a leaf node. Increasing this value helps simplify the tree and might be seen as a form of pruning because it forces the tree to generalize more.
  
  # max_leaf_nodes: If you want to control the maximum number of leaf nodes in each tree, you can set this parameter. It directly limits tree complexity by restricting the number of leaves.

  # fit model
  rf_model.fit(X_train, y_train)

  y_pred = rf_model.predict(X_test)

  # calculate the accuracy
  accuracy = accuracy_score(y_test, y_pred)
  print(f'Accuracy: {accuracy * 100:.2f}%')

 # check for robustness k fold cross validation
 # retain only experimment motivated features

  # get the feature importances
  feature_importances = rf_model.feature_importances_

  # plot the feature importances
  plt.figure(figsize=(10, 6))
  plt.barh(predictors , feature_importances, color='skyblue')
  plt.xlabel('Feature Importance')
  plt.title('Feature Importance in Random Forest')
  plt.show()

  # Print feature importances for each predictor
  for feature, importance in zip(predictors, feature_importances):
      print(f'{feature}: {importance:.4f}')
      
  # save output as csv
  outfile = pd.DataFrame({'data': input_file, 'accuracy': accuracy, 'predictors': predictors, 'feature_importances': feature_importances})
  return outfile.to_csv(f'{TO_DATA}{input_file.replace('.csv','')}_ac{round(accuracy,4)}_nrPred{len(predictors)}.csv', index=False, sep=';')

if __name__ == "__main__":
  # Parse arguments from command line
  parser = argparse.ArgumentParser(description="Train Random Forest model and visualize feature importances.")
  parser.add_argument('input_file', type=str, help="Path to the input CSV file.")
    
  args = parser.parse_args()
  
  main(args.input_file)
