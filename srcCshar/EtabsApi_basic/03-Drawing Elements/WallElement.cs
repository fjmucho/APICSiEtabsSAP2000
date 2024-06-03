using ETABSv17;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EtabsApi
{
  public  class WallElement:Element
    {
        public List<Point> coordinats { get; set; }

        double[] x;
        double[] y;
        double[] z;
        string temp1 = "";

        public WallElement(cSapModel _mySapModel, string _name,List<Point> _coordinats, WallSection section,string _userName="") :base(_mySapModel,_name,_userName)
        {
            name = _name;
            coordinats = _coordinats;
            x = new double[coordinats.Count];
            y = new double[coordinats.Count];
            z = new double[coordinats.Count];
            for (int i = 0; i < _coordinats.Count; i++)
            {
                x[i] = _coordinats[i].x;
                y[i] = _coordinats[i].y;
                z[i] = _coordinats[i].z;
            }
            temp1 = name;
            int ret = _mySapModel.AreaObj.AddByCoord(_coordinats.Count, ref x, ref y, ref z, ref temp1, section.name, "", CSys.Global.ToString());  ;
        }

        public override int elementModifire(ref double[] modifiresValues)
        {
            int ret = mySapModel.AreaObj.SetModifiers(name, ref modifiresValues);
            return ret;
        }
    }
}
