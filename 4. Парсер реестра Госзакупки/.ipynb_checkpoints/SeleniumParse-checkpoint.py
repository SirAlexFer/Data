class SeleniumParse:
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    
    def __init__(self, path_chrome_driver):

        
        self.path_chrome_driver = path_chrome_driver
        #self.path_chrome_application = path_chrome_application
        #self.time_limit = time_limit
        #caps = self.DesiredCapabilities().CHROME
        #caps["pageLoadStrategy"] = "normal" 

        options = self.Options()
        #options.headless= True
        #options.binary_location = self.path_chrome_application
        self.browser = self.webdriver.Chrome(options=options,executable_path = path_chrome_driver)
        
        
            
    def get_url(self,url:str):
        """Присваивает URL определенному объектк"""
        self.browser.get(url)
        
    def get_html_soap(self):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        return soup
    
    def out_browser(self):
        self.browser.quit()