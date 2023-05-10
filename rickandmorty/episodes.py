import requests

__HOST = "https://rickandmortyapi.com/api"
__DOCS = "https://rickandmortyapi.com/documentation/"

__all__ = ['get_episode_results',
            'get_episode_info',
            'get_episode_single',
            'get_episode_all',
            #'get_episode_multi',
            #'episode_filter'
            ]

def get_episode_results(page_num=1):
    """
    Get 20 episodes from the specified page number
    
    Parameters
    ----------
    page_num = int: page to return, default is 1
    
    Returns
    -------
    json: 20 episodes with various fields
    """
    endpoint = "/episode"
    params = {
        "page": page_num
        }
    data = requests.get(__HOST + endpoint, params).json()
    return data['results']

def get_episode_info():
    """
    Get summary of number of pages and episodes available
    
    Parameters
    ----------
    None
    
    Returns
    -------
    json: information about the episodes available on the rick and morty API.
    """
    endpoint = "/episode"
    data = requests.get(__HOST + endpoint).json()
    return data['info']

def get_episode_single(id):
    """
    Get an episode from their ID
    
    Parameters
    ----------
    id = int: id of the episode to be returned
    
    Returns
    -------
    json: information about the episode
    """
    endpoint = f"/episode/{int(id)}"

    data = requests.get(__HOST + endpoint).json()
    return data

def get_episode_all():
    """
    Get a list of all the episode names from the api
    
    Parameters
    ----------
    None
    
    Returns
    -------
    results = list: of episode names
    """
    results = []
    num_of_pages = get_episode_info()['pages'] + 1

    for i in range(1, num_of_pages):
        episodes = get_episode_results(i)
        for epi in episodes:
            results.append((epi['id'], epi['name']))
    return results