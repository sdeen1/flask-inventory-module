# Inventory Module

## Outline

1. Inventory CRUD  
    a. Add new items or add to existing inventory (update)   
    b. Update item price  
    c. Display all items  
    d. Delete an item or remove from existing inventory (update)  
    e. Rudimentary check in and out feature  
2. Login capability - store user information, including whether or not user has admin privileges  
    a. Login page  
    b. Create new user page, needs to be locked down so that only an admin can add new users  
    c. Logout page

## Todo:
### Create
- [ ] Make the errors from validation more user friendly on the Add Item page.  
- [ X ] Set up and add the database.
- [ X ] Add logic to the routes to add data from addItem.html to the database.
### Read
- [ X ] Display all the items on the index.html page.
- [ ] Formatting: make all item names and descriptions start with an upper case letter.
- [ ] Formatting: format all the prices to have dollar signs and decimals
- [ ] Formatting: check for None or blank values and make them "N/A"
### Delete
- [ X ] Add a delete button to the index page
- [ X ] Delete item from database
### Update
- [ X ] Create update route (see https://wtforms.readthedocs.io/en/3.0.x/crash_course/#editing-existing-objects)
- ~~[ ] Create UpdateItemForm in forms.py~~
- ~~[ ] Create updateItem.html~~
- [ X ] Update item's info in database
### "Rent"
- [ X ] Create "rent" route
- [ X ] Create "return" route
