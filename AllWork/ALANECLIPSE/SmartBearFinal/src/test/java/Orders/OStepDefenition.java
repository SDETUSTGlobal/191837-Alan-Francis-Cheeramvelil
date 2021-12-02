package Orders;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

import cucumber.annotation.en.Given;
import cucumber.annotation.en.Then;
import cucumber.annotation.en.When;
import cucumber.annotation.en.And;


public class OStepDefenition {
	WebDriver driver = new ChromeDriver(); 
	   @Given("^user has navigated to orders page $")   
	   public void goToViewAllOrders() {   
	       
	      driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Process.aspx");   
	   }   
	      
	   @When("^the user chooses the type of product required  $")   
	      
	      
	   @Then("^the unit proce of the product is displayed in the corresponding textbox$")   
	   public void unitprice() {
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtUnitPrice"));
	   }
				   
		 
		   
	   
	   @When("^the user enters the quantity of the product required$") 
	   @And("^clicks the calculate button$")   
	   @Then("^the total cost is displayed in the corresponding textbox $")   
	   public void calculate() {
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]")).click();
				   
		   }  
	   
	   @When("^The user enters name,street,city,state,zip as personal information$")   
	      
	      
	   @Then("^The input values are displayed in the textboxes $")   
	   public void entervalues() {
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtName")).sendKeys("Alan Francis");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox2")).sendKeys("Alberts");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox3")).sendKeys("Kottayam");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox4")).sendKeys("Kerala");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox5")).sendKeys("686001");
		   
	   }
	   @When("^card type is selected as visa$")   
	   @And("^the card number and expiry date is entered and the process buton is clicked")
	   @Then("^it is shown that the new order is successfully added")
	   public void payment(){
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_cardList_0")).click();
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox6")).sendKeys("293747585904");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox1")).sendKeys("02/29");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_InsertButton")).click();
	   }
	   @When("^the reset button is clicked$")
	   @Then("^all the data from the columns are erased$")
	   public void reset(){
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/input")).click();
	   }
	   
	   @When("^the user chooses the type of product required  $")   
	      
	      
	   @Then("^the unit proce of the product is displayed in the corresponding textbox$")   
	   public void unitpricemaster() {
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtUnitPrice"));
	   }
				   
		 
		   
	   
	   @When("^the user enters the quantity of the product required$") 
	   @And("^clicks the calculate button$")   
	   @Then("^the total cost is displayed in the corresponding textbox $")   
	   public void calculatemaster() {
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]")).click();
				   
		   }  
	   
	   @When("^The user enters name,street,city,state,zip as personal information$")   
	      
	      
	   @Then("^The input values are displayed in the textboxes $")   
	   public void entervaluesmaster() {
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtName")).sendKeys("Alan Francis CC");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox2")).sendKeys("AlbertAAs");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox3")).sendKeys("KottayamAA");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox4")).sendKeys("KeralaAA");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox5")).sendKeys("686031");
		   
	   }
	   @When("^card type is selected as Mastercard$")   
	   @And("^the card number and expiry date is entered and the process buton is clicked")
	   @Then("^it is shown that the new order is successfully added")
	   public void paymentmaster(){
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_cardList_1")).click();
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox6")).sendKeys("2943747585904");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox1")).sendKeys("02/49");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_InsertButton")).click();
	   }
	   @When("^the reset button is clicked$")
	   @Then("^all the data from the columns are erased$")
	   public void resetmaster(){
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/input")).click();
	   }
	   
	   @When("^the user chooses the type of product required  $")   
	      
	      
	   @Then("^the unit proce of the product is displayed in the corresponding textbox$")   
	   public void unitpriceexpress() {
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtUnitPrice"));
	   }
				   
		 
		   
	   
	   @When("^the user enters the quantity of the product required$") 
	   @And("^clicks the calculate button$")   
	   @Then("^the total cost is displayed in the corresponding textbox $")   
	   public void calculateexpress() {
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]")).click();
				   
		   }  
	   
	   @When("^The user enters name,street,city,state,zip as personal information$")   
	      
	      
	   @Then("^The input values are displayed in the textboxes $")   
	   public void entervaluesexpress() {
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtName")).sendKeys("Alan Francis C");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox2")).sendKeys("AlbertsSS");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox3")).sendKeys("KottayamSS");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox4")).sendKeys("KeralaSS");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox5")).sendKeys("6860011");
		   
	   }
	   @When("^card type is selected as American Express$")   
	   @And("^the card number and expiry date is entered and the process buton is clicked")
	   @Then("^it is shown that the new order is successfully added")
	   public void paymentexpress(){
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_cardList_2")).click();
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox6")).sendKeys("2937475859094");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox1")).sendKeys("02/21");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_InsertButton")).click();
	   }
	   @When("^the reset button is clicked$")
	   @Then("^all the data from the columns are erased$")
	   public void resetexpress(){
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/input")).click();
	   }
}
	  
	      
	   

	      
	   


