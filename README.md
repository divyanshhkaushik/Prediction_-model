Project Title: Channel Interaction Probability Analysis
This project focuses on analyzing customer interaction data from different channels (Phone Call, WhatsApp, Chatbot) and calculating the probability of a customer using each channel. The provided script reads a dataset from a CSV file, cleans and processes the data, and allows for calculating the probabilities for a specific customer’s interactions with these channels.

Prerequisites
This project requires the following to be installed:

Python 3.x
Pandas library
You can install Pandas using pip if it's not already installed:

Project Structure
The script consists of the following major components:

prepare_data(file_path):

Reads a CSV dataset from the given file path.
Cleans the dataset by:
Dropping any unnamed columns that may have been added by default.
Replacing any missing values (NaN) with 0.
Ensures that the 'Chan' column is converted to categorical values representing:
1 for Phone Call,
2 for WhatsApp,
3 for Chatbot.
Returns the cleaned data.
calculate_channel_probabilities(customer_id, data):

Filters the dataset for a specific customer based on the provided customer_id.
If no data is found for the customer, the function lists all available customer IDs and returns.
Counts the number of times the customer interacted through each channel.
Calculates the probability for each channel based on the total interactions of that customer.
Displays the probabilities in a percentage format.
main():

Defines the file path to the dataset.
Loads and preprocesses the dataset using prepare_data().
Prompts the user to input a Customer ID.
Calls calculate_channel_probabilities() to display the interaction probabilities for the provided Customer ID.
How to Use
Prepare Your Dataset:
Ensure your CSV file is structured properly and includes:
id_new column representing unique customer IDs.
Chan column representing the channel of interaction where:
1 stands for Phone Call,
2 stands for WhatsApp,
3 stands for Chatbot.
Running the Script:
Place your dataset in an accessible directory and update the file_path in the main() function to point to the correct location.
Run the script:
bash
Copy code
python script_name.py
When prompted, input a valid Customer ID from the dataset.
The script will output the interaction probabilities for the selected customer.
Example
If the CSV file contains a customer with ID 12345 and this customer interacted via WhatsApp and Phone Call, the output will look like:

yaml
Copy code
Customer Data for ID 12345:
   id_new  Chan
0  12345      1
1  12345      2
2  12345      2

Channel Counts for Customer ID 12345:
WhatsApp: 66.67%
Phone Call: 33.33%
Chatbot: 0.00%
Notes
Ensure the dataset contains the necessary columns id_new (for customer IDs) and Chan (for interaction channels).
Missing values in the dataset are automatically replaced with 0 during preprocessing.
The script assumes the channel values are represented as integers (1, 2, 3).
