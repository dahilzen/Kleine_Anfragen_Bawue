import scrapy


class AnfragenSpider(scrapy.Spider):
    name = "klanfrage"
    start_urls = [
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.05.2016&Datbis=31.05.2016',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.06.2016&Datbis=30.06.2016',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.07.2016&Datbis=31.07.2016',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.08.2016&Datbis=31.08.2016',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.09.2016&Datbis=30.09.2016',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.10.2016&Datbis=31.10.2016',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.11.2016&Datbis=30.11.2016',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.12.2016&Datbis=31.12.2016',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.01.2017&Datbis=31.01.2017',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.02.2017&Datbis=09.02.2017',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=11.02.2017&Datbis=28.02.2017',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.03.2017&Datbis=31.03.2017',
        'http://www.statistik-bw.de/OPAL/Ergebnis.asp?WP=16&VT13=1&Datvon=01.04.2017&Datbis=30.04.2017',
    ]

    def parse(self, response):
        for anfrage in response.xpath('//table'):
            yield {
                'schlagwort' : response.xpath('//tr').re('Schlagwort:\s*(.*)'),
                'betreff' : response.xpath('//tr').re('Betreff:\s*(.*)'),
                'behandlung' : response.xpath('//tr').re('KlAnfr\s*(.*)'),
            }