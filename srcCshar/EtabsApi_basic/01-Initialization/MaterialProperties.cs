using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public class MaterialProperties:EtabsCore
    {
        #region Properties
        public eMatType type { get; set; }
        public string name { get; set; }
        public double E { get; set; }
        public double U { get; set; }
        public double A { get; set; }
        public double density { get; set; }
        #endregion

        #region Constructor
        public MaterialProperties(cSapModel _mySapModel, eMatType _type, string _name, double _E, double _U, double _A, double _density) :base(_mySapModel)
        {
            type = _type;
            name = _name;
            E = _E;
            U = _U;
            A = _A;
            density = _density;
        }
        public MaterialProperties(cSapModel _mySapModel, eMatType _type):base(_mySapModel)
        {
            type = _type;
        }

        
        #endregion
    }
}
