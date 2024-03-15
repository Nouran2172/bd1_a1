import sys
import pandas as pd

def load_dataset(file_path):

    try:
        # Read the CSV file as a DataFrame
        dataframe = pd.read_csv(file_path)
        return dataframe
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        sys.exit(1)
    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

def main():
    # Check if the user provided a file path as an argument
    if len(sys.argv) != 2:
        print("Usage: python load.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Load the dataset
    dataset = load_dataset("train_titanic.csv")
    
    # Display the loaded dataset
    print("Loaded dataset:")
    print(dataset)

if __name__ == "__main__":
    main()