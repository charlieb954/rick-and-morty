import requests

__all__ = ["Characters"]


class Characters:
    HOST = "https://rickandmortyapi.com/api"
    DOCS = "https://rickandmortyapi.com/documentation/"

    def get_character_results(self, page_num: int = 1) -> dict:
        """get 20 characters from the specified page number

        Args
            page_num (int): page to return

        Returns
            dict: 20 characters with various fields
        """
        endpoint = "/character"
        params = {"page": page_num}
        data = requests.get(self.HOST + endpoint, params).json()

        return data["results"]

    def get_character_info(self) -> dict:
        """get summary of number of pages and characters available

        Args
            None

        Returns
            (dict): information about the characters available on the rick and morty API
        """
        endpoint = "/character"
        data = requests.get(self.HOST + endpoint).json()
        return data["info"]

    def get_character_single(self, id: int) -> dict:
        """get a character from their ID

        Args
            id (int): id of the character to be returned

        Returns
            dict: information about the character
        """
        endpoint = f"/character/{int(id)}"
        data = requests.get(self.HOST + endpoint).json()
        return data

    def get_character_all(self) -> dict:
        """get a list of all the characters from the api

        Args
            None

        Returns
            results (tuple): characters id, characters name
        """
        results = []
        num_of_pages = self.get_character_info()["pages"] + 1

        for i in range(1, num_of_pages):
            chars = self.get_character_results(i)
            for char in chars:
                results.append((char["id"], char["name"]))

        return results

    def get_character_multi(self, ls: list) -> list:
        """get mutliple characters using their id

        Args
            ls (list): of integer ids

        Returns
            results (list): character dictionaries for ids
        """
        results = []
        for i in ls:
            char = self.get_character_single(i)
            results.append(char["results"])
        return results

    def character_filter(
        self,
        name: str = None,
        status: str = None,
        species: str = None,
        type: str = None,
        gender: str = None,
    ) -> dict:
        """get characters that match criteria of 1 or more filters.
        Name will include similar matches. For example:
        Morty will match Morty Smith and Alien Morty

        Args
            name (str): name of character
            status (str): character status (dead/alive/unknown)
            species (str): species of character
            type (str): type of sub-species
            gender (str): male/female/genderless/unknown

        Returns
            data (dict): characters matching criteria
        """
        endpoint = "/character"
        all_params = {
            "name": name,
            "status": status,
            "species": species,
            "type": type,
            "gender": gender,
        }
        params = {k: v for k, v in all_params.items() if v != None}
        data = requests.get(self.HOST + endpoint, params).json()

        return data
