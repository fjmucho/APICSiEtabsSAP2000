using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public class LoadCombinationData :EtabsCore
    {
        List<LoadCombination> loadCombinations;
        List<double> loadCombinationsFactors;
        public LoadCombinationData(cSapModel _mySapModel) : base(_mySapModel)
        {
            loadCombinations = new List<LoadCombination>();
            loadCombinationsFactors = new List<double>();
        }
        public void AddLoadCombination(LoadCombination _loadCombination, double _loadCombinationFactor)
        {
            if (loadCombinations.Contains(_loadCombination))
            {
                for (int i = 0; i < loadCombinations.Count; i++)
                {
                    if (loadCombinations[i].name == _loadCombination.name)
                    {
                        loadCombinationsFactors[i] = _loadCombinationFactor;
                    }
                }
            }
            else
            {
                loadCombinations.Add(_loadCombination);
                loadCombinationsFactors.Add(_loadCombinationFactor);
            }
            eCNameType lC = eCNameType.LoadCombo;
            mySapModel.RespCombo.SetCaseList(_loadCombination.name, ref lC, _loadCombination.name, _loadCombinationFactor);
        }
        public void AddLoadCombinations(List<LoadCombination> _loadCombinations, List<double> _loadCombinationsFactors)
        {
            for (int i = 0; i < _loadCombinations.Count; i++)
            {

                if (loadCombinations.Contains(_loadCombinations[i]))
                {
                    for (int j = 0; j < loadCombinations.Count; j++)
                    {
                        if (loadCombinations[j].name == _loadCombinations[i].name)
                        {
                            loadCombinationsFactors[j] = _loadCombinationsFactors[i];
                        }
                    }
                }
                else
                {
                    loadCombinations.Add(_loadCombinations[i]);
                    loadCombinationsFactors.Add(_loadCombinationsFactors[i]);
                }
                eCNameType lC = eCNameType.LoadCombo;
                mySapModel.RespCombo.SetCaseList(_loadCombinations[i].name, ref lC, _loadCombinations[i].name, _loadCombinationsFactors[i]);
            }
        }
    } 
}
