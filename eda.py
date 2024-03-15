import pandas as pd
from scipy.stats import skew

def main():
    # Load the dataset
    data = pd.read_csv("res_dpre.csv")


    # Calculate correlations in eda-in-2
    correlation_edafemale = data['Sex_female'].corr(data['Survived'])
    correlation_edamale = data['Sex_male'].corr(data['Survived'])



    # Calculate mean fare in eda-in-1
    mean_fare = data['Fare'].mean()
    

    # Calculate skewness of Embarked_C in eda-in-3
    skewness_embarked_c = skew(data['Embarked_C'], axis=0, bias=True)


    # Write results to text files if needed
    with open('eda-in-1.txt', 'w') as f:
        f.write(f'Mean fare: {mean_fare}\n')

    with open('eda-in-2.txt', 'w') as f:
        f.write(f'Correlation between Sex_female and Parch: {correlation_edafemale}\n')
        f.write(f'Correlation between Sex_male and Parch: {correlation_edamale}\n')
    
    with open('eda-in-3.txt', 'w') as f:
        f.write(f'Skewness of Embarked_C: {skewness_embarked_c}\n')
        # f.write(f'Correlation between Sex_male and Parch: {correlation_edamale}\n')

if __name__ == "__main__":
    main()