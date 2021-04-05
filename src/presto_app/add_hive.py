# this script is presto job from mysql to hive

import prestodb.dbapi as presto

with presto.Connection(host="presto", port=8080, user="alireza") as conn:

    cur = conn.cursor()

    cur.execute("USE hive.default")
    cur.execute("CREATE TABLE hive.default.tweets AS SELECT * FROM mysql.maindb.tweets")
    cur.fetchall()
