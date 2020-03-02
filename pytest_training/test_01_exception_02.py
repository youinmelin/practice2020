import pytest
def create_character(name: str, class_name:str):
    """
    Creates a new character and inserts it into the database.
    :raise IncalidCharacterNameError:
        if the character name is empty.

    :raise InvalidClassNameError:
        if the class name is invalid.

    :return: the newly created Character.
    """
    ...
                
def test_empty_name():
    with pytest.raises(InvalidCharacterNameError):
        create_character(name='', class_name='warrior')

def test_invalid_class_name():
    with pytest.raises(InvalidClassNameError):
        create_character(name='Solaire', class_name='mage')
