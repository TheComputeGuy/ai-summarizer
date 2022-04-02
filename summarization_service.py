import openai
import os
import nltk
from summarization_utils import post_processing
nltk.download('punkt')

TLDR_POSTFIX = "\n tl;dr:"
SUMMARIZE_PREFIX = "Summarize this for a second-grade student:\n\n"
CURIE_ENGINE = "curie"
BATCH_SIZE = 500
NUM_TOKENS = 125

openai.api_key = os.getenv("OPENAI_API_KEY")

def _generate_summary(input_text):
    gpt3_prompt = SUMMARIZE_PREFIX + input_text + TLDR_POSTFIX
    response = openai.Completion.create(
        engine=CURIE_ENGINE,
        prompt=gpt3_prompt,
        temperature=0,
        max_tokens=NUM_TOKENS,
        top_p=1.0,
        frequency_penalty=1.0,
        presence_penalty=1.0
    )
    batch_summary = response["choices"][0]["text"]

    return post_processing(response_text = batch_summary)

def process_in_batches(input_text):
  sentences = nltk.tokenize.sent_tokenize(input_text)
  tokens = 0
  batch_sentence = ""
  batches = []
  for sentence in sentences:
    tokens = tokens + len(nltk.word_tokenize(sentence))
    if tokens <= BATCH_SIZE:
      batch_sentence += sentence
    else:
      batches.append(batch_sentence)
      batch_sentence = sentence
      tokens = len(nltk.word_tokenize(sentence))
  
  # Pass each batch for summarization. And collect summarization for all sentences
  summary = ''
  for batch in batches:
      response = _generate_summary(batch)
      summary = summary + response
  return summary