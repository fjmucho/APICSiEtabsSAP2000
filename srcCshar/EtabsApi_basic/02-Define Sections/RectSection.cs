 using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
    public class RectSection : FrameSection
    {
        #region properities
        public double width { get; set; }
        public double height { get; set; }
        public MaterialProperties material { get; set; }
        #endregion
        //Constructor for existing frame R section in ETABS (No creation for frame R section in etabs, Just be used in analysis and get results P,M2,M3,N
        public RectSection(cSapModel _mySapModel, MaterialProperties material, string _name, double _width, double _height, 
           int color, string _notes = "", string _guid = "") : base(_mySapModel, _name, _notes, _guid)
        {
            height = _height;
            width = _width;
            //'set new frame section property
             int ret = MySapModel.PropFrame.SetRectangle(_name, material.name, height ,width,color,_notes,_guid);
        }

        public override int setModefires(ref double[] modefireValus)
        {
            int ret = mySapModel.PropFrame.SetModifiers(name, ref modefireValus);
            return ret;
        }
    }
}
