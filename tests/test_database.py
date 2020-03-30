__author__ = 'hzlaimingxing'


from health_checker.client.database.mysql import DatabaseManager


d = dict(host="127.0.0.1", user='root', password='fsy768394890', size=3)
db = DatabaseManager(**d)
print(db.binlog_size)


