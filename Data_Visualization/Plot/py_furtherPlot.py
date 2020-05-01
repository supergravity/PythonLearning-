#!/usr/bin/env python

from array import array
from ROOT import TCanvas, TFile, TLegend, TPad, TGraphErrors, TGaxis, TPaveText, TBox
from ROOT import RooPlot
from types import MethodType


# default vars {{{
oUTPUT_fORMAT='eps'
lEG_xMIN=0.65
lEG_xMAX=0.89
lEG_yMIN=0.55
lEG_yMAX=0.85
tOP_bOTTOM_sEPARATION=0.3
oVERLAP_mARGIN=0.01
pLOT_X_mIN=0.13
pLOT_y_mIN=0.105
pLOT_x_mAX=0.95
pLOT_y_mAX=0.9
TGaxis.SetMaxDigits(2);

# default vars end }}}

# class definition {{{
# class used for manage the arguments importing to functions
class PSet():
    def __init__(self, **kwargs):
        self.__NameList=dict(kwargs)
        if not self.__NameList['Usage']:
            self.__NameList.update( {'Usage':'default usage'} )
        return

    def get(self,objName):
        checked=False
        for key,value in self.__NameList:
            if key == objName:
                checked=True
        if checked:
            return self.__NameList[objName]
        else:
            RaiseErrors(objName)
    def RaiseErrors(self, objName):
        raise KeyError('--------- Error -- PSet used in {uName} needs argument [{aName}] --------------'.format(uName=self.__NameList['usage'],aName=objName))


# function argument checker
def checkArgument(funcName, ipArg, usedArgName=[]):
    if ipArg is None:
        raise KeyError('------------ ERROR -- {fName} needs input arguments ----------------'.format(fName=funcName))
    else:
        for argName in usedArgName:
            if not argName in ipArg.keys():
                raise KeyError('--------- Error -- {fName} needs argument [{aName}] --------------'.format(fName=funcName,aName=argName))
def LegendCreation(plotFrame, optDict):
    if not 'axisOpt' in optDict.keys():
        leg=TLegend(lEG_xMIN,lEG_yMIN,lEG_xMAX,lEG_yMAX)
    else:
        axis=optDict['axisOpt']
        leg=TLegend(axis['xmin'],axis['ymin'],axis['xmax'],axis['ymax'])
    if 'addOptions' in optDict.keys():
        for addOption in optDict['addOptions']:
            leg.AddEntry(plotFrame.findObject(addOption['objName']),addOption['description'],'l')
    else:
        raise KeyError('--- LegendCreation() : no "addOptions" found in input option ---')
    if 'Columns' in optDict.keys():
        leg.SetNColumns(optDict['Columns'])
    leg.SetFillColor(4000)
    leg.SetFillStyle(4000)
    leg.SetBorderSize(0)
    return leg
def TBoxCreation(self, optDict):
    box=TBox()
    if 'color' in optDict.keys():
        box.SetFillColor(optDict['color'])
    else:
        box.SetFillColor(7)
    box.DrawBox(
            optDict['xmin'],self.GetCanvas().GetUymin(),
            optDict['xmax'],self.GetCanvas().GetUymax()
            )
    return None
def TBoxCreation2(self,plotContent, optDict):
    self.info.append(TBox())
    box=self.info[-1]
    if 'color' in optDict.keys():
        box.SetFillColor(optDict['color'])
    else:
        box.SetFillColor(7)
    box.SetFillStyle(1000)

    box.DrawBox(
            optDict['xmin'],self.GetUpperPad().GetUymin(),
            optDict['xmax'],self.GetUpperPad().GetUymax()
            )
    plotContent.addObject(box)
    return None
def ChiSquareTextFunction(self,txt,plotFrame, optDict):
    chi2_Ndof=-1.
    if 'data' in optDict.keys() and 'PDF' in optDict.keys():
        chi2_Ndof=plotFrame.chiSquare(optDict['PDF'],optDict['data'])
    else:
        raise KeyError('--- ChiSquareTextFunction() : no "data" and "PDF" found in input option ---')
    txt.AddText("#frac{{ #chi^{{2}} }}{{nDoF}} = {0:.2f}".format(chi2_Ndof))
    return None
def LineTextFunction(self,txt,plotFrame,optDict):
    if 'word' in optDict.keys():
        content=optDict['word']
        txt.AddText(content)
    return None

# second generation code
def calculatePullPlot(myFrame,dataName,numOfRegion,axisTitle):
    pullFrame=RooPlot(myFrame.GetXaxis().GetXmin(),myFrame.GetXaxis().GetXmax())

    dataHist=myFrame.getHist(dataName)
    fitFragments=[ myFrame.getObject(i+1) for i in range(numOfRegion) ]
    pullHistFragments=[ dataHist.makePullHist(fitFrag,True) for fitFrag in fitFragments ]
    for pullHistFrag in pullHistFragments:
        pullFrame.addPlotable(pullHistFrag,'pX0')

    xaxis=pullFrame.GetXaxis()
    xaxis.SetLabelOffset(0.015)
    xaxis.SetTitle(axisTitle)
    xaxis.SetTitleSize(0.12)
    xaxis.SetLabelSize(0.08)

    yaxis=pullFrame.GetYaxis()
    yaxis.SetTitle('(Data-MC)/#sigma_{Data}')
    yaxis.SetTitleSize(0.08)
    yaxis.SetTitleOffset(0.4)
    yaxis.SetNdivisions(10)
    yaxis.SetLabelSize(0.06)
    pullFrame.SetTitle('')
    pullFrame.SetMinimum(-3.)
    pullFrame.SetMaximum( 3.)
    return pullFrame
def DrawOrigAxis(self,optDict):
    checkArgument('DrawOrigAxis',optDict,['XaxisTitle','Title'])
    obj=self.rootObj
    obj.SetTitle(optDict['Title'])
    obj.GetXaxis().SetTitle(optDict['XaxisTitle'])
    obj.SetStats(False)

    self.rootObj.Draw('axis')
    #self.AddDrawInfo(self.rootObj,'axis')
    return None
def LegendInfoModule(self,plotFrame, optDict):
    checkArgument('LegendInfoModule',optDict,['entry'])
    if not 'axisOpt' in optDict.keys():
        leg=TLegend(lEG_xMIN,lEG_yMIN,lEG_xMAX,lEG_yMAX)
    else:
        axis=optDict['axisOpt']
        leg=TLegend(axis['xmin'],axis['ymin'],axis['xmax'],axis['ymax'])

    for opt in optDict['entry']:
        leg.AddEntry(plotFrame.findObject(opt['objName']),opt['description'],'l')
    if 'Columns' in optDict.keys():
        leg.SetNColumns(optDict['Columns'])
    leg.SetFillColor(4000)
    leg.SetFillStyle(4000)
    leg.SetBorderSize(0)

    if 'ForbidRegInfo' in optDict.keys():
        if optDict['ForbidRegInfo']:
            return leg

    self.AddDrawInfo(leg,'same')
    return leg
def newTopPad(optDict={}):
    # load default values.
    par={
            'sep':tOP_bOTTOM_sEPARATION,
            'overlap':oVERLAP_mARGIN,
            'xmin':pLOT_X_mIN,
            'xmax':pLOT_x_mAX,
            'ymin':pLOT_y_mIN,
            'ymax':pLOT_y_mAX,
        }
    # if parameters are set, use user values.
    #for key, val in optDict.iteritems():
    for key, val in optDict.items():
        if key in par:
            par[key] = val

    pad=TPad('toppad','',0.,par['sep']-par['overlap'],1.,1.0)
    pad.SetTicks(1,1)
    pad.SetBottomMargin(0.05)
    pad.SetLeftMargin(par['xmin'])
    pad.SetRightMargin(1.-par['xmax'])
    pad.SetTopMargin( (1.-par['ymax'])/(1.-par['sep']) )
    pad.SetFillColor(4000)
    pad.SetFillStyle(4000)
    return pad
def newBottomPad(optDict={}):
    # load default values.
    par={
            'sep':tOP_bOTTOM_sEPARATION,
            'overlap':oVERLAP_mARGIN,
            'xmin':pLOT_X_mIN,
            'xmax':pLOT_x_mAX,
            'ymin':pLOT_y_mIN,
            'ymax':pLOT_y_mAX,
        }
    # if parameters are set, use user values.
    #for key, val in optDict.iteritems():
    for key, val in optDict.items():
        if key in par.keys():
            par[key] = val

    pad=TPad('botpad','',0.,0.,1.,par['sep']+par['overlap'])
    pad.SetTicks(1,1)
    pad.SetTopMargin(0.025)
    pad.SetLeftMargin(par['xmin'])
    pad.SetRightMargin(1.-par['xmax'])
    pad.SetBottomMargin( par['ymin']/par['sep'] )
    pad.SetFillColor(4000)
    pad.SetFillStyle(4000)
    return pad
def PullDistributionModule(self,plotContent, optDict):
    checkArgument('PullDistributionModule',optDict,['numOfRegion','dataName','frameName'])

    # separate canvas to top down pads
    self.SetCanvasSize(2000,2400)
    canv=self.GetCurrentPad()
    self.uppad=newTopPad()
    self.dnpad=newBottomPad()

    self.uppad.Draw()
    self.dnpad.Draw()


    self.uppad.cd()
    xtitle=plotContent.GetXaxis().GetTitle()
    plotContent.GetXaxis().SetTitle('')
    plotContent.GetXaxis().SetLabelSize(0)
    plotContent.Draw()
    self.uppad.Update()

    self.dnpad.cd()
    pull=calculatePullPlot(plotContent,optDict['dataName'],optDict['numOfRegion'],xtitle)
    pull.Draw('axis')
    self.SetCurrentPad(self.dnpad)

    self.errFunc=MethodType(ErrorRegionHighlight,self)
    highlightRegion=self.errFunc({ 'ymin':-1,'ymax':1,'color':7, 'ForbidRegInfo':True })

    highlightRegion.Draw('same')
    pull.Draw('same')
    self.SetCurrentPad(self.uppad)

    self.JustKeepObj(pull)
    self.JustKeepObj(highlightRegion)
    return None


def TextInfoModule(self,plotContent,optDict):
    checkArgument('TextInfoModule()',optDict,['content'])
    txt=None
    if 'axisOpt' in optDict.keys():
        axis=optDict['axisOpt']
        txt=TPaveText(axis['xmin'],axis['ymin'],axis['xmax'],axis['ymax'],'NDC')
    else:
        txt=TPaveText(0.11,0.15,0.4,0.30,'NDC')

    for content in optDict['content']:
        checkArgument('"content" variables in TextInfoModule()',content,['function','ipVar'])
        self.textFunc=MethodType(content['function'],self)
        self.textFunc(txt,plotContent,content['ipVar'])

    txt.SetFillColor(4000)
    txt.SetFillStyle(4000)
    txt.SetTextAlign(31)

    self.AddDrawInfo(txt,'same')
    return txt
def SignalRegionHighlight(self, optDict):
    checkArgument('SignalRegionHighlight',optDict,['xmin','xmax','color'])
    box=TBox(optDict['xmin'],self.GetCurrentPad().GetUymin(),
             optDict['xmax'],self.GetCurrentPad().GetUymax())
    box.SetFillColor(optDict['color'])

    if 'ForbidRegInfo' in optDict.keys():
        if optDict['ForbidRegInfo']:
            return box

    self.AddDrawInfo(box,'same')
    return box
def ErrorRegionHighlight(self,optDict):
    checkArgument('ErrorRegionHighlight',optDict,['ymin','ymax','color'])
    box=TBox(self.GetCurrentPad().GetUxmin(),optDict['ymin'],
             self.GetCurrentPad().GetUxmax(),optDict['ymax'])
    box.SetFillColor(optDict['color'])
    box.SetFillStyle(3444)

    if 'ForbidRegInfo' in optDict.keys():
        if optDict['ForbidRegInfo']:
            return box

    self.AddDrawInfo(box,'same')
    return box

# second generation code end


class ProcessObject():
    def __init__(self,inFileName):
        self.__fileIn=TFile.Open(inFileName)
        self.__canvas=TCanvas(inFileName,'',2000,2000)
        self.InitObjs()
        return
    def __del__(self):
        self.__fileIn.Close()
        return
    def GetObj(self, name):
        return self.__fileIn.Get(name)
    def GetCanvas(self):
        self.__canvas.Update()
        return self.__canvas
    def GetCurrentPad(self):
        self.__cpad.Update()
        return self.__cpad
    def GetUpperPad(self):
        self.__uppad.Update()
        return self.__uppad
    def GetLowerPad(self):
        self.__dnpad.Update()
        return self.__dnpad
    def Processing(self):
        for func in self.__sequence:
            func()
        return None
    def InitObjs(self):
        self.__canvas.Clear()
        self.__canvas.SetFillColor(4000)
        self.__canvas.SetFillStyle(4000)
        self.__plotList=[]
        self.__sequence=[]
        self.__nothing=[]
        self.SetCurrentPad(self.__canvas)
    def AddDrawInfo(self,obj,drawOpt):
        self.__plotList.append(tuple([obj,drawOpt]))
        return None
    def AddUpDownPad(self):
        self.__canvas.SetWindowSize(int(self.__canvas.GetWindowWidth()),int(self.__canvas.GetWindowHeight()*1.4))
        self.__uppad=self.NewTopPad()
        self.__dnpad=self.NewBottomPad()
        return None
    def AddSeq(self, func):
        self.__sequence.append(func)
        return None
    def JustKeepObj(self,obj):
        self.__nothing.append(obj)
        return None
    # load RooPlot in figs/loadName in root file.
    def MakePlot_fromRooPlot(self,**kwargs):
        self.InitObjs()
        checkArgument('MakePlot_fromRooPlot()', kwargs, ['loadObject','XaxisTitle','addInfo','outputName'])
        plotContent=self.GetObj(kwargs['loadObject'])
        plotContent.SetTitle('')
        plotContent.SetMaximum(int(plotContent.GetMaximum()*1.2))
        plotContent.GetXaxis().SetTitle(kwargs['XaxisTitle'])


        # add plotable content
        self.info=[]
        if 'addInfo' in kwargs.keys():
            for info in kwargs['addInfo']:
                self.func=MethodType(info['function'],self)
                self.func(plotContent,info['ipVar'])

        self.GetCurrentPad().cd()
        plotContent.Draw()
        for plot in self.__plotList:
            plot[0].Draw(plot[1])



        outtag=kwargs['outputName']
        self.GetCanvas().SaveAs('figRooPlot_{tag}.{figFormat}'.format(figFormat=oUTPUT_fORMAT,tag=outtag))
        return None

	# testting
    def MakePlot_fromRootObj(self,**kwargs):
        self.InitObjs()
        checkArgument('MakePlot_fromRootObj()', kwargs, ['loadObject','addInfo','outputName'])
        self.rootObj=self.GetObj(kwargs['loadObject'])

        # add plotable content
	# if something needs to Draw('same') add them in self.info list
	# or you can call self.AddDrawInfo() function
        for info in kwargs['addInfo']:
            self.func=MethodType(info['function'],self)
            self.func(info['ipVar'])

        for plot in self.__plotList:
            plot[0].Draw(plot[1])

        if len(self.__plotList):
            self.rootObj.Draw('same')
        else:
            self.rootObj.Draw()
        self.GetCanvas().SaveAs('figRootObject_{figname}.{figFormat}'.format(figFormat=oUTPUT_fORMAT,figname=kwargs['outputName']))
        return None
	#tested 
    def SetCanvasSize(self,x,y):
        self.__canvas.SetCanvasSize(x,y)
        return None
    def SetCurrentPad(self,pad):
        self.__cpad=pad
        return None

    def calculatePullPlot(self,myFrame,dataName,numOfRegion):
        pullFrame=RooPlot(myFrame.GetXaxis().GetXmin(),myFrame.GetXaxis().GetXmax())

        dataHist=myFrame.getHist(dataName)
        fitFragments=[ myFrame.getObject(i+1) for i in range(numOfRegion) ]
        pullHistFragments=[ dataHist.makePullHist(fitFrag,True) for fitFrag in fitFragments ]
        for pullHistFrag in pullHistFragments:
            pullFrame.addPlotable(pullHistFrag,'pX0')
        pullFrame.GetYaxis().SetTitle('#frac{Data-MC}{#sigma_{Data}}')
        pullFrame.SetTitle('')
        pullFrame.SetMinimum(-3.)
        pullFrame.SetMaximum( 3.)
        return pullFrame
    def calculateInterestingRegionInPull(self,plotPad,xTitle):
        x=array('d',[plotPad.GetUxmin(),plotPad.GetUxmax()])
        ex=array('d',[0.,0.])
        y=array('d',[0.,0.])
        ey=array('d',[1.,1.])
        ge=TGraphErrors(2,x,y,ex,ey)
        ge.SetFillColor(7)
        ge.SetFillStyle(3444)
        ge.SetTitle('')
        ge.GetXaxis().SetRangeUser(x[0],x[1])
        ge.GetXaxis().SetLabelOffset(0.015)
        ge.GetXaxis().SetTitle(xTitle)
        ge.GetXaxis().SetTitleSize(0.12)
        ge.GetXaxis().SetLabelSize(0.08)

        ge.GetYaxis().SetRangeUser(-3.,3.)
        ge.GetYaxis().SetTitle('(Data-MC)/#sigma_{Data}')
        ge.GetYaxis().SetTitleSize(0.08)
        ge.GetYaxis().SetTitleOffset(0.5)
        ge.GetYaxis().SetLabelSize(0.08)
        ge.GetYaxis().SetNdivisions(5)

        return ge
    def NewTopPad(self):
        pad=TPad('toppad','',0.,tOP_bOTTOM_sEPARATION-oVERLAP_mARGIN,1.,1.0)
        pad.SetTicks(1,1)
        pad.SetBottomMargin(0.05)
        pad.SetLeftMargin(pLOT_X_mIN)
        pad.SetRightMargin(1.-pLOT_x_mAX)
        pad.SetTopMargin( (1.-pLOT_y_mAX)/(1.-tOP_bOTTOM_sEPARATION) )
        pad.SetFillColor(4000)
        pad.SetFillStyle(4000)
        return pad
    def NewBottomPad(self):
        pad=TPad('botpad','',0.,0.,1.,tOP_bOTTOM_sEPARATION+oVERLAP_mARGIN)
        pad.SetTicks(1,1)
        pad.SetTopMargin(0.025)
        pad.SetLeftMargin(pLOT_X_mIN)
        pad.SetRightMargin(1.-pLOT_x_mAX)
        pad.SetBottomMargin( pLOT_y_mIN/tOP_bOTTOM_sEPARATION )
        pad.SetFillColor(4000)
        pad.SetFillStyle(4000)
        return pad
# class definition end }}}





if __name__ == '__main__':
##### no kinematic cut #####
#    processProcedure_MC=ProcessObject('workspace_extraStep_1st_shortRangeLbFit_noKinematicCut.root')
#    # Lb fitting result
#    processProcedure_MC.MakePlot_fromRooPlot(
#            loadName='LbModel',
#            XaxisTitle='J/#psipK^{-} Mass(GeV)',
#            tag='noKinematicCut',
#            addInfo=[
#                { 'function': PullDistributionModule,
#                    'ipVar':
#                    {
#                        'frameName':'LbModelForPull',
#                        'numOfRegion':1,
#                        'dataName':'data',
#                    },
#                },
#                { 'function': LegendInfoModule,
#                    'ipVar':
#                    {
#                        'entry': [
#                            { 'objName': 'data'             , 'description':'2016 full data' },
#                            { 'objName': 'totModel', 'description':'totalFit' },
#                            { 'objName': 'comb', 'description':'combinatorial' },
#                            { 'objName': 'Lb', 'description':'#Lambda^{0}_{b}' },
#                            ],
#                        'axisOpt': { 'xmin':0.15,'xmax':0.65,'ymin':0.65,'ymax':0.85 },
#                        'Columns': 2,
#                    },
#                },
#                { 'function': TextInfoModule,
#                    'ipVar':
#                    {
#                        'axisOpt': { 'xmin':0.50,'xmax':0.90,'ymin':0.05,'ymax':0.35 },
#                        'content': [
#                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
#                            # 2nd poly caused yield
#                            { 'function':LineTextFunction, 'ipVar': {'word':'#Lambda^{0}_{b} yield: 2.305#times10^{3}#pm2.21#times10^{2}'} },
#                            { 'function':LineTextFunction, 'ipVar': {'word':'bkg yield: 4.798#times10^{5}#pm7.25#times10^{2}'} },
#                            ## 3rd poly caused yield
#                            #{ 'function':LineTextFunction, 'ipVar': {'word':'#Lambda^{0}_{b} yield: 1.26#times10^{3}#pm1.55#times10^{2}'} },
#                            #{ 'function':LineTextFunction, 'ipVar': {'word':'bkg yield: 2.29#times10^{5}#pm5.00#times10^{2}'} },
#                            ]
#                    },
#                },
#            ],
#        )
#    # lB fitting result
#    processProcedure_MC.MakePlot_fromRooPlot(
#            loadName='lBModel',
#            XaxisTitle='J/#psi#bar{p}K^{+} Mass(GeV)',
#            tag='noKinematicCut',
#            addInfo=[
#                { 'function': PullDistributionModule,
#                    'ipVar':
#                    {
#                        'frameName':'LbModelForPull',
#                        'numOfRegion':1,
#                        'dataName':'data',
#                    },
#                },
#                { 'function': LegendInfoModule,
#                    'ipVar':
#                    {
#                        'entry': [
#                            { 'objName': 'data'             , 'description':'2016 full data' },
#                            { 'objName': 'totModel', 'description':'totalFit' },
#                            { 'objName': 'comb', 'description':'combinatorial' },
#                            { 'objName': 'lB', 'description':'#bar{#Lambda}^{0}_{b}' },
#                            ],
#                        'axisOpt': { 'xmin':0.15,'xmax':0.65,'ymin':0.65,'ymax':0.85 },
#                        'Columns': 2,
#                    },
#                },
#                { 'function': TextInfoModule,
#                    'ipVar':
#                    {
#                        'axisOpt': { 'xmin':0.50,'xmax':0.90,'ymin':0.05,'ymax':0.35 },
#                        'content': [
#                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
#                            # 2nd poly caused yield
#                            { 'function':LineTextFunction, 'ipVar': {'word':'#bar{#Lambda}^{0}_{b} yield: 2.373#times10^{3}#pm2.24#times10^{2}'} },
#                            { 'function':LineTextFunction, 'ipVar': {'word':'bkg yield: 4.764#times10^{5}#pm7.24#times10^{2}'} },
#                            ## 3rd poly caused yield
#                            #{ 'function':LineTextFunction, 'ipVar': {'word':'#Lambda^{0}_{b} yield: 1.26#times10^{3}#pm1.55#times10^{2}'} },
#                            #{ 'function':LineTextFunction, 'ipVar': {'word':'bkg yield: 2.29#times10^{5}#pm5.00#times10^{2}'} },
#                            ]
#                    },
#                },
#            ],
#        )
#
#    processProcedure=ProcessObject('workspace_extraStep_2nd_stabilityLbCheck_noKineCut.root')
#    # Lb parameter scanning
#    processProcedure.MakePlot_fromRootObj(
#            tag='noKineCutLb_cp1_profScan',
#            loadObject='nll_profscan_cp1',
#            addInfo=[
#                {
#                    'function':DrawOrigAxis,
#                    'ipVar': {
#                        'XaxisTitle': '1^{st} order parameter',
#                        'Title': 'Profile likelihood scan'
#                        },
#		},
#                {
#                    'function':SignalRegionHighlight,
#                    'ipVar':{
#                        # 2nd poly caused var
#                        #'xmin':-0.13215-0.0358,'xmax':-0.13215+0.0357,
#
#                        # 3rd poly caused var
#                        'xmin':-0.111-0.0251,'xmax':-0.138+0.0249,
#                        'color':7,
#                        },
#                },
#                ],
#            )
#    processProcedure.MakePlot_fromRootObj(
#            tag='noKineCutLb_cp2_profScan',
#            loadObject='nll_profscan_cp2',
#            addInfo=[
#                {
#                    'function':DrawOrigAxis,
#                    'ipVar': {
#                        'XaxisTitle': '2^{nd} order parameter',
#                        'Title': 'Profile likelihood scan'
#                        },
#		},
#                {
#                    'function':SignalRegionHighlight,
#                    'ipVar':{
#                        # 2nd poly caused var
#                        'xmin':-1.117-0.0748,'xmax':-0.117+0.0753,
#                        ## 3rd poly caused var
#                        #'xmin':0.18645-0.411,'xmax':0.18645+0.403,
#                        'color':7,
#                        },
#                },
#                ],
#            )
#    #processProcedure.MakePlot_fromRootObj(
#    #        tag='cp3_scan',
#    #        loadObject='nll_profscan_cp3',
#    #        addInfo=[
#    #            {
#    #                'function':DrawOrigAxis,
#    #                'ipVar': {
#    #                    'XaxisTitle': '3^{rd} order parameter',
#    #                    'Title': 'Profile likelihood scan'
#    #                    },
#    #    	},
#    #            {
#    #                'function':SignalRegionHighlight,
#    #                'ipVar':{
#    #                    # 3rd poly caused var
#    #                    'xmin':-2.8253-0.827,'xmax':-2.8253+0.845,
#    #                    'color':7,
#    #                    },
#    #            },
#    #            ],
#    #        )
#
#    # lB parameter scanning
#    processProcedure.MakePlot_fromRootObj(
#            tag='noKineCutlB_cp1_profScan',
#            loadObject='nll_profscan_cp1__lBScanLikelihood',
#            addInfo=[
#                {
#                    'function':DrawOrigAxis,
#                    'ipVar': {
#                        'XaxisTitle': '1^{st} order parameter',
#                        'Title': 'Profile likelihood scan'
#                        },
#		},
#                {
#                    'function':SignalRegionHighlight,
#                    'ipVar':{
#                        # 2nd poly caused var
#                        'xmin':-0.138-0.0251,'xmax':-0.138+0.0249,
#
#                        ## 3rd poly caused var
#                        #'xmin':-0.131-0.0424,'xmax':-0.131+0.0415,
#                        'color':7,
#                        },
#                },
#                ],
#            )
#    processProcedure.MakePlot_fromRootObj(
#            tag='noKineCutlB_cp2_profScan',
#            loadObject='nll_profscan_cp2__lBScanLikelihood',
#            addInfo=[
#                {
#                    'function':DrawOrigAxis,
#                    'ipVar': {
#                        'XaxisTitle': '2^{nd} order parameter',
#                        'Title': 'Profile likelihood scan'
#                        },
#		},
#                {
#                    'function':SignalRegionHighlight,
#                    'ipVar':{
#                        # 2nd poly caused var
#                        'xmin':-0.0995-0.0754,'xmax':-0.995+0.0758,
#                        ## 3rd poly caused var
#                        #'xmin':0.18645-0.411,'xmax':0.18645+0.403,
#                        'color':7,
#                        },
#                },
#                ],
#            )
#    #processProcedure.MakePlot_fromRootObj(
#    #        tag='cp3_scan',
#    #        loadObject='nll_profscan_cp3',
#    #        addInfo=[
#    #            {
#    #                'function':DrawOrigAxis,
#    #                'ipVar': {
#    #                    'XaxisTitle': '3^{rd} order parameter',
#    #                    'Title': 'Profile likelihood scan'
#    #                    },
#    #    	},
#    #            {
#    #                'function':SignalRegionHighlight,
#    #                'ipVar':{
#    #                    # 3rd poly caused var
#    #                    'xmin':-2.8253-0.827,'xmax':-2.8253+0.845,
#    #                    'color':7,
#    #                    },
#    #            },
#    #            ],
#    #        )
###### no kinematic cut end #####
#
#
#
###### with kinematic cut #####
#    processProcedure_MC=ProcessObject('workspace_extraStep_1st_shortRangeLbFit_withKinematicCut.root')
#    # Lb fitting result
#    processProcedure_MC.MakePlot_fromRooPlot(
#            loadName='LbModel',
#            XaxisTitle='J/#psipK^{-} Mass(GeV)',
#            tag='withKinematicCut',
#            addInfo=[
#                { 'function': PullDistributionModule,
#                    'ipVar':
#                    {
#                        'frameName':'LbModelForPull',
#                        'numOfRegion':1,
#                        'dataName':'data',
#                    },
#                },
#                { 'function': LegendInfoModule,
#                    'ipVar':
#                    {
#                        'entry': [
#                            { 'objName': 'data'             , 'description':'2016 full data' },
#                            { 'objName': 'totModel', 'description':'totalFit' },
#                            { 'objName': 'comb', 'description':'combinatorial' },
#                            { 'objName': 'Lb', 'description':'#Lambda^{0}_{b}' },
#                            ],
#                        'axisOpt': { 'xmin':0.15,'xmax':0.65,'ymin':0.65,'ymax':0.85 },
#                        'Columns': 2,
#                    },
#                },
#                { 'function': TextInfoModule,
#                    'ipVar':
#                    {
#                        'axisOpt': { 'xmin':0.50,'xmax':0.90,'ymin':0.05,'ymax':0.35 },
#                        'content': [
#                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
#                            # 2nd poly caused yield
#                            { 'function':LineTextFunction, 'ipVar': {'word':'#Lambda^{0}_{b} yield: 7.233#times10^{2}#pm1.29#times10^{2}'} },
#                            { 'function':LineTextFunction, 'ipVar': {'word':'bkg yield: 1.652#times10^{5}#pm4.24#times10^{2}'} },
#                            ## 3rd poly caused yield
#                            #{ 'function':LineTextFunction, 'ipVar': {'word':'#Lambda^{0}_{b} yield: 1.26#times10^{3}#pm1.55#times10^{2}'} },
#                            #{ 'function':LineTextFunction, 'ipVar': {'word':'bkg yield: 2.29#times10^{5}#pm5.00#times10^{2}'} },
#                            ]
#                    },
#                },
#            ],
#        )
#    # lB fitting result
#    processProcedure_MC.MakePlot_fromRooPlot(
#            loadName='lBModel',
#            XaxisTitle='J/#psi#bar{p}K^{+} Mass(GeV)',
#            tag='withKinematicCut',
#            addInfo=[
#                { 'function': PullDistributionModule,
#                    'ipVar':
#                    {
#                        'frameName':'LbModelForPull',
#                        'numOfRegion':1,
#                        'dataName':'data',
#                    },
#                },
#                { 'function': LegendInfoModule,
#                    'ipVar':
#                    {
#                        'entry': [
#                            { 'objName': 'data'             , 'description':'2016 full data' },
#                            { 'objName': 'totModel', 'description':'totalFit' },
#                            { 'objName': 'comb', 'description':'combinatorial' },
#                            { 'objName': 'lB', 'description':'#bar{#Lambda}^{0}_{b}' },
#                            ],
#                        'axisOpt': { 'xmin':0.15,'xmax':0.65,'ymin':0.65,'ymax':0.85 },
#                        'Columns': 2,
#                    },
#                },
#                { 'function': TextInfoModule,
#                    'ipVar':
#                    {
#                        'axisOpt': { 'xmin':0.50,'xmax':0.90,'ymin':0.05,'ymax':0.35 },
#                        'content': [
#                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
#                            # 2nd poly caused yield
#                            { 'function':LineTextFunction, 'ipVar': {'word':'#bar{#Lambda}^{0}_{b} yield: 7.172#times10^{2}#pm1.33#times10^{2}'} },
#                            { 'function':LineTextFunction, 'ipVar': {'word':'bkg yield: 1.646#times10^{5}#pm4.22#times10^{2}'} },
#                            ## 3rd poly caused yield
#                            #{ 'function':LineTextFunction, 'ipVar': {'word':'#Lambda^{0}_{b} yield: 1.26#times10^{3}#pm1.55#times10^{2}'} },
#                            #{ 'function':LineTextFunction, 'ipVar': {'word':'bkg yield: 2.29#times10^{5}#pm5.00#times10^{2}'} },
#                            ]
#                    },
#                },
#            ],
#        )
#
#    processProcedure=ProcessObject('workspace_extraStep_2nd_stabilityLbCheck_withKineCut.root')
#    # Lb parameter scanning
#    processProcedure.MakePlot_fromRootObj(
#            tag='withKineCutLb_cp1_profScan',
#            loadObject='nll_profscan_cp1',
#            addInfo=[
#                {
#                    'function':DrawOrigAxis,
#                    'ipVar': {
#                        'XaxisTitle': '1^{st} order parameter',
#                        'Title': 'Profile likelihood scan'
#                        },
#		},
#                {
#                    'function':SignalRegionHighlight,
#                    'ipVar':{
#                        # 2nd poly caused var
#                        #'xmin':-0.13215-0.0358,'xmax':-0.13215+0.0357,
#
#                        # 3rd poly caused var
#                        'xmin':-0.131-0.0424,'xmax':-0.131+0.0415,
#                        'color':7,
#                        },
#                },
#                ],
#            )
#    processProcedure.MakePlot_fromRootObj(
#            tag='withKineCutLb_cp2_profScan',
#            loadObject='nll_profscan_cp2',
#            addInfo=[
#                {
#                    'function':DrawOrigAxis,
#                    'ipVar': {
#                        'XaxisTitle': '2^{nd} order parameter',
#                        'Title': 'Profile likelihood scan'
#                        },
#		},
#                {
#                    'function':SignalRegionHighlight,
#                    'ipVar':{
#                        # 2nd poly caused var
#                        'xmin':-1.220-0.125,'xmax':-1.220+0.128,
#                        ## 3rd poly caused var
#                        #'xmin':0.18645-0.411,'xmax':0.18645+0.403,
#                        'color':7,
#                        },
#                },
#                ],
#            )
#    #processProcedure.MakePlot_fromRootObj(
#    #        tag='cp3_scan',
#    #        loadObject='nll_profscan_cp3',
#    #        addInfo=[
#    #            {
#    #                'function':DrawOrigAxis,
#    #                'ipVar': {
#    #                    'XaxisTitle': '3^{rd} order parameter',
#    #                    'Title': 'Profile likelihood scan'
#    #                    },
#    #    	},
#    #            {
#    #                'function':SignalRegionHighlight,
#    #                'ipVar':{
#    #                    # 3rd poly caused var
#    #                    'xmin':-2.8253-0.827,'xmax':-2.8253+0.845,
#    #                    'color':7,
#    #                    },
#    #            },
#    #            ],
#    #        )
#
#    # lB parameter scanning
#    processProcedure.MakePlot_fromRootObj(
#            tag='withKineCutlB_cp1_profScan',
#            loadObject='nll_profscan_cp1__lBScanLikelihood',
#            addInfo=[
#                {
#                    'function':DrawOrigAxis,
#                    'ipVar': {
#                        'XaxisTitle': '1^{st} order parameter',
#                        'Title': 'Profile likelihood scan'
#                        },
#		},
#                {
#                    'function':SignalRegionHighlight,
#                    'ipVar':{
#                        # 2nd poly caused var
#                        'xmin':-0.2216-0.0427,'xmax':-0.2216+0.0416,
#
#                        ## 3rd poly caused var
#                        #'xmin':-0.131-0.0424,'xmax':-0.131+0.0415,
#                        'color':7,
#                        },
#                },
#                ],
#            )
#    processProcedure.MakePlot_fromRootObj(
#            tag='withKineCutlB_cp2_profScan',
#            loadObject='nll_profscan_cp2__lBScanLikelihood',
#            addInfo=[
#                {
#                    'function':DrawOrigAxis,
#                    'ipVar': {
#                        'XaxisTitle': '2^{nd} order parameter',
#                        'Title': 'Profile likelihood scan'
#                        },
#		},
#                {
#                    'function':SignalRegionHighlight,
#                    'ipVar':{
#                        # 2nd poly caused var
#                        'xmin':-0.945-0.125,'xmax':-0.945+0.129,
#                        ## 3rd poly caused var
#                        #'xmin':0.18645-0.411,'xmax':0.18645+0.403,
#                        'color':7,
#                        },
#                },
#                ],
#            )

    lbl00=ProcessObject('workspace_0thStep_LbL0Shape_noKinematicCut.ptRange20.30.root') # plotBlock {{{

    fitres=lbl00.GetObj('fitRes/Run2016Data_pLbL0').floatParsFinal()
    sigNum=fitres.find('numLb')
    bkgNum=fitres.find('numCombBkg_Run2016Data_pLbL0')
    ptRange='ptRange20To30'

    lbl00.MakePlot_fromRooPlot(
            loadObject='figs/Run2016Data_pLbL0',
            XaxisTitle='J/#psi#Lambda^{0} Mass(GeV)',
            outputName='{range}_LbL0Dist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/Run2016Data_pLbL0',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'sig'     , 'description':'#Lambda^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.60,'xmax':0.85,'ymin':0.35,'ymax':0.50 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    fitres=lbl00.GetObj('fitRes/Run2016Data_nLbL0').floatParsFinal()
    sigNum=fitres.find('numlB')
    bkgNum=fitres.find('numCombBkg_Run2016Data_nLbL0')

    lbl00.MakePlot_fromRooPlot(
            loadObject='figs/Run2016Data_nLbL0',
            XaxisTitle='J/#psi#bar{#Lambda}^{0} Mass(GeV)',
            outputName='{range}_lBl0Dist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/Run2016Data_nLbL0',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'sig'     , 'description':'#bar{#Lambda}^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.60,'xmax':0.85,'ymin':0.35,'ymax':0.50 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    # plotBlock end }}}
    lbl01=ProcessObject('workspace_0thStep_LbL0Shape_noKinematicCut.ptRange30.33.root') # plotBlock {{{
    fitres=lbl01.GetObj('fitRes/Run2016Data_pLbL0').floatParsFinal()
    sigNum=fitres.find('numLb')
    bkgNum=fitres.find('numCombBkg_Run2016Data_pLbL0')
    ptRange='ptRange30To33'

    lbl01.MakePlot_fromRooPlot(
            loadObject='figs/Run2016Data_pLbL0',
            XaxisTitle='J/#psi#Lambda^{0} Mass(GeV)',
            outputName='{range}_LbL0Dist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/Run2016Data_pLbL0',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'sig'     , 'description':'#Lambda^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.60,'xmax':0.85,'ymin':0.35,'ymax':0.50 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    fitres=lbl01.GetObj('fitRes/Run2016Data_nLbL0').floatParsFinal()
    sigNum=fitres.find('numlB')
    bkgNum=fitres.find('numCombBkg_Run2016Data_nLbL0')

    lbl01.MakePlot_fromRooPlot(
            loadObject='figs/Run2016Data_nLbL0',
            XaxisTitle='J/#psi#bar{#Lambda}^{0} Mass(GeV)',
            outputName='{range}_lBl0Dist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/Run2016Data_nLbL0',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'sig'     , 'description':'#bar{#Lambda}^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.60,'xmax':0.85,'ymin':0.35,'ymax':0.50 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    # plotBlock end }}}
    lbl02=ProcessObject('workspace_0thStep_LbL0Shape_noKinematicCut.ptRange33.38.root') # plotBlock {{{
    fitres=lbl02.GetObj('fitRes/Run2016Data_pLbL0').floatParsFinal()
    sigNum=fitres.find('numLb')
    bkgNum=fitres.find('numCombBkg_Run2016Data_pLbL0')
    ptRange='ptRange33To38'

    lbl02.MakePlot_fromRooPlot(
            loadObject='figs/Run2016Data_pLbL0',
            XaxisTitle='J/#psi#Lambda^{0} Mass(GeV)',
            outputName='{range}_LbL0Dist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/Run2016Data_pLbL0',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'sig'     , 'description':'#Lambda^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.60,'xmax':0.85,'ymin':0.35,'ymax':0.50 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    fitres=lbl02.GetObj('fitRes/Run2016Data_nLbL0').floatParsFinal()
    sigNum=fitres.find('numlB')
    bkgNum=fitres.find('numCombBkg_Run2016Data_nLbL0')

    lbl02.MakePlot_fromRooPlot(
            loadObject='figs/Run2016Data_nLbL0',
            XaxisTitle='J/#psi#bar{#Lambda}^{0} Mass(GeV)',
            outputName='{range}_lBl0Dist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/Run2016Data_nLbL0',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'sig'     , 'description':'#bar{#Lambda}^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.60,'xmax':0.85,'ymin':0.35,'ymax':0.50 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    # plotBlock end }}}
    lbl03=ProcessObject('workspace_0thStep_LbL0Shape_noKinematicCut.ptRange38.45.root') # plotBlock {{{
    fitres=lbl03.GetObj('fitRes/Run2016Data_pLbL0').floatParsFinal()
    sigNum=fitres.find('numLb')
    bkgNum=fitres.find('numCombBkg_Run2016Data_pLbL0')
    ptRange='ptRange38To45'

    lbl03.MakePlot_fromRooPlot(
            loadObject='figs/Run2016Data_pLbL0',
            XaxisTitle='J/#psi#Lambda^{0} Mass(GeV)',
            outputName='{range}_LbL0Dist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/Run2016Data_pLbL0',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'sig'     , 'description':'#Lambda^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.60,'xmax':0.85,'ymin':0.35,'ymax':0.50 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    fitres=lbl03.GetObj('fitRes/Run2016Data_nLbL0').floatParsFinal()
    sigNum=fitres.find('numlB')
    bkgNum=fitres.find('numCombBkg_Run2016Data_nLbL0')

    lbl03.MakePlot_fromRooPlot(
            loadObject='figs/Run2016Data_nLbL0',
            XaxisTitle='J/#psi#bar{#Lambda}^{0} Mass(GeV)',
            outputName='{range}_lBl0Dist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/Run2016Data_nLbL0',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'sig'     , 'description':'#bar{#Lambda}^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.60,'xmax':0.85,'ymin':0.35,'ymax':0.50 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    # plotBlock end }}}
    lbl04=ProcessObject('workspace_0thStep_LbL0Shape_noKinematicCut.ptRange45.root') # plotBlock {{{
    fitres=lbl04.GetObj('fitRes/Run2016Data_pLbL0').floatParsFinal()
    sigNum=fitres.find('numLb')
    bkgNum=fitres.find('numCombBkg_Run2016Data_pLbL0')
    ptRange='ptRange45'

    lbl04.MakePlot_fromRooPlot(
            loadObject='figs/Run2016Data_pLbL0',
            XaxisTitle='J/#psi#Lambda^{0} Mass(GeV)',
            outputName='{range}_LbL0Dist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/Run2016Data_pLbL0',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'sig'     , 'description':'#Lambda^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.60,'xmax':0.85,'ymin':0.35,'ymax':0.50 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    fitres=lbl04.GetObj('fitRes/Run2016Data_nLbL0').floatParsFinal()
    sigNum=fitres.find('numlB')
    bkgNum=fitres.find('numCombBkg_Run2016Data_nLbL0')

    lbl04.MakePlot_fromRooPlot(
            loadObject='figs/Run2016Data_nLbL0',
            XaxisTitle='J/#psi#bar{#Lambda}^{0} Mass(GeV)',
            outputName='{range}_lBl0Dist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/Run2016Data_nLbL0',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'sig'     , 'description':'#bar{#Lambda}^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.60,'xmax':0.85,'ymin':0.35,'ymax':0.50 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    # plotBlock end }}}
    lbtk0=ProcessObject('workspace_extraStep_1st_shortRangeLbFit_noKinematicCut.ptRange20.30.root') # plotBlock {{{
    fitres=lbtk0.GetObj('fitRes/LbModel').floatParsFinal()
    sigNum=fitres.find('numLb')
    bkgNum=fitres.find('numCombBkg_ShortRangeLbFit')
    ptRange='ptRange20To30'

    lbtk0.MakePlot_fromRooPlot(
            loadObject='figs/LbModel',
            XaxisTitle='J/#psi pK^{-} Mass(GeV)',
            outputName='{range}_LbTkDist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/LbModel',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'Lb'      , 'description':'#Lambda^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.20,'xmax':0.45,'ymin':0.10,'ymax':0.35 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    fitres=lbtk0.GetObj('fitRes/lBModel').floatParsFinal()
    sigNum=fitres.find('numlB')
    bkgNum=fitres.find('numCombBkg_ShortRangelBFit')

    lbtk0.MakePlot_fromRooPlot(
            loadObject='figs/lBModel',
            XaxisTitle='J/#psi #bar{p}K^{+} Mass(GeV)',
            outputName='{range}_lBTkDist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/lBModel',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'lB'      , 'description':'#bar{#Lambda}^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.20,'xmax':0.45,'ymin':0.10,'ymax':0.35 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    # plotBlock end }}}
    lbtk1=ProcessObject('workspace_extraStep_1st_shortRangeLbFit_noKinematicCut.ptRange30.33.root') # plotBlock {{{
    fitres=lbtk1.GetObj('fitRes/LbModel').floatParsFinal()
    sigNum=fitres.find('numLb')
    bkgNum=fitres.find('numCombBkg_ShortRangeLbFit')
    ptRange='ptRange30To33'

    lbtk1.MakePlot_fromRooPlot(
            loadObject='figs/LbModel',
            XaxisTitle='J/#psi pK^{-} Mass(GeV)',
            outputName='{range}_LbTkDist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/LbModel',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'Lb'      , 'description':'#Lambda^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.20,'xmax':0.45,'ymin':0.10,'ymax':0.35 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    fitres=lbtk1.GetObj('fitRes/lBModel').floatParsFinal()
    sigNum=fitres.find('numlB')
    bkgNum=fitres.find('numCombBkg_ShortRangelBFit')

    lbtk1.MakePlot_fromRooPlot(
            loadObject='figs/lBModel',
            XaxisTitle='J/#psi #bar{p}K^{+} Mass(GeV)',
            outputName='{range}_lBTkDist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/lBModel',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'lB'      , 'description':'#bar{#Lambda}^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.20,'xmax':0.45,'ymin':0.10,'ymax':0.35 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    # plotBlock end }}}
    lbtk2=ProcessObject('workspace_extraStep_1st_shortRangeLbFit_noKinematicCut.ptRange33.38.root') # plotBlock {{{
    fitres=lbtk2.GetObj('fitRes/LbModel').floatParsFinal()
    sigNum=fitres.find('numLb')
    bkgNum=fitres.find('numCombBkg_ShortRangeLbFit')
    ptRange='ptRange33To38'

    lbtk2.MakePlot_fromRooPlot(
            loadObject='figs/LbModel',
            XaxisTitle='J/#psi pK^{-} Mass(GeV)',
            outputName='{range}_LbTkDist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/LbModel',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'Lb'      , 'description':'#Lambda^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.20,'xmax':0.45,'ymin':0.10,'ymax':0.35 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    fitres=lbtk2.GetObj('fitRes/lBModel').floatParsFinal()
    sigNum=fitres.find('numlB')
    bkgNum=fitres.find('numCombBkg_ShortRangelBFit')

    lbtk2.MakePlot_fromRooPlot(
            loadObject='figs/lBModel',
            XaxisTitle='J/#psi #bar{p}K^{+} Mass(GeV)',
            outputName='{range}_lBTkDist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/lBModel',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'lB'      , 'description':'#bar{#Lambda}^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.20,'xmax':0.45,'ymin':0.10,'ymax':0.35 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    # plotBlock end }}}
    lbtk3=ProcessObject('workspace_extraStep_1st_shortRangeLbFit_noKinematicCut.ptRange38.45.root') # plotBlock {{{
    fitres=lbtk3.GetObj('fitRes/LbModel').floatParsFinal()
    sigNum=fitres.find('numLb')
    bkgNum=fitres.find('numCombBkg_ShortRangeLbFit')
    ptRange='ptRange38To45'

    lbtk3.MakePlot_fromRooPlot(
            loadObject='figs/LbModel',
            XaxisTitle='J/#psi pK^{-} Mass(GeV)',
            outputName='{range}_LbTkDist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/LbModel',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'Lb'      , 'description':'#Lambda^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.20,'xmax':0.45,'ymin':0.10,'ymax':0.35 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    fitres=lbtk3.GetObj('fitRes/lBModel').floatParsFinal()
    sigNum=fitres.find('numlB')
    bkgNum=fitres.find('numCombBkg_ShortRangelBFit')

    lbtk3.MakePlot_fromRooPlot(
            loadObject='figs/lBModel',
            XaxisTitle='J/#psi #bar{p}K^{+} Mass(GeV)',
            outputName='{range}_lBTkDist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/lBModel',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'lB'      , 'description':'#bar{#Lambda}^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.20,'xmax':0.45,'ymin':0.10,'ymax':0.35 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    # plotBlock end }}}
    lbtk4=ProcessObject('workspace_extraStep_1st_shortRangeLbFit_noKinematicCut.ptRange45.root') # plotBlock {{{
    fitres=lbtk4.GetObj('fitRes/LbModel').floatParsFinal()
    sigNum=fitres.find('numLb')
    bkgNum=fitres.find('numCombBkg_ShortRangeLbFit')
    ptRange='ptRange45'

    lbtk4.MakePlot_fromRooPlot(
            loadObject='figs/LbModel',
            XaxisTitle='J/#psi pK^{-} Mass(GeV)',
            outputName='{range}_LbTkDist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/LbModel',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'Lb'      , 'description':'#Lambda^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.20,'xmax':0.45,'ymin':0.10,'ymax':0.35 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    fitres=lbtk4.GetObj('fitRes/lBModel').floatParsFinal()
    sigNum=fitres.find('numlB')
    bkgNum=fitres.find('numCombBkg_ShortRangelBFit')

    lbtk4.MakePlot_fromRooPlot(
            loadObject='figs/lBModel',
            XaxisTitle='J/#psi #bar{p}K^{+} Mass(GeV)',
            outputName='{range}_lBTkDist_noKinematicCut'.format(range=ptRange),
            addInfo=[
                { 'function': PullDistributionModule,
                    'ipVar':
                    {
                        'frameName':'figs/lBModel',
                        'numOfRegion':1,
                        'dataName':'data',
                    },
                },
                { 'function': LegendInfoModule,
                    'ipVar':
                    {
                        'entry': [
                            { 'objName': 'data'    , 'description':'2016 full data' },
                            { 'objName': 'totModel', 'description':'totalFit' },
                            { 'objName': 'lB'      , 'description':'#bar{#Lambda}^{0}_{b} signal' },
                            ],
                        'axisOpt': { 'xmin':0.20,'xmax':0.45,'ymin':0.10,'ymax':0.35 },
                        'Columns': 1,
                    },
                },
                { 'function': TextInfoModule,
                    'ipVar':
                    {
                        'axisOpt': { 'xmin':0.20,'xmax':0.85,'ymin':0.55,'ymax':0.80 },
                        'content': [
                            # 2nd poly caused yield
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'sig yield: {mean:.2E} #pm {err:.2E}'.format(mean=sigNum.getVal(),err=sigNum.getError())}
                            },
                            { 'function':LineTextFunction, 'ipVar':
                                {'word':'bkg yield: {mean:.2E} #pm {err:.2E}'.format(mean=bkgNum.getVal(),err=bkgNum.getError())}
                            },
                            { 'function':ChiSquareTextFunction, 'ipVar':{'data':'data','PDF':'totModel'} },
                            ]
                    },
                },
            ],
        )
    # plotBlock end }}}
#workspace_0thStep_LbL0Shape_noKinematicCut.ptRange30.33.root
#workspace_0thStep_LbL0Shape_noKinematicCut.ptRange33.38.root
#workspace_0thStep_LbL0Shape_noKinematicCut.ptRange38.45.root
#workspace_0thStep_LbL0Shape_noKinematicCut.ptRange45.root
#workspace_extraStep_1st_shortRangeLbFit_noKinematicCut.ptRange30.33.root
#workspace_extraStep_1st_shortRangeLbFit_noKinematicCut.ptRange33.38.root
#workspace_extraStep_1st_shortRangeLbFit_noKinematicCut.ptRange38.45.root
#workspace_extraStep_1st_shortRangeLbFit_noKinematicCut.ptRange45.root
