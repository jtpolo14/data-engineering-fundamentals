## SQL Game Plan

Lecture 01

- download https://sqlitebrowser.org/dl/, install, open
- New Database (Note the SQL query!!!!!)
- add fields
- names, types, constraints
- Keys: primary, foreign
- Schema
```sql
CREATE TABLE "project" (
	"pid"	INTEGER UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	"status"	TEXT NOT NULL,
	"created"	TEXT,
	PRIMARY KEY("pid" AUTOINCREMENT)
);
``` 

Lecture 02

- Queries and Keywords
- INSERT
  - INSERT INTO project (title, status, created) VALUES ("p1 - onboard agent", "on track", "20260215");
- SELECT
- FROM
- WHERE
```sql
SELECT * FROM project WHERE status = "on track";
```
