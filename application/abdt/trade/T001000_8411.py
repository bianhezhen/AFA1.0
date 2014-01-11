# -*- coding: gbk -*-
################################################################################
#   ����ҵ��ϵͳ���������������ѯ
#===============================================================================
#   �����ļ�:   T001000_8410.py
#   ��˾���ƣ�  ������ͬ�Ƽ����޹�˾
#   ��    �ߣ�  XZH
#   �޸�ʱ��:   2008-06-10
################################################################################
import TradeContext,AfaLoggerFunc,AfaUtilTools,AfaDBFunc,TradeFunc,os,AbdtFunc
from types import *


#=====================�������������ѯ==============================================
def TrxMain( ):


    AfaLoggerFunc.tradeInfo('**********�������������ѯ(8411)��ʼ**********')



    TradeContext.tradeResponse.append(['O1AFAPDATE', TradeContext.TranDate])    #��������
    TradeContext.tradeResponse.append(['O1AFAPTIME', TradeContext.TranTime])    #����ʱ��


    #�жϵ�λЭ���Ƿ���Ч
    if ( not AbdtFunc.ChkUnitInfo( ) ):
        return False


    try:
        sql = ""
        sql = "SELECT * FROM ABDT_BATCHINFO WHERE "
        sql = sql + "APPNO="    + "'" + TradeContext.I1APPNO  + "'" + " AND "      #ҵ����
        sql = sql + "BUSINO="   + "'" + TradeContext.I1BUSINO + "'" + " AND "      #��λ���
        sql = sql + "ZONENO="   + "'" + TradeContext.I1ZONENO + "'" + " AND "      #��������
        sql = sql + "BRNO="     + "'" + TradeContext.I1SBNO   + "'" + " AND "      #��������

        if ( len(TradeContext.I1BATCHNO) == 0 ):
            sql = sql + "INDATE="  + "'" + TradeContext.I1WORKDATE    + "'" + " AND "     #ί������
            sql = sql + "STATUS<>" + "'" + '40'  + "'"                                    #״̬
        else:
            sql = sql + "INDATE="  + "'" + TradeContext.I1WORKDATE    + "'" + " AND "     #ί������
            sql = sql + "BATCHNO=" + "'" + TradeContext.I1BATCHNO  + "'"                  #ί�к�

        AfaLoggerFunc.tradeInfo( sql )

        records = AfaDBFunc.SelectSql( sql )
        if ( records == None ):
            AfaLoggerFunc.tradeFatal( AfaDBFunc.sqlErrMsg )
            return ExitSubTrade( '9000', '��ѯ������Ϣ���쳣' )

        if ( len(records) == 0 ):
            return ExitSubTrade( '9000', 'û�и�ί�кŵ�������Ϣ' )

        #����None
        AfaUtilTools.ListFilterNone( records )

        TradeContext.tradeResponse.append(['O1BATCHNO',         str(records[0][0])])         #ί�к�(���κ�)
        TradeContext.tradeResponse.append(['O1APPNO',           str(records[0][1])])         #ҵ����
        TradeContext.tradeResponse.append(['O1BUSINO',          str(records[0][2])])         #��λ���
        TradeContext.tradeResponse.append(['O1ZONENO',          str(records[0][3])])         #������
        TradeContext.tradeResponse.append(['O1BRNO',            str(records[0][4])])         #�����
        TradeContext.tradeResponse.append(['O1USERNO',          str(records[0][5])])         #����Ա
        TradeContext.tradeResponse.append(['O1ADMINNO',         str(records[0][6])])         #����Ա
        TradeContext.tradeResponse.append(['O1TERMTYPE',        str(records[0][7])])         #�ն�����
        TradeContext.tradeResponse.append(['O1FILENAME',        str(records[0][8])])         #�ϴ��ļ���
        TradeContext.tradeResponse.append(['O1INDATE',          str(records[0][9])])         #ί������
        TradeContext.tradeResponse.append(['O1INTIME',          str(records[0][10])])        #ί��ʱ��
        TradeContext.tradeResponse.append(['O1BATCHDATE',       str(records[0][11])])        #�ύ����
        TradeContext.tradeResponse.append(['O1BATCHTIME',       str(records[0][12])])        #�ύʱ��
        TradeContext.tradeResponse.append(['O1TOTALNUM',        str(records[0][13])])        #�ܱ���
        TradeContext.tradeResponse.append(['O1TOTALAMT',        str(records[0][14])])        #�ܽ��
        TradeContext.tradeResponse.append(['O1SUCCNUM',         str(records[0][15])])        #�ɹ�����
        TradeContext.tradeResponse.append(['O1SUCCAMT',         str(records[0][16])])        #�ɹ����
        TradeContext.tradeResponse.append(['O1FAILNUM',         str(records[0][17])])        #ʧ�ܱ���
        TradeContext.tradeResponse.append(['O1FAILAMT',         str(records[0][18])])        #ʧ�ܽ��
        TradeContext.tradeResponse.append(['O1UNSETNUM',        '0'])                        #δ��������
        TradeContext.tradeResponse.append(['O1UNSETAMT',        '0.00'])                     #δ�������
        TradeContext.tradeResponse.append(['O1STATUS',          str(records[0][19])])        #״̬
        TradeContext.tradeResponse.append(['O1BEGINDATE',       str(records[0][20])])        #��Ч����
        TradeContext.tradeResponse.append(['O1ENDDATE',         str(records[0][21])])        #ʧЧ����
        TradeContext.tradeResponse.append(['O1PROCMSG',         str(records[0][22])])        #������Ϣ
        TradeContext.tradeResponse.append(['O1NOTE1',           str(records[0][23])])        #��ע1
        TradeContext.tradeResponse.append(['O1NOTE2',           str(records[0][24])])        #��ע2
        TradeContext.tradeResponse.append(['O1NOTE3',           str(records[0][25])])        #��ע3
        TradeContext.tradeResponse.append(['O1NOTE4',           str(records[0][26])])        #��ע4
        TradeContext.tradeResponse.append(['O1NOTE5',           str(records[0][27])])        #��ע5


        #���������Ϣ
        BatchResultMsg = str(records[0][22])

        AfaLoggerFunc.tradeInfo('**********�������������ѯ(8411)����**********')


        #����
        TradeContext.tradeResponse.append(['errorCode', '0000'])
        TradeContext.tradeResponse.append(['errorMsg',  BatchResultMsg])
        return True

    except Exception, e:
        AfaLoggerFunc.tradeFatal( str(e) )
        return ExitSubTrade( '9999', '�������������ѯ,���ݿ��쳣' )


def ExitSubTrade( errorCode, errorMsg ):

    if( len( errorCode )!=0 ):
        TradeContext.tradeResponse.append(['errorCode', errorCode])
        TradeContext.tradeResponse.append(['errorMsg',  errorMsg])

    if( errorCode.isdigit( )==True and long( errorCode )==0 ):
        return True

    else:
        return False
        