package DomainLogicPatternsImplementations.RevenueRecognition.domainmodel.recognitionrules;

import DomainLogicPatternsImplementations.RevenueRecognition.domainmodel.Contract;
import DomainLogicPatternsImplementations.RevenueRecognition.domainmodel.RevenueRecognition;

/**
 * Created by Praise on 2017/02/27.
 */
public class CompleteRecognitionStrategy extends RecognitionStrategy {

    @Override
    public void calculateRevenueRecognitions(Contract contract) {
        contract.addRevenueRecognition(new RevenueRecognition(contract.getRevenue(), contract.getWhenSigned()));
    }
}
