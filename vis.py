import matplotlib.pyplot as plt
import pandas as pd

def create_histogram(dataframe):
    # Convert boolean values to numerical (1 for True, 0 for False)
    embarked_c_numeric = dataframe['Fare'].astype(int)
    
    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.hist(embarked_c_numeric, bins=100, color='skyblue', edgecolor='black')
    plt.title('Histogram of Fare')
    plt.xlabel('Fare')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('vis.png')
    plt.close()

if __name__ == "__main__":
    # Load the dataset
    dataframe = pd.read_csv("res_dpre.csv")
    
    # Create histogram
    create_histogram(dataframe)