import pymysql


#def query(name):
# 连接数据库
db = pymysql.connect("14.18.117.150", "monitor", "Sheer6Theiroophe@", "vps_monitor")
cur = db.cursor()
sql = """SELECT AVG(band)AS avgBand,alias FROM vps_monitor WHERE alias="node1" AND update_time > DATE_SUB(NOW(),INTERVAL 1 HOUR)"""
cur.execute(sql)
result = cur.fetchall()
print(result)
print(type(result))