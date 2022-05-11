-- SQLite
-- ALTER TABLE spwift_highertaxon DROP COLUMN disciplin_id;
BEGIN TRANSACTION;
CREATE TABLE transient(id,spid,name);
INSERT INTO transient SELECT id,spid,name FROM spwift_highertaxon;
DROP TABLE spwift_highertaxon;
ALTER TABLE transient RENAME TO spwift_highertaxon;
COMMIT;