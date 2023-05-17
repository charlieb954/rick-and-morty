import requests

__all__ = ["Locations"]


class Locations:
    HOST = "https://rickandmortyapi.com/api"
    DOCS = "https://rickandmortyapi.com/documentation/"

    def get_location_results(self, page_num: int = 1) -> dict:
        """get 20 locations from the specified page number

        Args
            page_num (int): page to return

        Returns
            (dict): 20 characters with various fields
        """
        endpoint = "/location"
        params = {"page": page_num}
        data = requests.get(self.HOST + endpoint, params).json()
        return data["results"]

    def get_location_info(self) -> dict:
        """get summary of number of pages and locations available

        Args
            None

        Returns
            (dict): information about the locations available on the rick and morty API.
        """
        endpoint = "/location"
        data = requests.get(self.HOST + endpoint).json()
        return data["info"]

    def get_location_single(self, id: int) -> dict:
        """get a location from their ID

        Args
            id (int): id of the location to be returned

        Returns
            (dict): information about the location
        """
        endpoint = f"/location/{int(id)}"

        data = requests.get(self.HOST + endpoint).json()
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

        for i in range(1, num_of_pages):
            locations = self.get_location_results(i)
            for loc in locations:
                results.append((loc["id"], loc["name"]))
        return results
