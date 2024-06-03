using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
    public class Grid
    {
        //create API helper object
        ETABSv17.cHelper myHelper;
        public Grid()
        {
           /// myHelper = new ETABSv17.Helper();
        }
        public static int GetGridSys(string gridName)
        {

            //create etabs object 
            ETABSv17.cHelper myHelper = new ETABSv17.Helper();
            ETABSv17.cOAPI myETABSObject = myHelper.CreateObjectProgID("CSI.ETABS.API.ETABSObject");
            //ETABSv17.cOAPI myETABSObject = myHelper.CreateObject(ProgramPath);
            var mySapModel = myETABSObject.SapModel;

            //start ETABS application
            int ret = myETABSObject.ApplicationStart();
            //Get a reference to cSapModel to access all API classes and functions
            // ETABSv17.cSapModel mySapModel = default(ETABSv17.cSapModel);
            mySapModel = myETABSObject.SapModel;
            //Initialize model
            ret = mySapModel.InitializeNewModel(eUnits.Ton_m_C);
       
            double X0 = 0;
            double Y0 = 0;
            double RZ = 0;
            string gridSystemType = "";
            int NX = 0;
            int NY = 0;
            string[] GridLineIDX = null;
            string[] GridLineIDY = null;
            double[] ordinatX = null;
            double[] oredinatY = null;
            bool[] VisibleX = null;
            bool[] VisibleY = null;
            string[] BubbleLocX = null;
            string[] BubbleLocY = null;
            ret = mySapModel.GridSys.GetGridSys_2("G1", ref X0, ref Y0, ref RZ, ref gridSystemType, ref NX, ref NY, ref GridLineIDX, ref GridLineIDY, ref ordinatX,
               ref oredinatY, ref VisibleX, ref VisibleY, ref BubbleLocX, ref BubbleLocY);

            return ret;
        } 

        public static int DrawGridSys(int StoryN, double storyHieghtTypical, double storyHieghtBottom, 
            int nLineX, int nLineY, double xSpacing, int ySpacing, eUnits unitType)
        {
            //create etabs object 
            ETABSv17.cHelper myHelper = new ETABSv17.Helper();
            ETABSv17.cOAPI myETABSObject = myHelper.CreateObjectProgID("CSI.ETABS.API.ETABSObject");
            //ETABSv17.cOAPI myETABSObject = myHelper.CreateObject(ProgramPath);
            var mySapModel = myETABSObject.SapModel;

            //start ETABS application
            int ret = myETABSObject.ApplicationStart();
            //Get a reference to cSapModel to access all API classes and functions
            // ETABSv17.cSapModel mySapModel = default(ETABSv17.cSapModel);
            mySapModel = myETABSObject.SapModel;
            //Initialize model
            ret = mySapModel.InitializeNewModel(eUnits.Ton_m_C);
            ret = mySapModel.File.NewGridOnly( StoryN,  storyHieghtTypical,  storyHieghtBottom,  nLineX,  nLineY,  xSpacing,  ySpacing);
            return ret;

        }
    }
}
