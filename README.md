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

### Navbar
A navbar that links to the resources below. More links can be added by adding buttons that follow the same formula and path of the newly linked item.

### Employee
Employees hold information about the employees.

1. Employee table holds infromation about an employee
    - first name(string) the first name of the employee
    - last name(string) the last name of the employee
    - department id(foreign key) the id of the employee's department
    - start date is the time the employee was created
    - end date is a date input
    - is supervisor is a boolean value to represent if supervisor
    - training_program (many to many) many to many relationship generated with training programs

### Training Programs
Training programs information is stored in the training_programs table
It contains the following information

name - string, max length 40 characters
description - string, max length 200 characters
start_date - date, start date of the event
end_date - date, end date of the event
max_attendees - integer, maximum people who can attend the event

### Departments
1. id
1. name (string)


## Faker Data Setup
Use your models to create fake data in the employee_portal/manage/commands/faker_factory.py
you can view the documentation for seeder arguments here
https://github.com/Brobin/django-seed
