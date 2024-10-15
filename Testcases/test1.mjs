import { Builder, By, until } from 'selenium-webdriver';
import { expect } from 'chai'; 

// const { Builder, By, until } = require('selenium-webdriver');
// const { expect } = require('chai');

describe('Contact Form UI Element Visibility Tests', function () {
    let driver;

    before(async function () {
        driver = await new Builder().forBrowser('chrome').build();
    });

    after(async function () {
        await driver.quit();
    });
    

    it('should display the contact form elements', async function () {
        await driver.get('http://localhost:8081/contact.html'); // Make sure this points to the correct frontend

        // Check that the name input is visible
        const nameField = await driver.findElement(By.name('name'));
        expect(await nameField.isDisplayed()).to.be.true;

        // Check that the email input is visible
        const emailField = await driver.findElement(By.name('email'));
        expect(await emailField.isDisplayed()).to.be.true;

        // Check that the subject input is visible
        const subjectField = await driver.findElement(By.name('subject'));
        expect(await subjectField.isDisplayed()).to.be.true;

        // Check that the message textarea is visible
        const messageField = await driver.findElement(By.xpath("//textarea[@name='message']"));
        expect(await messageField.isDisplayed()).to.be.true;

        // Check that the submit button is visible
        const submitButton = await driver.findElement(By.css('button[type="submit"]'));
        expect(await submitButton.isDisplayed()).to.be.true;


        // // Check that the error messages are not visible initially
        // const nameError = await driver.findElement(By.id('name-error'));
        // const emailError = await driver.findElement(By.id('email-error'));
        // expect(await nameError.isDisplayed()).to.be.false;
        // expect(await emailError.isDisplayed()).to.be.false;
    });
});
