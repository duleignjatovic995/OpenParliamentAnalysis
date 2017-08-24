"""
This file contains stop words for Serbian language merged from various sources
"""
# Classic stop words
stop_words = ['a', 'ako', 'ali', 'baš', 'bez', 'bi', 'bih', 'bijah', 'bijahu', 'bijasmo', 'bijaste', 'bijaše', 'bila',
              'bile', 'bili', 'bilo', 'bio', 'bismo', 'biste', 'biti', 'biće', 'biše', 'bje', 'bjeh', 'bjehu', 'bjesmo',
              'bjeste', 'bješe', 'blizu', 'broj', 'budem', 'budemo', 'budete', 'budeš', 'budimo', 'budite', 'budu',
              'bumo', 'da', 'dana', 'danas', 'do', 'dobar', 'dobiti', 'dok', 'dole', 'doæi', 'doći', 'došao', 'drugi',
              'duž', 'dva', 'ga', 'gde', 'gore', 'hoće', 'hoćemo', 'hoćete', 'hoćeš', 'hoću', 'hvala', 'i', 'iako',
              'ide', 'ih', 'ili', 'ima', 'imam', 'imao', 'ispod', 'iz', 'izmeðu', 'između', 'iznad', 'izvan', 'izvoli',
              'ići', 'ja', 'je', 'jedan', 'jedini', 'jedna', 'jedne', 'jedno', 'jednom', 'jer', 'jesam', 'jesi',
              'jesmo', 'jest', 'jeste', 'jesu', 'jim', 'joj', 'još', 'ju', 'juèe', 'juče', 'kad', 'kada', 'kako', 'kao',
              'koga', 'koja', 'koje', 'koji', 'kojima', 'koju', 'kroz', 'li', 'mali', 'manji', 'me', 'mene', 'meni',
              'mi', 'mimo', 'misli', 'mnogo', 'mogu', 'moj', 'moja', 'moje', 'mora', 'moraju', 'moram', 'moramo',
              'morao', 'morate', 'moraš', 'moæi', 'moći', 'može', 'možemo', 'možete', 'možeš', 'mu', 'na', 'nad',
              'nakon', 'nam', 'nama', 'nas', 'naći', 'naš', 'naša', 'naše', 'našeg', 'ne', 'negde', 'nego', 'neka',
              'nekad', 'neki', 'nekog', 'neku', 'nema', 'nemam', 'netko', 'neće', 'nećemo', 'nećete', 'nećeš', 'neću',
              'nešto', 'ni', 'nije', 'nijedan', 'nikada', 'nikoga', 'nikoje', 'nikoju', 'nisam', 'nisi', 'nismo',
              'niste', 'nisu', 'ništa', 'njega', 'njegov', 'njegova', 'njegovo', 'njemu', 'njen', 'njezin', 'njezina',
              'njezino', 'njih', 'njihov', 'njihova', 'njihovo', 'njim', 'njima', 'njoj', 'nju', 'no', 'o', 'od',
              'odmah', 'oko', 'okolo', 'on', 'ona', 'onaj', 'oni', 'ono', 'osim', 'ostali', 'otišao', 'ova', 'ovako',
              'ovamo', 'ovde', 'ove', 'ovo', 'pa', 'pak', 'pitati', 'po', 'pod', 'pojedini', 'pored', 'posle',
              'povodom', 'početak', 'praviti', 'pre', 'preko', 'prema', 'prije', 'prvi', 'put', 'radije', 's', 'sa',
              'sada', 'sam', 'samo', 'se', 'sebe', 'sebi', 'si', 'smeti', 'smo', 'ste', 'stvar', 'stvarno', 'su',
              'sutra', 'svaki', 'sve', 'svi', 'svim', 'svog', 'svoj', 'svoja', 'svoje', 'svom', 'svugde', 'ta', 'tada',
              'taj', 'tako', 'takođe', 'tamo', 'tačno', 'te', 'tebe', 'tebi', 'ti', 'tim', 'to', 'toj', 'tome', 'treba',
              'trebaju', 'trebam', 'trebamo', 'trebate', 'trebaš', 'tu', 'tvoj', 'tvoja', 'tvoje', 'u', 'umalo',
              'unutra', 'upotrebiti', 'uz', 'uzeti', 'učinio', 'učiniti', 'vam', 'vama', 'vas', 'vaš', 'vaša', 'vaše',
              'veoma', 'već', 'većina', 'vi', 'video', 'više', 'vrlo', 'za', 'zahvaliti', 'zar', 'zašto', 'zbog',
              'znati', 'će', 'ćemo', 'ćete', 'ćeš', 'ću', 'često', 'čiji', 'šta', 'što', 'žele', 'želeo', 'želi',
              'želim', 'želimo', 'želite', 'želiš', '.', ',', ':', ';', '"', "'", '-']
# Part of stop words containing čćžđš without čćžđš
bald_stop_words = ['bas', 'bijase', 'bice', 'bise', 'bjese', 'budes', 'doci', 'dosao', 'duz', 'hoce', 'hocemo',
                   'hocete', 'hoces',
                   'hocu', 'izmedju', 'ici', 'jos', 'juce', 'moras', 'moci', 'moze', 'mozemo', 'mozete', 'mozes',
                   'naci', 'nasa',
                   'nase', 'naseg', 'nece', 'necemo', 'necete', 'neces', 'necu', 'nesto', 'nista', 'otisao', 'pocetak',
                   'takodje',
                   'tacno', 'trebas', 'ucinio', 'uciniti', 'vasa', 'vase', 'vec', 'vecina', 'vise', 'zasto', 'ce',
                   'cemo', 'cete',
                   'ces', 'cu', 'cesto', 'ciji', 'sta', 'sto', 'zele', 'zeleo', 'zeli', 'zelim', 'zelimo', 'zelite',
                   'zelis']

waste_words = ['izmen', 'dopun', 'visok', 'posupk', 'javn', 'drzavn', 'vlad', 'republik', 'srbij', 'potvrđivanj',
               'sporazum', 'odluk', 'sporazum']
