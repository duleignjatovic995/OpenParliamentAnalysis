import pymysql
from data import get_data

hostname = 'localhost'
username = 'root'
password = '$CaravanPalace95'
database = 'open_par'


def get_akt_ids():
    lst = []
    data = get_data.get_json('http://otvoreniparlament.rs/akt')
    num_pages = data['paginator']['last_page']
    for i in range(num_pages + 1):
        page = get_data.get_json(url='http://otvoreniparlament.rs/akt', page=i)
        content = page['akta']
        for obj in content:
            lst.append(obj['akt_id'])
    return lst


def cache_akt():
    connenction = pymysql.connect(host=hostname, user=username, password=password, db=database, charset='utf8mb4')
    akt_ids = get_akt_ids()
    for id in akt_ids:
        naslov, sazetak = get_data.akt_opis(id)
        query = "INSERT INTO open_par.akt(akt_id, naslov, sazetak) VALUES (" + str(
            id) + ", '" + naslov + "', '" + sazetak + "');"
        with connenction.cursor() as cursor:
            try:
                cursor.execute(query)
                connenction.commit()
                print('akt id: ', id)
            except pymysql.err.IntegrityError:
                print('isti primarni kljuc')
            except:
                pass


def get_cached_akt():
    connenction = pymysql.connect(host=hostname, user=username, password=password, db=database, charset='utf8mb4')
    query = "SELECT sazetak FROM open_par.akt WHERE sazetak != '';"
    with connenction.cursor() as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except:
            print('Greska')
    row = [item[0] for item in result]
    return row


if __name__ == '__main__':
    # cache_akt()
    print(get_cached_akt())
