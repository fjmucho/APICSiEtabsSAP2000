
using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public class FrameAnalysisResult: AnalysisResult
    {
        public FrameElement[] frames { get; set; }
        // no getter or setter
        int noOfResults = 0;
        string[] objectName;
        string[] loadCaseName;
        double[] objSta;
        string[] elementName;
        double[] elmSta;
        string[] stepType;
        double[] stepNumber;
        double[] temp1;
        double[] temp2;
        double[] temp3;
        double[] temp4;
        double[] temp5;
        double[] temp6;
        public FrameAnalysisResult(cSapModel _mySapModel, LoadPattern _loadCase, FrameElement[] _frames) : base(_mySapModel, _loadCase)
        {
            frames = _frames;
            for (int i = 0; i < frames.Length; i++)
            {
                mySapModel.Results.FrameForce(frames[i].name, eItemTypeElm.ObjectElm, ref noOfResults, ref objectName, ref objSta, ref elementName, ref elmSta, ref loadCaseName, ref stepType, ref stepNumber, ref temp1, ref temp2, ref temp3, ref temp4, ref temp5, ref temp6);
                frames[i].p = temp1;
                frames[i].v2 = temp2;
                frames[i].v3 = temp3;
                frames[i].t = temp4;
                frames[i].m2 = temp5;
                frames[i].m3 = temp6;
                frames[i].resultsStations = objSta;
            }
        }
        public FrameAnalysisResult(cSapModel _mySapModel, LoadCombination _loadCombination, FrameElement[] _frames) : base(_mySapModel, _loadCombination)
        {
            frames = _frames;

            for (int i = 0; i < frames.Length; i++)
            {
                mySapModel.Results.FrameForce(frames[i].name, eItemTypeElm.ObjectElm, ref noOfResults, ref objectName, ref objSta, ref elementName, ref elmSta, ref loadCaseName, ref stepType, ref stepNumber, ref temp1, ref temp2, ref temp3, ref temp4, ref temp5, ref temp6);
                frames[i].p = temp1;
                frames[i].v2 = temp2;
                frames[i].v3 = temp3;
                frames[i].t = temp4;
                frames[i].m2 = temp5;
                frames[i].m3 = temp6;
            }
        }
    }
}
