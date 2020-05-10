import io.appium.java_client.MobileBy;
import io.appium.java_client.android.AndroidDriver;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;

public class TestCase1 {
    private static final String APPIUM = "http://localhost:4723/wd/hub";

    private AndroidDriver driver;
    File theApp=new File("src/TheApp-v1.9.0.apk");

    @Before
    public void setUpAndroid() throws Exception {
        DesiredCapabilities caps = new DesiredCapabilities();
        caps.setCapability("platformName", "Android");
        caps.setCapability("platformVersion", "9");
        caps.setCapability("deviceName", "appium");
        caps.setCapability("automationName", "UiAutomator2");
        caps.setCapability("app", theApp.getAbsolutePath());
        caps.setCapability("newCommandTimeout",100 );
        driver = new AndroidDriver(new URL(APPIUM), caps);
    }


    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    public void test() throws MalformedURLException {
//simple without optimisations
//        driver.findElement(MobileBy.AccessibilityId("Login Screen")).click();
//        driver.findElement(MobileBy.AccessibilityId("username")).sendKeys("alice");
//        driver.findElement(MobileBy.AccessibilityId("password")).sendKeys("mypassword");
//        driver.findElement(MobileBy.AccessibilityId("loginBtn")).click();

//With WebdDriverWait optimisations
        WebDriverWait wait = new WebDriverWait(driver, 10);

        WebElement screen = wait.until(ExpectedConditions.presenceOfElementLocated(MobileBy.AccessibilityId("Login Screen")));
        screen.click();

        WebElement username = wait.until(ExpectedConditions.presenceOfElementLocated(MobileBy.AccessibilityId("username")));
        username.sendKeys("alice");

        WebElement password = driver.findElement(MobileBy.AccessibilityId("password"));
        password.sendKeys("mypassword");

        WebElement login = driver.findElement(MobileBy.AccessibilityId("loginBtn"));
        login.click();

    }
}

