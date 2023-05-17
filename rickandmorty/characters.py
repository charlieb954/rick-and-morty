import requests
import urllib3

__all__ = ["Characters"]


class Characters:
    HOST = "https://rickandmortyapi.com/api/character/"
    DOCS = "https://rickandmortyapi.com/documentation/"

    def get_character_results(self, page_num: int = 1) -> dict:
        """get 20 characters from the specified page number

        Args
            page_num (int): page to return

        Returns
            dict: 20 characters with various fields
        """
        params = {"page": page_num}
        data = requests.get(self.HOST, params).json()

        return data["results"]

    def get_character_info(self) -> dict:
        """get summary of number of pages and characters available

        Args
            None

        Returns
            (dict): info on the characters available on the rick and morty API
        """
        data = requests.get(self.HOST).json()
        return data["info"]

    def get_character_single(self, id: int) -> dict:
        """get a character from their ID

        Args
            id (int): id of the character to be returned

        Returns
            dict: information about the character
        """
        data = requests.get(self.HOST + str(id)).json()
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

    def get_character_multi(self, ids: list) -> list:
        """get mutliple characters using their id

        Args
            ids (list): of integer ids

        Returns
            results (list): character dictionaries for ids
        """
        results = [self.get_character_single(id)["results"] for id in ids]

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
        all_params = {
            "name": name,
            "status": status,
            "species": species,
            "type": type,
            "gender": gender,
        }
        params = {k: v for k, v in all_params.items() if v is not None}
        data = requests.get(self.HOST, params).json()

        return data
