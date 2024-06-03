using ETABSv17;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EtabsApi
{
    public class Diaphragm :EtabsCore
    {
        public string name { get; set; }
        public bool semi_rigid { get; set; } // true id the diaphram is semi rigid and false otherwise

        public Diaphragm(cSapModel _mySapModel,string _name,bool _semi_rigid):base(_mySapModel)
        {
            name = _name;
            semi_rigid = _semi_rigid;
            int ret = _mySapModel.Diaphragm.SetDiaphragm(name, semi_rigid);
        }

    }
}
