from openai import OpenAI
import streamlit as st
import os

def openaiClient(apiKey, baseUrl):
  client = OpenAI(
    api_key=os.environ.get(apiKey),
    base_url=os.environ.get(baseUrl)
  )
  return client

def chatCompletion(client, model, messages, max_tokens, temperature, top_p):
  with st.chat_message("assistant"):
    stream = client.chat.completions.create(
      model=model,
      messages=messages,
      max_tokens=max_tokens,
      temperature=temperature,
      top_p=top_p,
      stop=None,
      stream=True
    )
    result = st.write_stream(chunk.choices[0].delta.content for chunk in stream if chunk.choices[0].delta.content)
    return result

def deepseek(model, messages, max_tokens, temperature, top_p):
  SILICONFLOW_API_KEY = "SILICONFLOW_API_KEY"
  SILICONFLOW_BASE_URL = "SILICONFLOW_BASE_URL"
  client = openaiClient(SILICONFLOW_API_KEY, SILICONFLOW_BASE_URL)
  result = chatCompletion(client, model, messages, max_tokens, temperature, top_p)
  return result
