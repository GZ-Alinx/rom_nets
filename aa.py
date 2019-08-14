import pymysql


#def query(name):
# 连接数据库
db = pymysql.connect("数据库地址", "用户名", "密码", "数据库")
")
cur = db.cursor()
sql = """SELECT AVG(band)AS avgBand,alias FROM vps_monitor WHERE alias="node1" AND update_time > DATE_SUB(NOW(),INTERVAL 1 HOUR)"""
cur.execute(sql)
result = cur.fetchall()
print(result)
print(type(result))
