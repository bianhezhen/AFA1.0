# -*- coding: gbk -*-
###############################################################################
#   农信银系统：往账.主机类操作(1.本地操作 2.主机记账 3.中心记帐).个人现金通存
#==============================================================================
#   交易文件:   TRCC002_8561.py
#   公司名称：  北京赞同科技有限公司
#   作    者：  关彬捷
#   修改时间:   2008-10-20
###############################################################################
import TradeContext,AfaLoggerFunc,AfaUtilTools,AfaDBFunc,TradeFunc,AfaFlowControl,os,AfaFunc,time
from types import *
from rccpsConst import *
import rccpsDBFunc,rccpsState,rccpsHostFunc,rccpsGetFunc
import rccpsMap8563CTradeContext2Dwtrbka_dict


#=====================交易前处理(登记流水,主机前处理)==========================
def SubModuleDoFst():
    AfaLoggerFunc.tradeInfo( '***农信银系统：往账.主机类操作(1.本地操作).个人现金通存[TRCC002_8561]进入***' )
    #=================必要性检查===============================================
    AfaLoggerFunc.tradeInfo(">>>开始必要性检查")
    
    #检查本机构是否有通存通兑业务权限
    if not rccpsDBFunc.chkTDBESAuth(TradeContext.BESBNO):
        return AfaFlowControl.ExitThisFlow("S999","本机构无通存通兑业务权限")
    
    #磁道信息
    if TradeContext.PYETYP == '0':
        if TradeContext.SCTRKINF == '':
            return AfaFlowControl.ExitThisFlow("磁道信息不能为空")
        
        #if TradeContext.THTRKINF == '':
        #    return AfaFlowControl.ExitThisFlow("磁道信息不能为空")
            
        if len(TradeContext.SCTRKINF) > 37:
            return AfaFlowControl.ExitThisFlow('S999','磁道信息非法')
            
        #if len(TradeContext.THTRKINF) > 104:
        #    return AfaFlowControl.ExitThisFlow('S999','磁道信息非法')
    elif TradeContext.PYETYP == '2':
        TradeContext.SCTRKINF = ''.rjust(37,'0')
        TradeContext.THTRKINF = ''.rjust(37,'0')
        
    #存折号码
    if TradeContext.PYETYP == '1':
        if TradeContext.BNKBKNO == '':
            return AfaFlowControl.ExitThisFlow('存折号码不能为空')
    elif TradeContext.PYETYP == '3':
        TradeContext.BNKBKNO = ''
    
    AfaLoggerFunc.tradeInfo(">>>结束必要性检查")
    
    #=================登记通存通兑业务登记簿===================================
    AfaLoggerFunc.tradeInfo(">>>开始登记通存通兑业务登记簿")
    
    TradeContext.SNDMBRCO = TradeContext.SNDSTLBIN      #发送成员行号
    TradeContext.RCVMBRCO = TradeContext.RCVSTLBIN      #接收成员行号
    TradeContext.TRCNO    = TradeContext.SerialNo       #交易流水号
    TradeContext.NCCWKDAT = TradeContext.NCCworkDate    #中心工作日期
    TradeContext.MSGFLGNO = TradeContext.SNDMBRCO + TradeContext.TRCDAT + TradeContext.TRCNO  #报文标识号
    TradeContext.OPRNO    = PL_TDOPRNO_TC               #业务种类:个人现金通存
    TradeContext.DCFLG    = PL_DCFLG_CRE                #借贷标识:贷记
    TradeContext.BRSFLG   = PL_BRSFLG_SND               #往来标识:往账
    #if TradeContext.PYITYP == '0' or '2':
    #    TradeContext.TRCCO = '3000002'                  #交易代码:3000002卡现金通存
    #elif TradeContext.PYITYP == '1' or '3':
    #    TradeContext.TRCCO = '3000004'                  #交易代码:3000004折现金通存
    #else:
    #    return AfaFlowContorl.ExitThisFlow("S999","收款人账户类型非法")
    TradeContext.PYRMBRCO = TradeContext.SNDSTLBIN
    TradeContext.PYEMBRCO = TradeContext.RCVSTLBIN
    
    wtrbka_dict = {}
    if not rccpsMap8563CTradeContext2Dwtrbka_dict.map(wtrbka_dict):
        return AfaFlowContorl.ExitThisFlow("S999","为通存通兑业务登记簿赋值异常")
        
    if not rccpsDBFunc.insTransWtr(wtrbka_dict):
        return AfaFlowControl.ExitThisFlow('S999','登记通存通兑业务登记簿异常')
    
    AfaLoggerFunc.tradeInfo(">>>结束登记通存通兑业务登记簿")
    
    #=================设置业务状态为记账处理中=================================
    AfaLoggerFunc.tradeInfo(">>>开始设置业务状态为记账处理中")
    
    stat_dict = {}
    stat_dict['BJEDTE'] = TradeContext.BJEDTE       #交易日期
    stat_dict['BSPSQN'] = TradeContext.BSPSQN       #报单序号
    stat_dict['BCSTAT'] = PL_BCSTAT_ACC             #PL_BCSTAT_ACC 记账
    stat_dict['BDWFLG'] = PL_BDWFLG_WAIT            #PL_BDWFLG_WAIT 处理中
    
    if not rccpsState.setTransState(stat_dict):
        return AfaFlowControl.ExitThisFlow('S999','设置状态为记账处理中异常')
    
    AfaLoggerFunc.tradeInfo(">>>结束设置业务状态为记账处理中")
    
    if not AfaDBFunc.CommitSql( ):
        AfaLoggerFunc.tradeFatal( AfaDBFunc.sqlErrMsg )
        return AfaFlowControl.ExitThisFlow("S999","Commit异常")
    
    AfaLoggerFunc.tradeInfo(">>>结束设置业务状态为记账处理中")
    
    #=================为主机记账做准备=========================================
    AfaLoggerFunc.tradeInfo(">>>开始为主机记账做准备")
    
    TradeContext.HostCode = '8813' 
       
    TradeContext.PKFG = 'T'                                         #通存通兑标识
    TradeContext.CATR = '0'                                         #现转标识:0-现金
    TradeContext.RCCSMCD  = PL_RCCSMCD_XJTCWZ                         #主机摘要码:现金通存往账
    TradeContext.SBAC = ''
    TradeContext.ACNM = ''
    TradeContext.RBAC = TradeContext.BESBNO + PL_ACC_NXYDQSWZ       #贷方账号
    TradeContext.RBAC = rccpsHostFunc.CrtAcc(TradeContext.RBAC,25)
    TradeContext.OTNM = "农信银待清算往账"
    TradeContext.CTFG = '7'                                         #结转标识:结转-0
    
    AfaLoggerFunc.tradeInfo("借方账号1:[" + TradeContext.SBAC + "]")
    AfaLoggerFunc.tradeInfo("贷方账号1:[" + TradeContext.RBAC + "]")
    
    if TradeContext.CHRGTYP == '0':
        #现金收取手续费
        TradeContext.ACUR = '2'                                         #重复次数 
        
        TradeContext.I2PKFG = 'T'                                       #通存通兑标识
        TradeContext.I2CATR = '0'                                       #现转标识:0-现金
        TradeContext.I2TRAM = TradeContext.CUSCHRG                      #手续费金额
        TradeContext.I2SMCD = PL_RCCSMCD_SXF                            #主机摘要码:手续费
        TradeContext.I2SBAC = ''
        TradeContext.I2ACNM = ''
        TradeContext.I2RBAC = TradeContext.BESBNO + PL_ACC_TCTDSXF      #贷方账号:通存通兑手续费
        TradeContext.I2RBAC = rccpsHostFunc.CrtAcc(TradeContext.I2RBAC,25)
        TradeContext.I2OTNM = "农信银手续费"
        TradeContext.I2CTFG = '8'                                       #结转标识:不结转-1
    elif TradeContext.CHRGTYP == '1':
        #现金通存无法收取本行账户手续费
        return AfaFlowControl.ExitThisFlow("S999","现金通存无法转账收取手续费")
    elif TradeContext.CHRGTYP == '2':
        AfaLoggerFunc.tradeInfo(">>>不收手续费")
    else:
        return AfaFlowControl.ExitThisFlow("S999","非法手续费收取方式")
        
    if TradeContext.existVariable("I2SBAC") and TradeContext.existVariable('I2RBAC'):
        AfaLoggerFunc.tradeInfo("借方账号2:[" + TradeContext.I2SBAC + "]")
        AfaLoggerFunc.tradeInfo("贷方账号2:[" + TradeContext.I2RBAC + "]")
    
    AfaLoggerFunc.tradeInfo(">>>结束为主机记账做准备")
    
    AfaLoggerFunc.tradeInfo( '***农信银系统：往账.主机类操作(1.本地操作).个人现金通存[TRCC002_8561]退出***' )
    
    return True


#=====================交易中处理(修改流水,主机后处理,中心前处理)===============
def SubModuleDoSnd():
    AfaLoggerFunc.tradeInfo( '***农信银系统：往账.主机类操作(2.主机记账).个人现金通存[TRCC002_8561]进入***' )
    
    #=================设置业务状态为记账成功或失败=============================
    
    stat_dict = {}
    stat_dict['BJEDTE']  = TradeContext.BJEDTE
    stat_dict['BSPSQN']  = TradeContext.BSPSQN
    stat_dict['BESBNO']  = TradeContext.BESBNO
    stat_dict['BETELR']  = TradeContext.BETELR
    stat_dict['SBAC']    = TradeContext.SBAC
    stat_dict['ACNM']    = TradeContext.ACNM
    stat_dict['RBAC']    = TradeContext.RBAC
    stat_dict['OTNM']    = TradeContext.OTNM
    if TradeContext.existVariable('TRDT'):
        stat_dict['TRDT'] = TradeContext.TRDT
    if TradeContext.existVariable('TLSQ'):
        stat_dict['TLSQ'] = TradeContext.TLSQ
    stat_dict['MGID']    = TradeContext.errorCode
    stat_dict['STRINFO'] = TradeContext.errorMsg
    
    if TradeContext.errorCode == '0000':
        AfaLoggerFunc.tradeInfo(">>>开始设置业务状态为记账成功")
        
        stat_dict['BCSTAT']  = PL_BCSTAT_ACC
        stat_dict['BDWFLG']  = PL_BDWFLG_SUCC
        stat_dict['PRTCNT']  = 1
        
        if not rccpsState.setTransState(stat_dict):
            return AfaFlowControl.ExitThisFlow('S999', "设置业务状态为记账成功异常")
        
        AfaLoggerFunc.tradeInfo(">>>结束设置业务状态为记账成功")
        
    else:
        AfaLoggerFunc.tradeInfo(">>>开始设置业务状态为记账失败")
        
        stat_dict['BCSTAT']  = PL_BCSTAT_ACC
        stat_dict['BDWFLG']  = PL_BDWFLG_FAIL
        
        if not rccpsState.setTransState(stat_dict):
            return AfaFlowControl.ExitThisFlow('S999', "设置业务状态为记账失败异常")
        
        AfaLoggerFunc.tradeInfo(">>>结束设置业务状态为记账失败")
    
    if not AfaDBFunc.CommitSql( ):
        AfaLoggerFunc.tradeFatal( AfaDBFunc.sqlErrMsg )
        return AfaFlowControl.ExitThisFlow("S999","Commit异常")
    
    if TradeContext.errorCode != '0000':
        return AfaFlowControl.ExitThisFlow(TradeContext.errorCode,TradeContext.errorMsg)
    
    #=================为发送农信银中心做准备===================================
    AfaLoggerFunc.tradeInfo(">>>开始为发送农信银中心做准备")
    
    TradeContext.MSGTYPCO = 'SET003'
    TradeContext.SNDBRHCO = TradeContext.BESBNO
    TradeContext.SNDCLKNO = TradeContext.BETELR
    TradeContext.SNDTRDAT = TradeContext.BJEDTE
    TradeContext.SNDTRTIM = TradeContext.BJETIM
    TradeContext.MSGFLGNO = TradeContext.SNDMBRCO + TradeContext.BJEDTE + TradeContext.TRCNO
    TradeContext.ORMFN    = ''
    TradeContext.OPRTYPNO = '30'
    TradeContext.ROPRTPNO = ''
    TradeContext.TRANTYP  = '0'
    
    TradeContext.CUR = 'CNY'
    TradeContext.LOCCUSCHRG = TradeContext.CUSCHRG
    TradeContext.CUSCHRG = '0.00'
    
    
    AfaLoggerFunc.tradeInfo(">>>结束为发送农信银中心做准备")
    
    
    #=================设置业务状态为发送处理中=================================
    AfaLoggerFunc.tradeInfo(">>>开始设置状态为发送处理中")
    
    if not rccpsState.newTransState(TradeContext.BJEDTE,TradeContext.BSPSQN,PL_BCSTAT_SND,PL_BDWFLG_WAIT):
        return AfaFlowControl.ExitThisFlow('S999',"设置业务状态为发送处理中异常")
    
    AfaLoggerFunc.tradeInfo(">>>结束设置状态为发送处理中")
    
    if not AfaDBFunc.CommitSql( ):
        AfaLoggerFunc.tradeFatal( AfaDBFunc.sqlErrMsg )
        return AfaFlowControl.ExitThisFlow("S999","Commit异常")
        
    AfaLoggerFunc.tradeInfo( '***农信银系统：往账.主机类操作(2.主机记账).个人现金通存[TRCC002_8561]退出***' )
    return True
    
        
#=====================交易后处理===============================================
def SubModuleDoTrd():
    AfaLoggerFunc.tradeInfo( '***农信银系统：往账.主机类操作(3.中心记账).个人现金通存[TRCC002_8561]进入***' )
    
    #=================设置业务状态为发送成功或失败,若发送失败则自动抹账========
    
    stat_dict = {}
    stat_dict['BJEDTE']  = TradeContext.BJEDTE
    stat_dict['BSPSQN']  = TradeContext.BSPSQN
    stat_dict['BESBNO']  = TradeContext.BESBNO
    stat_dict['BETELR']  = TradeContext.BETELR
    stat_dict['BCSTAT']  = PL_BCSTAT_SND
    stat_dict['BDWFLG']  = PL_BDWFLG_SUCC
    stat_dict['PRCCO']   = TradeContext.errorCode
    stat_dict['STRINFO'] = TradeContext.errorMsg
    
    AfaLoggerFunc.tradeInfo("TradeContext.errorCode = [" + TradeContext.errorCode + "]")
    
    if TradeContext.errorCode == '0000':
        AfaLoggerFunc.tradeInfo(">>>开始设置业务状态为发送成功")
        
        stat_dict['BCSTAT']  = PL_BCSTAT_SND
        stat_dict['BDWFLG']  = PL_BDWFLG_SUCC
        
        if not rccpsState.setTransState(stat_dict):
            return AfaFlowControl.ExitThisFlow('S999', "设置业务状态为发送成功异常")
        
        AfaLoggerFunc.tradeInfo(">>>结束设置业务状态为发送成功")
        
    else:
        AfaLoggerFunc.tradeInfo(">>>开始设置业务状态为发送失败")
        
        stat_dict['BCSTAT']  = PL_BCSTAT_SND
        stat_dict['BDWFLG']  = PL_BDWFLG_FAIL
        
        if not rccpsState.setTransState(stat_dict):
            return AfaFlowControl.ExitThisFlow('S999', "设置业务状态为发送失败异常")
        
        AfaLoggerFunc.tradeInfo(">>>结束设置业务状态为发送失败")
        
        if not AfaDBFunc.CommitSql( ):
            AfaLoggerFunc.tradeFatal( AfaDBFunc.sqlErrMsg )
            return AfaFlowControl.ExitThisFlow("S999","Commit异常")
        
        #=============发起主机抹账=============================================
        AfaLoggerFunc.tradeInfo(">>>开始设置业务状态为抹账处理中")
        
        #=====特殊处理  关彬捷 20081127 调8813抹账,需产生新的前置流水号进行记账====
        if rccpsGetFunc.GetRBSQ(PL_BRSFLG_SND) == -1 :
            return AfaFlowControl.ExisThisFlow('S999',"产生新的前置流水号异常")
        
        
        #为抹账会计分录赋值
        TradeContext.HostCode='8813'
        
        TradeContext.PKFG = 'T'                                         #通存通兑标识
        TradeContext.RVFG = '2'                                         #红蓝字标志 2
        TradeContext.CATR = '0'                                         #现转标识:0-现金
        TradeContext.RCCSMCD = PL_RCCSMCD_XJTCWZ                        #主机摘要码:现金通存往账
        TradeContext.SBAC = ''
        TradeContext.ACNM = ''
        TradeContext.RBAC = TradeContext.BESBNO + PL_ACC_NXYDQSWZ       #贷方账号
        TradeContext.RBAC = rccpsHostFunc.CrtAcc(TradeContext.RBAC,25)
        TradeContext.OTNM = "农信银待清算往账"
        TradeContext.CTFG = '7'                                         #结转标识:结转-0
        
        AfaLoggerFunc.tradeInfo("借方账号1:[" + TradeContext.SBAC + "]")
        AfaLoggerFunc.tradeInfo("贷方账号1:[" + TradeContext.RBAC + "]")
        
        if TradeContext.CHRGTYP == '0':
            #现金收取手续费
            TradeContext.ACUR   = '2'                                       #重复次数
            
            TradeContext.I2PKFG = 'T'                                       #通存通兑标识
            TradeContext.I2RVFG = '2'                                       #红蓝字标志 2
            TradeContext.I2CATR = '0'                                       #现转标识:0-现金
            TradeContext.I2TRAM = TradeContext.LOCCUSCHRG                   #手续费金额
            TradeContext.I2SMCD = PL_RCCSMCD_SXF                            #主机摘要码:手续费
            TradeContext.I2SBAC = ''
            TradeContext.I2ACNM = ''
            TradeContext.I2RBAC = TradeContext.BESBNO + PL_ACC_TCTDSXF      #贷方账号:通存通兑手续费
            TradeContext.I2RBAC = rccpsHostFunc.CrtAcc(TradeContext.I2RBAC,25)
            TradeContext.I2OTNM = "农信银手续费"
            TradeContext.I2CTFG = '8'                                       #结转标识:不结转-1
        
        
        #====设置业务状态为抹账处理中====
        if not rccpsState.newTransState(TradeContext.BJEDTE,TradeContext.BSPSQN,PL_BCSTAT_HCAC,PL_BDWFLG_WAIT):
            return AfaFlowControl.ExitThisFlow('S999','设置业务状态为抹账处理中异常')
        
        AfaLoggerFunc.tradeInfo(">>>结束设置业务状态为抹账处理中")
        
        if not AfaDBFunc.CommitSql( ):
            AfaLoggerFunc.tradeFatal( AfaDBFunc.sqlErrMsg )
            return AfaFlowControl.ExitThisFlow("S999","Commit异常")
            
        AfaLoggerFunc.tradeInfo(">>>开始发起主机抹账")
        
        #=====调起抹账主机接口====
        rccpsHostFunc.CommHost( TradeContext.HostCode )
        
        AfaLoggerFunc.tradeInfo(">>>结束发起主机抹账")
        
        stat_dict = {}
        
        stat_dict['BJEDTE']  = TradeContext.BJEDTE
        stat_dict['BSPSQN']  = TradeContext.BSPSQN
        stat_dict['MGID']    = TradeContext.errorCode
        stat_dict['STRINFO'] = TradeContext.errorMsg
            
        AfaLoggerFunc.tradeInfo("TradeContext.errorCode = [" + TradeContext.errorCode + "]")
        if TradeContext.errorCode == '0000':
            AfaLoggerFunc.tradeInfo(">>>开始设置业务状态为抹账成功")
            
            stat_dict['BCSTAT'] = PL_BCSTAT_HCAC
            stat_dict['BDWFLG'] = PL_BDWFLG_SUCC
            stat_dict['TRDT']   = TradeContext.TRDT
            stat_dict['TLSQ']   = TradeContext.TLSQ
            stat_dict['PRTCNT'] = 1                            #打印次数
            
            if not rccpsState.setTransState(stat_dict):
                return AfaFlowControl.ExitThisFlow('S999','设置业务状态抹账成功异常')
            
            AfaLoggerFunc.tradeInfo(">>>结束设置业务状态为抹账成功")
            
        else:
            AfaLoggerFunc.tradeInfo(">>>开始设置业务状态为抹账失败")
            
            stat_dict['BCSTAT'] = PL_BCSTAT_HCAC
            stat_dict['BDWFLG'] = PL_BDWFLG_FAIL
            
            if not rccpsState.setTransState(stat_dict):
                return AfaFlowControl.ExitThisFlow('S999','设置业务状态抹账成功异常')
            
            AfaLoggerFunc.tradeInfo(">>>结束设置业务状态为抹账失败")
            
    if not AfaDBFunc.CommitSql( ):
        AfaLoggerFunc.tradeFatal( AfaDBFunc.sqlErrMsg )
        return AfaFlowControl.ExitThisFlow("S999","Commit异常")
        
    TradeContext.errorCode = '0000'
    
    AfaLoggerFunc.tradeInfo( '***农信银系统：往账.主机类操作(3.中心记账).个人现金通存[TRCC002_8561]退出***' )
    return True
