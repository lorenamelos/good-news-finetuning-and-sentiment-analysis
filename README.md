# Sentimental Analysis of News Headlines 📰

## Overview
### Text Classification with DistilBERT

1. **Dataset Creation**: We start by creating a custom dataset called `dataset.json`. This dataset contains news headlines along with their corresponding sentiment labels (positive or negative). The data was obtain by scraping news websites using the Beautiful Soup library.

2. **Model Finetuning**: We then finetune the pre-trained DistilBERT model on the `dataset.json` dataset. Finetuning involves adapting the model's parameters to better fit the specific task of sentiment classification. This step is crucial for achieving high performance on our custom task.

3. **Inference**: After finetuning, we use the trained model to make predictions on new, unseen news headlines. Given a news headline, the model predicts whether it expresses a positive or negative sentiment.

## Objective
The objective of this project is to demonstrate how to finetune the DistilBERT model on a custom dataset for text classification. Specifically, we aim to classify news headlines as either positive or negative based on their sentiment.

Text classification is a fundamental Natural Language Processing (NLP) task that involves assigning a label or class to a piece of text. This project focuses on text classification using the DistilBERT model, a distilled version of the BERT model that retains much of its performance while being faster and more memory-efficient.

## Further developments:

1 . It was a little bit hard to find good news over the internet. What made me thought about doing a data analysis about how many bad news we have for each good one we find.

The text step is to gather more data to make this analisys from the sentiment model I just fine-tuned during this notebook.

Other resources to add to the dataset for GOOD NEWS:

  1. https://www.positive.news/
  2. https://www.today.com/news/good-news
  3. https://www.foxnews.com/category/good-news
  4. https://www.rescue.org/uk/hopeful-news?gad_source=1&gclid=Cj0KCQjw6auyBhDzARIsALIo6v8o-OBraUZ7ZCD8QgbdhEeYq60SURXZcN_bTfCTeZIw3g_VGmBg-EcaAmnuEALw_wcB

2. Another idea is to create an app that will scrap the internet and return at least one good new to the users, so they can have at least one cheerful news to keep the hope alive. :)

3. Inspired questions: how can we develop a better society focusing on the good news? if the bad news increase the anxiety and depression, can watch only good news become some sort of prescription to those who suffer from this mental problems?

## Conclusion

By this guide, you will learn how to leverage the power of the DistilBERT model for text classification tasks. Whether you're interested in sentiment analysis or other forms of text classification, the techniques demonstrated here serve as a solid foundation for building and deploying NLP models in real-world applications.

## Finetuned model On HuggingFace

The finetuned model can be found here: https://huggingface.co/lmelos/good_news_detector

<img src="https://github.com/lorenamelos/good-news-finetuning-and-sentiment-analysis/assets/120689570/53d44bf2-2d7b-4c41-95b5-2c4d0c6c4ffb" width="50"/> 
