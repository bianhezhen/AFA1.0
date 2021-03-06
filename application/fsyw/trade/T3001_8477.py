###############################################################################
# -*- coding: gbk -*-
# 文件标识：
# 摘    要：安徽非税
#
# 当前版本：1.0
# 作    者：WJJ
# 完成日期：2007年10月15日
###############################################################################
import TradeContext, AfaDBFunc, AfaLoggerFunc, os, sys, HostComm, HostContext, ConfigParser
from types import *

#读取主机信息
def GetLappConfig( CfgFileName = None ):
    try:
        config = ConfigParser.ConfigParser( )

        if( CfgFileName == None ):
            CfgFileName = os.environ['AFAP_HOME'] + '/conf/lapp.conf'

        config.readfp( open( CfgFileName ) )

        TradeContext.HOST_HOSTIP   = config.get('HOST_DZ', 'HOSTIP')
        TradeContext.HOST_USERNO   = config.get('HOST_DZ', 'USERNO')
        TradeContext.HOST_PASSWD   = config.get('HOST_DZ', 'PASSWD')
        
        TradeContext.HOST_LDIR     = os.environ['AFAP_HOME'] + "/data/ahfs/"        #本地路径
        TradeContext.HOST_RDIR     = 'FTAXLIB'            #config.get('HOST_DZ', 'RDIR')  #远程路径
        TradeContext.TRACE         = config.get('HOST_DZ', 'TRACE')

        return 0

    except Exception, e:
        print str(e)
        return -1
        
#下载帐号流水明细文件
def GetDetailFile(rfilename, lfilename):
    try:
        #创建文件
        ftpShell = os.environ['AFAP_HOME'] + '/data/ahfs/shell/ahfs_ahfs.sh'
        ftpFp = open(ftpShell, "w")

        ftpFp.write('open ' + TradeContext.HOST_HOSTIP + '\n')
        ftpFp.write('user ' + TradeContext.HOST_USERNO + ' ' + TradeContext.HOST_PASSWD + '\n')

        #下载文件
        ftpFp.write('cd '  + TradeContext.HOST_RDIR + '\n')
        ftpFp.write('lcd ' + TradeContext.HOST_LDIR + '\n')
        ftpFp.write('quote type c 1381 ' + '\n')
        ftpFp.write('get ' + rfilename + ' ' + lfilename + '\n')

        ftpFp.close()

        ftpcmd = 'ftp -n < ' + ftpShell + ' 1>/dev/null 2>/dev/null '

        ret = os.system(ftpcmd)
        if ( ret != 0 ):
            return -1
        else:
            return 0

    except Exception, e:
        AfaLoggerFunc.tradeInfo(e)
        AfaLoggerFunc.tradeInfo('FTP处理异常')
        return -1
        
        
def SubModuleMainFst( ):
    TradeContext.__agentEigen__  = '0'   #从表标志
    
    #通讯区打包
    HostContext.I1TRCD = '8847'                        #交易码
    HostContext.I1SBNO = TradeContext.brno             #交易机构号
    HostContext.I1USID = TradeContext.teller           #交易柜员号
    HostContext.I1AUUS = ""                            #授权柜员
    HostContext.I1AUPS = ""                            #授权柜员密码
    HostContext.I1WSNO = TradeContext.termId           #终端号
       
    #20111102 陈浩修改 文件名加序列号 确保唯一性
    #begin    
    #获取一个4位的序列号，用于拼上送核心的开户文件名 确保唯一性
    CrtSequence( )
        
    #HostContext.I1FINA = 'AG12345678'                             #文件名称
    HostContext.I1FINA = 'AG1234'+ TradeContext.sequenceNo         #文件名称 (10位)
    #end
    
    #HostContext.I1FINA = TradeContext.brno            #文件名称    
    HostContext.I1STDT = TradeContext.bgDate           #开始日期 
    HostContext.I1EDDT = TradeContext.edDate           #终止日期 
    HostContext.I1ACCN = TradeContext.accno            #对公活期帐号
    AfaLoggerFunc.tradeInfo('返回结果:起始日期     = ' + HostContext.I1STDT)        #交易时间
    AfaLoggerFunc.tradeInfo('返回结果:终止日期     = ' + HostContext.I1EDDT)        #交易时间
    AfaLoggerFunc.tradeInfo('返回结果:交易帐号     = ' + HostContext.I1ACCN)        #交易时间

    HostTradeCode = "8847".ljust(10,' ')
    HostComm.callHostTrade( os.environ['AFAP_HOME'] + '/conf/hostconf/AH8847.map', HostTradeCode, "0002" )
    if( HostContext.host_Error ):
        AfaLoggerFunc.tradeInfo('>>>主机交易失败=[' + str(HostContext.host_ErrorType) + ']:' +  HostContext.host_ErrorMsg)
        TradeContext.errorCode  =   "0001"
        TradeContext.errorMsg   =   HostContext.host_ErrorMsg
        return False
    else:
        if ( HostContext.O1MGID == "AAAAAAA" ):
            AfaLoggerFunc.tradeInfo('>>>查询处理结果=[' + HostContext.O1MGID + ']交易成功')
            AfaLoggerFunc.tradeInfo('返回结果:文件名称     = ' + HostContext.O1FINA)        #文件名称
            AfaLoggerFunc.tradeInfo('返回结果:交易日期     = ' + HostContext.O1TRDT)        #交易日期
            AfaLoggerFunc.tradeInfo('返回结果:交易时间     = ' + HostContext.O1TRTM)        #交易时间
        else:
            TradeContext.errorCode  =   "0001"
            TradeContext.errorMsg   =   HostContext.O1INFO
            return False
    
    AfaLoggerFunc.tradeInfo( "********************中台帐号流水明细查询开始***************" )
    if GetLappConfig() < 0 :
        TradeContext.errorCode  =   "0001"
        TradeContext.errorMsg   =   "读取配置文件错误"
        return False
        
    AfaLoggerFunc.tradeInfo(TradeContext.HOST_HOSTIP)
    AfaLoggerFunc.tradeInfo(TradeContext.HOST_USERNO)
    AfaLoggerFunc.tradeInfo(TradeContext.HOST_PASSWD)
    AfaLoggerFunc.tradeInfo(TradeContext.TRACE      )
    AfaLoggerFunc.tradeInfo(TradeContext.HOST_LDIR  )
    AfaLoggerFunc.tradeInfo(TradeContext.HOST_RDIR  )

    #fileName    =   os.environ['AFAP_HOME'] + "/data/ahfs/" + TradeContext.FileName
    lFileName    =   'DOWN_8477_' + TradeContext.busiNo + '.txt'
    if GetDetailFile( HostContext.O1FINA,lFileName ) != 0 : 
        TradeContext.errorCode  =   "0001"
        TradeContext.errorMsg   =   "ftp流水明细文件失败"
        return False
        
    AfaLoggerFunc.tradeInfo( "********************中台帐号流水明细查询结束***************" )
    TradeContext.errorCode      =   "0000"
    TradeContext.errorMsg       =   "中台帐号流水明细查询成功"
    TradeContext.downFileName   =   lFileName
    return True


#20111102 陈浩添加
#begin
#------------------------------------------------------------------
#生成一个4位的序号
#------------------------------------------------------------------     
def CrtSequence( ):
    
    try:
        sqlStr = "SELECT NEXTVAL FOR FSYW_ONLINE_SEQ FROM SYSIBM.SYSDUMMY1"

        records = AfaDBFunc.SelectSql( sqlStr )
        if records == None :
            AfaLoggerFunc.tradeFatal( AfaDBFunc.sqlErrMsg )
            return ExitSubTrade( '9000', '生成序列号异常' )
        AfaLoggerFunc.tradeInfo( "序列号：" + str(records[0][0]) )
        
        #序列号
        TradeContext.sequenceNo = str(records[0][0]).rjust(4,'0')
        
        return True

    except Exception, e:
        AfaLoggerFunc.tradeFatal( str(e) )
        return ExitSubTrade( '9999', '生成序列号异常' )
        
#end        