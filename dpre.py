import pandas as pd

def data_preprocessing(dataframe):
    
    
   # Example preprocessing steps
    # Data Cleaning
    

    dataframe['Age'] = dataframe['Age'].fillna(dataframe['Age'].mean())
    dataframe = dataframe.drop(['Cabin'], axis=1)
    dataframe['Embarked'] = dataframe['Embarked'].fillna(dataframe['Embarked'].mode()[0])


    X = dataframe.drop(['PassengerId','Name','Ticket'],axis=1)
    encoded_data = pd.get_dummies(X, columns=['Sex', 'Embarked'])
    encoded_data
    
    return encoded_data

def main():
    # Load the dataset
    dataframe = pd.read_csv('train_titanic.csv')
    
    # Perform data preprocessing
    preprocessed_data = data_preprocessing(dataframe)
    
    # Save preprocessed data to CSV
    preprocessed_data.to_csv('res_dpre.csv', index=False)

if __name__ == "__main__":
    main()