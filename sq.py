import mysql.connector
import leaderboard
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="USER",
  password="PASS",
  database="leaderboard"
)

mycursor = mydb.cursor()

def lb(arg):
	mycursor.execute("DROP TABLE leaders")
	mycursor.execute("CREATE TABLE leaders (PlayerID integer(10), level integer(10), position integer(10))")
	for i in range(1,arg+1):
		topper = leaderboard.lead_webcr(i)
		top = json.loads(topper) 
		player = top.get("id")
		lev = top.get("in_level")
		pos = top.get("rank")
		sql = f"INSERT INTO leaders (PlayerID, level, position) VALUES ({player}, {lev}, {pos})"
		mycursor.execute(sql)

	mycursor.execute("SELECT * FROM leaders")

	myresult = mycursor.fetchall()

	return myresult


def RankInfo(arg):
	mycursor.execute("DROP TABLE comleader")
	mycursor.execute("CREATE TABLE comleader (PlayerID integer(10), level integer(10), position integer(10))")
	playerList = leaderboard.leaderb()
	for info in playerList:
		top = json.loads(info) 
		player = top.get("id")
		lev = top.get("in_level")
		pos = top.get("rank")
		sql = f"INSERT INTO comleader (PlayerID, level, position) VALUES ({player}, {lev}, {pos})"
		mycursor.execute(sql)

	cmd = f"SELECT * FROM comleader WHERE position = {arg}"

	mycursor.execute(cmd)

	myresult = mycursor.fetchall()

	return myresult

