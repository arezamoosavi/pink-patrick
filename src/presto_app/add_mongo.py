# this script is presto job from mysql to mongodb

import prestodb.dbapi as presto

# conn = presto.Connection(host="presto", port=8080, user="alireza")
# conn = presto.Connection(
#     host="presto", port=8080, user="alireza", catalog="tcph", schema="sf10"
# )

with presto.Connection(host="presto", port=8080, user="alireza") as conn:

    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE mongodb.admin.tweets AS SELECT * FROM mysql.maindb.tweets"
    )
    cur.fetchall()
