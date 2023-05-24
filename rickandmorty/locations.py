import requests

__all__ = ["Locations"]


class Locations:
    HOST = "https://rickandmortyapi.com/api/location/"
    DOCS = "https://rickandmortyapi.com/documentation/"

    def get_location_results(self, page_num: int = 1) -> dict:
        """get 20 locations from the specified page number

        Args
            page_num (int): page to return

        Returns
            (dict): 20 characters with various fields
        """
        params = {"page": page_num}
        data = requests.get(self.HOST, params).json()
        return data["results"]

    def get_location_info(self) -> dict:
        """get summary of number of pages and locations available

        Args
            None

        Returns
            (dict): info on the locations available on the rick and morty API.
        """
        data = requests.get(self.HOST).json()
        return data["info"]

    def get_location_single(self, id: int) -> dict:
        """get a location from their ID

        Args
            id (int): id of the location to be returned

        Returns
            (dict): information about the location
        """

        data = requests.get(self.HOST + str(id)).json()
        return data

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
                results.append((loc["id"], loc["name"]))
        return results
