---
title: Arabic Flip
emoji: 🇲🇦
colorFrom: red
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---

https://huggingface.co/spaces/monsoon-nlp/spanish-flip

Designed for HuggingFace Spaces + Gradio

Flips masculine and feminine words within a Spanish sentence, when appropriate.

How it works: this loads a seq2seq model from these two HuggingFace models:
- https://huggingface.co/monsoon-nlp/es-seq2seq-gender-encoder
- https://huggingface.co/monsoon-nlp/es-seq2seq-gender-decoder

Both were based on BETO ( https://huggingface.co/dccuchile/beto ) and then
trained on sentences which I flipped more programmatically with spaCy.

Applications:
- gender bias in finetuned models
- data augmentation for more representation

For help setting up data augmentation (adding or replacing sentences within
a dataset) try https://github.com/MonsoonNLP/seq2seq-for-data-augmentation
