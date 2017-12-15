import scrapy

#scrapy runspider scraper.py -t json -o barcelona_result.json

class VoteSpider(scrapy.Spider):
    name = "vote_spider"
    start_urls = ['http://www.gencat.cat/governacio/resultatsparlament2015/resu/09AU/DAU09089CI_L2.htm']

    def parse(self, response):
        table = response.xpath("//table[@id='TVGEN']")
        white_votes = table.xpath(".//tbody/tr[4]")

        print (white_votes.extract())

        name = white_votes.xpath(".//th[1]/text()").extract_first()
        votes = white_votes.xpath(".//td[1]/text()").extract_first()
        yield {
            'name'  : name,
            'votes' : votes
        }

        table = response.xpath("//table[@id='TVOTOS']")

        parties = table.xpath(".//tbody/tr")
        for party in parties:
            name = party.xpath(".//th[@class='siglas15 titmov15']/text()").extract_first()
            votes = party.xpath(".//td[@class='vots s15']/text()").extract_first()
            if (name != None) :
                yield {
                    'name' : name,
                    'votes': votes
                }


          #if (name != None): votesList.append((name, votes))

        #print(votesList)


#print (votesList[0])