from MainFunction import MainFunction

class GetContractGov(MainFunction):
    def __init__(self,path_chrome_driver):
        from SeleniumParse import SeleniumParse
        
        self.path_chrome_driver = path_chrome_driver
        self.browser = SeleniumParse(self.path_chrome_driver)
    
    def __del__(self):
        self.browser.out_browser()
        
    
    def parse_general(self,url_contract):
        dict_params = {}
        
        self.url_id = self._get_id(url_contract)
        self.url__contract_1 = 'https://zakupki.gov.ru/223/contract/public/contract/view/subject-contract.html?id='+self.url_id
        
        self.browser.get_url(self.url__contract_1)
        soup = self.browser.get_html_soap()
        job_elements = soup.find_all("tr")
        
        list_params = [
            'Цена договора', 'Валюта','Дата начала исполнения договора',
            'Условие начала исполнения договора','Дата окончания исполнения договора',
            'Условие окончания исполнения договора'
        ]
        
        for param in list_params:
            dict_params[param] = self._return_td(param, job_elements)
        dict_params['id'] = self.url_id
        return dict_params
    
    def parse_table(self,url_contract):
        import numpy as np
        
        self.url_id_table = self._get_id(url_contract)
        self.url__contract_1 = 'https://zakupki.gov.ru/223/contract/public/contract/view/subject-contract.html?id='+self.url_id_table
        self.browser.get_url(self.url__contract_1)
        
        elements = self.browser.browser.find_elements_by_tag_name('tbody')
        list_info_good = []
        elements_2 = elements[-1].find_elements_by_tag_name('td')
        for elem_2 in elements_2:
            list_info_good.append(elem_2.text)
            
        arr = np.array(list_info_good)
        mass = arr.reshape(-1,8)
        return arr.reshape(-1,8),self.url_id_table