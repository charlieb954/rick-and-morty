import requests

HOST = "https://rickandmortyapi.com/api"
DOCS = "https://rickandmortyapi.com/documentation/"

def get_character_results(page_num=1):
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
    data = requests.get(HOST + endpoint, params).json()
    return data['results']

def get_character_info():
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
    data = requests.get(HOST + endpoint).json()
    return data['info']

def get_character_single(id):
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
    data = requests.get(HOST + endpoint, params).json()
    return data['results']

def get_character_all():
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
    num_of_pages = get_character_info()['pages'] + 1

    for i in range(1, num_of_pages):
        chars = get_character_results(i)
        for char in chars:
            results.append(char)
        
    return results

def get_character_multi(ls):
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
        char = get_character_single(i)
        results.append(char['results'])
    return results

def character_filter(name=None, status=None, species=None, type=None, gender=None):
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
    data = requests.get(HOST + endpoint, params).json()
    
    return data

def get_location_results(page_num=1):
    endpoint = "/location"
    params = {
        "page": page_num
        }
    data = requests.get(HOST + endpoint, params).json()
    return data['results']

def get_location_info():
    """
    Get summary of number of pages and characters available
    
    Parameters
    ----------
    None
    
    Returns
    -------
    json: information from rick and morty api
    """
    endpoint = "/location"
    data = requests.get(HOST + endpoint).json()
    return data['info']

def get_location_single(id):
    pass

def get_locations_all():
    results = []
    num_of_pages = get_location_info()['pages'] + 1

    for i in range(1, num_of_pages):
        locations = get_location_results(i)
        for loc in locations:
            results.append(loc['name'])
    return results

def get_episode_results(page_num=1):
    endpoint = "/episode"
    params = {
        "page": page_num
        }
    data = requests.get(HOST + endpoint, params).json()
    return data['results']

def get_episode_info():
    endpoint = "/episode"
    data = requests.get(HOST + endpoint).json()
    return data['info']

def get_episode_single(id):
    pass

def get_episode_all():
    results = []
    num_of_pages = get_episode_info()['pages'] + 1

    for i in range(1, num_of_pages):
        episodes = get_episode_results(i)
        for epi in episodes:
            results.append(epi['name'])
    return results