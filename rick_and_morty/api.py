import requests

class RickandMorty:
    HOST = "https://rickandmortyapi.com/api"
    DOCS = "https://rickandmortyapi.com/documentation/"
    
    def get_character_info(self, page_num=1):
        """
        each page will return a maximum of 20 results
        """
        
        endpoint = "/character"
        params = {
            "page": page_num
            }
        data = requests.get(self.HOST + endpoint, params).json()
        return data
    
    def get_character_single(self, id):
        endpoint = "/character"
        params = {
            "id": id
        }
        data = requests.get(self.HOST + endpoint, params).json()
        return data['results']
    
    def get_character_all(self):
        num_of_pages = self.get_character_info()['info']['pages'] + 1
        
        all_results = []
        for i in range(1, num_of_pages):
            chars = self.get_character_info(i)
            for char in chars['results']:
                all_results.append(char)
            
        return all_results
    
    def character_multi(self, ls):
        pass
    
    def character_filter(self, name, status, species, type, gender):
        pass
    
    def character_count(self):
        pass
    
    def characters_results(self):
        """
        each page will return a maximum of 20 results
        """
        
        endpoint = "/character"
        params = {
            "page": page_num
            }
        data = requests.get(self.HOST + endpoint, params).json()
        return data['results']
    
    def episodes(self):
        endpoint="/episode"
        return requests.get(self.HOST + endpoint).json()
    
    def locations(self):
        endpoint="/location"
        return requests.get(self.HOST + endpoints).json()