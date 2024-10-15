
import { Builder, By, until } from 'selenium-webdriver';
import { expect } from 'chai'; // Use import instead of require


// const { Builder, By, until } = require('selenium-webdriver');
// const { expect } = require('chai');

describe('Contact Form Submission Tests', function () {
    let driver;

    before(async function () {
        // Set up the Selenium WebDriver
        driver = await new Builder().forBrowser('chrome').build();
    });

    after(async function () {
        // Quit the driver after tests
        await driver.quit();
    });

    it('should submit the contact form successfully', async function () {
        // Navigate to the form page
        await driver.get('http://localhost:3000/contact');

        // Fill out the form
        await driver.findElement(By.name('name')).sendKeys('John Doe');
        await driver.findElement(By.name('email')).sendKeys('john.doe@example.com');
        await driver.findElement(By.name('message')).sendKeys('Hello, this is a test message.');

        // Submit the form
        await driver.findElement(By.css('button[type="submit"]')).click();

        // Wait for confirmation message
        const confirmationMessage = await driver.wait(
            until.elementLocated(By.id('confirmation')),
            5000
        );

        // Assert confirmation message is displayed
        const messageText = await confirmationMessage.getText();
        expect(messageText).to.include('Thank you for your message!');
    });

    it('should show error for missing required fields', async function () {
        // Navigate to the form page
        await driver.get('http://localhost:3000/contact');

        // Leave fields empty and submit
        await driver.findElement(By.css('button[type="submit"]')).click();

        // Wait for error messages
        const nameError = await driver.wait(
            until.elementLocated(By.id('name-error')),
            5000
        );
        const emailError = await driver.wait(
            until.elementLocated(By.id('email-error')),
            5000
        );

        // Assert error messages are displayed
        const nameErrorText = await nameError.getText();
        const emailErrorText = await emailError.getText();
        expect(nameErrorText).to.include('Name is required');
        expect(emailErrorText).to.include('Email is required');
    });
});
