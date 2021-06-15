# ABC Corp is a mid-sized insurer in the US and in the recent past their fraudulent claims have 
# increased significantly for their personal auto insurance portfolio. They have developed a ML 
# based predictive model to identify propensity of fraudulent claims. Now, they assign highly 
# experienced claim adjusters for top 5 percentile of claims identified by the model.
# Your objective is to identify the top 5 percentile of claims from each state. Your output 
# should be policy number, state, claim cost, and fraud score.


# Import your libraries
import pandas as pd

# Start writing code
percentiles = fraud_score.groupby('state')['fraud_score'].transform(lambda x: x.quantile(.95))

fraud_score['percentiles'] = percentiles
fraud_score[fraud_score['fraud_score']>=fraud_score['percentiles']].drop('percentiles', axis=1)

# fraud_score["percentile"] = fraud_score.groupby('state')['fraud_score'].rank(pct=True)
