using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public abstract class Element:EtabsCore
    {
        #region MemberVariable
        public string name { get; set; }
        public string userName { get; set; }
        public static cSapModel myStaticSapModel { get; set; }
        #endregion
        public Element(cSapModel _mySapModel, string _name,string _userName="" ) : base(_mySapModel)
        {
            name = _name;
            myStaticSapModel = _mySapModel;
            userName = _userName;
        }
        public abstract int elementModifire(ref double [] modifiresValues);

    }
}
