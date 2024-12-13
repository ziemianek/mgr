todo:
- [] fix warnings in mysql container
- [] create healthchecks for mysqldb
- [] add persistent volume to db
- [] create ansible to run/clear envinronment
- [] better setup for github repo
- [] database security
- [] create api tests
- [] do gitops research
- [] setup gitops

done:
- [x] create todo list
- [x] fix weird container naming
- [x] add this mysql -u root -p < docker-entrypoint-initdb.d/schema.sql to entrypoint
    - [x] fix entrypoint
    - at the end i managed to not use entrypoint script
- [x] handle api versioning
- [x] update readme/ generate cool readme
