This directory contains data used for assessing a LLM or other language models ability to analyze the sentiment of reviews for papers submited to the Semantic Web Journal.

# Contents

- The `human-reviewed-assessments-base.csv` file contains the data on the determined sentiment of the reviews by human readers.

  <small>**NOTE**: I question the validity of the previous analyst's sentiment determination. Moving foward we will use the new `non-reviewed-assements-base.csv` for comparison with GPT reviewed senetiments.</small>

- `non-reviewed-assessments-base.csv` file contains the **NEW** dataset of all the paper reviews that have not been analyzed for sentiment analysis.

## no-context-llm-assessments

Contains the determined sentiments for OpenAI's ChatGPT models with no context given to the sentiment labels.

## old

Contains the previous datasets used for determination before formulating a more scientific approach to the study and analysis. Below are the files within and what they contain:

- `gpt4-reviewed-assessments.csv` contains the data on the determined sentiment of the reviews by a GPT4 model from OpenAI in August 2024.
- `non-reviewed-assessments-base.csv` file contains the **OLD** dataset of all the paper reviews that have not been analyzed for sentiment analysis. Some of these reviews are no longer accessible to those without certain account privileges, so a new dataset was created to circumvent this problem.
