from botcity.web import WebBot, Browser, By

class Bot(WebBot):
    def action(self, execution=None):
        # Configure whether or not to run on headless mode
        self.headless = False

        # Uncomment to change the default Browser to Firefox
        self.browser = Browser.CHROME
        
        # Uncomment to set the WebDriver path
        self.driver_path = r"C:\chromedriver_win32\chromedriver.exe"

        # Opens the BotCity website.
        self.browse("http://127.0.0.1:5000/upload")
        self.wait(3000)

        for i in range(1,10):
            txt_name = f"Name::Field {i}"
            txt_last_name = f"Last Name::Field {i}"
            txt_file= f"C:\\tmp\\somefiles\\file{i}.txt"

            # for name field: searching for an element by ID, click on element, send key *name*
            name_field = self.find_element(selector='name', by=By.ID)
            name_field.click()
            name_field.send_keys(txt_name)

            # for last name field: searching for an element by ID, click on element, send key *last name*
            last_name_field = self.find_element(selector='last_name', by=By.ID)
            last_name_field.click()
            last_name_field.send_keys(txt_last_name)

            print("Trying to upload file")
            file = self.find_element('//input[@type="file"]',By.XPATH)

            print("Trying to send file")
            file.send_keys(txt_file)
            self.wait(1000)

            submit = self.find_element('/html/body/form/p[7]/input',By.XPATH)
            self.wait(1000)
            submit.click()

        # Stop the browser and clean up
        self.stop_browser()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
