using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public abstract class EtabsCore
    {
        #region MemberVariables
        protected cSapModel mySapModel;
        #endregion

        #region Properties
        public cSapModel MySapModel
        {
            get
            {
                return mySapModel;
            }
            set
            {
                mySapModel = value;
            }
        }

        #endregion

        #region Constructor

        public EtabsCore(cSapModel _mySapModel)
        {
            mySapModel = _mySapModel;
        }

        #endregion

    }
}
