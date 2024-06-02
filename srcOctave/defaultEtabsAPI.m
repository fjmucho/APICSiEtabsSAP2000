%% clean-up the workspace & command window
clear; clc;

%%set the following flag to true to attach to an existing instance of the program otherwise a new instance of the program will be started
AttachToInstance = false(); % true(); %#

%% set the following flag to true to manually specify the path to ETABS.exe
%% this allows for a connection to a version of ETABS other than the latest installation
%% otherwise the latest installed version of ETABS will be launched
SpecifyPath = false(); % true(); %

%% if the above flag is set to true, specify the path to ETABS below
ProgramPath = 'C:\\Program Files\\Computers and Structures\\ETABS 18\\ETABS.exe';

%% full path to API dll
%% set it to the installation folder
APIDLLPath = 'C:\\Program Files\\Computers and Structures\\ETABS 18\\ETABSv1.dll';

%% full path to the model
%% set it to the desired path of your model
ModelDirectory = 'C:\\CSi_ETABS_API_Example';
if ~exist(ModelDirectory, 'dir')
    mkdir(ModelDirectory);
end
ModelName = 'API_1-001.edb';
ModelPath = strcat(ModelDirectory, filesep, ModelName);

%% create API helper object
a = NET.addAssembly(APIDLLPath);
helper = ETABSv1.Helper;
helper = NET.explicitCast(helper,'ETABSv1.cHelper');

if AttachToInstance
    %% attach to a running instance of ETABS
    ETABSObject = helper.GetObject('CSI.ETABS.API.ETABSObject');
    ETABSObject = NET.explicitCast(ETABSObject,'ETABSv1.cOAPI');
else
    if SpecifyPath
        %% create an instance of the ETABS object from the specified path
        ETABSObject = helper.CreateObject(ProgramPath);
    else
        %% create an instance of the ETABS object from the latest installed ETABS
        ETABSObject = helper.CreateObjectProgID('CSI.ETABS.API.ETABSObject');
    end
    ETABSObject = NET.explicitCast(ETABSObject,'ETABSv1.cOAPI');
    
    %% start ETABS application
    ETABSObject.ApplicationStart;
end
helper = 0;

%% create SapModel object
SapModel = NET.explicitCast(ETABSObject.SapModel,'ETABSv1.cSapModel');

%% initialize model
ret = SapModel.InitializeNewModel;

%% create new blank model
File = NET.explicitCast(SapModel.File,'ETABSv1.cFile');
ret = File.NewBlank;

%% define material property
PropMaterial = NET.explicitCast(SapModel.PropMaterial,'ETABSv1.cPropMaterial');
ret = PropMaterial.SetMaterial('CONC', ETABSv1.eMatType.Concrete);

%% assign isotropic mechanical properties to material
ret = PropMaterial.SetMPIsotropic('CONC', 3600, 0.2, 0.0000055);

%% define rectangular frame section property
PropFrame = NET.explicitCast(SapModel.PropFrame,'ETABSv1.cPropFrame');
ret = PropFrame.SetRectangle('R1', 'CONC', 12, 12);

%% define frame section property modifiers
ModValue = NET.createArray('System.Double',8);
for i = 1 : 8
    ModValue(i) = 1;
end
ModValue(1) = 1000;
ModValue(2) = 0;
ModValue(3) = 0;
ret = PropFrame.SetModifiers('R1', ModValue);

%% switch to k-ft units
ret = SapModel.SetPresentUnits(ETABSv1.eUnits.kip_ft_F);

%% add frame object by coordinates
FrameObj = NET.explicitCast(SapModel.FrameObj,'ETABSv1.cFrameObj');
FrameName1 = System.String(' ');
FrameName2 = System.String(' ');
FrameName3 = System.String(' ');
[ret, FrameName1] = FrameObj.AddByCoord(0, 0, 0, 0, 0, 10, FrameName1, 'R1', '1', 'Global');
[ret, FrameName2] = FrameObj.AddByCoord(0, 0, 10, 8, 0, 16, FrameName2, 'R1', '2', 'Global');
[ret, FrameName3] = FrameObj.AddByCoord(-4, 0, 10, 0, 0, 10, FrameName3, 'R1', '3', 'Global');

%% assign point object restraint at base
PointObj = NET.explicitCast(SapModel.PointObj,'ETABSv1.cPointObj');
PointName1 = System.String(' ');
PointName2 = System.String(' ');
Restraint = NET.createArray('System.Boolean',6);
for i = 1 : 4
    Restraint(i) = true();
end
for i = 5 : 6
    Restraint(i) = false();
end
[ret, PointName1, PointName2] = FrameObj.GetPoints(FrameName1, PointName1, PointName2);
ret = PointObj.SetRestraint(PointName1, Restraint);

%% assign point object restraint at top
for i = 1 : 2
    Restraint(i) = true();
end
for i = 3 : 6
    Restraint(i) = false();
end
[ret, PointName1, PointName2] = FrameObj.GetPoints(FrameName2, PointName1, PointName2);
ret = PointObj.SetRestraint(PointName2, Restraint);

%% refresh view, update (initialize) zoom
View = NET.explicitCast(SapModel.View,'ETABSv1.cView');
ret = View.RefreshView(0, false());

%% add load patterns
LoadPatterns = NET.explicitCast(SapModel.LoadPatterns,'ETABSv1.cLoadPatterns');
ret = LoadPatterns.Add('1', ETABSv1.eLoadPatternType.Other, 1, true());
ret = LoadPatterns.Add('2', ETABSv1.eLoadPatternType.Other, 0, true());
ret = LoadPatterns.Add('3', ETABSv1.eLoadPatternType.Other, 0, true());
ret = LoadPatterns.Add('4', ETABSv1.eLoadPatternType.Other, 0, true());
ret = LoadPatterns.Add('5', ETABSv1.eLoadPatternType.Other, 0, true());
ret = LoadPatterns.Add('6', ETABSv1.eLoadPatternType.Other, 0, true());
ret = LoadPatterns.Add('7', ETABSv1.eLoadPatternType.Other, 0, true());

%% assign loading for load pattern 2
[ret, PointName1, PointName2] = FrameObj.GetPoints(FrameName3, PointName1, PointName2);
PointLoadValue = NET.createArray('System.Double',6);
for i = 1 : 6
    PointLoadValue(i) = 0.0;
end
PointLoadValue(3) = -10;
ret = PointObj.SetLoadForce(PointName1, '2', PointLoadValue);
ret = FrameObj.SetLoadDistributed(FrameName3, '2', 1, 10, 0, 1, 1.8, 1.8);

%% assign loading for load pattern 3
[ret, PointName1, PointName2] = FrameObj.GetPoints(FrameName3, PointName1, PointName2);
for i = 1 : 6
    PointLoadValue(i) = 0.0;
end
PointLoadValue(3) = -17.2;
PointLoadValue(5) = -54.4;
ret = PointObj.SetLoadForce(PointName2, '3', PointLoadValue);

%% assign loading for load pattern 4
ret = FrameObj.SetLoadDistributed(FrameName2, '4', 1, 11, 0, 1, 2, 2);

%% assign loading for load pattern 5
ret = FrameObj.SetLoadDistributed(FrameName1, '5', 1, 2, 0, 1, 2, 2, 'Local');
ret = FrameObj.SetLoadDistributed(FrameName2, '5', 1, 2, 0, 1, -2, -2, 'Local');

%% assign loading for load pattern 6
ret = FrameObj.SetLoadDistributed(FrameName1, '6', 1, 2, 0, 1, 0.9984, 0.3744, 'Local');
ret = FrameObj.SetLoadDistributed(FrameName2, '6', 1, 2, 0, 1, -0.3744, 0, 'Local');

%% assign loading for load pattern 7
ret = FrameObj.SetLoadPoint(FrameName2, '7', 1, 2, 0.5, -15, 'Local');

%% switch to k-in units
ret = SapModel.SetPresentUnits(ETABSv1.eUnits.kip_in_F);

%% save model
ret = File.Save(ModelPath);

%% run model (this will create the analysis model)
Analyze = NET.explicitCast(SapModel.Analyze,'ETABSv1.cAnalyze');
ret = Analyze.RunAnalysis();

%% initialize for ETABS results
ETABSResult = zeros(7,1,'double');
[ret, PointName1, PointName2] = FrameObj.GetPoints(FrameName2, PointName1, PointName2);

%% get ETABS results for load cases 1 through 7
AnalysisResults = NET.explicitCast(SapModel.Results,'ETABSv1.cAnalysisResults');
AnalysisResultsSetup = NET.explicitCast(AnalysisResults.Setup,'ETABSv1.cAnalysisResultsSetup');

for i = 1 : 7
    NumberResults = 0;
    Obj = NET.createArray('System.String',2);
    Elm = NET.createArray('System.String',2);
    ACase = NET.createArray('System.String',2);
    StepType = NET.createArray('System.String',2);
    StepNum = NET.createArray('System.Double',2);
    U1 = NET.createArray('System.Double',2);
    U2 = NET.createArray('System.Double',2);
    U3 = NET.createArray('System.Double',2);
    R1 = NET.createArray('System.Double',2);
    R2 = NET.createArray('System.Double',2);
    R3 = NET.createArray('System.Double',2);
    ret = AnalysisResultsSetup.DeselectAllCasesAndCombosForOutput;
    ret = AnalysisResultsSetup.SetCaseSelectedForOutput(int2str(i));
    if i <= 4
        [ret, NumberResults, Obj, Elm, ACase, StepType, StepNum, U1, U2, U3, R1, R2,    R3] = AnalysisResults.JointDispl(PointName2, ETABSv1.eItemTypeElm.ObjectElm, NumberResults, Obj, Elm, ACase, StepType, StepNum, U1, U2, U3, R1, R2, R3);
        ETABSResult(i) = U3(1);
    else
        [ret, NumberResults, Obj, Elm, ACase, StepType, StepNum, U1, U2, U3, R1, R2, R3] = AnalysisResults.JointDispl(PointName1, ETABSv1.eItemTypeElm.ObjectElm, NumberResults, Obj, Elm, ACase, StepType, StepNum, U1, U2, U3, R1, R2, R3);
        ETABSResult(i) = U1(1);
    end
end

%% close ETABS
ret = ETABSObject.ApplicationExit(false());
File = 0;
PropMaterial = 0;
PropFrame = 0;
FrameObj = 0;
PointObj = 0;
View = 0;
LoadPatterns = 0;
Analyze = 0;
AnalysisResults = 0;
AnalysisResultsSetup = 0;
SapModel = 0;
ETABSObject = 0;

%% fill independent results
IndResult = zeros(7,1,'double');
IndResult(1) = -0.02639;
IndResult(2) = 0.06296;
IndResult(3) = 0.06296;
IndResult(4) = -0.2963;
IndResult(5) = 0.3125;
IndResult(6) = 0.11556;
IndResult(7) = 0.00651;

%% fill percent difference
PercentDiff = zeros(7,1,'double');
for i = 1 : 7
    PercentDiff(i) = (ETABSResult(i) / IndResult(i)) - 1;
end

%% display results
ETABSResult
IndResult
PercentDiff