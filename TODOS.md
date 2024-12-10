faster mysql container stopping
fix db not setting up in container
fix weird container naming
fix warnings in mysql container
create healthchecks for mysqldb
add persistent volume to db
add this mysql -u root -p < docker-entrypoint-initdb.d/schema.sql to entrypoint
create ansible to run/clear envinronment