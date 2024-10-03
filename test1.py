import pandas as pd

# Function to prepare and preprocess the data
def prepare_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Drop unnamed columns that may have been added by default
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

    # Handle missing data by replacing NaN with 0
    data.fillna(0, inplace=True)

    # Convert 'Chan' to categorical values: 1 for Phone Call, 2 for WhatsApp, 3 for Chatbot
    data['Chan'] = data['Chan'].astype(int)

    return data

# Function to calculate probabilities for a specific customer
def calculate_channel_probabilities(customer_id, data):
    # Filter for the specific customer based on ID
    customer_data = data[data['id_new'] == customer_id]

    # If no records exist for the customer
    if customer_data.empty:
        print(f"No data available for customer ID: {customer_id}")
        print("Available customers in the dataset:")
        print(data['id_new'].unique())  # List of all unique customer IDs in the dataset
        return

    # Debugging: Display customer-specific data
    print(f"\nCustomer Data for ID {customer_id}:\n", customer_data)

    # Count occurrences of each channel used by the customer
    channel_counts = customer_data['Chan'].value_counts()
    print(f"Channel Counts for Customer ID {customer_id}:\n", channel_counts)

    # Calculate the total number of interactions for this customer
    total_interactions = channel_counts.sum()

    # Calculate probabilities for each channel
    channel_probabilities = {
        'Phone Call': channel_counts.get(1, 0) / total_interactions if total_interactions > 0 else 0,
        'WhatsApp': channel_counts.get(2, 0) / total_interactions if total_interactions > 0 else 0,
        'Chatbot': channel_counts.get(3, 0) / total_interactions if total_interactions > 0 else 0
    }

    # Display the calculated probabilities
    print(f"\nProbabilities for Customer ID {customer_id}:")
    for channel, prob in channel_probabilities.items():
        print(f"{channel}: {prob:.2%}")

# Main function to run the script
def main():
    # Define the file path to your CSV dataset
    file_path = r'C:\Users\dell\Downloads\66c0115acc881_epic6_cx_data_analytics_case_2.csv'

    # Prepare and load the data
    data = prepare_data(file_path)

    # Prompt for the Customer ID as input
    customer_id_input = int(input("Enter the Customer ID (id_new): "))

    # Calculate and display the probabilities for the provided Customer ID
    calculate_channel_probabilities(customer_id_input, data)

# Execute the main function
if __name__ == "__main__":
    main()
