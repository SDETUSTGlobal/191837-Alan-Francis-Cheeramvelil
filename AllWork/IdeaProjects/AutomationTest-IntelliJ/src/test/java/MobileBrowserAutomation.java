import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;
import
        io.appium.java_client.remote.AndroidMobileCapabilityType;
import io.appium.java_client.remote.IOSMobileCapabilityType;
import io.appium.java_client.remote.MobileCapabilityType;
import org.openqa.selenium.By;
import org.openqa.selenium.remote.BrowserType;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import java.net.MalformedURLException;
import java.net.URL;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class MobileBrowserAutomation {
    public AndroidDriver driver;
    	System.setProperty("webdriver.chrome.driver","C://Software//chromedriver//chromedriver.exe");
    WebDriver driverchrome =new ChromeDriver();
    @BeforeTest
    public void setUp() throws MalformedURLException {
        String appiumServerURL =
                "http://127.0.0.1:4723/wd/hub";
        DesiredCapabilities dc = new DesiredCapabilities();
        dc.setCapability(MobileCapabilityType.PLATFORM_NAME,
                "Android");

        dc.setCapability(MobileCapabilityType.PLATFORM_VERSION,
                "10.0");
        dc.setCapability(MobileCapabilityType.BROWSER_NAME,
                BrowserType.CHROME);
        dc.setCapability(MobileCapabilityType.DEVICE_NAME,
                "KBAIGF00D7339H3");

        dc.setCapability(MobileCapabilityType.AUTOMATION_NAME,
                "UiAutomator2");
        driver = new AndroidDriver(new URL(appiumServerURL),
                dc);

    }
    @Test
    public void verifyUserCanLoginToFaceBook() throws
            InterruptedException {
        String username = ""; // Enter your valid facebook username
        String password = ""; // Enter your valid facebook password
        driverchrome.get("https://m.facebook.com/");

        driverchrome.findElement(By.id("m_login_email")).sendKeys(username)
        ;

        driverchrome.findElement(By.id("m_login_password")).sendKeys(password);
        driverchrome.findElement(By.name("login")).click();
    }
}