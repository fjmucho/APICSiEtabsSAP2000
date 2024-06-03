
using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public class FrameElement:Element
    {
        public Point startPoint { get; set; }
        public Point endPoint { get; set; }
        public CSys cSys { get; set; }
        public FrameSection frameSection { get; set; }
        public double[] p { get; set; }
        public double[] v2 { get; set; }
        public double[] v2_envMax { get; set; }
        public double[] v2_envMin { get; set; }
        public double[] v3 { get; set; }
        public double[] t { get; set; }
        public double[] m2 { get; set; }
        public double[] m3 { get; set; }
        public double[] m3_envMax { get; set; }
        public double[] m3_envMin { get; set; }

        public double[] resultsStations { get; set; }
        public List<double> areaSteel { get; set; }
        public List<double> areaSteel_envMax { get; set; }
        public List<double> areaSteel_envMin { get; set; }
        public List<double> shearSteel { get; set; }
        public List<double> shearSteel_envMax { get; set; }
        public List<double> shearSteel_envMin { get; set; }
        public List<double> c1 { get; set; }
        public List<double> c1_envMax { get; set; }
        public List<double> c1_envMin { get; set; }
        public List<double> j { get; set; }
        public List<double> j_envMax { get; set; }
        public List<double> j_envMin { get; set; }
        public List<double> shearStress { get; set; }

        // no getter or setter propeties
        string temp1 = "";
        string temp2 = "";
        string temp3 = "";
        string sectionName;
        public FrameElement(cSapModel _mySapModel, double _xStart, double _ystart, double _zStart, double _xEnd, double _yEnd, 
            double _zEnd, FrameSection _frameSection , string _name , string _userName="", CSys _cSys = CSys.Global) : 
            base(_mySapModel, _name,_userName)
        {
            frameSection = _frameSection;
            startPoint = new Point();
            endPoint = new Point();
            startPoint.x = _xStart;
            startPoint.y = _ystart;
            startPoint.z = _zStart;
            endPoint.x = _xEnd;
            endPoint.y = _yEnd;
            endPoint.z = _zEnd;
            cSys = _cSys;
    

            if (frameSection == null)
            {
                sectionName = "None";
            }
            else
            {
                sectionName = frameSection.name;
            }

            temp1 = name;
            temp2 = "";
            temp3 = "";

            int ret  = mySapModel.FrameObj.AddByCoord(startPoint.x, startPoint.y, startPoint.z, endPoint.x, endPoint.y, endPoint.z, 
                ref temp1, sectionName, "",cSys.ToString());
            name = temp1;
          

            // Set names of points
            mySapModel.FrameObj.GetPoints(name, ref temp2, ref temp3);
            startPoint.name = temp2;
            endPoint.name = temp3;

        }

        public FrameElement(cSapModel _mySapModel, Point _startPoint, Point _endPoint, FrameSection _frameSection, string _name  ,CSys _cSys = CSys.Global, string _userName="" ) : 
            this(_mySapModel, _startPoint.x, _startPoint.y, _startPoint.z, _endPoint.x, _endPoint.y, _endPoint.z, _frameSection, _name, _userName, _cSys)
        { }
        //Constructor for existing frame with section in ETABS (No creation for frame in etabs, just to set P,M2,M3,N)


        #region Methods
        public void RotateLocalAxes(double rotationAngel)
        {
            mySapModel.FrameObj.SetLocalAxes(name, rotationAngel, eItemType.Objects);
        }

        public override int elementModifire(ref double[] modifiresValues)
        {
            int ret = mySapModel.FrameObj.SetModifiers(name, ref modifiresValues);
            return ret;
        }
        #endregion
    }
}
