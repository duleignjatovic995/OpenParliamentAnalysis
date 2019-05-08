"""
    Akt entities functions.
"""
from data.get_data import get_json


def akt_naslov_list():
    """
    Returns list of al akt entities titles.
    :return: list of akt titles.
    """
    lst = []
    data = get_json('http://otvoreniparlament.rs/akt')
    num_pages = data['paginator']['last_page']
    for i in range(num_pages + 1):
        page = get_json(url='http://otvoreniparlament.rs/akt', page=i)
        content = page['akta']
        for obj in content:
            lst.append(obj['naslov'])
    return lst


def akt_opis(akt_id):
    url = 'http://otvoreniparlament.rs/akt/' + str(akt_id)
    data = get_json(url)['akt']
    naziv = data['naslov']
    sazetak = data['sazetak']
    return naziv, sazetak