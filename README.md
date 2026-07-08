# PRODIGY_GA_01

## Task 01 - GPT-2 Fine-Tuning for Generative AI

This project was developed as part of the Prodigy InfoTech Generative AI Internship.

## Objective

Fine-tune GPT-2 on a custom instruction-response dataset to generate answers for Generative AI concepts.
# GPT-2 Fine-Tuning for Generative AI Interview Assistant

## Features
- Custom instruction-response dataset (113 Q&A)
- GPT-2 fine-tuning using Hugging Face Transformers
- Dataset preprocessing pipeline
- Automatic dataset merging utility
- Interactive inference
- Modular project structure

## Tech Stack
- Python
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- GPT-2
- Git

## Project Structure
data/
├── dataset_v2/
├── dataset_v3.json
├── tokenized/

models/
src/
├── preprocess.py
├── train.py
├── inference.py
├── merge_dataset.py

## Training Pipeline
Dataset → Tokenization → Fine-tuning GPT-2 → Inference

## Future Improvements
- Gradio UI
- Larger dataset
- Evaluation metrics
- Better decoding strategies

## Features

- GPT-2 Fine-tuning
- Custom instruction-response dataset
- Text preprocessing
- Tokenization using Hugging Face
- Text generation (Inference)
- Modular project structure

## Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets

## Project Structure

```text
data/
src/
models/
outputs/
```

## Installation

```bash
pip install -r requirements.txt
```

## Train

```bash
python src/train.py
```

## Inference

```bash
python src/inference.py
```

## Sample Prompt

```
What is GPT-2?
```

## Sample Output

```
GPT-2 is a transformer language model developed for text generation.
```

## Future Improvements

- Larger training dataset
- Better response quality
- Gradio Web Interface
- Improved evaluation
