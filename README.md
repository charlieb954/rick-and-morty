# RICK AND MORTY API WRAPPER

Python API wrapper to query https://rickandmortyapi.com/

Example usage:
1. git clone &lt;ssh url&gt;
2. from terminal run python3

        import rick_and_morty

        # get all character names and ids
        rick_and_morty.characters.get_character_all()

        # get location info
        rick_and_morty.locations.get_location_info()

        # get episode single
        rick_and_morty.episodes.get_episode_single(id=1)