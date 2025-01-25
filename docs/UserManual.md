# **User Manual for Rabbit Breeding**

This manual provides step-by-step instructions to operate the Rabbit Management System script. This script is designed to manage data about rabbit breeding schedules and related tasks, storing information in an SQLite database. It calculates key dates (palpation, nesting, and due date) based on breeding dates.

---

## **Features**
- Add data about rabbit breeding schedules.
- Automatically calculate important dates (palpation, nesting, and due).
- View stored rabbit data in a tabular format.
- Easy-to-use menu options for inputting or viewing data.

---

## **Setup Instructions**
### **Dependencies**
Ensure you have Python installed along with the following modules:
- `sqlite3` (built-in with Python)
- `datetime` (built-in with Python)
- `sys` (built-in with Python)
- `utils` (a custom module for utility functions like `Utils.clear()`)

### **Database Initialization**
The script initializes and manages an SQLite database named `rabbits.db`. The database contains a table named `rabbits` with the following columns:
- `name`: Name of the female rabbit.
- `last_bred`: Breeding date (Month and Day, e.g., "May 5").
- `buck`: Name of the male rabbit used for breeding.
- `palpatate`: Palpation date (15 days after breeding).
- `nest_date`: Nest box preparation date (27 days after breeding).
- `due_date`: Kindling date (31 days after breeding).
- `comments`: Any additional comments about the rabbit.

The database and table are created automatically when the script runs for the first time.

---

## **How to Use the Script**

### **Starting the Script**
Run the script from the command line or terminal:
```bash
python script_name.py
```

### **Main Menu**
Upon starting, the script will present the following options:
1. **Input Data (I)**: Add information about a rabbit's breeding schedule.
2. **View Data (V)**: View all stored rabbit breeding information.
3. **Exit (E)**: Exit the program.

You can input your choice by typing:
- `I` for Input,
- `V` for View,
- `E` for Exit.

---

### **Inputting Data**
When you select **Input Data (I)**, the script will prompt you for the following details:
1. **Name of the doe (female rabbit)**: Enter the name.
2. **Breeding date**: Enter the date in the format `Month Day` (e.g., "May 5").
3. **Buck used for breeding**: Enter the name of the male rabbit.
4. **Comments**: Provide any additional notes.

#### **Automatic Calculations**
The script calculates:
- **Palpation Date**: 15 days after the breeding date.
- **Nest Box Date**: 27 days after the breeding date.
- **Kindling Date**: 31 days after the breeding date.

The calculated dates are displayed on-screen for review before saving.

#### **Data Insertion**
The entered and calculated information is saved into the database. If the operation is successful, the script displays:
```
Data added to file
```

If an error occurs, an appropriate error message is displayed.

---

### **Viewing Data**
When you select **View Data (V)**, the script displays all rabbit breeding records in a tabular format:
```
Female   Breed Date   Buck   Palpate   Nest Box   Kindling Date   Comments
```

Each record is displayed in a row, with values separated by tabs for readability.

---

### **Exiting the Program**
Select **Exit (E)** to close the program. Before exiting, the script:
1. Closes the connection to the database.
2. Exits gracefully.

---

## **Error Handling**
- If invalid input is provided, the script displays an error message:
  ```
  Invalid input. Please enter 'I' to input data, 'V' to view data, or 'E' to exit.
  ```
- The script gracefully handles database errors during data insertion or retrieval.

---

## **Customizations**
You can modify the script to:
1. Add additional fields to the `rabbits` table.
2. Customize the number of days used for calculations.
3. Enhance the utility module `utils` with more functions for better usability.

---

## **Additional Notes**
- The database file `rabbits.db` will be created in the same directory as the script.
- Data is stored locally; there is no cloud integration.
- The `Utils.clear()` function is assumed to clear the screen. Ensure that the `utils` module is available and configured for your system.

---

With this manual, you should be able to effectively operate the Rabbit Management System to track breeding schedules and ensure efficient record-keeping!