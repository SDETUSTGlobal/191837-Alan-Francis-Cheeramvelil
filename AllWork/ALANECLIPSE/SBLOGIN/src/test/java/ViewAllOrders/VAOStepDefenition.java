package ViewAllOrders;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

import cucumber.annotation.en.Given;
import cucumber.annotation.en.Then;
import cucumber.annotation.en.When;
import cucumber.annotation.en.And;


public class VAOStepDefenition {
	//System.setProperty("webdriver.chrome.driver","C://Software//chromedriver//chromedriver.exe");
	WebDriver driver = new ChromeDriver(); 
	   @Given("^I am on View All Orders Page$")   
	   public void goToViewAllOrders() {   
	       
	      driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Default.aspx");   
	   }   
	      
	   @When("^user clicks check all button $")   
	      
	      
	   @Then("^All active orders are checked$")   
	   public void activeorders() {
		   driver.findElement(By.id("ctl00_MainContent_btnCheckAll")).click();
				   
		 
		   }   
	   
	   @When("^user clicks uncheckall button$")   
	      
	      
	   @Then("All the active orders taht are checked should be unchecked$")   
	   public void uncheck() {
		   driver.findElement(By.id("ctl00_MainContent_btnUncheckAll")).click();
				   
		   }  
	   
	   @When("^delete selected button is clicked$")   
	      
	      
	   @Then("all the orders that are checked are deleted from the table $")   
	   public void delete() {
		   driver.findElement(By.id("ctl00_MainContent_btnDelete")).click();
	   }
	   @When("^the edit link is clicked d$")   
	      
	      
	   @Then("navigate to product page $")   
	   public void navigatetoproductpage() {
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/div[3]/table/tbody/tr[2]/td[13]/input")).click();
	   driver.close();
	   }
	   

}


	      
	   

		

	   


