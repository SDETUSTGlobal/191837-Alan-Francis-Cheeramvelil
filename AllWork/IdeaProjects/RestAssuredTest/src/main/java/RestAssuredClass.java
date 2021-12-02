 import java.util.ArrayList;
import static io.restassured.RestAssured.*;
import static java.util.concurrent.TimeUnit.MILLISECONDS;

    public class myFirstRestAssuredClass {

        final static String url="http://demo.guru99.com/V4/sinkministatement.php?CUSTOMER_ID=68195&PASSWORD=1234!&Account_No=1";

        public static void main(String args[]) {

            getResponseBody();
            getResponseStatus();

            ; }


    }
