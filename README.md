# Can the Confidence Scores of Reviewers be Consistent with the Review Content?
Data and code for the paper "Can the Confidence Scores of Reviewers be Consistent with the Review Content?" by Wenqing Wu, Chengzhi Zhang and Haixu Xi. <br>
The purpose of this paper is to explore the consistency between evaluation reports and their confidence scores, and to investigate the impact of confidence scores on paper decision-making. We used data from ICLR 2017-2019, 2021 and 2022, as well as ACL-17, CoNLL-16, COLING-20, and ARR-22 as experimental data.<br>
Our work includes the followig aspects:<br>
1.We collected a large amount of data containing confidence scores and attempted to process the data through automatic recognition by identifying contradictory statements and their aspects in the comment texts. The accuracy of identifying hedge sentences can reach 0.88. <br>
2.This paper investigates and analyzes the consistency between confidence scores and review content. We conducted research and analysis on consistency at the word level, sentence level, and aspect level, respectively. <br>
3.This paper examines the impact of confidence scores on paper decisions. We conducted regression analysis with the decision outcome of papers as the dependent variable, confidence scores and aspect items as independent variables.
# Data and model
We have provided URLs for downloading and viewing the data for ICLR 2021 and ICLR 2022. Other data can obtain from https://github.com/neulab/ReviewAdvisor [1] and https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/3618 [2] <br> 
Hedge words can find from [3] <br>
# Instructions
- hedge_model file: train the hedge sentence prediction model.<br>
-- data_process.py: process input data.<br>
-- load_data.py：load the training data.<br>
-- main.py：train the model.<br>
-- read_hedge.py：Extract hedge sentences and patial hedege words from the HedgePeer dataset (https://github.com/Tirthankar-Ghosal/HedgePeer-Dataset) to form training and testing sets.<br>
-- model.py：model structure.<br>
-- predict.py：predict test data.<br>
-- util.py：data process tool.<br>
run the main.py can train a hedge sentence prediction model.<br>
run the predict.py can predict the result of test data.<br>
- tagger: Aspect tagger for peer review. Aspect identifying tool proposed by Yuan et al [1] (https://github.com/neulab/ReviewAdvisor). Specific details can be checked at previous link.<br>

- Dataset: contain used data's url and information on data statistics.<br>
  -- (1-5)conf_asp.json: Aspect count for hedge sentences.<br>
  -- sent_asp.xlsx and text_asp.xlsx: data of regression analysis.<br>
  -- conf(1-5)_hedge)word.json: hedge word count for review report.<br>
  -- 2021(2)_****.txt: ICLR 2021 and ICLR 2022 data URL.<br>

- regression_analysis.py: regression model for paper decision and confidence score and aspect. <br>
- review_count.py: process peer review content and data statistics.<br>
- text_preprocess.py: Preprocessing crawled data.<br>
- text_reptile.py, Reptile.py and process_screview.py: crawl data from openreview and save to local.<br>
# Acknowledgement
We thank the openreview.net team for the commitment to promoting transparency and openness in scientific communication.
# Reference
[1] Yuan, W., Liu, P., Neubig, G.: Can we automate scientific reviewing? Journal of Artificial Intelligence Research 75, 171–212 (2022) <br>
[2] Dycke, N., Kuznetsov, I., Gurevych, I.: Nlpeer: A unified resource for the computational study of peer review. arXiv preprint arXiv:2211.06651 (2022) <br>
[3] Xie, S., Mi, C.: Promotion and caution in research article abstracts: The use of positive, negative and hedge words across disciplines and rankings. Learned Publishing 36(2), 249–265 (2023)
