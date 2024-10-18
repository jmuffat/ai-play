CREATE TABLE IF NOT EXISTS ver (
    ver_id TEXT PRIMARY KEY,
    ver_value INTEGER
);

INSERT OR IGNORE INTO ver(ver_id,ver_value) VALUES ('db',0);

SELECT ver_value FROM ver WHERE ver_id='db';