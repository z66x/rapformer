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

Rapformer is a custom autoregressive transformer trained from scratch to generate rap lyrics. No OpenAI API keys, no LangChain wrappers — just pure PyTorch and a custom data pipeline.

Built as an upgrade to [zwixGPT](https://github.com/z66x/zwixGPT), which was character-level. Rapformer moves to subword tokenization via a custom SentencePiece BPE model trained on the corpus itself.

## 📊 Stats

| | |
|---|---|
| Parameters | 14M |
| Tokenizer | SentencePiece BPE, vocab size 10,000 |
| Training corpus | ~500K words, 789 songs |
| Artists | Kanye West, Kendrick Lamar, Drake, Eminem, Travis Scott, J. Cole, XXXTentacion, NF |
| Final test loss | ~4.0 (theoretical floor: ln(10000) ≈ 9.21 at init) |

## 🛠️ Stack

- **Model** — decoder-only transformer, Pre-LayerNorm, causal multi-head self-attention, residual connections, built in raw PyTorch
- **Tokenizer** — custom SentencePiece BPE trained on the rap corpus (`vocab_size=10000`, `byte_fallback=True`)
- **Backend** — FastAPI + Uvicorn
- **Frontend** — pure HTML/CSS, liquid-glass UI
- **Infra** — Docker, deployed to Hugging Face Spaces via Git LFS

## 🧪 Training Notes

Test loss plateaued around step 1500 at ~4.0 — a data ceiling, not a model failure. At 10K vocab with ~900K tokens, many subword pieces are seen infrequently enough that generalization hits a floor that regularization can't fix. Output quality at `temperature=1.2, top_k=50` is the sweet spot found empirically across multiple runs.

First generation the model ever produced unprompted:

> *"I used to be nice, I'd rather be"*

## 🚀 Usage

Drop a seed phrase into the UI, adjust the sliders:
- **Creativity (temperature)** — lower = safer and more coherent, higher = chaotic and unpredictable
- **Word pool (top-k)** — how many candidate tokens the model considers at each step

Hit generate. Let it yap.