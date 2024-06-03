
using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public class AssignLoad:EtabsCore
    {
        protected LoadPattern loadPattern { get; set; }
        protected CSys cSys { get; set; } 
        protected bool replaceAssignedLoad { get; set; }
        public AssignLoad(cSapModel _mySapModel, LoadPattern _loadPattern, CSys _cSys = CSys.Global, bool _replaceAssignedLoad = true) : base(_mySapModel)
        {
            loadPattern = _loadPattern;
            cSys = _cSys;
            replaceAssignedLoad = _replaceAssignedLoad;
        }
    }
}
