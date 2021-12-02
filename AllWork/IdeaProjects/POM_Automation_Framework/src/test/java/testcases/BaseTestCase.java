package testcases;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import org.testng.annotations.AfterMethod;

public class BaseTestCase {
    @BeforeMethod
    public void setUp() {
        System.out.println("Before Method executed..!");
    }
    @Test
    public void test() {
        System.out.println("Test");
    }
    @AfterMethod
    public void tearDown() {
        System.out.println("After Method executed..!");
    }
}
