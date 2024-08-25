import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data("API_SP.POP.TOTL_DS2_en_csv_v2_3401680.csv"):
    # Load the dataset
    df = pd.read_csv(API_SP.POP.TOTL_DS2_en_csv_v2_3401680.csv)
    return df

def preprocess_data(df):
    # Print column names to understand the dataset structure
    print(df.columns)
    
    # Drop rows where 'SP.POP.TOTL' (total population) or 'Year' is NaN
    df = df[['Country Name', 'Year', 'SP.POP.TOTL']].dropna()
    
    # Convert 'Year' to integer
    df['Year'] = df['Year'].astype(int)
    
    return df

def plot_population_distribution(df):
    # Set up the matplotlib figure
    plt.figure(figsize=(14, 7))
    
    # Create a bar plot for total population by year
    sns.barplot(x='Year', y='SP.POP.TOTL', data=df, palette='viridis')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Total Population')
    plt.title('Total Population by Year')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Show plot
    plt.tight_layout()
    plt.show()

def main():
    # Load and preprocess data
    file_path = 'world_population.csv'
    df = load_data(file_path)
    df = preprocess_data(df)
    
    # Plot data
    plot_population_distribution(df)

if __name__ == "__main__":
    main()
