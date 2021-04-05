.PHONY: down up run-twitter run-presto-mongo run-presto-hive \
mongo-up mongo-down hive-up hive-down hive-exec

down:
	docker-compose down -v

up:
	docker-compose up --build -d app presto mysql

run-twitter:
	docker-compose exec app python twitter_app/twitter_stream.py

mysql-exec:
	docker-compose exec mysql bash
	# mysql -u mainuser -p maindb
	# select count(*) from tweets;

run-presto-mongo:
	docker-compose exec app python presto_app/add_mongo.py

run-presto-hive:
	docker-compose exec app python presto_app/add_hive.py

mongo-up:
	docker-compose up --build -d mongodb

mongo-down:
	docker-compose stop mongodb
	docker-compose rm mongodb

mongo-exec:
	docker-compose exec mongodb bash
	# mongo -u "root" -p rootpassword --authenticationDatabase "admin"
	# use admin
	# db.tweets.count()

hive-up:
	docker-compose up --build -d namenode datanode hive-metastore hive-server hive-metastore-postgresql

hive-down:
	docker-compose stop namenode datanode hive-metastore hive-server hive-metastore-postgresql
	docker-compose rm namenode datanode hive-metastore hive-server hive-metastore-postgresql

hive-exec:
	docker-compose exec hive-server bash
	# hive
	# select count(*) from tweets;