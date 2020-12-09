import requests

class RickandMorty:
    HOST = "https://rickandmortyapi.com/api"
    DOCS = "https://rickandmortyapi.com/documentation/"
    
    def get_character_results(self, page_num=1):
        """
        Get 20 characters from the specified page number
        
        Parameters
        ----------
        page_num = int: page to return
        
        Returns
        -------
        json: 20 characters with various fields
        """
        endpoint = "/character"
        params = {
            "page": page_num
            }
        data = requests.get(self.HOST + endpoint, params).json()
        return data['results']

    def get_character_info(self):
        """
        Get summary of number of pages and characters available
        
        Parameters
        ----------
        None
        
        Returns
        -------
        json: information from rick and morty api
        """
        endpoint = "/character"
        data = requests.get(self.HOST + endpoint, params).json()
        return data['info']
    
    def get_character_single(self, id):
        """
        Get a character from their ID
        
        Parameters
        ----------
        id = int: id of the character to be returned
        
        Returns
        -------
        json: information about the character
        """
        endpoint = "/character"
        params = {
            "id": int(id)
        }
        data = requests.get(self.HOST + endpoint, params).json()
        return data['results']
    
    def get_character_all(self):
        """
        Get a list of all the characters from the api
        
        Parameters
        ----------
        None
        
        Returns
        -------
        results = list: dictionaries of characters
        """
        results = []
        num_of_pages = self.get_character_info()['info']['pages'] + 1

        for i in range(1, num_of_pages):
            chars = self.get_character_results(i)
            for char in chars['results']:
                results.append(char)
            
        return results
    
    def get_character_multi(self, ls):
        """
        Get mutliple characters using their id
        
        Parameters
        ----------
        ls = list: of integer ids
        
        Returns
        -------
        results = list: character dictionaries for ids
        """
        results = []
        for i in ls:
            char = self.get_character_single(i)
            results.append(char['results'])
        return results
    
    def character_filter(self, name=None, status=None, species=None, type=None, gender=None):
        """
        Get characters that match criteria of 1 or more filters
        
        Parameters
        ----------
        name = str: name of character
        status = str: character status (dead/alive/unknown)
        species = str: species of character
        type = str: type of sub-species
        gender = str: male/female/genderless/unknown
        
        Returns
        -------
        data = json: characters matching criteria 
        """
        endpoint = '/character'
        all_params = {
            "name": name,
            "status": status,
            "species": species,
            "type": type,
            "gender": gender
        }
        params = {k:v for k,v in all_params.items() if v != None}
        data = requests.get(self.HOST + endpoint, params).json()
        
        return data
    
    def episodes(self):
        endpoint="/episode"
        return requests.get(self.HOST + endpoint).json()
    
    def locations(self):
        endpoint="/location"
        return requests.get(self.HOST + endpoints).json()