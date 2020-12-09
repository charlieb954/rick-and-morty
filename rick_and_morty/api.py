import requests

class RickandMorty:
    HOST = "https://rickandmortyapi.com/api"
    DOCS = "https://rickandmortyapi.com/documentation/"
    
    def get_characters_results(self, page_num=1)):
        """
        each page will return a maximum of 20 results
        """
        endpoint = "/character"
        params = {
            "page": page_num
            }
        data = requests.get(self.HOST + endpoint, params).json()
        return data['results']

    def get_character_info(self:
        """
        summary data of number of pages and characters available
        """
        endpoint = "/character"
        data = requests.get(self.HOST + endpoint, params).json()
        return data['info']
    
    def get_character_single(self, id):
        endpoint = "/character"
        params = {
            "id": id
        }
        data = requests.get(self.HOST + endpoint, params).json()
        return data['results']
    
    def get_character_all(self):
        results = []
        num_of_pages = self.get_character_info()['info']['pages'] + 1

        for i in range(1, num_of_pages):
            chars = self.get_character_results(i)
            for char in chars['results']:
                results.append(char)
            
        return results
    
    def character_multi(self, ls):
        results = []
        for i in ls:
            char = self.get_character_single(i)
            results.append(char['results'])
        return results
    
    def character_filter(self, name, status, species, type, gender):
        pass
    
    def character_count(self):
        pass
    
    def episodes(self):
        endpoint="/episode"
        return requests.get(self.HOST + endpoint).json()
    
    def locations(self):
        endpoint="/location"
        return requests.get(self.HOST + endpoints).json()