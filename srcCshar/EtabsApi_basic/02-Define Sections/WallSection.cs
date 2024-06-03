using ETABSv17;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EtabsApi
{
   public class WallSection:Section
    {
        public double thinkness { get; set; }
        public MaterialProperties material { get; set; }
        public eWallPropType wallType { get; set; }
        public eShellType shellType { get; set; }
        public WallSection(cSapModel _mySapModel, string _name,
            eWallPropType _wallType, eShellType _shellType, MaterialProperties _material, 
            double _thinkness) :base(_mySapModel, _name)
        {
            name = _name;
            thinkness = _thinkness;
            if (_material == null)
            {
                this.material.name = "4000Psi";
            }
            else
            {
                material = _material;
            }
            shellType = _shellType;
            wallType = _wallType;
            int ret = _mySapModel.PropArea.SetWall(this.name, wallType, shellType, _material.name, thinkness);
        } 
        public override int setModefires(ref double[] modefireValus)
        {
            int ret = mySapModel.PropFrame.SetModifiers(name, ref modefireValus);
            return ret;
        }
    }
}
