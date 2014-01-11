connect to afa user afa using afa;

DROP TABLE AFA_DATE;
CREATE TABLE AFA_DATE(
    WORKDATE    VARCHAR(8)           NOT NULL,
    WORKTIME    VARCHAR(6)           NOT NULL,
    HOSTDATE    VARCHAR(8) ,
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60),
    CONSTRAINT AFA_HOSTDATE PRIMARY KEY (WORKDATE,WORKTIME)
)
;
