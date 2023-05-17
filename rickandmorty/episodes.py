import requests

__all__ = ["Episodes"]


class Episodes:
    HOST = "https://rickandmortyapi.com/api"
    DOCS = "https://rickandmortyapi.com/documentation/"

    def get_episode_results(self, page_num: int = 1) -> dict:
        """get 20 episodes from the specified page number

        Args
            page_num (int): page to return, default is 1

        Returns
            (dict): 20 episodes with various fields
        """
        endpoint = "/episode"
        params = {"page": page_num}
        data = requests.get(self.HOST + endpoint, params).json()
        return data["results"]

    def get_episode_info(self) -> dict:
        """get summary of number of pages and episodes available

        Args
            None

        Returns
            (dict): information about the episodes available on the rick and morty API.
        """
        endpoint = "/episode"
        data = requests.get(self.HOST + endpoint).json()
        return data["info"]

    def get_episode_single(self, id: int):
        """get an episode from their ID

        Args
            id (int): id of the episode to be returned

        Returns
            (dict): information about the episode
        """
        endpoint = f"/episode/{int(id)}"

        data = requests.get(self.HOST + endpoint).json()
        return data

    def get_episode_all(self) -> list:
        """get a list of all the episode names from the api

        Args
            None

        Returns
            results (list): of episode names
        """
        results = []
        num_of_pages = self.get_episode_info()["pages"] + 1

        for i in range(1, num_of_pages):
            episodes = self.get_episode_results(i)
            for epi in episodes:
                results.append((epi["id"], epi["name"]))
        return results
