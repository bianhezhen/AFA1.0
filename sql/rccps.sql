--
--ER/STUDIO 7.0 SQL CODE GENERATION
-- COMPANY :      ICBCOA
-- PROJECT :      ????????????????????.DM1
-- AUTHOR :       ICBC
--
-- DATE CREATED : THURSDAY, JUNE 05, 2008 10:59:51
-- TARGET DBMS : IBM DB2 UDB 8.X
--

DROP TABLE RCC_ATRCHK
;
DROP TABLE RCC_BILBKA
;
DROP TABLE RCC_BILINF
;
DROP TABLE RCC_CADBNK
;
DROP TABLE RCC_CSHALM
;
DROP TABLE RCC_ERRINF
;
DROP TABLE RCC_HDCBKA
;
DROP TABLE RCC_HDDZCZ
;
DROP TABLE RCC_HDDZHZ
;
DROP TABLE RCC_HDDZMX
;
DROP TABLE RCC_HPCBKA
;
DROP TABLE RCC_HPDZCZ
;
DROP TABLE RCC_HPDZHZ
;
DROP TABLE RCC_HPDZMX
;
DROP TABLE RCC_INSBKA
;
DROP TABLE RCC_MBRIFA
;
DROP TABLE RCC_MRQTBL
;
DROP TABLE RCC_PAMTBL
;
DROP TABLE RCC_PAYBNK
;
DROP TABLE RCC_PBDATE
;
DROP TABLE RCC_PJCBKA
;
DROP TABLE RCC_QSQHQD
;
DROP TABLE RCC_REKBAL
;
DROP TABLE RCC_SPBSTA
;
DROP TABLE RCC_SSTLOG
;
DROP TABLE RCC_SUBBRA
;
DROP TABLE RCC_TRCBKA
;
DROP TABLE RCC_TRCCAN
;
DROP TABLE RCC_TRCSTA
;
DROP TABLE RCC_ZTCBKA
;
--
-- TABLE: RCC_ATRCHK
--

CREATE TABLE RCC_ATRCHK(
    SNDBNKCO    VARCHAR(10)          NOT NULL ,
    TRCDAT      VARCHAR(8)           NOT NULL ,
    TRCNO       VARCHAR(8)           NOT NULL ,
    ROPRTPNO    VARCHAR(2),
    TRCCO       VARCHAR(7),
    RCVBNKCO    VARCHAR(10),
    CUR         VARCHAR(3),
    RDTCNT      DECIMAL(10, 0),
    RDTAMT      DECIMAL(15, 2),
    RCTCNT      DECIMAL(10, 0),
    RCTAMT      DECIMAL(15, 2),
    SDTCNT      DECIMAL(10, 0),
    SDTAMT      DECIMAL(15, 2),
    SCTCNT      DECIMAL(10, 0),
    SCTAMT      DECIMAL(15, 2),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_BILBKA
--

CREATE TABLE RCC_BILBKA(
    BJEDTE        VARCHAR(8)           NOT NULL ,
    BSPSQN        VARCHAR(12)          NOT NULL ,
    BRSFLG        VARCHAR(1)           NOT NULL ,
    BESBNO        VARCHAR(10),
    BEACSB        VARCHAR(10),
    BETELR        VARCHAR(6),
    BEAUUS        VARCHAR(6),
    DCFLG         VARCHAR(1),
    OPRATTNO      VARCHAR(2),
    NCCWKDAT      VARCHAR(8),
    TRCCO         VARCHAR(7),
    TRCDAT        VARCHAR(8),
    TRCNO         VARCHAR(8),
    SNDBNKCO      VARCHAR(12),
    SNDBNKNM      VARCHAR(60),
    RCVBNKCO      VARCHAR(12),
    RCVBNKNM      VARCHAR(60),
    BILVER        VARCHAR(2),
    BILNO         VARCHAR(8),
    CHRGTYP       VARCHAR(1),
    LOCCUSCHRG    DECIMAL(15, 2),
    BILRS         VARCHAR(1),
    HPCUSQ        SMALLINT          NOT NULL,
    HPSTAT        VARCHAR(2),
    NOTE1         VARCHAR(10),
    NOTE2         VARCHAR(20),
    NOTE3         VARCHAR(60),
    NOTE4         VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_BILINF
--

CREATE TABLE RCC_BILINF(
    BILVER      VARCHAR(2)           NOT NULL ,
    BILNO       VARCHAR(8)           NOT NULL ,
    BILRS       VARCHAR(1)           NOT NULL ,
    BILTYP      VARCHAR(2),
    BILDAT      VARCHAR(8),
    PAYWAY      VARCHAR(1),
    PAYBNKCO    VARCHAR(10),
    PAYBNKNM    VARCHAR(60),
    PYRACC      VARCHAR(32),
    PYRNAM      VARCHAR(60),
    PYRADDR     VARCHAR(60),
    PYEACC      VARCHAR(32),
    PYENAM      VARCHAR(60),
    PYEADDR     VARCHAR(60),
    PYHACC      VARCHAR(32),
    PYHNAM      VARCHAR(60),
    PYHADDR     VARCHAR(60),
    PYITYP      VARCHAR(1),
    PYIACC      VARCHAR(32),
    PYINAM      VARCHAR(60),
    BILAMT      DECIMAL(15, 2),
    OCCAMT      DECIMAL(15, 2),
    RMNAMT      DECIMAL(15, 2),
    CUR         VARCHAR(3),
    SEAL        VARCHAR(10),
    USE         VARCHAR(20),
    REMARK      VARCHAR(30),
    HPCUSQ      SMALLINT          NOT NULL,
    HPSTAT      VARCHAR(2),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_CADBNK
--

CREATE TABLE RCC_CADBNK(
    CARDBIN    VARCHAR(8)        NOT NULL ,
    BANKBIN    VARCHAR(10)       NOT NULL,
    NOTE1      VARCHAR(10),
    NOTE2      VARCHAR(20),
    NOTE3      VARCHAR(60),
    NOTE4      VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_CSHALM
--

CREATE TABLE RCC_CSHALM(
    BJEDTE      VARCHAR(8)           NOT NULL ,
    BSPSQN      VARCHAR(12)          NOT NULL ,
    NCCWKDAT    VARCHAR(8),
    TRCCO       VARCHAR(7),
    TRCDAT      VARCHAR(6),
    TRCNO       VARCHAR(8),
    SNDBNKCO    VARCHAR(10),
    SNDBNKNM    VARCHAR(60),
    RCVBNKCO    VARCHAR(10),
    RCVBNKNM    VARCHAR(60),
    CUR         VARCHAR(3),
    POSITION    DECIMAL(15, 2),
    POSALAMT    DECIMAL(15, 2),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_ERRINF
--

CREATE TABLE RCC_ERRINF(
    MBRTYP    VARCHAR(1)         NOT NULL ,
    ERRKEY    VARCHAR(8)         NOT NULL ,
    ERRSTR    VARCHAR(255),
    NOTE1     VARCHAR(10),
    NOTE2     VARCHAR(20),
    NOTE3     VARCHAR(60),
    NOTE4     VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_HDCBKA
--

CREATE TABLE RCC_HDCBKA(
    BJEDTE      VARCHAR(8)           NOT NULL ,
    BSPSQN      VARCHAR(12)          NOT NULL ,
    BRSFLG      VARCHAR(1)           NOT NULL ,
    BESBNO      VARCHAR(10),
    BETELR      VARCHAR(6),
    BEAUUS      VARCHAR(6),
    NCCWKDAT    VARCHAR(8),
    TRCCO       VARCHAR(7),
    TRCDAT      VARCHAR(8),
    TRCNO       VARCHAR(8),
    SNDBNKCO    VARCHAR(10),
    SNDBNKNM    VARCHAR(60),
    RCVBNKCO    VARCHAR(10),
    RCVBNKNM    VARCHAR(60),
    BOJEDT      VARCHAR(8),
    BOSPSQ      VARCHAR(12),
    ORTRCCO     VARCHAR(7),
    CUR         VARCHAR(3),
    OCCAMT      DECIMAL(15, 2),
    CONT        VARCHAR(255),
    PYRACC      VARCHAR(32),
    PYEACC      VARCHAR(32),
    ISDEAL      VARCHAR(1),
    PRCCO       VARCHAR(8),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_HDDZCZ
--

CREATE TABLE RCC_HDDZCZ(
    SNDBNKCO    VARCHAR(10)       NOT NULL ,
    TRCDAT      VARCHAR(8)        NOT NULL ,
    TRCNO       VARCHAR(8)        NOT NULL ,
    NCCWKDAT    VARCHAR(8),
    BJEDTE      VARCHAR(8),
    BSPSQN      VARCHAR(12),
    EACTYP      VARCHAR(1),
    EACINF      VARCHAR(60),
    ISDEAL      VARCHAR(1),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_HDDZHZ
--

CREATE TABLE RCC_HDDZHZ(
    NCCWKDAT    VARCHAR(8)           NOT NULL ,
    TRCCO       VARCHAR(7)           NOT NULL ,
    BRSFLG      VARCHAR(1)           NOT NULL ,
    TRCNAM      VARCHAR(60),
    TRCRSNM     VARCHAR(60),
    TCNT        SMALLINT          NOT NULL,
    CTAMT       DECIMAL(16, 2),
    DTAMT       DECIMAL(16, 2),
    OFSTAMT     DECIMAL(16, 2),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_HDDZMX
--

CREATE TABLE RCC_HDDZMX(
    SNDBNKCO    VARCHAR(10)          NOT NULL ,
    TRCDAT      VARCHAR(8)           NOT NULL ,
    TRCNO       VARCHAR(8)           NOT NULL ,
    NCCWKDAT    VARCHAR(8),
    MSGTYPCO    VARCHAR(6),
    RCVMBRCO    VARCHAR(10),
    SNDMBRCO    VARCHAR(10),
    TRCCO       VARCHAR(7),
    SNDBRHCO    VARCHAR(6),
    SNDCLKNO    VARCHAR(8),
    SNDTRDAT    VARCHAR(8),
    SNDTRTIM    VARCHAR(6),
    MSGFLGNO    VARCHAR(26),
    ORMFN       VARCHAR(26),
    OPRTYPNO    VARCHAR(2),
    ROPRTPNO    VARCHAR(2),
    OPRSTNO     VARCHAR(3),
    SNDBNKNM    VARCHAR(60),
    RCVBNKCO    VARCHAR(10),
    RCVBNKNM    VARCHAR(60),
    CUR         VARCHAR(3),
    OCCAMT      DECIMAL(15, 2),
    PYRACC      VARCHAR(32),
    PYRNAM      VARCHAR(60),
    PYRADDR     VARCHAR(60),
    PYEACC      VARCHAR(32),
    PYENAM      VARCHAR(60),
    PYEADDR     VARCHAR(60),
    OPRATTNO    VARCHAR(2),
    SEAL        VARCHAR(10),
    ORTRCCO     VARCHAR(7),
    ORSNDBNK    VARCHAR(10),
    ORRCVBNK    VARCHAR(10),
    ORTRCDAT    VARCHAR(8),
    ORTRCNO     VARCHAR(8),
    REMARK      VARCHAR(30),
    BILDAT      VARCHAR(8),
    BILNO       VARCHAR(8),
    BILTYP      VARCHAR(2),
    CPSAMT      DECIMAL(16, 2),
    RFUAMT      DECIMAL(16, 2),
    STRINFO     VARCHAR(60),
    USE         VARCHAR(20),
    BJEDTE      VARCHAR(8),
    BSPSQN      VARCHAR(12),
    BCSTAT      VARCHAR(2),
    BDWFLG      VARCHAR(1),
    EACTYP      VARCHAR(1),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_HPCBKA
--

CREATE TABLE RCC_HPCBKA(
    BJEDTE      VARCHAR(8)           NOT NULL ,
    BSPSQN      VARCHAR(12)          NOT NULL ,
    BRSFLG      VARCHAR(1)           NOT NULL ,
    BESBNO      VARCHAR(10),
    BETELR      VARCHAR(6),
    BEAUUS      VARCHAR(6),
    NCCWKDAT    VARCHAR(8),
    TRCCO       VARCHAR(7),
    TRCDAT      VARCHAR(8),
    TRCNO       VARCHAR(8),
    SNDBNKCO    VARCHAR(10),
    SNDBNKNM    VARCHAR(60),
    RCVBNKCO    VARCHAR(10),
    RCVBNKNM    VARCHAR(60),
    BOJEDT      VARCHAR(8),
    BOSPSQ      VARCHAR(12),
    ORTRCCO     VARCHAR(7),
    BILVER      VARCHAR(2),
    BILNO       VARCHAR(8),
    BILDAT      VARCHAR(8),
    PAYWAY      VARCHAR(1),
    CUR         VARCHAR(3),
    BILAMT      DECIMAL(15, 2),
    PYRACC      VARCHAR(32),
    PYRNAM      VARCHAR(60),
    PYEACC      VARCHAR(32),
    PYENAM      VARCHAR(60),
    CONT        VARCHAR(255),
    ISDEAL       VARCHAR(1),
    PRCCO       VARCHAR(8),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_HPDZCZ
--

CREATE TABLE RCC_HPDZCZ(
    SNDBNKCO    VARCHAR(10)       NOT NULL ,
    TRCDAT      VARCHAR(8)        NOT NULL ,
    TRCNO       VARCHAR(8)        NOT NULL ,
    NCCWKDAT    VARCHAR(8),
    BJEDTE      VARCHAR(8),
    BSPSQN      VARCHAR(12),
    EACTYP      VARCHAR(1),
    EACINF      VARCHAR(60),
    ISDEAL      VARCHAR(1),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_HPDZHZ
--

CREATE TABLE RCC_HPDZHZ(
    NCCWKDAT    VARCHAR(8)           NOT NULL ,
    TRCCO       VARCHAR(7)           NOT NULL ,
    BRSFLG      VARCHAR(1)           NOT NULL ,
    TRCNAM      VARCHAR(60),
    TRCRSNM     VARCHAR(60),
    TCNT        SMALLINT          NOT NULL,
    CTAMT       DECIMAL(16, 2),
    DTAMT       DECIMAL(16, 2),
    OFSTAMT     DECIMAL(16, 2),
    CLAMT       DECIMAL(16, 2),
    DLAMT       DECIMAL(16, 2),
    OFSLAMT     DECIMAL(16, 2),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_HPDZMX
--

CREATE TABLE RCC_HPDZMX(
    SNDBNKCO    VARCHAR(10)          NOT NULL ,
    TRCDAT      VARCHAR(8)           NOT NULL ,
    TRCNO       VARCHAR(8)           NOT NULL ,
    NCCWKDAT    VARCHAR(8),
    MSGTYPCO    VARCHAR(6),
    RCVMBRCO    VARCHAR(10),
    SNDMBRCO    VARCHAR(10),
    TRCCO       VARCHAR(7),
    SNDBRHCO    VARCHAR(6),
    SNDCLKNO    VARCHAR(8),
    SNDTRDAT    VARCHAR(8),
    SNDTRTIM    VARCHAR(6),
    MSGFLGNO    VARCHAR(26),
    ORMFN       VARCHAR(26),
    OPRTYPNO    VARCHAR(2),
    ROPRTPNO    VARCHAR(2),
    SNDBNKNM    VARCHAR(60),
    RCVBNKCO    VARCHAR(10),
    RCVBNKNM    VARCHAR(60),
    CUR         VARCHAR(3),
    OCCAMT      DECIMAL(15, 2),
    PYRACC      VARCHAR(32),
    PYRNAM      VARCHAR(60),
    PYRADDR     VARCHAR(60),
    PYEACC      VARCHAR(32),
    PYENAM      VARCHAR(60),
    PYEADDR     VARCHAR(60),
    OPRATTNO    VARCHAR(2),
    SEAL        VARCHAR(10),
    BILDAT      VARCHAR(8),
    BILNO       VARCHAR(8),
    BILVER      VARCHAR(2),
    PAYWAY      VARCHAR(1),
    BILAMT      DECIMAL(15, 2),
    RMNAMT      DECIMAL(15, 2),
    USE         VARCHAR(20),
    REMARK      VARCHAR(30),
    BJEDTE      VARCHAR(8),
    BSPSQN      VARCHAR(12),
    BCSTAT      VARCHAR(2),
    BDWFLG      VARCHAR(1),
    EACTYP      VARCHAR(1),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_INSBKA
--

CREATE TABLE RCC_INSBKA(
    BJEDTE      VARCHAR(8)        NOT NULL ,
    BSPSQN      VARCHAR(12)       NOT NULL ,
    NCCWKDAT    VARCHAR(8),
    TRDT        VARCHAR(8),
    TLSQ        VARCHAR(10),
    SBAC        VARCHAR(32),
    RBAC        VARCHAR(32),
    DASQ        VARCHAR(8),
    MGID        VARCHAR(7),
    BDWFLG      VARCHAR(1),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_MBRIFA
--

CREATE TABLE RCC_MBRIFA(
    OPRTYPNO    VARCHAR(2)        NOT NULL ,
    ORWKDAT     VARCHAR(8)        NOT NULL,
    ORSYSST     VARCHAR(2)        NOT NULL,
    NWWKDAT     VARCHAR(8)        NOT NULL,
    NWSYSST     VARCHAR(2)        NOT NULL,
    HOLFLG      VARCHAR(1)        NOT NULL,
    STRINFO     VARCHAR(60),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_MRQTBL
--

CREATE TABLE RCC_MRQTBL(
    BJEDTE      VARCHAR(8)           NOT NULL ,
    BSPSQN      VARCHAR(12)          NOT NULL ,
    TRCCO       VARCHAR(8),
    SNDBNKCO    VARCHAR(10),
    SNDBNKNM    VARCHAR(60),
    TRCDAT      VARCHAR(8),
    TRCNO       VARCHAR(8),
    NPCBKID     VARCHAR(12),
    NPCBKNM     VARCHAR(60),
    NPCACNT     VARCHAR(32),
    OCCAMT      DECIMAL(15, 2),
    REMARK      VARCHAR(60),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_PAMTBL
--

CREATE TABLE RCC_PAMTBL(
    BPATPE    VARCHAR(1)         NOT NULL ,
    BPARAD    VARCHAR(18)     NOT NULL ,
    BPACMT    VARCHAR(60),
    BPADAT    VARCHAR(255),
    BPAINF    VARCHAR(60),
    BEFTDT    VARCHAR(8),
    BINVDT    VARCHAR(8),
    NOTE1     VARCHAR(10),
    NOTE2     VARCHAR(20),
    NOTE3     VARCHAR(60),
    NOTE4     VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_PAYBNK
--

CREATE TABLE RCC_PAYBNK(
    BANKBIN       VARCHAR(10)       NOT NULL ,
    BANKSTATUS    VARCHAR(1),
    BANKATTR      VARCHAR(2),
    STLBANKBIN    VARCHAR(10),
    BANKNAM       VARCHAR(60),
    BANKADDR      VARCHAR(60)    NOT NULL,
    BANKPC        VARCHAR(6)        NOT NULL,
    BANKTEL       VARCHAR(30)       NOT NULL,
    EFCTDAT       VARCHAR(8)        NOT NULL,
    INVDAT        VARCHAR(8),
    ALTTYPE       VARCHAR(1),
    PRIVILEGE     VARCHAR(20)       NOT NULL,
    NEWOFLG       VARCHAR(1),
    STRINFO       VARCHAR(60),
    NOTE1         VARCHAR(10),
    NOTE2         VARCHAR(20),
    NOTE3         VARCHAR(60),
    NOTE4         VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_PBDATE
--

CREATE TABLE RCC_PBDATE(
    TRCDAT      VARCHAR(8)         NOT NULL ,
    TRCNO       VARCHAR(8)         NOT NULL ,
    SNDBNKCO    VARCHAR(10)        NOT NULL ,
    TRCCO       VARCHAR(7),
    RCVBNKCO    VARCHAR(10),
    EFCTDAT     VARCHAR(8),
    PBDATYP     VARCHAR(3),
    PBDAFILE    VARCHAR(255),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_PJCBKA
--

CREATE TABLE RCC_PJCBKA(
    BJEDTE      VARCHAR(8)           NOT NULL ,
    BSPSQN      VARCHAR(12)          NOT NULL ,
    BRSFLG      VARCHAR(1)           NOT NULL ,
    BESBNO      VARCHAR(10),
    BETELR      VARCHAR(6),
    BEAUUS      VARCHAR(6),
    NCCWKDAT    VARCHAR(8),
    TRCCO       VARCHAR(7),
    TRCDAT      VARCHAR(8),
    TRCNO       VARCHAR(8),
    SNDBNKCO    VARCHAR(10),
    SNDBNKNM    VARCHAR(60),
    RCVBNKCO    VARCHAR(10),
    RCVBNKNM    VARCHAR(60),
    BOJEDT      VARCHAR(8),
    BOSPSQ      VARCHAR(12),
    ORTRCCO     VARCHAR(7),
    BILDAT      VARCHAR(8),
    BILNO       VARCHAR(8),
    BILPNAM     VARCHAR(60),
    BILENDDT    VARCHAR(8),
    BILAMT      DECIMAL(15, 2),
    PYENAM      VARCHAR(60),
    HONBNKNM    VARCHAR(60),
    CONT        VARCHAR(60),
    ISDEAL       VARCHAR(1),
    PRCCO       VARCHAR(8),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_QSQHQD
--

CREATE TABLE RCC_QSQHQD(
    STRDAT         VARCHAR(8)           NOT NULL ,
    ENDDAT         VARCHAR(8)           NOT NULL ,
    BESBNO         VARCHAR(10)          NOT NULL ,
    BESBNM         VARCHAR(60),
    TRCCHRGCNT     SMALLINT          NOT NULL,
    TRCCHRGAMT     DECIMAL(15, 2),
    BILCHRGCNT     SMALLINT          NOT NULL,
    BILCHRGAMT     DECIMAL(15, 2),
    UCSWCHRGCNT    SMALLINT          NOT NULL,
    UCSWCHRGAMT    DECIMAL(15, 2),
    TCNT           SMALLINT          NOT NULL,
    TAMT           DECIMAL(15, 2),
    ISDEAL         VARCHAR(1),
    FEDT           VARCHAR(8),
    RBSQ           VARCHAR(12),
    TRDT           VARCHAR(8),
    TLSQ           VARCHAR(10),
    MGID           VARCHAR(7),
    NOTE1          VARCHAR(20),
    NOTE2          VARCHAR(20),
    NOTE3          VARCHAR(60),
    NOTE4          VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_REKBAL
--

CREATE TABLE RCC_REKBAL(
    BJEDTE       VARCHAR(8)           NOT NULL ,
    BSPSQN       VARCHAR(12)          NOT NULL ,
    BOJEDT       VARCHAR(8),
    BOSPSQ       VARCHAR(12),
    NCCWKDAT     VARCHAR(8),
    TRCDAT       VARCHAR(8)           NOT NULL,
    TRCNO        VARCHAR(8)           NOT NULL,
    SNDBNKCO     VARCHAR(10)          NOT NULL,
    TRCCO        VARCHAR(7),
    RCVBNKCO     VARCHAR(10),
    CUR          VARCHAR(3),
    LBDCFLG      VARCHAR(1),
    LSTDTBAL     DECIMAL(15, 2),
    NTTDCFLG     VARCHAR(1),
    NTTBAL       DECIMAL(15, 2),
    BALDCFLG     VARCHAR(1),
    TODAYBAL     DECIMAL(15, 2),
    AVLBAL       DECIMAL(15, 2),
    NTODAYBAL    DECIMAL(15, 2),
    CHKRST       VARCHAR(1),
    NOTE1        VARCHAR(10),
    NOTE2        VARCHAR(20),
    NOTE3        VARCHAR(60),
    NOTE4        VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_SPBSTA
--

CREATE TABLE RCC_SPBSTA(
    BJEDTE    VARCHAR(8)        NOT NULL ,
    BSPSQN    VARCHAR(12)       NOT NULL ,
    BCURSQ    SMALLINT       NOT NULL,
    BCSTAT    VARCHAR(2),
    BDWFLG    VARCHAR(1),
    NOTE1     VARCHAR(10),
    NOTE2     VARCHAR(20),
    NOTE3     VARCHAR(60),
    NOTE4     VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_SSTLOG
--

CREATE TABLE RCC_SSTLOG(
    BJEDTE    VARCHAR(8)        NOT NULL ,
    BSPSQN    VARCHAR(12)       NOT NULL ,
    BCURSQ    SMALLINT       NOT NULL ,
    BESBNO    VARCHAR(10),
    BEACSB    VARCHAR(10),
    BETELR    VARCHAR(6),
    BEAUUS    VARCHAR(6),
    FEDT      VARCHAR(8),
    RBSQ      VARCHAR(12),
    TRDT      VARCHAR(8),
    TLSQ      VARCHAR(10),
    SBAC      VARCHAR(32),
    ACNM      VARCHAR(60),
    RBAC      VARCHAR(32),
    OTNM      VARCHAR(60),
    DASQ      VARCHAR(8),
    MGID      VARCHAR(7),
    PRCCO     VARCHAR(8),
    BCSTAT    VARCHAR(2),
    BDWFLG    VARCHAR(1),
    PRTCNT    SMALLINT       NOT NULL,
    BJETIM    VARCHAR(20),
    NOTE1     VARCHAR(10),
    NOTE2     VARCHAR(20),
    NOTE3     VARCHAR(60),
    NOTE4     VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_SUBBRA
--

CREATE TABLE RCC_SUBBRA(
    BESBNO     VARCHAR(10)       NOT NULL ,
    BESBNM     VARCHAR(60),
    BESBTP     VARCHAR(2),
    BTOPSB     VARCHAR(10),
    BEACSB     VARCHAR(10),
    BANKBIN    VARCHAR(10),
    SUBFLG     VARCHAR(1),
    STRINFO    VARCHAR(60),
    NOTE1      VARCHAR(10),
    NOTE2      VARCHAR(20),
    NOTE3      VARCHAR(60),
    NOTE4      VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_TRCBKA
--

CREATE TABLE RCC_TRCBKA(
    BJEDTE        VARCHAR(8)           NOT NULL ,
    BSPSQN        VARCHAR(12)          NOT NULL ,
    BRSFLG        VARCHAR(1)           NOT NULL,
    BESBNO        VARCHAR(10)          NOT NULL,
    BEACSB        VARCHAR(10),
    BETELR        VARCHAR(6)           NOT NULL,
    BEAUUS        VARCHAR(6),
    DCFLG         VARCHAR(1),
    OPRNO         VARCHAR(2),
    OPRATTNO      VARCHAR(2),
    NCCWKDAT      VARCHAR(8)           NOT NULL,
    TRCCO         VARCHAR(7)           NOT NULL,
    TRCDAT        VARCHAR(8),
    TRCNO         VARCHAR(8)           NOT NULL,
    SNDBNKCO      VARCHAR(10),
    SNDBNKNM      VARCHAR(60),
    RCVBNKCO      VARCHAR(10),
    RCVBNKNM      VARCHAR(60),
    CUR           VARCHAR(3)           NOT NULL,
    OCCAMT        DECIMAL(15, 2)    NOT NULL,
    CHRGTYP       VARCHAR(1),
    LOCCUSCHRG    DECIMAL(15, 2)    NOT NULL,
    CUSCHRG       DECIMAL(15, 2)    NOT NULL,
    PYRACC        VARCHAR(32),
    PYRNAM        VARCHAR(60),
    PYRADDR       VARCHAR(60),
    PYEACC        VARCHAR(32),
    PYENAM        VARCHAR(60),
    PYEADDR       VARCHAR(60),
    SEAL          VARCHAR(10),
    USE           VARCHAR(20),
    REMARK        VARCHAR(60),
    BILTYP        VARCHAR(2),
    BILDAT        VARCHAR(8),
    BILNO         VARCHAR(8),
    COMAMT        DECIMAL(15, 2),
    OVPAYAMT      DECIMAL(15, 2),
    CPSAMT        DECIMAL(15, 2),
    RFUAMT        DECIMAL(15, 2),
    CERTTYPE      VARCHAR(2),
    CERTNO        VARCHAR(20),
    BOJEDT        VARCHAR(8),
    BOSPSQ        VARCHAR(12),
    ORTRCDAT      VARCHAR(10),
    ORTRCCO       VARCHAR(7),
    ORTRCNO       VARCHAR(8),
    ORSNDBNK      VARCHAR(10),
    ORRCVBNK      VARCHAR(10),
    STRINFO       VARCHAR(60),
    NOTE1         VARCHAR(10),
    NOTE2         VARCHAR(20),
    NOTE3         VARCHAR(60),
    NOTE4         VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_TRCCAN
--

CREATE TABLE RCC_TRCCAN(
    BJEDTE      VARCHAR(8)           NOT NULL ,
    BSPSQN      VARCHAR(12)          NOT NULL ,
    BRSFLG      VARCHAR(1),
    BESBNO      VARCHAR(10),
    BETELR      VARCHAR(6),
    BEAUUS      VARCHAR(6),
    NCCWKDAT    VARCHAR(8),
    TRCCO       VARCHAR(7),
    TRCDAT      VARCHAR(6),
    TRCNO       VARCHAR(8),
    SNDBNKCO    VARCHAR(10),
    SNDBNKNM    VARCHAR(60),
    RCVBNKCO    VARCHAR(10),
    RCVBNKNM    VARCHAR(60),
    BOJEDT      VARCHAR(8),
    BOSPSQ      VARCHAR(12),
    ORTRCCO     VARCHAR(7),
    CUR         VARCHAR(3),
    OCCAMT      DECIMAL(15, 2),
    CONT        VARCHAR(255),
    CLRESPN     VARCHAR(1),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_TRCSTA
--

CREATE TABLE RCC_TRCSTA(
    NCCWKDAT    VARCHAR(8)           NOT NULL ,
    BESBNO      VARCHAR(10)          NOT NULL ,
    TRCCO       VARCHAR(7)           NOT NULL ,
    BRSFLG      VARCHAR(1)           NOT NULL ,
    BTOPSB      VARCHAR(10),
    BEACSB      VARCHAR(10),
    TCNT        SMALLINT          NOT NULL,
    TAMT        DECIMAL(15, 2),
    ISDEAL      VARCHAR(1),
    STRINFO     VARCHAR(60),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;



--
-- TABLE: RCC_ZTCBKA
--

CREATE TABLE RCC_ZTCBKA(
    BJEDTE      VARCHAR(8)           NOT NULL ,
    BSPSQN      VARCHAR(12)          NOT NULL ,
    BRSFLG      VARCHAR(1)           NOT NULL ,
    BESBNO      VARCHAR(10),
    BEACSB      VARCHAR(10),
    BETELR      VARCHAR(6),
    BEAUUS      VARCHAR(6),
    NCCWKDAT    VARCHAR(8),
    TRCCO       VARCHAR(7),
    TRCDAT      VARCHAR(8),
    TRCNO       VARCHAR(8),
    SNDBNKCO    VARCHAR(10),
    SNDBNKNM    VARCHAR(60),
    RCVBNKCO    VARCHAR(10),
    RCVBNKNM    VARCHAR(60),
    BOJEDT      VARCHAR(8),
    BOSPSQ      VARCHAR(12),
    ORTRCCO     VARCHAR(7),
    CUR         VARCHAR(3),
    OCCAMT      DECIMAL(15, 2),
    CONT        VARCHAR(255),
    NCCTRCST    VARCHAR(2),
    MBRTRCST    VARCHAR(2),
    ISDEAL      VARCHAR(1),
    NOTE1       VARCHAR(10),
    NOTE2       VARCHAR(20),
    NOTE3       VARCHAR(60),
    NOTE4       VARCHAR(60)
)in afa_data index in afa_idx;

ALTER TABLE rcc_cadbnk ADD 
    CONSTRAINT rcc_cadbnk_pk PRIMARY KEY (CARDBIN)
;

-- 
-- TABLE: errinf 
--

ALTER TABLE rcc_errinf ADD 
    CONSTRAINT rcc_errinf_pk PRIMARY KEY (MBRTYP, ERRKEY)
;

-- 
-- TABLE: hdcbka 
--

ALTER TABLE rcc_hdcbka ADD 
    CONSTRAINT rcc_hdcbka_pk PRIMARY KEY (BJEDTE, BSPSQN)
;

-- 
-- TABLE: hddzcz 
--

ALTER TABLE rcc_hddzcz ADD 
    CONSTRAINT rcc_hddzcz_pk PRIMARY KEY (SNDBNKCO, TRCDAT, TRCNO)
;

-- 
-- TABLE: hddzhz 
--

ALTER TABLE rcc_hddzhz ADD 
    CONSTRAINT rcc_hddzhz PRIMARY KEY (NCCWKDAT, TRCCO, TRCRSNM)
;

-- 
-- TABLE: hddzmx 
--

ALTER TABLE rcc_hddzmx ADD 
    CONSTRAINT rcc_hddzmx_pk PRIMARY KEY (SNDBNKCO, TRCDAT, TRCNO)
;

-- 
-- TABLE: hdhbka 
--

ALTER TABLE rcc_hdhbka ADD 
    CONSTRAINT rcc_hdhbka_pk PRIMARY KEY (BJEDTE, BSPSQN)
;

-- 
-- TABLE: hdnbka 
--

ALTER TABLE rcc_hdnbka ADD 
    CONSTRAINT rcc_hdnbka_pk PRIMARY KEY (BJEDTE, BSPSQN)
;

-- 
-- TABLE: hpcbka 
--

ALTER TABLE rcc_hpcbka ADD 
    CONSTRAINT rcc_hpcbka_pk PRIMARY KEY (BJEDTE, BSPSQN)
;

-- 
-- TABLE: hphbka 
--

ALTER TABLE rcc_hphbka ADD 
    CONSTRAINT rcc_hphbka_pk PRIMARY KEY (BSPSQN, BRSFLG)
;

-- 
-- TABLE: hpnbka 
--

ALTER TABLE rcc_hpnbka ADD 
    CONSTRAINT rcc_hpnbka_pk PRIMARY KEY (BJEDTE, BSPSQN)
;

"
drop index rcc_cadbnk;

CREATE UNIQUE INDEX rcc_cadbnk_idx1 ON rcc_cadbnk(CARDBIN)
;

drop index rcc_errinf;

CREATE UNIQUE INDEX rcc_errinf_idx1 ON rcc_errinf(MBRTYP, ERRKEY)
;

drop index rcc_hdcbka;

CREATE UNIQUE INDEX rcc_hdcbka_idx1 ON rcc_hdcbka(BJEDTE, BSPSQN)
;

drop index rcc_hddzcz;

CREATE UNIQUE INDEX rcc_hddzcz_idx1 ON rcc_hddzcz(SNDBNKCO, TRCDAT, TRCNO)
;

drop index rcc_hddzhz;

CREATE UNIQUE INDEX rcc_hddzhz_idx1 ON rcc_hddzhz(NCCWKDAT, TRCCO, TRCRS)
;

drop index rcc_cadbnk;

CREATE UNIQUE INDEX rcc_hddzmx_idx1 ON rcc_hddzmx(SNDBNKCO, TRCDAT, TRCNO)
;

drop index rcc_hdhbka;

CREATE UNIQUE INDEX rcc_hdhbka_idx1 ON rcc_hdhbka(BJEDTE, BSPSQN)
;

drop index rcc_hdnbka;

CREATE UNIQUE INDEX rcc_hdnbka_idx1 ON rcc_hdnbka(BJEDTE, BSPSQN)
;

drop index rcc_hpcbka;

CREATE UNIQUE INDEX rcc_hpcbka_idx1 ON rcc_hpcbka(BJEDTE, BSPSQN)
;

drop index rcc_cadbnk;

CREATE UNIQUE INDEX rcc_hphbka_idx1 ON rcc_hphbka(BSPSQN, BRSFLG)
;

drop index rcc_hpnbka;

CREATE UNIQUE INDEX rcc_hpnbka_idx1 ON rcc_hpnbka(BJEDTE, BSPSQN)
;

drop index rcc_hpninf;

CREATE UNIQUE INDEX rcc_hpninf_idx1 ON rcc_hpninf(BILVER, BILNO, BILRS)
;

drop index rcc_mbrifa;

CREATE UNIQUE INDEX rcc_mbrifa_idx1 ON rcc_mbrifa(OprTypNo)
;

drop index rcc_cadbnk;

CREATE UNIQUE INDEX rcc_paybnk_idx1 ON rcc_paybnk(BANKBIN)
;

drop index rcc_pbdate;

CREATE UNIQUE INDEX rcc_pbdate_idx1 ON rcc_pbdate(RECDAT, TRCNO, SNDBNKCO)
;

drop index rcc_pbinfo;

CREATE UNIQUE INDEX rcc_pbinfo_idx1 ON rcc_pbinfo(BJEDTE, BSPSQN)
;

drop index rcc_pjcbka;

CREATE UNIQUE INDEX rcc_pjcbka_idx1 ON rcc_pjcbka(BJEDTE, BSPSQN)
;

drop index rcc_rekbal;

CREATE UNIQUE INDEX rcc_rekbal_idx1 ON rcc_rekbal(TRCDAT, TRCNO, SNDBNKCO)
;

drop index rcc_spbsta;

CREATE UNIQUE INDEX rcc_spbsta_idx1 ON rcc_spbsta(BJEDTE, BSPSQN)
;

drop index rcc_cadbnk;

CREATE UNIQUE INDEX rcc_sstlog_idx1 ON rcc_sstlog(BJEDTE, BSPSQN, BCURSQ)
;

drop index rcc_cadbnk;

CREATE UNIQUE INDEX rcc_subbra_idx1 ON rcc_subbra(BESBNO)
;
"