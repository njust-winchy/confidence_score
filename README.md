# Can the Confidence Scores of Reviewers be Consistent with the Review Content?
Data and code for the paper "Can the Confidence Scores of Reviewers be Consistent with the Review Content?" by Wenqing Wu, Chengzhi Zhang and Haixu Xi. <br>
The purpose of this paper is to explore the consistency between evaluation reports and their confidence scores, and to investigate the impact of confidence scores on paper decision-making. We used data from ICLR 2017-2019, 2021 and 2022, as well as ACL-17, CoNLL-16, COLING-20, and ARR-22 as experimental data.<br>
Our work includes the followig aspects:<br>
1.We collected a large amount of data containing confidence scores and attempted to process the data through automatic recognition by identifying contradictory statements and their aspects in the comment texts. The accuracy of identifying hedge sentences can reach 0.88. <br>
2.This paper investigates and analyzes the consistency between confidence scores and review content. We conducted research and analysis on consistency at the word level, sentence level, and aspect level, respectively. <br>
3.This paper examines the impact of confidence scores on paper decisions. We conducted regression analysis with the decision outcome of papers as the dependent variable, confidence scores and aspect items as independent variables.
# Data and model
The data and pretrained model can download by Baidu Netdisk, the data includes preprocess data and raw data.<br>
link：https://pan.baidu.com/s/1WyQNxiRXbwDVKJkTcWUluQ <br>
password：y3yi <br>
# Instructions
- hedge_model file: train the hedge sentence prediction model.<br>
-- data_process.py: process input data.<br>
-- load_data.py：load the training data.<br>
-- main.py：train the model.<br>
-- read_hedge.py：Extract hedge sentences from the HedgePeer dataset (https://github.com/Tirthankar-Ghosal/HedgePeer-Dataset) to form training and testing sets.<br>
-- model.py：model structure.<br>
-- predict.py：predict test data.<br>
-- util.py：data process tool.<br>
run the main.py can train a hedge sentence prediction model.<br>
run the predict.py can predict the result of test data.<br>
- tagger: Aspect annotation tool by Yuan et al (https://github.com/neulab/ReviewAdvisor). Specific details can be checked at previous link.<br>

- (1-5)conf_asp.json: Aspect count for hedge sentences.<br>

- conf(1-5)_hedge)word.json: hedge word count for review report.<br>

- new_hedge_word.text: hedge word list.

- regression_analysis.py: regression model. <br>

- review_count.py: count peer review content<br>

- sent_asp.xlsx and text_asp.xlsx: data of regression analysis.
# Acknowledgement
We thank the openreview.net team for the commitment to promoting transparency and openness in scientific communication.
