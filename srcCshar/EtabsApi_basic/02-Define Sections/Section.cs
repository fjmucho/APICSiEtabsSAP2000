using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public abstract class Section :EtabsCore
    {
        #region properities
            public string name { get; set; }
            public string  guid { get; set; }
            public string  notes { get; set; }
            protected static cSapModel myStaticSapModel;
        #endregion 

        #region Constructors
        protected Section(cSapModel _mySapModel, string _name, string _notes = "", string _guid = "") : base(_mySapModel)
        {
            name = _name;
            notes = _notes;
            guid = _guid;
            myStaticSapModel = _mySapModel;
        }
        #endregion
        public abstract int setModefires(ref double[] modefireValus);
   

    }
}
