import requests

__HOST = "https://rickandmortyapi.com/api"
__DOCS = "https://rickandmortyapi.com/documentation/"

__all__ = ['get_character_results',
            'get_character_info',
            'get_character_single',
            'get_character_all',
            'get_character_multi',
            'character_filter']

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
    data = requests.get(__HOST + endpoint, params).json()
    return data['results']

def get_character_info():
    """
    Get summary of number of pages and characters available
    
    Parameters
    ----------
    None
    
    Returns
    -------
    json: information about the characters available on the rick and morty API
    """
    endpoint = "/character"
    data = requests.get(__HOST + endpoint).json()
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
    endpoint = f"/character/{int(id)}"
    data = requests.get(__HOST + endpoint).json()
    return data

def get_character_all():
    """
    Get a list of all the characters from the api
    
    Parameters
    ----------
    None
    
    Returns
    -------
    results = tuple: characters id, characters name
    """
    results = []
    num_of_pages = get_character_info()['pages'] + 1

    for i in range(1, num_of_pages):
        chars = get_character_results(i)
        for char in chars:
            results.append((char['id'], char['name']))
        
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
    data = requests.get(__HOST + endpoint, params).json()
    
    return data