# Sentiment-Analysis-SWJ

This project is testing the sentiment analysis capabilities of LLMs and other language models (i.e., BERT).

# Interrater Reliability

### Approach

Chosen members from the lab will read the same 20 reviews that were systematically randomly sampled from a pool of 100 paper reviews from the SWJ and determine the sentiments, categorizing them as positive, neutral, or negative. Then Fleiss' Kappa (FK) interrater reliability formula will be used to get the results. If the FK value returned is approximately 0.70 (or 0.60 if we want to be less strict), then we can review the rest independently. If the FK value is less than that, we will have to reassess by either selecting another 20 to review together until the score is “good enough”, or more clearly define our labels.

These human sentiments will then be compared against accessible OpenAI LLM Models, as well as BERT and RoBERTa language models from Hugging Face, to see the results. Further experimentation will be conducted using unique techniques to assess the differences in results and agreements among the models.

## Rater Task

Each rater will perform the following for all 20 scientific paper reviews from `initial-sample-human-reviewed-assessments.md` in the `deliverables\data\` directory:

1. Read review
2. Determine sentiment of the **overall** review from the following choices: `Positive`, `Neutral`, or `Negative`.
3. Enter their name in the `analyst` column and their rating in the `sentiment` column.

## Definitions and Examples

When determining the sentiment of an overall document (review), we will use a polarity feature approach for each sentence. A positive sentence will receive a score of +1, a negative sentence will receive a score of -1, and a neutral sentence will receive a score of 0. For easy calculation, after each paragraph, calculate the total. Then, when the document is completely read, calculate the total sum among the paragraphs. A positive score indicates an overall positive sentiment, a negative score indicates a negative sentiment, and a score of zero indicates neutral sentiment.

# OpenAI Models Used

TBD

# Useful Links

[Hugging Face](https://huggingface.co/) - Repo for Language Models, data sets, and machine learning materials.

[Datatab - Fleiss Kappa](https://datatab.net/tutorial/fleiss-kappa)

# Relevant Papers

[Opinion Polarity Identification through Adjectives](https://arxiv.org/abs/1011.4623) - Has examples of defining sentiment using polarity (adjectives for determing sentiment)

[Classifying Emotion in News Sentences: When Machine Classification Meets Human Classification ](https://www.researchgate.net/publication/41392153_Classifying_Emotion_in_News_Sentences_When_Machine_Classification_Meets_Human_Classification) - More examples and explanations for using polarity.

[Comprehensive review and comparative analysis of transformer models in sentiment analysis](https://link.springer.com/article/10.1007/s10115-024-02214-3) - Excellent introductory to the concepts and terminology

[Optimization Techniques for Sentiment Analysis Based on LLM (GPT-3)](https://arxiv.org/abs/2405.09770)

[Exploring transformer models for sentiment classification: A comparison of BERT, RoBERTa, ALBERT, DistilBERT, and XLNet](https://onlinelibrary.wiley.com/doi/10.1111/exsy.13701)

[Measuring Fleiss' Kappa](https://arxiv.org/abs/2303.12502)

[Fleiss' Kappa](https://rave.ohiolink.edu/ejournals/article/318558932)

[National Library of Medicine - Interrater Reliability](https://pmc.ncbi.nlm.nih.gov/articles/PMC9426226/)
