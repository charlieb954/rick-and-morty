import requests

__all__ = ["Episodes"]


class Episodes:
    HOST = "https://rickandmortyapi.com"
    ENDPOINT = "/api/episode/"
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

    def get_episode_results(self, page_num: int = 1) -> dict:
        """get 20 episodes from the specified page number

        Args
            page_num (int): page to return, default is 1

        Returns
            (dict): 20 episodes with various fields
        """
        params = {"page": page_num}
        resp = self._get(params)
        return resp

    def get_episode_info(self) -> dict:
        """get summary of number of pages and episodes available

        Args
            None

        Returns
            (dict): info on the episodes available on the rick and morty API.
        """
        resp = self._get()
        return resp

    def get_episode_single(self, id: int):
        """get an episode from their ID

        Args
            id (int): id of the episode to be returned

        Returns
            (dict): information about the episode
        """
        resp = self._get(q_id=id)
        return resp

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
                results.append(epi)
        return results
