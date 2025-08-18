# sentiment-analysis-swj

This project is testing the sentiment analysis capabilities of LLMs and other language models (i.e., BERT).

# LLM Sentiment Analysis

1. Create base dataset (done).
2. Use the SAME PROMPT to fill in review determination (pos,neg,neutral) for EACH MODEL
   a. Initially try a smaller dataset with a variety of prompts to determine the best one.
3. Analyze results. Look for discrepencies and variation between each model.
4. Determine best model.

## LM Fine Tuning Test Phase

1. Pick language model (i.e.,BERT).
2. With base dataset get sentiment results from LM.
3. Compare results with human reviewed dataset.
4. Fine-tune language model.
5. Repeat steps 2-3.
6. Determine results.

# Latest OpenAI Models (newest to oldest as of 08/01/2024)

- gpt-4o-2024-08-06 chatgpt-4o-latest (gpt-4o-2024-05-13)

- gpt-4o-mini (gpt-4o-mini-2024-07-18)

- gpt-4-turbo (gpt-4-turbo-2024-04-09)

- gpt-4 (gpt-4-0613)

### Legacy Models

- gpt-3.5-turbo-1106
- gpt-3.5-turbo (gpt-3.5-turbo-0125)

# Useful Links

[Hugging Face](https://huggingface.co/) - Repo for Language Models, data sets, and machine learning materials.

[Measuring Fleiss' Kappa](https://arxiv.org/abs/2303.12502)

[Datatab - Fleiss Kappa](https://datatab.net/tutorial/fleiss-kappa)

# Relevant Papers

[Comprehensive review and comparative analysis of transformer models in sentiment analysis](https://link.springer.com/article/10.1007/s10115-024-02214-3) - Excellent introductory to the concepts and terminology

[Optimization Techniques for Sentiment Analysis Based on LLM (GPT-3)](https://arxiv.org/abs/2405.09770)

[Exploring transformer models for sentiment classification: A comparison of BERT, RoBERTa, ALBERT, DistilBERT, and XLNet](https://onlinelibrary.wiley.com/doi/10.1111/exsy.13701)

[Fleiss' Kappa](https://rave.ohiolink.edu/ejournals/article/318558932)

[National Library of Medicine - Interrater Reliability](https://pmc.ncbi.nlm.nih.gov/articles/PMC9426226/)
