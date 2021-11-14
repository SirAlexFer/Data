class MainFunction:
    from selenium import webdriver
    from bs4 import BeautifulSoup

        
        
    def _get_id(self, url_):
        from urllib.parse import urlparse
        from urllib.parse import parse_qs
        parsed = urlparse(url_)
        try:
            return(parse_qs(parsed.query))['id'][0]
        except:
            return(0)
    
    def _return_td(self,parameter,job_elements):
        import unicodedata
        for elem in job_elements:
            if parameter in elem.text:
                try:
                    text = elem.find_all("td")[1].text.strip()
                    text = unicodedata.normalize("NFKD",text)
                    return text
                except:
                    return '---'
#    def _get_request(self,url):
#        import time
#        import requests
#        from bs4 import BeautifulSoup
#        for i in range(6):
#            page = requests.get(url)
#            soup = BeautifulSoup(page.content, "html.parser")
#            if  'Страница не найдена' not in soup.text:
#                break
#            else:
#                time.sleep(10)    
#        return soup