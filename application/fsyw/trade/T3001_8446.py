# -*- coding: gbk -*-
###############################################################################
# 文件标识：
# 摘    要：代收非税对帐
#
# 当前版本：1.0
# 作    者：WJJ
# 完成日期：2007年10月22日
#
# 取代版本：
# 原 作 者：
# 完成日期：
###############################################################################
import TradeContext,ConfigParser,AfaUtilTools,AfaDBFunc,os,AfaLoggerFunc,HostContext,HostComm,sys,datetime
from types import *


#读取批量配置文件中信息
def GetLappConfig( CfgFileName = None ):

    try:
        config = ConfigParser.ConfigParser( )

        if( CfgFileName == None ):
            CfgFileName = os.environ['AFAP_HOME'] + '/conf/lapp.conf'

        config.readfp( open( CfgFileName ) )

        TradeContext.HOST_HOSTIP   = config.get('HOST_DZ', 'HOSTIP')
        TradeContext.HOST_USERNO   = config.get('HOST_DZ', 'USERNO')
        TradeContext.HOST_PASSWD   = config.get('HOST_DZ', 'PASSWD')
        TradeContext.HOST_LDIR     = config.get('HOST_DZ', 'LDIR')
        TradeContext.HOST_RDIR     = config.get('HOST_DZ', 'RDIR')
        TradeContext.CORP_CDIR     = config.get('HOST_DZ', 'CDIR')
        TradeContext.BANK_CDIR     = config.get('HOST_DZ', 'BDIR')
        TradeContext.TRACE         = config.get('HOST_DZ', 'TRACE')

        return 0

    except Exception, e:
        print str(e)
        return -1

#下载对帐文件
def GetDzFile(rfilename, lfilename):

    try:
        #创建文件
        ftpShell = os.environ['AFAP_HOME'] + '/data/ahfs/shell/ftphost.sh'
        ftpFp = open(ftpShell, "w")

        ftpFp.write('open ' + TradeContext.HOST_HOSTIP + '\n')
        ftpFp.write('user ' + TradeContext.HOST_USERNO + ' ' + TradeContext.HOST_PASSWD + '\n')

        #下载文件
        ftpFp.write('cd '  + TradeContext.HOST_RDIR + '\n')
        ftpFp.write('lcd ' + TradeContext.HOST_LDIR + '\n')
        ftpFp.write('bin ' + '\n')
        ftpFp.write('get ' + rfilename + ' ' + lfilename + '\n')

        ftpFp.close()

        ftpcmd = 'ftp -n < ' + ftpShell + ' 1>/dev/null 2>/dev/null '

        AfaLoggerFunc.tradeInfo('下载文件' + rfilename + lfilename)

        ret = os.system(ftpcmd)
        if ( ret != 0 ):
            return -1
        else:
            return 0

    except Exception, e:
        AfaLoggerFunc.tradeInfo(e)
        AfaLoggerFunc.tradeInfo('FTP处理异常')
        return -1

#格式化文件
def FormatFile(sFileName, dFileName):

    try:
        srcFileName    = TradeContext.HOST_LDIR + '/' + sFileName
        dstFileName    = TradeContext.HOST_LDIR + '/' + dFileName

        #调用格式:cvt2ascii -T 生成文本文件 -P 物理文件 -F fld文件 [-D 间隔符] [-S] [-R]
        CvtProg     = os.environ['AFAP_HOME'] + '/data/cvt/cvt2ascii'
        fldFileName    = os.environ['AFAP_HOME'] + '/data/cvt/agent03.fld'
        cmdstr=CvtProg + " -T " + dstFileName + " -P " + srcFileName + " -F " + fldFileName

        AfaLoggerFunc.tradeInfo( cmdstr )


        ret = os.system(cmdstr)
        if ( ret != 0 ):
            return -1
        else:
            return 0

    except Exception, e:
        AfaLoggerFunc.tradeInfo(e)
        AfaLoggerFunc.tradeInfo('格式化文件异常')
        return -1

##########################################签到##########################################
def Ahdx_Login():

    try:
        sqlStr = "SELECT STATUS FROM ABDT_UNITINFO WHERE"
        sqlStr = sqlStr + " APPNO = '"      + TradeContext.appNo  + "'"
        sqlStr = sqlStr + " AND BUSINO = '" + TradeContext.busiNo + "'"
        sqlStr = sqlStr + " AND AGENTTYPE IN ('1','2')"

        #AfaLoggerFunc.tradeInfo(sqlStr)

        records = AfaDBFunc.SelectSql( sqlStr )
        if (records==None or len(records) < 0):
            AfaLoggerFunc.tradeInfo('>>>处理结果:签到失败,数据库异常')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","签到失败,数据库异常"
            return False

        elif ( len(records) == 0 ):
            AfaLoggerFunc.tradeInfo('>>>处理结果:没有发现该单位信息,不能签到')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","没有发现该单位信息,不能签到"
            return False


        sqlStr = "UPDATE ABDT_UNITINFO SET STATUS='1' WHERE"
        sqlStr = sqlStr + " APPNO = '"      + TradeContext.appNo  + "'"
        sqlStr = sqlStr + " AND BUSINO = '" + TradeContext.busiNo + "'"
        sqlStr = sqlStr + " AND AGENTTYPE IN ('1','2')"

        retcode = AfaDBFunc.UpdateSqlCmt( sqlStr )
        if (retcode==None or retcode <= 0):
            AfaLoggerFunc.tradeInfo('>>>处理结果:签到失败,数据库异常')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","签到失败,数据库异常"
            return False

        AfaLoggerFunc.tradeInfo('>>>处理结果:签到成功')

    except Exception, e:
        AfaLoggerFunc.tradeInfo(str(e))
        TradeContext.errorCode,TradeContext.errorMsg    =   "0001",str(e)
        return False



##########################################签退##########################################
def Ahdx_Logout():
    try:
        sqlStr = "SELECT STATUS FROM ABDT_UNITINFO WHERE"
        sqlStr = sqlStr + " APPNO = '"      + TradeContext.appNo  + "'"
        sqlStr = sqlStr + " AND BUSINO = '" + TradeContext.busiNo + "'"
        sqlStr = sqlStr + " AND AGENTTYPE IN ('1','2')"

        #AfaLoggerFunc.tradeInfo(sqlStr)

        records = AfaDBFunc.SelectSql( sqlStr )
        if (records==None or len(records) < 0):
            AfaLoggerFunc.tradeInfo('>>>处理结果:签退失败,数据库异常')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","签到失败,数据库异常"
            return False

        elif ( len(records) == 0 ):
            AfaLoggerFunc.tradeInfo('>>>处理结果:没有发现该单位信息,不能签退')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","没有发现该单位信息,不能签退"
            return False

        sqlStr = "UPDATE ABDT_UNITINFO SET STATUS='2' WHERE"
        sqlStr = sqlStr + " APPNO = '"      + TradeContext.appNo  + "'"
        sqlStr = sqlStr + " AND BUSINO = '" + TradeContext.busiNo + "'"
        sqlStr = sqlStr + " AND AGENTTYPE IN ('1','2')"

        retcode = AfaDBFunc.UpdateSqlCmt( sqlStr )
        if (retcode==None or retcode <= 0):
            AfaLoggerFunc.tradeInfo('>>>处理结果:签退失败,数据库异常')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","签退失败,数据库异常"
            return False

        AfaLoggerFunc.tradeInfo('>>>处理结果:签退成功')

        return True

    except Exception, e:
        AfaLoggerFunc.tradeInfo(str(e))
        TradeContext.errorCode,TradeContext.errorMsg    =   "0001",str(e)
        return False


##########################################日终处理##########################################
def Ahdx_DayEnd():

    try:
        sqlStr = "SELECT STATUS,BRNO FROM ABDT_UNITINFO WHERE"
        sqlStr = sqlStr + " APPNO = '"      + TradeContext.appNo  + "'"
        sqlStr = sqlStr + " AND BUSINO = '" + TradeContext.busiNo + "'"
        sqlStr = sqlStr + " AND AGENTTYPE IN ('1','2')"

        records = AfaDBFunc.SelectSql( sqlStr )
        if (records==None or len(records) < 0):
            AfaLoggerFunc.tradeInfo('>>>处理结果:日终处理失败,数据库异常')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","日终处理失败,数据库异常"
            return False

        elif ( len(records) == 0 ):
            AfaLoggerFunc.tradeInfo('>>>处理结果:没有发现该单位信息,不能日终处理')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","没有发现该单位信息,不能日终处理"
            return False

        #=====对非当日的账，不需要签退====
        if ( records[0][0] != '2' and (TradeContext.WORKDATE == TradeContext.workDate)):
            AfaLoggerFunc.tradeInfo('>>>处理结果:必须先签退才能进行日终处理')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","必须先签退才能进行日终处理"
            return False

        AfaLoggerFunc.tradeInfo('>>>下载主机对帐文件')

        #通讯区打包
        HostContext.I1TRCD = '8818'                        #主机交易码
        HostContext.I1SBNO = records[0][1]                 #该交易的发起机构
        HostContext.I1USID = '999999'                      #交易柜员号
        HostContext.I1AUUS = ""                            #授权柜员
        HostContext.I1AUPS = ""                            #授权柜员密码
        HostContext.I1WSNO = ""                            #终端号
        HostContext.I1CLDT = "00000000"                    #批量委托日期
        HostContext.I1UNSQ = '000000000000'                #批量委托号
        HostContext.I1NBBH = TradeContext.appNo            #代理业务号(AG2003)
        HostContext.I1DATE = TradeContext.WORKDATE         #外系统日期
        HostContext.I1FINA = TradeContext.appNo            #下传文件名称

        HostTradeCode = "8818".ljust(10,' ')
        HostComm.callHostTrade( os.environ['AFAP_HOME'] + '/conf/hostconf/AH8818.map', HostTradeCode, "0002" )
        if( HostContext.host_Error ):
            AfaLoggerFunc.tradeInfo('>>>处理结果=[' + str(HostContext.host_ErrorType) + ']:' +  HostContext.host_ErrorMsg)
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001", '[' + str(HostContext.host_ErrorType) + ']:' +  HostContext.host_ErrorMsg
            return False

        else:
            if ( HostContext.O1MGID != 'AAAAAAA' ):
                AfaLoggerFunc.tradeInfo('>>>处理结果=[' + str(HostContext.O1MGID) + ']:' +  HostContext.O1INFO)

                #生成空文件
                fileName    =   TradeContext.HOST_LDIR + "/" + TradeContext.appNo + '_' + TradeContext.WORKDATE + '_2'
                fpFile      =   open( fileName,"w" )
                fpFile.close()
                AfaLoggerFunc.tradeInfo('>>>处理结果:没有正常交易(生成了空文件)')
                TradeContext.errorCode,TradeContext.errorMsg    =   "0001","没有正常交易(生成了空文件)"
                return False

            else:
                #AfaLoggerFunc.tradeInfo('返回结果:重复次数=' + HostContext.O1ACUR)                          #重复次数
                #AfaLoggerFunc.tradeInfo('返回结果:交易日期=' + HostContext.O1TRDT)                          #交易日期
                #AfaLoggerFunc.tradeInfo('返回结果:交易时间=' + HostContext.O1TRTM)                          #交易时间
                #AfaLoggerFunc.tradeInfo('返回结果:柜员流水=' + HostContext.O1TLSQ)                          #柜员流水
                #AfaLoggerFunc.tradeInfo('返回结果:成功标志=' + HostContext.O1OPFG)                          #是否提交成功(0-成功,1-失败)

                #下载主机对帐文件
                rFileName = TradeContext.appNo
                lFileName = TradeContext.appNo + '_' + TradeContext.WORKDATE + '_1'
                if ( GetDzFile(rFileName, lFileName) < 0 ):
                    AfaLoggerFunc.tradeInfo('>>>处理结果:日终处理失败(下载文件)')
                    TradeContext.errorCode,TradeContext.errorMsg    =   "0001","日终处理失败(下载文件)"
                    return False

                AfaLoggerFunc.tradeInfo('>>>转码主机对帐文件')
                dFileName = TradeContext.appNo + '_' + TradeContext.WORKDATE + '_2'
                if ( FormatFile(lFileName, dFileName) < 0 ):
                    AfaLoggerFunc.tradeInfo('>>>处理结果:日终处理失败(格式化)')
                    TradeContext.errorCode,TradeContext.errorMsg    =   "0001","日终处理失败(格式化)"
                    return False

                AfaLoggerFunc.tradeInfo('>>>处理结果:日终处理成功')

        return True

    except Exception, e:
        AfaLoggerFunc.tradeInfo(str(e))
        TradeContext.errorCode,TradeContext.errorMsg    =   "0001",str(e)
        return False

def printRow( Contextlist,hp ):

    if ( len(Contextlist)!= 6 ):
        AfaLoggerFunc.tradeInfo( "序列长度不是6" )
        return False

    else:
        lineList    =   []
        lineList.append( Contextlist[0] )
        lineList.append( Contextlist[1] )
        lineList.append( Contextlist[2] )
        lineList.append( Contextlist[3] )

        if   Contextlist[4].strip() == '1':
            lineList.append("正常收入")
            lineList.append(Contextlist[5].strip())
            lineList.append("")
        elif Contextlist[4].strip() == '2':
            lineList.append("退付")
            lineList.append("")
            lineList.append(Contextlist[5].strip())
        elif Contextlist[4].strip() == '3':
            lineList.append("上缴国库")
        elif Contextlist[4].strip() == '4':
            lineList.append("上缴专户")
        elif Contextlist[4].strip() == '5':
            lineList.append("待查收入")
            lineList.append(Contextlist[5].strip())
            lineList.append("")

        if len(lineList) != 7 :
            TradeContext.errorCode,TradeContext.errorMsg    =   '0001','统计项目个数错误'
            return False

        else:
            #统计合计：加上贷方减去借方
            if not lineList[len(lineList)-2] and lineList[len(lineList)-1]:          #贷方为空,借方不空
                TradeContext.banlance   =   str( float(TradeContext.banlance)  - float(lineList[len(lineList)-1]) )
                lineList.append( TradeContext.banlance )
            elif not lineList[len(lineList)-1] and lineList[len(lineList)-2]:        #贷方不空,借方为空
                TradeContext.banlance   =   str( float(TradeContext.banlance)  + float(lineList[len(lineList)-2]) )
                lineList.append( TradeContext.banlance )
            else:
                TradeContext.errorCode,TradeContext.errorMsg    =   '0001','借贷方全部为空或者全部不为空'
                return False

        for i in range(len(fieldWidthList)):
            hp.write("│")
            hp.write( lineList[i].center(fieldWidthList[i]) )

        hp.write("│")
        hp.write("\n")

##########################################对帐处理##########################################
def Ahdx_DzSend():
    totalnum = 0
    totalamt = 0
    try:
        sqlStr = "SELECT STATUS FROM ABDT_UNITINFO WHERE"
        sqlStr = sqlStr + " APPNO = '"      + TradeContext.appNo  + "'"
        sqlStr = sqlStr + " AND BUSINO = '" + TradeContext.busiNo + "'"
        sqlStr = sqlStr + " AND AGENTTYPE IN ('1','2')"

        #AfaLoggerFunc.tradeInfo(sqlStr)

        records = AfaDBFunc.SelectSql( sqlStr )
        if (records==None or len(records) < 0):
            AfaLoggerFunc.tradeInfo('>>>处理结果:对帐处理失败,数据库异常')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","对帐处理失败,数据库异常"
            return False

        elif ( len(records) == 0 ):
            AfaLoggerFunc.tradeInfo('>>>处理结果:没有发现该单位信息,不能对帐处理')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","没有发现该单位信息,不能对帐处理"
            return False

        #=====对非当日账不需要签退====
        if ( records[0][0] != '2' and (TradeContext.WORKDATE == TradeContext.workDate)):
            AfaLoggerFunc.tradeInfo('>>>处理结果:必须先签退才能进行对帐处理')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","必须先签退才能进行对帐处理"
            return False

        sFileName = TradeContext.HOST_LDIR + '/' + TradeContext.appNo + '_' + TradeContext.WORKDATE + '_2'
        if ( not (os.path.exists(sFileName) and os.path.isfile(sFileName)) ):
            AfaLoggerFunc.tradeInfo("对帐文件不存在,必须先日终处理才能进行对帐处理")
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","对帐文件不存在,必须先日终处理才能进行对帐处理"
            return False

        hpTmp   =   open( sFileName,"r" )
        if not hpTmp.read() :
            AfaLoggerFunc.tradeInfo("当天没有正常收入交易")
            #begin 20100716 蔡永贵修改 由于此处并没有抛出异常终止程序，故此处errorCode还是应该置为0000
            #TradeContext.errorCode,TradeContext.errorMsg    =   "0001","当天没有交易"
            TradeContext.errorCode,TradeContext.errorMsg    =   "0000","当天没有交易"
            #end
            #return False

        #对帐初始化
        sqlstr = "UPDATE FS_MAINTRANSDTL SET CHKFLAG='" + '*' + "' WHERE "
        sqlstr = sqlstr + " APPNO='"        + TradeContext.appNo    + "'"
        sqlstr = sqlstr + " AND BUSINO='"   + TradeContext.busiNo   + "'"
        sqlstr = sqlstr + " AND WORKDATE='" + TradeContext.WORKDATE + "'"

        AfaLoggerFunc.tradeInfo(sqlstr)

        retcode = AfaDBFunc.UpdateSqlCmt( sqlstr )
        if (retcode==None or retcode <= 0):
            AfaLoggerFunc.tradeInfo('没有任何交易数据')

        #打开主机下载文件
        hFp = open(sFileName, "r")

        #读取一行
        linebuf = hFp.readline()
        while ( len(linebuf) > 0 ):
            if ( len(linebuf) < 996 ):
                AfaLoggerFunc.tradeInfo('该批次下载文件格式错误(长度),请检查')
                hFp.close()
                return False

            swapbuf = linebuf[0:996].split('<fld>')

#            if ( len(swapbuf) != 55 ):
#                AfaLoggerFunc.tradeInfo('该批次下载文件格式错误(域数),请检查')
#                hFp.close()
#                return False

            #显示记录信息
            #PrtRecInfo(swapbuf)

            linebuf = hFp.readline()

            if ( swapbuf[0].strip()  != TradeContext.appNo or \
                 swapbuf[3].strip()  != TradeContext.WORKDATE or \
                 swapbuf[5].strip()  != TradeContext.WORKDATE ):
                continue

            #先查询数据库中记录是否存在
            sqlstr = "SELECT BRNO,TELLERNO,REVTRANF,AMOUNT,BANKSTATUS,CORPSTATUS FROM FS_MAINTRANSDTL WHERE"
            sqlstr = sqlstr + " APPNO='"        + TradeContext.appNo    + "'"
            sqlstr = sqlstr + " AND BUSINO='"   + TradeContext.busiNo   + "'"
            sqlstr = sqlstr + " AND WORKDATE='" + TradeContext.WORKDATE + "'"
            sqlstr = sqlstr + " AND SERIALNO='" + swapbuf[4].strip()    + "'"

            AfaLoggerFunc.tradeInfo(sqlstr)

            ChkFlag = '*'
            records = AfaDBFunc.SelectSql( sqlstr )
            if ( records==None or len(records) == 0 ):
                AfaLoggerFunc.tradeInfo('数据库中记录匹配失败(表中无记录)')
                AfaLoggerFunc.tradeInfo(sqlstr)
                continue

            else:
                h_tradeamt = (long)((float)(swapbuf[32].strip())*100   + 0.1)
                m_tradeamt = (long)((float)(records[0][3].strip())*100 + 0.1)

                if ( swapbuf[9].strip() != records[0][0] ):
                    AfaLoggerFunc.tradeInfo('数据库中记录匹配失败(机构号不符):' + swapbuf[9].strip()  + '|' + records[0][0] + '|')
                    #PrtRecInfo(swapbuf)
                    ChkFlag = '2'

                elif ( swapbuf[10].strip() != records[0][1] ):
                    AfaLoggerFunc.tradeInfo('数据库中记录匹配失败(柜员号不符):' + swapbuf[10].strip() + '|' + records[0][1] + '|')
                    #PrtRecInfo(swapbuf)
                    ChkFlag = '3'

                elif ( h_tradeamt != m_tradeamt ):
                    AfaLoggerFunc.tradeInfo('数据库中记录匹配失败(发生额不符):' + str(h_tradeamt) + '|' + str(m_tradeamt) + '|')
                    #PrtRecInfo(swapbuf)
                    ChkFlag = '4'

                elif ( swapbuf[50].strip() == '1' ):
                    ChkFlag = '1'

                else:
                    ChkFlag = '0'

            #再修改与数据库进行匹配
            sqlstr = "UPDATE FS_MAINTRANSDTL SET CHKFLAG='" + ChkFlag + "' WHERE "
            sqlstr = sqlstr + " APPNO='"        + TradeContext.appNo    + "'"
            sqlstr = sqlstr + " AND BUSINO='"   + TradeContext.busiNo   + "'"
            sqlstr = sqlstr + " AND WORKDATE='" + TradeContext.WORKDATE + "'"
            sqlstr = sqlstr + " AND SERIALNO='" + swapbuf[4].strip()    + "'"

            #AfaLoggerFunc.tradeInfo(sqlstr)

            retcode = AfaDBFunc.UpdateSqlCmt( sqlstr )
            if (retcode==None or retcode <= 0):
                AfaLoggerFunc.tradeInfo('修改记录对帐状态,数据库异常')
                hFp.close()
                TradeContext.errorCode,TradeContext.errorMsg    =   "0001","修改记录对帐状态,数据库异常"
                return False

            totalnum = totalnum + 1
            totalamt = totalamt + m_tradeamt

        hFp.close()

        #每天只能做一次对账
        sqlstr  =   "select this,date from fs_remain where busino='" + TradeContext.busiNo + "'"
        sqlstr  =   sqlstr + " and bankno = '" + TradeContext.bankbm + "'" + "order by date desc"

        AfaLoggerFunc.tradeInfo(sqlstr)

        records = AfaDBFunc.SelectSql( sqlstr )
        if( records == None ):
            TradeContext.errorCode  =   "9999"
            TradeContext.errorMsg   =   "非税余额表异常"
            AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
            return False

        if( len(records)==0 ):
            TradeContext.errorCode  =   "0001"
            TradeContext.errorMsg   =   "非税余额表异常(没有单位信息)"
            AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
            return False


        #取出昨天的余额
        sqlstr = "select this from fs_remain where busino='" + TradeContext.busiNo + "' and date='" + TradeContext.wyesterdate + "'"

        sqlstr = sqlstr + " and bankno = '" + TradeContext.bankbm + "'" + " order by date desc"

        AfaLoggerFunc.tradeInfo( sqlstr )
        records = AfaDBFunc.SelectSql( sqlstr )
        if( records == None ):
            TradeContext.errorCode  =   "9999"
            TradeContext.errorMsg   =   "非税余额表异常"
            AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
            return False

        if( len(records)==0 ):
            TradeContext.errorCode  =   "0001"
            TradeContext.errorMsg   =   "非税余额表异常(没有对账日期前一天的信息)"
            AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
            return False

        TradeContext.lastRemain     =   records[0][0]       #上期余额
        TradeContext.banlance       =   records[0][0]       #统计余额变化


        #如果当天没有余额信息则插入一条
        #TradeContext.remain="44676653.13"
        sqlstr  =   "insert into fs_remain(busino,date,this,bankno) values('" + TradeContext.busiNo + "','" + TradeContext.WORKDATE + "','" + TradeContext.remain + "','" + TradeContext.bankbm + "')"
        if( AfaDBFunc.InsertSql( sqlstr ) < 1 ):
            AfaDBFunc.RollbackSql( )
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001",'插入本期余额失败' + sqlstr
            AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
            AfaLoggerFunc.tradeInfo( AfaDBFunc.sqlErrMsg )
            return False

        AfaDBFunc.CommitSql( )

        #生成对帐文件,从主交易表中取出数据
        sqlStr = "SELECT bankserno,USERNO,NOTE1,USERNAME,NOTE2,AMOUNT FROM FS_MAINTRANSDTL WHERE "
        sqlStr = sqlStr + " APPNO='"    + TradeContext.appNo    + "'"
        sqlStr = sqlStr + " AND BUSINO='"   + TradeContext.busiNo   + "'"
        sqlStr = sqlStr + " AND WORKDATE='" + TradeContext.WORKDATE + "'"
        sqlStr = sqlStr + " AND CHKFLAG='0' AND NOTE2='1' AND BANKSTATUS='0' and REVTRANF='0' order by userno"


        AfaLoggerFunc.tradeInfo( sqlStr )
        records = AfaDBFunc.SelectSql( sqlStr )
        if (records==None ):
            AfaLoggerFunc.tradeInfo('查询主要交易失败,数据库异常')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","生成对帐处理失败,数据库异常"
            return False

        normalNum   = 0           #正常笔数
        tuifuNum    = 0           #退付笔数
        normalAmt   = 0           #正常金额合计
        tuifuAmt    = 0           #退付金额合计



##############################王军江添加于2007－10－16###########################################################
        fileName   = TradeContext.busiNo + "duizhang" +  ".txt"
        dzFileName = os.environ['AFAP_HOME'] + "/data/ahfs/" + fileName
        dzfp= open(dzFileName,  "w")

        lineWidth       =   144             #报表列表宽度
        WidthList       =   [10,10,20,40,32,14,14,14]
        dzfp.write('对账单'.center(lineWidth))
        dzfp.write('\n')
        dzfp.write('\n')

        dzfp.write('     机构名称：'   + TradeContext.I1SBNM + '\t' )
#        dzfp.write('     制表日期：' + TradeContext.workDate   + '\t\t\t\t\n' )
        dzfp.write('     制表日期：' + TradeContext.WORKDATE   + '\t\t\t\t\n' )    #将制表日期改为所对账务那天的日期
        dzfp.write('     对公帐户：' + TradeContext.busiAccno  + '\t\t\t\t' )
        dzfp.write('     上期余额：' + TradeContext.lastRemain + '\n' )
        dzfp.write('     ┌─────┬─────┬──────────┬────────────────────┬────────────────┬───────┬───────┬───────┐'+'\n')
        dzfp.write('     │银行流水号│缴款书编号│    执收单位编号    │                  缴款人                │正常 待查 退付 上缴国库 上缴专户│    贷方      │       借方   │    合计      │'+'\n')

        banlance    =   float(TradeContext.lastRemain)          #上期余额
        normalNum   =   0
        tuifuNum    =   0

        AfaLoggerFunc.tradeInfo( '当前流水缴费数：' + str( len(records) ) )
        i = 0
        while ( i  < len(records) ):
            rowLine     =   '     │'
            lineList    =   list(records[i])

            if lineList[4]  ==  '1':                            #正常收入
                lineList[4] =   '正常收入'
                lineList.append('')
                banlance    =   banlance + float(lineList[5])
                lineList.append( str(banlance) )
                normalNum   =   normalNum + 1

            elif lineList[4]  ==  '2' :                         #退付收入
                lineList[4]     =   '退付收入'
                lineList.insert(len(lineList)-1,'')

                banlance        =   banlance - float(lineList[6])
                lineList.append( str(banlance) )
                tuifuNum        =   tuifuNum + 1
            else:
                AfaLoggerFunc.tradeInfo('资金性质错误')
                return False

            dzfp.write('     ├─────┼─────┼──────────┼────────────────────┼────────────────┼───────┼───────┼───────┤'+'\n')

            dzfp.write('     │')
            for j in range( len(WidthList) ):
                if j == 4:
                    dzfp.write( lineList[j].center(WidthList[j]) )
                else:
                    dzfp.write( lineList[j].ljust(WidthList[j]) )
                dzfp.write('│')
            else:
                dzfp.write('\n')

            i=i+1
################################################################################################################

        #统计待查收入  流水号、缴款书编号、交款人、收费金额
        #sqlstr  =   "select afc401,afc001,afc006,afc011 from fs_fc74 where date='" + TradeContext.WORKDATE + "'and busino='" + TradeContext.busiNo + "' and afc016='" + TradeContext.brno + "' and flag != '*'"
        dateTmp     =   TradeContext.WORKDATE[0:4] + '-' + TradeContext.WORKDATE[4:6] + '-' + TradeContext.WORKDATE[6:8]
        sqlstr  =   "select afc401,afc001,afc006,afc011 from fs_fc74 where afc015='" + dateTmp + "'and busino='" + TradeContext.busiNo + "' and afc016='" + TradeContext.brno + "' and flag != '*' and afa101 = '" + TradeContext.bankbm + "'"
        AfaLoggerFunc.tradeInfo( sqlstr )
        records =   AfaDBFunc.SelectSql( sqlstr )
        if (records==None) :
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","获取待查数据失败,数据库异常"
            AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
            AfaLoggerFunc.tradeInfo( sqlstr + AfaDBFunc.sqlErrMsg )
            return False

        i           =   0
        AfaLoggerFunc.tradeInfo( '当前待查数目：' + str( len(records) ) )
        daichaNum   =   0           #待查笔数
        while ( i < len(records) ):
            lineList    =   list(records[i])
            lineList[1] =   ''

            lineList.insert(2,'')           #执收单位编码
            lineList.insert(4,'待查')       #资金性质

            banlance    =   banlance + float(lineList[len(lineList)-1])
            lineList.append('')           #贷方
            lineList.append( str(banlance) )
            daichaNum   =   daichaNum + 1

            dzfp.write('     ├─────┼─────┼──────────┼────────────────────┼────────────────┼───────┼───────┼───────┤'+'\n')

            dzfp.write('     │')
            for j in range( len(WidthList) ):

                if j == 4:
                    dzfp.write( lineList[j].center(WidthList[j]) )
                else:
                    dzfp.write( lineList[j].ljust(WidthList[j]) )
                dzfp.write('│')
            else:
                dzfp.write('\n')

            i=i+1


        #---------------------统计退付--------------
        sqlStr = "SELECT bankserno,USERNO,NOTE1,USERNAME,NOTE2,AMOUNT FROM FS_MAINTRANSDTL WHERE "
        sqlStr = sqlStr + " APPNO='"    + TradeContext.appNo    + "'"
        sqlStr = sqlStr + " AND BUSINO='"   + TradeContext.busiNo   + "'"
        sqlStr = sqlStr + " AND WORKDATE='" + TradeContext.WORKDATE + "'"
        sqlStr = sqlStr + " AND CHKFLAG='0' AND NOTE2='2' AND BANKSTATUS='0' and REVTRANF='0' order by userno"

        AfaLoggerFunc.tradeInfo( sqlStr )
        records = AfaDBFunc.SelectSql( sqlStr )
        if (records==None ):
            AfaLoggerFunc.tradeInfo('查询主要交易失败,数据库异常')
            TradeContext.errorCode,TradeContext.errorMsg    =   "0001","生成对帐处理失败,数据库异常"
            return False

        i = 0
        while ( i  < len(records) ):
            rowLine     =   '     │'
            lineList    =   list(records[i])

            if lineList[4]  ==  '1':                            #正常收入
                lineList[4] =   '正常收入'
                lineList.append('')
                banlance    =   banlance + float(lineList[5])
                lineList.append( str(banlance) )
                normalNum   =   normalNum + 1

            elif lineList[4]  ==  '2' :                         #退付收入
                lineList[4]     =   '退付收入'
                lineList.insert(len(lineList)-1,'')             #资金性质贷方为空

                banlance        =   banlance - float(lineList[6])
                lineList.append( str(banlance) )
                tuifuNum        =   tuifuNum + 1
            else:
                AfaLoggerFunc.tradeInfo('资金性质错误')
                return False

            dzfp.write('     ├─────┼─────┼──────────┼────────────────────┼────────────────┼───────┼───────┼───────┤'+'\n')

            dzfp.write('     │')
            for j in range( len(WidthList) ):
                if j == 4:
                    dzfp.write( lineList[j].center(WidthList[j]) )
                else:
                    dzfp.write( lineList[j].ljust(WidthList[j]) )
                dzfp.write('│')
            else:
                dzfp.write('\n')

            i=i+1
        else:
            dzfp.write('     └─────┴─────┴──────────┴────────────────────┴────────────────┴───────┴───────┴───────┘'+'\n' )


        normalAmt   =   0
        tuifuAmt    =   0
        daichaAmt   =   0

        sqlStr = "SELECT sum(double(AMOUNT)) FROM FS_MAINTRANSDTL WHERE "
        sqlStr = sqlStr + " APPNO='"    + TradeContext.appNo    + "'"
        sqlStr = sqlStr + " AND BUSINO='"   + TradeContext.busiNo   + "'"
        sqlStr = sqlStr + " AND WORKDATE='" + TradeContext.WORKDATE + "'"
        sqlStr = sqlStr + " AND CHKFLAG='0' AND NOTE2='1' AND BANKSTATUS='0' and REVTRANF='0'"
        AfaLoggerFunc.tradeInfo( sqlStr )
        records = AfaDBFunc.SelectSql( sqlStr )
        normalAmt = records[0][0]
        if (normalAmt==None) :
            normalAmt = 0


        sqlStr = "SELECT sum(double(AMOUNT)) FROM FS_MAINTRANSDTL WHERE "
        sqlStr = sqlStr + " APPNO='"    + TradeContext.appNo    + "'"
        sqlStr = sqlStr + " AND BUSINO='"   + TradeContext.busiNo   + "'"
        sqlStr = sqlStr + " AND WORKDATE='" + TradeContext.WORKDATE + "'"
        sqlStr = sqlStr + " AND CHKFLAG='0' AND NOTE2='2' AND BANKSTATUS='0' and REVTRANF='0'"
        AfaLoggerFunc.tradeInfo( sqlStr )
        records = AfaDBFunc.SelectSql( sqlStr )
        tuifuAmt = records[0][0]
        if (tuifuAmt==None) :
            tuifuAmt = 0

        dateTmp     =   TradeContext.WORKDATE[0:4] + '-' + TradeContext.WORKDATE[4:6] + '-' + TradeContext.WORKDATE[6:8]
        sqlstr  =   "select sum(double(AFC011)) from fs_fc74 where AFC015='" + dateTmp + "'and busino='" + TradeContext.busiNo + "' and afc016='" + TradeContext.brno + "' and flag != '*'"
        AfaLoggerFunc.tradeInfo( sqlstr )
        records = AfaDBFunc.SelectSql( sqlstr )
        daichaAmt = records[0][0]
        if (daichaAmt==None) :
            daichaAmt = 0

        sLastLine   =   "     总笔数：" + str(daichaNum+normalNum+tuifuNum)+ "\t\t正常笔数：" + str(normalNum) + "\t\t待查笔数：" + str(daichaNum) + "\t\t退付笔数：" + str(tuifuNum) + "\t\t制表人："
        dzfp.write(sLastLine + "\n")
        sLastLine   =   "     正常收入合计：" + str(normalAmt)+ "\t\t退付合计：" + str(tuifuAmt) + "\t\t待查合计：" + str(daichaAmt)
        dzfp.write(sLastLine + "\n")
        dzfp.write("     本期余额："+ TradeContext.remain )
        dzfp.close()

        #文件长度
        TradeContext.DZFILESIZE = str(os.path.getsize(dzFileName))

        #对帐文件名
        TradeContext.DZFILENAME = fileName


    except Exception, e:
        AfaLoggerFunc.tradeInfo(str(e))
        AfaLoggerFunc.tradeInfo('对帐处理异常')
        TradeContext.errorCode,TradeContext.errorMsg    =   "0001","对帐处理异常"
        dzfp.close()
        return False

#fieldWidthList  =   [14,24,24,40,60,16,16,16]           #宽度列表
#fieldHeadList   =   ["银行流水号","缴款书号","执收单位编码","缴款人","资金性质（正常、待查收入、退付、上缴国库、上缴专户）","贷方","借方","合计"]
#width           =   14+24+24+40+60+16+16+16+9



###########################################主函数###########################################
def SubModuleMainFst():

    AfaLoggerFunc.tradeInfo('**********代收非税对帐开始*********')
#    TradeContext.WORKDATE = AfaUtilTools.GetSysDate( )
    TradeContext.WORKTIME = AfaUtilTools.GetSysTime( )

    #张恒修改加上银行编码条件
    sqlstr = "select this from fs_8446_remain where busino='" + TradeContext.busiNo + "' and date='" + TradeContext.WORKDATE + "' and bankno = '"+TradeContext.bankbm+"' order by date desc"

    AfaLoggerFunc.tradeInfo('取前一天余额')
    AfaLoggerFunc.tradeInfo(sqlstr)
    records = AfaDBFunc.SelectSql( sqlstr )
    if( records == None ):
        TradeContext.errorCode  =   "9999"
        TradeContext.errorMsg   =   "非税余额表异常"
        AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
        return False

    if( len(records)==0 ):
        TradeContext.errorCode  =   "0001"
        TradeContext.errorMsg   =   "非税余额表异常(没有对账日期信息)"
        AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
        return False

    TradeContext.remain     =   records[0][0]       #本期余额

    TradeContext.errorCode,TradeContext.errorMsg    =   "0000","对帐成功"

    #=====得到对账的前一天的日期 add by pgt 20090401====
    wyear  = int(TradeContext.WORKDATE[:4])
    wmonth = int(TradeContext.WORKDATE[4:6])
    wday   = int(TradeContext.WORKDATE[6:])
    wdate       = datetime.date(wyear,wmonth,wday)     #对账的日期
    TradeContext.wyesterdate = wdate - datetime.timedelta(days=1)
    TradeContext.wyesterdate = TradeContext.wyesterdate.strftime("%Y%m%d")

    AfaLoggerFunc.tradeInfo('wyesterdate<<<<<<'+TradeContext.wyesterdate)
    AfaLoggerFunc.tradeInfo('workDate<<<<<<'+TradeContext.workDate)

    #每天只能做一次对账
    sqlstr  =   "select this from fs_remain where busino='" + TradeContext.busiNo + "' and date='" + TradeContext.WORKDATE + "'"

    #begin 20100701 蔡永贵增加
    sqlstr  =   sqlstr + " and bankno = '" + TradeContext.bankbm + "'"
    #end

    AfaLoggerFunc.tradeInfo( sqlstr )
    records = AfaDBFunc.SelectSql( sqlstr )
    if( records == None  ):
        TradeContext.errorCode  =   "0001"
        TradeContext.errorMsg   =   "非税余额表异常"
        AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
        return False

    #如果当天没有对账，则取出昨天的数据
    if ( len( records)>0 ):
        TradeContext.errorCode  =   "0001"
        TradeContext.errorMsg   =   "每天只能做一次对账"
        AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
        return False

    #查询对公户账户
    sqlstr          =   "select accno from ABDT_UNITINFO where appno='" + TradeContext.appNo + "' and busino='" + TradeContext.busiNo + "'"
    records = AfaDBFunc.SelectSql( sqlstr )
    if( records == None or len(records) == 0 ):
        TradeContext.errorCode  =   "0001"
        TradeContext.errorMsg   =   "查找到对公账户异常"
        AfaLoggerFunc.tradeInfo( sqlstr )
        AfaLoggerFunc.tradeInfo( AfaDBFunc.sqlErrMsg )
        return False

    TradeContext.busiAccno      =   records[0][0]

    #获取位置文件
    GetLappConfig()

    #=====如果对非当天的账，则不进行签退处理====
    AfaLoggerFunc.tradeInfo('WORKDATE=='+str(TradeContext.WORKDATE))
    if(TradeContext.WORKDATE == TradeContext.workDate):
        TradeContext.errorCode  =   "0001"
        TradeContext.errorMsg   =   "不能对当日帐，请次日对帐"
        AfaLoggerFunc.tradeInfo( TradeContext.errorMsg )
        return False
        #AfaLoggerFunc.tradeInfo('>>>签退')
        #Ahdx_Logout()

    AfaLoggerFunc.tradeInfo('>>>日终处理')
    Ahdx_DayEnd()     #下载主机文件并且格式化文件

    AfaLoggerFunc.tradeInfo('>>>对帐处理')
    Ahdx_DzSend()

    #AfaLoggerFunc.tradeInfo('>>>签到')
    #Ahdx_Login()

    AfaLoggerFunc.tradeInfo('**********代收非税对帐结束**********')
    return True


