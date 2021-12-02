package LOGIN;


import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

import cucumber.annotation.en.Given;
import cucumber.annotation.en.Then;
import cucumber.annotation.en.When;
import cucumber.annotation.en.And;


public class SBLoginStepDefenition {
	  
	   WebDriver driver =new ChromeDriver();  
	   @Given("^I am on login page$")   
	   public void goToFacebook() {   
	       
	      driver.navigate().to("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx");   
	   }   
	      
	   @When("^I enter valid data on the page$")   
	      
	      
	   @Then("^User registration should be successful$")   
	   public void User_registration_should_be_successful() {
		   if(driver.getCurrentUrl().equalsIgnoreCase("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx"))
				   {  
		         System.out.println("Test Pass");   
		      } else {   
		         System.out.println("Test Failed");   
		      }   
		      driver.close();   
		   }  
		}

	   