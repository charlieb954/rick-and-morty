import requests
from pandas import DataFrame

__all__ = ["Characters"]


class Characters:
    HOST = "https://rickandmortyapi.com"
    ENDPOINT = "/api/character/"
    DOCS = "https://rickandmortyapi.com/documentation/"
    JSON = True

    def _get(self, params: dict = None, q_id: int = None) -> dict:
        if q_id is not None:
            url = self.HOST + self.ENDPOINT + str(q_id)
            resp = requests.get(url=url)
        else:
            resp = requests.get(url=self.HOST + self.ENDPOINT, params=params)

        if self.JSON is True:
            return resp.json()
        else:
            return resp

    def get_character_results(self, page_num: int = 1, to_pandas: bool = False) -> dict:
        """get 20 characters from the specified page number

        Args
            page_num (int): page to return

        Returns
            dict: 20 characters with various fields
        """
        params = {"page": page_num}
        resp = self._get(params=params)

        if to_pandas is True and self.JSON is True:
            return resp["info"], DataFrame(resp["results"])
        else:
            return resp

    def get_character_info(self) -> dict:
        """get summary of number of pages and characters available

        Args
            None

        Returns
            (dict): info on the characters available on the rick and morty API
        """
        resp = self._get()
        return resp

    def get_character_single(self, id: int) -> dict:
        """get a character from their ID

        Args
            id (int): id of the character to be returned

        Returns
            dict: information about the character
        """
        resp = self._get(q_id=id)
        return resp

    def get_character_all(self) -> list:
        """get a list of all the characters from the api

        Args
            None

        Returns

        """
        results = []
        num_of_pages = self.get_character_info()["pages"] + 1

        for page in range(1, num_of_pages):
            chars = self.get_character_results(page)
            for char in chars:
                results.append(char)

        return results

    def get_character_multiple(self, ids: list) -> list:
        """get mutliple characters using their id

        Args
            ids (list): of integer ids

        Returns
            results (list): character dictionaries for ids
        """
        results = [self.get_character_single(id=_id) for _id in ids]

        return results

    def get_character_filter(
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
        resp = self._get(params=params)

        return resp
