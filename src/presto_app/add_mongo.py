# this script is presto job from mysql to mongodb

import prestodb.dbapi as presto

# conn = presto.Connection(host="presto", port=8080, user="demo")
conn = presto.Connection(
    host="presto", port=8080, user="demo", catalog="tcph", schema="sf10"
)

cur = conn.cursor()

cur.execute("CREATE TABLE mongodb.presto.tweets AS SELECT * FROM mysql.maindb.tweets")

