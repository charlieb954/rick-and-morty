============
rickandmorty
============


.. image:: https://img.shields.io/pypi/v/rickandmorty.svg
        :target: https://pypi.python.org/pypi/rickandmorty

.. image:: https://img.shields.io/travis/charlieb954/rickandmorty.svg
        :target: https://travis-ci.com/charlieb954/rickandmorty

.. image:: https://readthedocs.org/projects/rickandmorty/badge/?version=latest
        :target: https://rickandmorty.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/charlieb954/rickandmorty/shield.svg
     :target: https://pyup.io/repos/github/charlieb954/rickandmorty/
     :alt: Updates



Python API wrapper to query https://rickandmortyapi.com/


* Free software: MIT license
* Documentation: https://rickandmorty.readthedocs.io.


Examples
--------
..  code-block:: python
        
        from rickandmorty import Characters, Episodes, Locations

        characters, episodes, locations = Characters(), Episodes(), Locations()

        all_characters = characters.get_characters_all()
        all_episodes = episodes.get_episodes_all()
        all_locations = locations.get_locations_all()


Features
--------

* Retrieve all character information from the Rick and Morty API.
* Retrieve all episode information from the Rick and Morty API.
* Retrieve all location information from the Rick and Morty API.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
