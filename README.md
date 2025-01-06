# Expense Tracker CLi

The Expense Tracker is a command-line application designed to help users manage their personal finances by tracking their expenses. This tool allows users to add, list, and summarize their expenses for specific months, providing insights into spending habits and helping with budget management.

### Features

- **Add Expenses**: Users can add new expenses with a description and amount.
- **List Expenses**: View all recorded expenses in a user-friendly format.
- **Monthly Summary**: Generate a summary of expenses for a specific month, allowing users to see how much they spent and on what.
- **Error Handling**: The application includes robust error handling to ensure that user inputs are validated and processed correctly.

### Technologies Used

- Python
- JSON for data storage
- Command-line interface

### Installation

Clone this repository and run the application:

```
git clone https://github.com/ivano-lab/expense-tracker-cli
```
Go to the application directory and run:

```
expense_tracker.py
```

Make sure that you have Python 3 or higher installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/downloads/).

### Usage

The list of commands and their expected output is shown below:

- add --description "Lunch" --amount 20

```Expense added successfully (ID: 1)```

- add --description "Dinner" --amount 10

- ```Expense added successfully (ID: 2)```
- list

```
ID  Date       Description  Amount
1   2025-01-06  Lunch        $20
2   2024-01-06  Dinner       $10
```

- delete --id 2

- ```Expense deleted successfully (ID: 2)```
 

- summary

```Total expenses: $30```

- summary --month 1

```
Total expenses for month 1: $30
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
