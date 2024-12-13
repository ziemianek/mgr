todo:
- [] fix warnings in mysql container
- [] create healthchecks for mysqldb
- [] add persistent volume to db
- [] better setup for github repo
- [] database security
- [] do gitops research
- [] setup gitops
- [] add parameteres to docker_compose role
- [] add role to build api image
- [] better design for roles to create/delete local env


done:
- [x] create todo list
- [x] fix weird container naming
- [x] add this mysql -u root -p < docker-entrypoint-initdb.d/schema.sql to entrypoint
    - [x] fix entrypoint
    - at the end i managed to not use entrypoint script
- [x] handle api versioning
- [x] update readme/ generate cool readme
- [x] create api tests
- [x] create ansible to run/clear envinronment
