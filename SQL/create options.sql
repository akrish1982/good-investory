--
-- File generated with SQLiteStudio v3.1.1 on Mon Jul 24 21:17:48 2017
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: options
CREATE TABLE options (
    INSTRUMENT       CHAR    NOT NULL,
    SYMBOL           CHAR    NOT NULL,
    EXPIRY_DT        DATE,
    STRIKE_PR        DECIMAL,
    OPTION_TYP       DECIMAL,
    OPEN             DECIMAL,
    HIGH,
    LOW,
    CLOSE,
    SETTLE_PR,
    CONTRACTS        DECIMAL,
    VAL_INLAKH,
    OPEN_INT,
    CHG_IN_OI,
    Percent_Move,
    TIMESTAMP,
    Premium,
    EMPTY,
    LOT_SIZE         INTEGER,
    Underlying_price
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
