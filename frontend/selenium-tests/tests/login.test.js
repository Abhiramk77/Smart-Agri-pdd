import { Builder, By, until } from 'selenium-webdriver';
import chrome from 'selenium-webdriver/chrome.js';
import assert from 'assert';

describe('Login Flow E2E Test', function () {
  this.timeout(30000); // 30 seconds timeout
  let driver;

  before(async function () {
    const options = new chrome.Options();
    options.addArguments('--headless');
    options.addArguments('--no-sandbox');
    options.addArguments('--disable-dev-shm-usage');
    options.addArguments('--disable-gpu');

    driver = await new Builder()
      .forBrowser('chrome')
      .setChromeOptions(options)
      .build();
  });

  after(async function () {
    if (driver) {
      await driver.quit();
    }
  });

  it('should successfully log in as farmer and redirect to dashboard', async function () {
    // Navigate to the local dev server
    await driver.get('http://localhost:5173/#/login');

    // Wait for the email input to be visible
    const emailInput = await driver.wait(until.elementLocated(By.id('email')), 5000);
    
    // Type the farmer email
    await emailInput.sendKeys('farmer@farming.com');

    // Click the login button
    const loginButton = await driver.findElement(By.id('login-button'));
    await loginButton.click();

    // Wait for redirect to happen (wait for URL to change to dashboard)
    await driver.wait(until.urlContains('/dashboard'), 10000);

    // Verify the URL
    const currentUrl = await driver.getCurrentUrl();
    assert.strictEqual(currentUrl.includes('/dashboard'), true, 'User was not redirected to the dashboard');
  });
});
