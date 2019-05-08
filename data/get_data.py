import requests
import json
from collections import defaultdict


# todo refactor file

def get_json(url, page=1):
    headers = {'content-type': 'application/json'}
    params = {'page': page}
    r = requests.get(url, headers=headers, params=params)
    json_string = r.text.strip().replace('{"error":404}', '')
    data = json.loads(json_string)
    return data


"""
    Get entity functions.
"""


def get_osobe():
    data = get_json('http://otvoreniparlament.rs/osoba')
    content = data['osobe']
    for obj in content:
        _print_osoba(obj)


def get_poslanicki_klub():
    data = get_json('http://otvoreniparlament.rs/poslanicki-klub')
    content = data['poslanickiKlub']
    for obj in content:
        _print_poslanicki_klub(obj)


def get_politicke_partije():
    data = get_json('http://otvoreniparlament.rs/politicka-partija')
    content = data['politickePartije']
    for obj in content:
        _print_partija(obj)


def get_aktuelno():
    data = get_json('http://otvoreniparlament.rs/aktuelno')
    num_pages = data['vesti']['last_page']
    for i in range(1, num_pages + 1):
        # r = requests.get('http://otvoreniparlament.rs/aktuelno', headers={'content-type': 'application/json'},
        #                  params={'page': i})
        # json_string = r.text.strip().replace('{"error":404}', '')
        # data = json.loads(json_string)
        data = get_json(url='http://otvoreniparlament.rs/aktuelno', page=i)
        content = data['vesti']['data']
        for obj in content:
            print('id: ', obj['id'])
            print('naslov: ', obj['naslov'])
            print('datum ', obj['datum'])
            opis = obj['opis'].replace('<p>', '').replace('</p>', '').replace('<br />', '').replace('&scaron;', 'š') \
                .replace('<em>', '').replace('</em>', '')
            print('opis: ', opis)
            print()


"""
    Print entity functions.
"""


def _print_osoba(obj):
    print('id: ', obj['id'])
    print('ime: ', obj['ime'])
    print('prezime: ', obj['prezime'])
    print('datum rodjenja', obj['datum_rodjenja'])
    print('pol: ', obj['pol'])
    print('mesto rodjenja: ', obj['mesto_rodjenja'])
    print('profesija: ', obj['profesija'])
    print('biografija: ', obj['biografija'])
    print('\n')


def _print_poslanicki_klub(obj):
    print('id: ', obj['id'])
    print('naziv: ', obj['naziv'])
    print('opis: ', obj['opis'])
    print('last_update', obj['updated_at'])
    print('saziv id', obj['saziv_id'])
    print('\n')


def _print_partija(obj):
    print('id: ', obj['id'])
    print('naziv: ', obj['naziv'])
    print('\n')


"""
    ***************** Task specific functions *****************
"""

"""
    Akt entities functions.
"""


def akt_naslov_list():
    """
    Returns list of al akt entities titles.
    :return: list of akt titles. {"key"}
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



"""
    Functions for poslanik entities and their speeches.
"""


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


if __name__ == '__main__':
    # print(get_osobe())
    # print(osoba_poslanik_list())
    # print(poslanik_id_list())
    # print(poslanik_govori_list())
    print(akt_opis(3225))
