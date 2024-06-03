
using ETABSv17;
using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public class LoadCombination :EtabsCore
    {
        public string name { get; set; }
        public LoadCombinationType type { get; set; }
        public List<double> scalFactors { get; set; }
        public List<LoadPattern> loadCases { get; set; }
        public LoadCombination(cSapModel _mySapModel, string _name, LoadCombinationType _type) : base(_mySapModel)
        {
            name = _name;
            type = _type;
            loadCases = new List<LoadPattern>();
            scalFactors = new List<double>();
            mySapModel.RespCombo.Add(name, (int)type);
        }

          
        public int AddLoadCases(List<LoadPattern> _loadCases, List<double> _loadCasesFactors)
        {
            int result = 0;
            for (int i = 0; i < _loadCases.Count; i++)
            {
                eCNameType lC = eCNameType.LoadCase;
                int ret = mySapModel.RespCombo.SetCaseList(name, ref lC, _loadCases[i].name, _loadCasesFactors[i]);
                result = ret;
            }
            return result;
        }
        public int ModifyLoadCase(string name,double SF) 
        {
            eCNameType lC = eCNameType.LoadCase;
            int ret = MySapModel.RespCombo.SetCaseList(this.name, ref lC, name, SF);
            return ret;
        }


    }
}
