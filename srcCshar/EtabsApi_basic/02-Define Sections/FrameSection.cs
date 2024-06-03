
using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public abstract class FrameSection:Section
    {
        #region Constructors
        protected FrameSection(cSapModel _mySapModel, string _name, string _notes = "", string _guid = "") : base(_mySapModel, _name, _notes, _guid)
        { }


        #endregion

        #region Methods

        public void RotateLocalAxes(double angel)
        {
            mySapModel.FrameObj.SetLocalAxes(name, angel, eItemType.Objects);
        }
   


        #endregion
    }
}
