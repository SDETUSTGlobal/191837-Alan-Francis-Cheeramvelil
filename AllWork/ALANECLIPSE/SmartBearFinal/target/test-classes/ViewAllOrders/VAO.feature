Feature: View all orders page 
User must be able to
View all active orders in a table format 
Given user has navigated to View all orders page 
Scenario: Check all button 
Given the user has logged in 
When user clicks the check all button 
Then all active orders are checked 
Scenario: UnCheck all button 
When user clicks the uncheck all button 
Then all the active orders that are checked  are unchecked 
Scenario:Delete selected button 
When user clicks the delete selected button 
Then all the orders that are checked are deleted from the table 
Scenario:Edit an order 
When the edit link is clicked 
Then navgate to Product page 


