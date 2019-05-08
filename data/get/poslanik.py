"""
    Functions for poslanik entities and their speeches.
"""
from data.get_data import get_json


def poslanik_govori(poslanik_id):
    """
    Returns list of speeches for all poslanik entities.
    :param poslanik_id: id of poslanik entity
    :return: list of speeches.
    """
    lst = []
    url = 'http://otvoreniparlament.rs/poslanik/' + str(poslanik_id) + '/govori'
    data = get_json(url)
    num_pages = data['govori']['last_page']
    for i in range(num_pages):
        page = get_json(url=url, page=i)
        govori = page['govori']['data']
        for govor in govori:
            lst.append(govor['govor'])
    return lst


def osoba_poslanik_list():
    """
    This is method for observing relations between entities
    "osoba" and "poslanik".
    :return: dict {"osoba_id": ["poslanik_id"*]}
    """
    lst1 = []
    lst2 = []
    osoba_poslanik_dict = defaultdict(list)

    data = get_json('http://otvoreniparlament.rs/poslanik')
    for stranka in data:
        # print(stranka)
        lista_poslanika = data[stranka]
        for poslanik in lista_poslanika:
            print(poslanik['ime'])
            osoba_id = poslanik['osoba_id']
            poslanik_id = poslanik['id']
            osoba_poslanik_dict[osoba_id].append(poslanik_id)
            lst1.append(osoba_id)
            lst2.append(poslanik_id)
    return osoba_poslanik_dict


def poslanik_id_list():
    """
    This method returns list of all active poslanik_id's
    :return: poslanik_id list
    """
    lst = []
    data = get_json('http://otvoreniparlament.rs/poslanik')
    for stranka in data:
        lista_poslanika = data[stranka]
        for poslanik in lista_poslanika:
            poslanik_id = poslanik['id']
            lst.append(poslanik_id)
    return lst


# todo: obavezno kesirati
def poslanik_govori_list():
    govori_dict = defaultdict(list)
    govori_list = []
    lst = poslanik_id_list()
    for id in lst:
        govori = poslanik_govori(id)
        print(govori)
        # govori_dict[id].append(govori)
        govori_list.append(govori)
    return govori_list
