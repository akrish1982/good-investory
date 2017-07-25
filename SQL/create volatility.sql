--
-- File generated with SQLiteStudio v3.1.1 on Mon Jul 24 21:19:42 2017
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: volatility
CREATE TABLE volatility (
    Date                                    DATE,
    Symbol                                  STRING,
    close                                   DECIMAL,
    prev_close                              DECIMAL,
    log_returns                             DECIMAL,
    Previous_Day_Volatility                 DECIMAL,
    Current_Day_Underlying_Daily_Volatility DECIMAL,
    Annualised_Volatility                   DECIMAL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
