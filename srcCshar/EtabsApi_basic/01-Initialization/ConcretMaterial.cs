using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
  public  class ConcretMaterial:MaterialProperties
    {
        #region Properites
        public double Fc { get; set; }
        public double FcsFactor { get; set; }
        public double StrainAtFc { get; set; }
        public double StrainUltimat { get; set; }
        public bool IsLightWeight { get; set; }

        #endregion
        #region Constructor
        public ConcretMaterial(cSapModel _mySapModel,eMatType type,string _name,double _density,double Fc, 
            double _Fcs_Factor , int SSType,int SSHys_Type,double _StrainAtFc,double _StrainUltimat,bool _IsLightWeight) :base(_mySapModel,type)
            
        {
            this.Fc = Fc;
            this.FcsFactor = _Fcs_Factor;
            this.density = _density;
            this.name = _name;
            this.StrainAtFc = _StrainAtFc;
            this.StrainUltimat = _StrainUltimat;
            this.IsLightWeight = IsLightWeight;


            int ret = MySapModel.PropMaterial.SetMaterial(_name, eMatType.Concrete);

            //assign material property weight per unit volume
            ret = MySapModel.PropMaterial.SetWeightAndMass(_name, 1, _density);

            ret = MySapModel.PropMaterial.SetOConcrete(_name, Fc, _IsLightWeight, _Fcs_Factor, SSType, SSHys_Type, 0, 0);
        }
        public ConcretMaterial(cSapModel _mySapModel,string _name,double _density,double E, double U, double A):base(_mySapModel,eMatType.Concrete,_name,E,U,A,_density)
        {
            // intialize concrete material
            int ret = MySapModel.PropMaterial.SetMaterial(_name, eMatType.Concrete);

            //assign material property weight per unit volume
            ret = MySapModel.PropMaterial.SetWeightAndMass(_name, 1, _density);

            //'assign isotropic mechanical properties
            ret = _mySapModel.PropMaterial.SetMPIsotropic(_name, E, U,A);
        }
        #endregion
    }
}
