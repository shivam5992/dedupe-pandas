from _process import Matcher
import pandas as pd 

clean_config = {
	'lower' : True,
	'punctuation' : True,
	'whitespace' : True,
	'digits' : True
}

match_config = {
	'exact_math' : True,
	'levenshtein_ratio' : True,
	'soundex' : True,
	'metaphone' : True, 
	'Jaro' : True,
}

match = Matcher(clean_config = clean_config, match_config = match_config)

input_config = {
	'column' : 'city',
	'input_data' : pd.read_csv('data/data1.csv'),
	'score_column' : 'confidence_score',
	'threshold' : 0.75,
	'_id' : 'id'
}

results = match.dedupe(input_config)
print results