import requests

__all__ = ["Locations"]


class Locations:
    HOST = "https://rickandmortyapi.com"
    ENDPOINT = "/api/location/"
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

    def get_location_results(self, page_num: int = 1) -> dict:
        """get 20 locations from the specified page number

        Args
            page_num (int): page to return

        Returns
            (dict): 20 characters with various fields
        """
        params = {"page": page_num}
        resp = self._get(params=params)
        return resp

    def get_location_info(self) -> dict:
        """get summary of number of pages and locations available

        Args
            None

        Returns
            (dict): info on the locations available on the rick and morty API.
        """
        resp = self._get()
        return resp

    def get_location_single(self, id: int) -> dict:
        """get a location from their ID

        Args
            id (int): id of the location to be returned

        Returns
            (dict): information about the location
        """
        resp = self._get(q_id=id)
        return resp

    def get_location_all(self) -> tuple:
        """get a list of all the location names from the api

        Args
            None

        Returns
            results (tuple): location id, location names
        """
        results = []
        num_of_pages = self.get_location_info()["pages"] + 1

        for page in range(1, num_of_pages):
            locations = self.get_location_results(page)
            for loc in locations:
                results.append(loc)
        return results
