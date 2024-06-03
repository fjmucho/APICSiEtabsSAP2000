
using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public class AssignLoadOnPoint: AssignLoad
    {
        public Point[] points { get; set; }
        public double f1 { get; set; }
        public double f2 { get; set; }
        public double f3 { get; set; }
        public double m1 { get; set; }
        public double m2 { get; set; }
        public double m3 { get; set; }
        public AssignLoadOnPoint(cSapModel _mySapModel, LoadPattern _loadPattern, Point _point, double _f1 = 0, double _f2 = 0, double _f3 = 0, double _m1 = 0, double _m2 = 0, double _m3 = 0, CSys _cSys = CSys.Global, bool _replaceAssignedLoad = true) : base(_mySapModel, _loadPattern, _cSys, _replaceAssignedLoad)
        {
            f1 = _f1;
            f2 = _f2;
            f3 = _f3;
            m1 = _m1;
            m2 = _m2;
            m3 = _m3;
            points = new Point[1];
            points[0] = _point;
            double[] arrayOfLoads = { f1, f2, f3, m1, m2, m3 };

            mySapModel.PointObj.SetLoadForce(points[0].name, loadPattern.name, ref arrayOfLoads, replaceAssignedLoad, cSys.ToString(), eItemType.Objects);
        }
        public AssignLoadOnPoint(cSapModel _mySapModel, LoadPattern _loadPattern, Point[] _points, double _f1 = 0, double _f2 = 0, double _f3 = 0, double _m1 = 0, double _m2 = 0, double _m3 = 0, CSys _cSys = CSys.Global, bool _replaceAssignedLoad = true) : base(_mySapModel, _loadPattern, _cSys, _replaceAssignedLoad)
        {
            f1 = _f1;
            f2 = _f2;
            f3 = _f3;
            m1 = _m1;
            m2 = _m2;
            m3 = _m3;
            points = new Point[_points.Length];
            points = _points;
            double[] arrayOfLoads = { f1, f2, f3, m1, m2, m3 };
            for (int i = 0; i < points.Length; i++)
            {
                mySapModel.PointObj.SetLoadForce(points[i].name, loadPattern.name, ref arrayOfLoads, replaceAssignedLoad, cSys.ToString(), eItemType.Objects);
            }
        }
    }
}
