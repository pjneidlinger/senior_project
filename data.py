from lxml import html
import requests

page0 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/scoring-per-game')
tree0 = html.fromstring(page0.content)

pts = tree0.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[22]/td[6]/text()[normalize-space()]')
pts = ' '.join(pts)

page1 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/rebounds')
tree1 = html.fromstring(page1.content)

trb = tree1.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[22]/td[11]/text()[normalize-space()]')
trb = ' '.join(trb)

page2 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/assists')
tree2 = html.fromstring(page2.content)

ast = tree2.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[22]/td[7]/text()[normalize-space()]')
ast = ' '.join(ast)

page3 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/steals')
tree3 = html.fromstring(page3.content)

stl = tree3.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[22]/td[7]/text()[normalize-space()]')
stl = ' '.join(stl)

page4 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/blocks')
tree4 = html.fromstring(page4.content)

blk = tree4.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[22]/td[8]/text()[normalize-space()]')
blk = ' '.join(blk)

page5 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/scoring-per-game/sort/fieldGoalPct')
tree5 = html.fromstring(page5.content)

fgp = tree5.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[22]/td[8]/text()[normalize-space()]')
fgp = ' '.join(fgp)

page6 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/scoring-per-game/sort/freeThrowPct')
tree6 = html.fromstring(page6.content)

ftp = tree6.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[22]/td[12]/text()[normalize-space()]')
ftp = ' '.join(ftp)

page7 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/turnovers/sort/avgTurnovers/order/false')
tree7 = html.fromstring(page7.content)

tov = tree7.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[22]/td[7]/text()[normalize-space()]')
tov = ' '.join(tov)

page8 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/3-points/sort/avgThreePointFieldGoalsMade')
tree8 = html.fromstring(page8.content)

tpm = tree8.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[24]/td[6]/text()[normalize-space()]')
tpm = ' '.join(tpm)

page9 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/field-goals/sort/avgFieldGoalsAttempted')
tree9 = html.fromstring(page9.content)

fga = tree9.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[24]/td[7]/text()[normalize-space()]')
fga = ' '.join(fga)

page10 = requests.get('http://www.espn.com/nba/statistics/player/_/stat/free-throws/sort/avgFreeThrowsAttempted')
tree10 = html.fromstring(page10.content)

fta = tree10.xpath('//*[@id="my-players-table"]/div/div[2]/table/tr[24]/td[7]/text()[normalize-space()]')
fta = ' '.join(fta)

fileout = open( "data.txt", 'w' )
fileout.write( pts )
fileout.write( "\n" )
fileout.write( trb )
fileout.write( "\n" )
fileout.write( ast )
fileout.write( "\n" )
fileout.write( stl )
fileout.write( "\n" )
fileout.write( blk )
fileout.write( "\n" )
fileout.write( fgp )
fileout.write( "\n" )
fileout.write( ftp )
fileout.write( "\n" )
fileout.write( tov )
fileout.write( "\n" )
fileout.write( tpm )
fileout.write( "\n" )
fileout.write( fga )
fileout.write( "\n" )
fileout.write( fta )
fileout.write( "\n" )
fileout.close()
