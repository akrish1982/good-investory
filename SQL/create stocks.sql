--
-- File generated with SQLiteStudio v3.1.1 on Mon Jul 24 21:19:05 2017
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: stocks
CREATE TABLE stocks (
    SYMBOL,
    SERIES,
    OPEN,
    HIGH,
    LOW,
    CLOSE,
    LAST,
    PREVCLOSE,
    TOTTRDQTY,
    TOTTRDVAL,
    TIMESTAMP   DATE,
    TOTALTRADES,
    ISIN,
    EMPTY
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
