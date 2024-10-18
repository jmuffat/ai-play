---
CREATE TABLE message (
        msg_id      STRING PRIMARY KEY,
        msg_date    TIMESTAMPTZ,
        msg_subject STRING
);

---
CREATE TABLE message_label (
    mlb_message STRING,
    mlb_label   STRING,

    PRIMARY KEY (mlb_message, mlb_label)
);

CREATE INDEX idxmlb_label ON message_label(mlb_label,mlb_message);

---
CREATE TABLE message_address (
        mad_message STRING,
        mad_rel STRING, -- from/to/cc
        mad_address STRING,
        mad_alias STRING,

        PRIMARY KEY (mad_message, mad_rel, mad_address)
);

CREATE INDEX idxmad_address ON message_address(mad_address,mad_rel,mad_message);
