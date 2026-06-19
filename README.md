---
title: Rapformer
emoji: 🎵
colorFrom: blue
colorTo: gray
sdk: docker
pinned: false
---

# Rapformer 🎧 

**Live Demo:** [Play with it on Hugging Face](https://huggingface.co/spaces/zwwixx/rapformer)

Rapformer is a custom Autoregressive Transformer language model trained from absolute scratch to spit bars. No OpenAI API keys, no LangChain wrappers—just pure PyTorch mathematics and zero-shot generation. 

## 📊 The Stats
* **Brain Size:** 14 Million Parameters
* **Diet:** Trained on a custom-scraped dataset of ~500,000 words of rap lyrics (Genius API)
* **Capabilities:** Zero-shot lyric generation, rhyme formatting, and ad-lib placement

## 🛠️ Under the Hood
I built the entire pipeline end-to-end:
* **Data Engineering:** Custom Python scraper with duplicate-detection memory to build the corpus.
* **Engine:** PyTorch (Multi-head attention & transformer blocks built from scratch).
* **Tokenizer:** Custom SentencePiece model (`tokrap.model`).
* **Backend:** FastAPI & Uvicorn (serving inference via an HTTP API).
* **Frontend:** Pure HTML/CSS with a custom liquid-glass UI (no bloated frameworks).
* **DevOps:** Containerized with Docker and deployed to Hugging Face Spaces via Git LFS.

## 🚀 How to use
Just drop a starting phrase (e.g., `"I woke up"`) into the UI, tweak the Temperature and Top-K sliders to control the model's creativity, and hit **LET ME YAP!**