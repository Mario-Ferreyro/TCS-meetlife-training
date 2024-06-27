package seleniumAssignment;

import java.util.Scanner;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.Select;

public class Form{
	public static void main(String[] args) throws InterruptedException{
		System.setProperty("webdriver.chrome.driver", "C:\\chromedriver-win64\\chromedriver-win64\\chrom ChromeOptions options getOptions();
		WebDriver webDriver = new ChromeDriver(options);
		//https://formy-project.herokuapp.com/form
		webDriver.get("https://formy-project.herokuapp.com/form");
		Scanner sc = new Scanner(System.in);
		Scanner scInt = new Scanner(System.in);

		WebElement firstName = webDriver.findElement(By.id("first-name"));
		System.out.println("Enter your first name: ");
		String fName = sc.nextLine();
		firstName.sendKeys (fName);
		Thread.sleep(1000);

		WebElement lastName = webDriver.findElement(By.id("last-name"));
		System.out.println("Enter your first name: ");
		String lName = sc.nextLine();
		lastName.sendKeys (lName);
		Thread.sleep(1000);

		WebElement jobTitle = webDriver.findElement(By.xpath("//*[@id='job-title']"));
		System.out.println("Enter your job title: ");
		String jTitle = sc.nextLine();
		jobTitle.sendKeys(jTitle);
		Thread.sleep(1000);


		int optionEducation = 0;
		do {
			System.out.println("Please enter your Highest level of education. Enter your option number:
			+ "\n 1) High School"
			+ "\n 2) College"
			+ "\n 3) Grad School");
			optionEducation = scInt.nextInt();
			if (optionEducation < 1 || optionEducation > 3)
				System.out.println("You choose a wrong option! please select a valid one");
		}while(optionEducation >= 4 || optionEducation <= 0);

		if (optionEducation == 1) {
			System.out.println("You selected: High school");
			WebElement radius1 = webDriver.findElement(By.id("radio-button-1")); radius1.click();
		}
		else if(optionEducation == 2) {
			System.out.println("You selected: College");
			WebElement radius2 = webDriver.findElement(By.id("radio-button-2"));
			radius2.click();
		}
		else if(optionEducation == 3) {
			System.out.println("You selected: Grad school");
			WebElement radius3 = webDriver.findElement(By.id("radio-button-3"));
			radius3.click();
		}
		Thread.sleep(1000);


		int optionSex = 0;
		do {
			System.out.println("Please enter your sex. Enter your option number:
			+ "\n 1) Male"
			+ "\n 2) Female"
			+ "\n 3) Prefer not to say");
			optionSex = scInt.nextInt();
		if(optionSex < 1 || optionSex > 3)
			System.out.println("You choose a wrong option! please select a valid one");
		}while(optionSex >= 4 || optionSex <= 0);
		if(optionSex == 1) {
			System.out.println("You selected: Male");
			WebElement check1 check1.click(); webDriver.findElement(By.id("checkbox-1"));
		}	
		else if(optionSex == 2) {
			System.out.println("You selected: Female");
			WebElement check2= webDriver.findElement(By.id("checkbox-2")); check2.click();
		}
		else if(optionSex == 3) {
			System.out.println("You selected: Prefer not to say");
			WebElement check3 webDriver.findElement(By.id("checkbox-3"));
			check3.click();
		}
		Thread.sleep(1000);

		
		System.out.println("Plese enter your years of experience: ");
		int experienceNum scInt.nextInt();
		Select selectMenu = new Select(webDriver.findElement(By.id("select-menu")));
		if(experienceNum <= 1) {
			selectMenu.selectByValue("1");
		}
		else if(experienceNum >= 2 && experienceNum <= 4) {
			selectMenu.selectByValue("2")
		}
		else if(experienceNum >= 5 && experienceNum <= 9) {
			selectMenu.selectByValue("3");
		}
		else if (experienceNum >= 10) {
			selectMenu.selectByValue("4");
		}
		Thread.sleep(1000);


		System.out.println("Enter the date(mm/dd/yyyy)");
		String dateString = sc.nextLine();
		WebElement date = webDriver.findElement(By.id("datepicker"));
		sendKeys (dateString);
		date.sendKeys (Keys. RETURN);
		Thread.sleep(5000);

		WebElement button = button.click(); ver.findElement(By.xpath("/html/body/div/form/div/div[8]/a"));
	}

	static ChromeOptions getOptions() {
		ChromeOptions options = new ChromeOptions();
		options.addArguments("--remote-allow-origins=*");
		return options;
	}

}
