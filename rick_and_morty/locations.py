import requests

__HOST = "https://rickandmortyapi.com/api"
__DOCS = "https://rickandmortyapi.com/documentation/"

def get_location_results(page_num=1):
    """
    Get 20 locations from the specified page number
    
    Parameters
    ----------
    page_num = int: page to return
    
    Returns
    -------
    json: 20 characters with various fields
    """
    endpoint = "/location"
    params = {
        "page": page_num
        }
    data = requests.get(__HOST + endpoint, params).json()
    return data['results']

def get_location_info():
    """
    Get summary of number of pages and locations available
    
    Parameters
    ----------
    None
    
    Returns
    -------
    json: information about the locations available on the rick and morty API.
    """
    endpoint = "/location"
    data = requests.get(__HOST + endpoint).json()
    return data['info']

def get_location_single(id):
    """
    Get a location from their ID
    
    Parameters
    ----------
    id = int: id of the location to be returned
    
    Returns
    -------
    json: information about the location
    """
    endpoint = f"/location/{int(id)}"

    data = requests.get(__HOST + endpoint).json()
    return data

def get_location_all():
    """
    Get a list of all the location names from the api
    
    Parameters
    ----------
    None
    
    Returns
    -------
    results = tuple: location id, location names
    """
    results = []
    num_of_pages = get_location_info()['pages'] + 1

    for i in range(1, num_of_pages):
        locations = get_location_results(i)
        for loc in locations:
            results.append((loc['id'], loc['name']))
    return results

