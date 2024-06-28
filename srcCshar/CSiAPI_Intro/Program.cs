using System;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// using SAP2000v1;
// using EtabsApi;
using CSiAPIv1;

namespace CSiAPI_Intro
{
    class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine("Hello World!");
            cOAPI sapObject = null;
            cSapModel smodel = null;
            int ret = -1;

            //attach to a running instance of ETABS 
            try
            {
                // sapObejct = (cOAPI)System.Runtime.InteropServices.Marshal.GetActiveObject("CSI.SAP2000.API.SapObject");
                sapObject = (cOAPI)System.Runtime.InteropServices.Marshal.GetActiveObject("CSI.ETABS.API.ETABSObject");
                // sapObject = (ETABSv1.cOAPI)System.Runtime.InteropServices.Marshal.GetActiveObject("CSI.ETABS.API.ETABSObject");
            } 
            catch (Exception ex) 
            {
                MessageBox.Show("No running instance of the program found or failed to attach.");
                return;
            }
            smodel = sapObject.SapModel;

            smodel.InitializeNewModel(eUnits.kN_m_C);

            smodel.File.NewBlank();

            string frameName = string.Empty;
            string point1 = string.Empty;
            string point2 = string.Empty;
            string strDummy = string.Empty;

            smodel.FrameObj.AddByCoord(0, 0, 0, 0, 0, 3, ref frameName);
            smodel.FrameObj.GetPoints(frameName, ref point1, ref strDummy);

            smodel.FrameObj.AddByCoord(6, 0, 0, 6, 0, 3, ref frameName);
            smodel.FrameObj.GetPoints(frameName, ref point2, ref strDummy);

            smodel.FrameObj.AddByCoord(0, 0, 3, 6, 0, 3, ref frameName);

            bool[] restr = { true, true, true, true, true, true };
            smodel.Pointobj.SetRestraint(point1, ref restr);
            smodel.Pointobj.SetRestraint(point2, ref restr);

            string lpName = "Test";

            // 1 = Force per unit length
            // 2 = Moment per unit length
            // smodel.FrameObj.SetLoadDistributed(FrameName, "DEAD", 1, 10, 0.0, 1.0, 15.0, 5.0);
            smodel.FrameObj.SetLoadDistributed(frameName, lpName, 1, 10, 0.0, 1.0, 15.0, 5.0);

            smodel.View.RefreshView();

            // Compara ...
            smodel.File.Save(@"C:\\CSi_ETABS_API_Example\test.edb");

        // una ves ejecutado una primera vez ya se peude 
        // comentar de la linia 26 a 56 y descomentar 60 a 63
            // smodel.SetModelIsLocked(false);
            // for (int i = 1, i<3; i++) {
            //     smodel.FrameObj.SetEndLengthOffset(i.ToString(), flase, 0.0, 0.0, 0.0);
            // }

            // 'run analysis
            smodel.Analyze.RunAnalysis();

            // 'deselect all cases and combos
            smodel.Results.Setup.DeselectAllCasesAndCombosForOutput();
            // 'check if case is selected
            smodel.Results.Setup.SetCaseSelectedForOutput(lpName);

            // // 'get frame forces
            // int NumberResults = 0;
            // string[] Obj = null;
            // double[] ObjSta = null;
            // string[] Elm = null;
            // double[] ElmSta = null;
            // string[] LoadCase = null;
            // string[] StepType = null;
            // double[] StepNum = null;
            // double[] P = null;
            // double[] V2 = null;
            // double[] V3 = null;
            // double[] T = null;
            // double[] M2 = null;
            // double[] M3 = null;
            // smodel.Results.FrameForce("All", eItemTypeElm.GroupElm, ref NumberResults,
            //     ref Obj, ref ObjSta, ref Elm, ref ElmSta, ref LoadCase, ref StepType, ref StepNum,
            //     ref P, ref V2, ref V3, ref T, ref M2, ref M3);

            // // ...
            // Console.WriteLine("Mesage de salida");
            // Console.WriteLine("mesnage1\tmensage2\tmensage3");
            // for (int i=0; i<NumberResults; i++) {
            //     Console.WriteLine($"{Obj[i]}\t{ObjSta[i]}\t{Math.Round(M3[i], 2)}");
            // }

            Console.ReadKey();
        }
        
    }
}