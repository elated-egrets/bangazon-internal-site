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

## Models:

### Departments
id
name (string)