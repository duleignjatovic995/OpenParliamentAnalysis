import requests
import json
from collections import defaultdict


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
    Task specific functions.
"""


def akt_naslov_list():
    lst = []
    data = get_json('http://otvoreniparlament.rs/akt')
    num_pages = data['paginator']['last_page']
    for i in range(num_pages + 1):
        page = get_json(url='http://otvoreniparlament.rs/akt', page=i)
        content = page['akta']
        for obj in content:
            lst.append(obj['naslov'])
    return lst


def poslanik_govori(poslanik_id):
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



# def poslanik_govor_list():
#     """
#     1. poslanik i osoba
#     2. {poslanik: osoba}
#     3. {osoba: [govori]}
#     :return:
#     """
#     lst = []
#     osoba_poslanik_dict = defaultdict(list)
#
#     data = get_json('http://otvoreniparlament.rs/poslanik')
#     for stranka in data:
#         print(stranka)
#         lista_poslanika = data[stranka]
#         for poslanik in lista_poslanika:
#             osoba_id = poslanik['osoba_id']
#             poslanik_id = poslanik['id']
#             osoba_poslanik_dict[osoba_id].append(poslanik_id)
#     print(len(osoba_poslanik_dict))


if __name__ == '__main__':
    print(poslanik_govori(8787))
