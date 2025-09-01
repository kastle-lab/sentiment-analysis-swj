# Sentiment-Analysis-SWJ

This project is testing the sentiment analysis capabilities of LLMs and other language models (i.e., BERT).

# Iterator Reliability

Chosen members from the lab will read the same 20 reviews that were systematically randomly sampled from a pool of 100 paper reviews from the SWJ and determine the sentiments, categorizing them as positive, neutral, or negative. Then Fleiss' Kappa (FK) interrater reliability formula will be used to get the results. If the FK value returned is approximately 0.70 (or 0.60 if we want to be less strict), then we can review the rest independently. If the FK value is less than that, we will have to reassess by either selecting another 20 to review together until the score is “good enough”, or more clearly define our labels.

These human sentiments will then be compared against accessible OpenAI LLM Models, as well as BERT and RoBERTa language models from Hugging Face, to see the results. Further experimentation will be conducted using unique techniques to assess the differences in results.

# LLM Sentiment Analysis

1. Create base dataset (done).
2. Use the SAME PROMPT to fill in review determination (pos,neg,neutral) for EACH MODEL
   a. Initially try a smaller dataset with a variety of prompts to determine the best one.
3. Analyze results. Look for discrepancies and variation between each model.
4. Determine best model.

## LM Fine Tuning Test Phase

1. Pick language model (i.e.,BERT).
2. With base dataset get sentiment results from LM.
3. Compare results with human reviewed dataset.
4. Fine-tune language model.
5. Repeat steps 2-3.
6. Determine results.

# OpenAI Models Used

TBD

# Useful Links

[Hugging Face](https://huggingface.co/) - Repo for Language Models, data sets, and machine learning materials.

[Datatab - Fleiss Kappa](https://datatab.net/tutorial/fleiss-kappa)

# Relevant Papers

[Opinion Polarity Identification through Adjectives](https://arxiv.org/abs/1011.4623) - Has examples of defining sentiment using polarity (adjectives for determing sentiment)

[Comprehensive review and comparative analysis of transformer models in sentiment analysis](https://link.springer.com/article/10.1007/s10115-024-02214-3) - Excellent introductory to the concepts and terminology

[Optimization Techniques for Sentiment Analysis Based on LLM (GPT-3)](https://arxiv.org/abs/2405.09770)

[Exploring transformer models for sentiment classification: A comparison of BERT, RoBERTa, ALBERT, DistilBERT, and XLNet](https://onlinelibrary.wiley.com/doi/10.1111/exsy.13701)

[Measuring Fleiss' Kappa](https://arxiv.org/abs/2303.12502)

[Fleiss' Kappa](https://rave.ohiolink.edu/ejournals/article/318558932)

[National Library of Medicine - Interrater Reliability](https://pmc.ncbi.nlm.nih.gov/articles/PMC9426226/)
