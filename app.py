from flask import Flask, render_template
import pymysql

app = Flask(__name__)


# network_Rx 下载流量
# network_Tx 上传流量

@app.route('/server/<name>')
def query(name):
    db = pymysql.connect("数据库地址", "用户名", "密码", "数据库")
    cur = db.cursor()
    #sql = """SELECT AVG(band)AS avgBand,alias FROM vps_monitor WHERE alias="%s" AND update_time > DATE_SUB(NOW(),INTERVAL 1 HOUR)"""%name
    #sql = """SELECT (ROUND(((ROUND(AVG(network_tx)))+(ROUND(AVG(network_rx)))) / 1024 ))AS 平均流量,alias AS 服务器节点 FROM vps_monitor WHERE alias="Nginx" AND update_time > DATE_SUB(NOW(),INTERVAL 1 HOUR)"""
    sql = """SELECT ((ROUND(AVG(network_tx)))+(ROUND(AVG(network_rx))))AS 平均流量,alias AS 服务器节点 FROM vps_monitor WHERE alias="%s" AND update_time > DATE_SUB(NOW(),INTERVAL 1 HOUR)"""%name
    cur.execute(sql)
    result = cur.fetchall()
    data = {
        "net":result[0][0],
        "name":result[0][1]
    }
    return render_template('data.html',data=data)



@app.route('/')
def hello_world():
    return '接口正常'


if __name__ == '__main__':
    app.run()
