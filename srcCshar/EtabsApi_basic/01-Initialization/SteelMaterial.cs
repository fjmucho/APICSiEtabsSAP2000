using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public class SteelMaterial:MaterialProperties
    {
        #region Properites
        public double poissonRatio { get; set; }
        public double shearModulus { get; set; }
        public double yieldStrength { get; set; }
        public double ultimateStrength { get; set; }
        #endregion

        #region Constructor
        public SteelMaterial(cSapModel _mySapModel, eMatType _type, string _name, double _youngsModulus, double _thermalCoeff, double _unitWeight, double _unitMass, double _poissonRatio, double _shearModulus, double _yieldStrength, double _ultimateStrength)
            : base(_mySapModel, _type, _name, _youngsModulus, _thermalCoeff, _unitWeight, _unitMass)
        {
            poissonRatio = _poissonRatio;
            shearModulus = _shearModulus;
            yieldStrength = _yieldStrength;
            ultimateStrength = _ultimateStrength;
        }
        #endregion
    }
}
