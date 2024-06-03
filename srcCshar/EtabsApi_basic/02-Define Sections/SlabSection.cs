using ETABSv17;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EtabsApi
{
    public class SlabSection : Section
    {
        public double thinkness { get; set; }
        public MaterialProperties material { get; set; }
        public eSlabType slabType { get; set; }
        public eShellType shellType { get; set; }

        public SlabSection(cSapModel _mySapModel,string _name, 
            eSlabType _slabType, eShellType _shellType, MaterialProperties _material, double _thinkness) 
            :base(_mySapModel,_name)
        {
            this.name = _name;
            this.thinkness = _thinkness;
            if (_material == null)
            {
                this.material.name = "4000Psi";
            }
            else
            {
                this.material = _material;
            }
            this.shellType = _shellType;
            this.slabType = _slabType;
            // set new area property
            int ret = _mySapModel.PropArea.SetSlab(name, slabType, shellType, material.name, thinkness);
        }
        public override int   setModefires(ref double[] modefireValus)
        {
            int ret = MySapModel.PropArea.SetModifiers(name, ref modefireValus);
            return ret;
        }
    }
}
