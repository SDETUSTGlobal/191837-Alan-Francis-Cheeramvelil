package ViewAllProducts;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import cucumber.annotation.en.Given;
import cucumber.annotation.en.Then;
import cucumber.annotation.en.When;

public class VAPStepDefenition {
	WebDriver driver = new ChromeDriver(); 
	   @Given("^User is logged in $")   
	   public void goToViewAllOrders() {   
	       
	      driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Default.aspx");   
	   }   
	      
	   @When("the  user clicks the link to View all Products page  $")   
	      
	      
	   @Then("^the page containing product details should be displayed $")   
	   public void productpage() {
		   driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Products.aspx");;

		   driver.close();
		 
		   }   
	   
	  
	 
	   }
	   




	      


