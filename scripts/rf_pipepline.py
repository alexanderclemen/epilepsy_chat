# This script is the random forest classifier pipeline
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys
sys.path.append("../")

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score

from src.constants import TO_DATA, predictors

def main(input_file:str) -> str:
  """Trains and evaluates a Random Forest Classifier.
  
  ...

  Args:
      input_file (str): name of .csv file (here: cwe_all_selected.csv, cwe_chronic_selected.csv, cwe_newonset_selected.csv)

  Returns:
      _type_: _description_
  """
  print(f'{input_file}')
  
  # read in data
  df = pd.read_csv(f'{TO_DATA}{input_file}', sep=';')
  
  X = df[predictors] # they are taken from a script in scr.rf
  y = df['cwe_sick'] # Labels
  
  print(f'Predictors: {predictors}')

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=666)

  # create the model with 100 trees, 
  rf_model = RandomForestClassifier(n_estimators=100,
                                    random_state=666)

  # fit model
  rf_model.fit(X_train, y_train)

  y_pred = rf_model.predict(X_test)

  # calculate the accuracy
  accuracy = accuracy_score(y_test, y_pred)
  print(f'Accuracy: {accuracy * 100:.2f}%')
  
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
  parser.add_argument('input_file', type=str, help="Path to the input file.")
    
  args = parser.parse_args()
  
  main(args.input_file)
