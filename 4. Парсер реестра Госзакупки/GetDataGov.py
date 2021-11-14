from MainFunction import MainFunction

class GetDataGov(MainFunction): 
    
    def __init__(self,path_chrome_driver):
        
        from SeleniumParse import SeleniumParse
        
        self.path_chrome_driver = path_chrome_driver
        self.browser = SeleniumParse(self.path_chrome_driver)
        
    def __del__(self):
        self.browser.out_browser()
        
    def parse_general(self,url_contract):
        dict_params = {}
        self.url_id = self._get_id(url_contract)
        
        
        url_general = 'https://zakupki.gov.ru/223/contract/public/contract/view/general-information.html?id='+self.url_id
        self.browser.get_url(url_general)
        soup = self.browser.get_html_soap()
        job_elements = soup.find_all("tr")
        
        list_params = [
            'Номер договора','Дата заключения договора','Извещение о закупке','Лот',
            'Способ закупки','Предмет договора','Дата размещения сведений','Идентификационный код заказчика',
            'Полное наименование заказчика','Сокращенное наименование заказчика','ОКОПФ',
            'ИНН','КПП','Дата постановки на учет в налоговом органе','ОКПО'
        ]
        
        for param in list_params:
            dict_params[param] = self._return_td(param, job_elements)
        return dict_params