#  Are the confidence scores of reviewers consistent with the review content? Evidence from top conference proceedings in AI
## Overview

**Data and code for the paper "Are the confidence scores of reviewers consistent with the review content? Evidence from top conference proceedings in AI".**

The purpose of this paper is to explore the consistency between evaluation reports and their confidence scores, and to investigate the impact of confidence scores on paper decision-making. We used data from ICLR 2017-2019, 2021 and 2022, as well as ACL-17, CoNLL-16, COLING-20, and ARR-22 as experimental data.<br>
Our work includes the followig aspects:<br>
  -  We collected a large amount of data containing confidence scores and attempted to process the data through automatic recognition by identifying contradictory statements and their aspects in the comment texts. The accuracy of identifying hedge sentences can reach 0.88. <br>
  -  This paper investigates and analyzes the consistency between confidence scores and review content. We conducted research and analysis on consistency at the word level, sentence level, and aspect level, respectively. <br>
  - This paper examines the impact of confidence scores on paper decisions. We conducted regression analysis with the decision outcome of papers as the dependent variable, confidence scores and aspect items as independent variables.
## Directory structure

<pre>
confidence_score                                         Root directory
├── Code                                                 Source code folder
│   ├── hedge_model                                      Train the hedge sentence prediction model.
│   │   ├── data_process.py                              Process input data.
│   │   ├── load_data.py.py                              Load the training data.
│   │   └── main.py                                      Train the model.
│   │   └── read_hedge.py                                Extract hedge sentences and patial hedege words from the HedgePeer dataset (https://github.com/Tirthankar-Ghosal/HedgePeer-Dataset) to form training and testing sets.  
│   │   └── model.py                                     Model structure. 
│   │   └── predict.py                                   Predict test data.  
│   │   └── util.py                                      Data process tool.  
│   ├── regression_analysis.py                           Regression model for paper decision and confidence score and aspect.
│   ├── review_count.py                                  Process peer review content and data statistics. 
│   ├── text_preprocess.py                               Preprocessing raw data.
│   ├── requirement.txt                                  Dependency python packages required to run code.
├── Data                                                 Dataset folder
│   ├── conf1_asp.json                                   Aspect count of hedge sentences with confidence score is 1.
│   ├── conf2_asp.json                                   Aspect count of hedge sentences with confidence score is 2.
│   ├── conf3_asp.json                                   Aspect count of hedge sentences with confidence score is 3.
│   ├── conf4_asp.json                                   Aspect count of hedge sentences with confidence score is 4.
│   ├── conf5_asp.json                                   Aspect count of hedge sentences with confidence score is 5.
│   ├── sent_asp.xlsx                                    Regression analysis data between confidence scores and aspects.
│   ├── text_asp.xlsx                                    Regression analysis data between confidence scores and aspects on decision-making.
│   ├── conf1_hedge_word.json                            Hedge word count for review report with confidence score is 1.
│   ├── conf2_hedge_word.json                            Hedge word count for review report with confidence score is 2.
│   ├── conf3_hedge_word.json                            Hedge word count for review report with confidence score is 3.
│   ├── conf4_hedge_word.json                            Hedge word count for review report with confidence score is 4.
│   ├── conf5_hedge_word.json                            Hedge word count for review report with confidence score is 5.
│   ├── 2021_oral-presentations.txt                      ICLR 2021 oral presentations data URL.
│   ├── 2021_poster-presentations.txt                    ICLR 2021 poster presentations data URL.  
│   ├── 2021_spotlight-presentations.txt                 ICLR 2021 spotlight presentations data URL.
│   ├── 2021_withdrawn-rejected-submissions.txt          ICLR 2021 withdrawn-rejected-submissions data URL.
│   ├── 2022_oral-submissions.txt                        ICLR 2022 oral submissions data URL.
│   ├── 2022_poster-submissions.txt                      ICLR 2022 poster submissions data URL.
│   ├── 2022_spotlight-submissions.txt                   ICLR 2022 spotlight submissions data URL.
│   ├── 2022_submitted-submissions.txt                   ICLR 2022 submitted submissions data URL.
│   ├── 2022_desk-rejected-withdrawn-submissions.txt     ICLR 2022 desk rejected withdrawn submissions data URL.
└── README.md
</pre>

## Data and model
 -  We have provided URLs for downloading and viewing the data for ICLR 2021 and ICLR 2022. Other datas can obtain from https://github.com/neulab/ReviewAdvisor [1] and https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/3618 [2] <br> 
 -  Hedge words can find from Citation [3] <br>
 -  Hedge sentence prediction model can find from Code/hedge_model folder.<br>

## Instructions

 -  Run the Code/hedge_model/main.py can train a hedge sentence prediction model.<br>
 -  Run the Code/hedge_model/predict.py can predict the result of test data.<br>
 -  Tagger: Aspect tagger tool for peer review. Aspect identifying tool proposed by Yuan et al [1] (https://github.com/neulab/ReviewAdvisor). Specific details can be checked at previous link.<br>


## Acknowledgement
We thank the openreview.net team for the commitment to promoting transparency and openness in scientific communication.
## Reference
[1] Yuan, W., Liu, P., Neubig, G. (2022). Can we automate scientific reviewing? Journal of Artificial Intelligence Research 75, 171–212  <br>
[2] Dycke, N., Kuznetsov, I., Gurevych, I. (2022). Nlpeer: A unified resource for the computational study of peer review. arXiv preprint arXiv:2211.06651 <br>
[3] Xie, S., Mi, C. (2023). Promotion and caution in research article abstracts: The use of positive, negative and hedge words across disciplines and rankings. Learned Publishing 36(2), 249–265.

## Citation
Please cite the following paper if you use this code and dataset in your work.
    
>Wenqing Wu, Haixu Xi, Chengzhi Zhang\*.  Are the confidence scores of reviewers consistent with the review content? Evidence from top conference proceedings in AI. ***Scientometrics***, 2024. [[doi]]()  [[Dataset & Source Code]](https://github.com/njust-winchy/confidence_score) 
