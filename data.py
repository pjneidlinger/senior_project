from lxml import html
import requests

page = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_leaders.html')
tree = html.fromstring(page.content)
fileout = open( "data.txt", 'w')


#name = tree.xpath('//*[@id = "leaders_pts_per_g"]/table/caption/text()[normalize-space()]')
#name = ' '.join(name)

pts = tree.xpath('//*[@id = "leaders_pts_per_g"]/table/tr[20]/td[3]/text()[normalize-space()]')
pts = ' '.join(pts)
pts = pts[1:]

trb = tree.xpath('//*[@id = "leaders_trb_per_g"]/table/tr[20]/td[3]/text()[normalize-space()]')
trb = ' '.join(trb)
trb = trb[1:]

ast = tree.xpath('//*[@id = "leaders_ast_per_g"]/table/tr[20]/td[3]/text()[normalize-space()]')
ast = ' '.join(ast)
ast = ast[1:]

fileout.write( pts )
fileout.write( "\n" )
fileout.write( trb )
fileout.write( "\n" )
fileout.write( ast )
fileout.close()


