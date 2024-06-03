
using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
    public abstract class   AnalysisResult:EtabsCore
    {
        protected LoadCombination loadCombination { get; set; }
        protected LoadPattern loadCase { get; set; }

        public AnalysisResult(cSapModel _mySapModel, LoadPattern _loadCase) :base(_mySapModel)
        {
            loadCase = _loadCase;
            mySapModel.Results.Setup.DeselectAllCasesAndCombosForOutput();
            mySapModel.Results.Setup.SetCaseSelectedForOutput(loadCase.name, true);

        }
        public AnalysisResult(cSapModel _mySapModel, LoadCombination _loadCombination) :base(_mySapModel)
        {
            loadCombination = _loadCombination;
            mySapModel.Results.Setup.DeselectAllCasesAndCombosForOutput();
            mySapModel.Results.Setup.SetComboSelectedForOutput(loadCombination.name, true);
        }

    }
}
