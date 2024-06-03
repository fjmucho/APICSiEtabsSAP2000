
using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public class LoadPattern :EtabsCore 
    {
        #region MemberVariables
        public string name { get; set; }
        public LoadPatternType type { get; set; }
        public double selfWeightMultiplier { get; set; }
        public bool isLoadCase { get; set; }
        #endregion

        #region constructor
        public LoadPattern(cSapModel _mySapModel, string _name, LoadPatternType _type = LoadPatternType.Other, double _selfWeightMultiplier = 0, bool _isLoadCase = true) : base(_mySapModel)
        {
            name = _name;
            type = _type;
            selfWeightMultiplier = _selfWeightMultiplier;
            isLoadCase = _isLoadCase;
            eLoadPatternType sapType = (eLoadPatternType)((int)type);
            mySapModel.LoadPatterns.Add(name, sapType, selfWeightMultiplier, isLoadCase);

        }
        #endregion
    }

    public class LoadPatternSeismic : EtabsCore
    {
        public int MyProperty { get; set; }
        public LoadPatternSeismic(cSapModel _mySapModel) :base(_mySapModel)
        {
         
 


        }
    }
}
