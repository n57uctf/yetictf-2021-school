const puppeteer = require('puppeteer');

const IP = '127.0.0.1:8080';
const SECRET = '6e55c909e31e8f09efa5b4c684634612'
const myArgs = process.argv.slice(2);

const url = myArgs[0];

(async () => {
    const browser = await puppeteer.launch({
        args: [
            '--disable-web-security',
            '--ignore-certificate-errors',
            '--no-sandbox',
            '--disable-setuid-sandbox'
        ],
        headless: true,
        ignoreHTTPSErrors: true,
    });
    const page = await browser.newPage();
    await page.setCookie({
        "name": "is_admin",
        "value": SECRET,
        "domain": IP,
        "path": "/",
        "httpOnly": false,
        "secure": false,
    });
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 10000});
    console.log("[INFO] rendered page: " + url);
    await page.close();
    await browser.close();
})();
