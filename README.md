# Bangazon Internal Site

## Setting up

1. Clone down repo into a directory
1. Create a virtual environent as sibling of this repo
   - `virtualenv <name_of_virtualenv>`
1. Activate virtual environment
   - `source <name_of_virtualenv>/bin/activate`
1. CD into repo
1. Run `pip install -r requirements.txt`

## File naming conventions/File Structure

All directories and files should be named lower case with snake case for multi word names.

Similar files such as models/views will go in their respective directories. Name those files with the following template

For models - `<resource name>_model.py`
For views - `<resource name>_<view type>_view.py`

examples
```
employee_model.py
employee_edit_view.py
```


## Resources

The following resources are available through the application

### Employee
Employees hold information about the employees.

1. Employee table holds infromation about an employee
    - first name(string) the first name of the employee
    - last name(string) the last name of the employee
    - department id(foreign key) the id of the employee's department
    - start date is the time the employee was created
    - end date is a date input
    - is supervisor is a boolean value to represent if supervisor

### Training Programs
Training programs hold information about the training events employees can attend.

The data is held between two tables

1. Training programs holds information about a type of training program offered
    - name (string) the name of the program
    - description (string) a description of the program

1. Training program events holds information about the individual sessions
    - training_program_id (foreign key) the id of the training program that will be taught
    - start_date (date) the start date of the event
    - end_date (date) the end date of the event
    - max_attendees (integer) the maximum number of attendees who can attend the event
