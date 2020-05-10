//Test Case is using Selenium IDE


import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import java.io.File;

import static org.junit.Assert.*;
public class TestCase2 {
    private WebDriver driver;
    File chromdriver = new File("src/chromedriver.exe");

    @Before
    public void setUp() {
        System.setProperty("webdriver.chrome.driver",chromdriver.getAbsolutePath());
        driver = new ChromeDriver();
    }

    @After
    public void tearDown() {
//        driver.quit();
    }

    @Test
    public void testCase() {

        // Test name: Test Case
        // Step # | name | target | value
        // 1 | open | /content/st_com/en.html |
        driver.get("https://www.st.com/content/st_com/en.html");

        /* ******************************
        //adding this part to accept the cookies

        ****************************** */
        driver.findElement(By.className("optanon-allow-all accept-cookies-button")).click();
        // 2 | setWindowSize | 1552x840 |
        driver.manage().window().setSize(new Dimension(1552, 840));
        // 3 | click | css=.st-nav__menu-item:nth-child(4) > .st-nav__menu-link |
        driver.findElement(By.cssSelector(".st-nav__menu-item:nth-child(4) > .st-nav__menu-link")).click();
        // 4 | click | linkText=Company Information |
        driver.findElement(By.linkText("Company Information")).click();
        // 5 | click | css=.show-for-medium-down > .st-header__inner |
        driver.findElement(By.cssSelector(".show-for-medium-down > .st-header__inner")).click();
        // 6 | click | css=.st-header-menu__submenu-item > .st-header-menu__link--disabled |
        driver.findElement(By.cssSelector(".st-header-menu__submenu-item > .st-header-menu__link--disabled")).click();
        // 7 | mouseOver | linkText=Automotive |
        {
            WebElement element = driver.findElement(By.linkText("Automotive"));
            Actions builder = new Actions(driver);
            builder.moveToElement(element).perform();
        }
        // 8 | mouseOut | linkText=Automotive |
        {
            WebElement element = driver.findElement(By.tagName("body"));
            Actions builder = new Actions(driver);
            builder.moveToElement(element, 0, 0).perform();
        }
    }
}


