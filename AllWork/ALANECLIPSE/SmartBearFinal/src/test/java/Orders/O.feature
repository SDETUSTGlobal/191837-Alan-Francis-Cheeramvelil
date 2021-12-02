
Feature: Orders page
User must be able to order the necessary product,give address and payment details

Scenario: Payment method is Visa 
Given user has navigated to orders page 
When the user chooses the type of product required 
Then the unit proce of the product is displayed in the corresponding textbox
When the user enters the quantity of the product required
And clicks the calculate button
Then the total cost is displayed in the corresponding textbox 
When The user enters name,street,city,state,zip as personal information
Then The input values are displayed in the textboxes
When card type is selected as visa
And the card number and expiry date is entered and the process button is clicked  
Then it is shown that the new order is successfully added
When the reset button is clicked
Then all the data from the columns are erased 


Scenario: Payment method is Mastercard 
Given user has navigated to orders page 
When the user chooses the type of product required 
Then the unit proce of the product is displayed in the corresponding textbox
When the user enters the quantity of the product required
And clicks the calculate button
Then the total cost is displayed in the corresponding textbox 
When The user enters name,street,city,state,zip as personal information
Then The input values are displayed in the textboxes
When card type is selected as Mastercard
And the card number and expiry date is entered and the process button is clicked  
Then it is shown that the new order is successfully added
When the reset button is clicked
Then all the data from the columns are erased 


Scenario: Payment method is American Express
Given user has navigated to orders page 
When the user chooses the type of product required 
Then the unit proce of the product is displayed in the corresponding textbox
When the user enters the quantity of the product required
And clicks the calculate button
Then the total cost is displayed in the corresponding textbox 
When The user enters name,street,city,state,zip as personal information
Then The input values are displayed in the textboxes
When card type is selected as American Express
And the card number and expiry date is entered and the process button is clicked  
Then it is shown that the new order is successfully added
When the reset button is clicked
Then all the data from the columns are erased 





