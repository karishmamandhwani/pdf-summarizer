---
title: PDF Summarizer
emoji: 📄
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.38.0"
app_file: main.py
pinned: false
---

# 📄 PDF Summarizer

A simple AI-powered web app that takes any PDF file and generates an instant, clear summary using an LLM API.

## Features
- Upload any PDF through a clean web interface
- Extracts text automatically
- Generates a structured, easy-to-read summary using Groq's Llama 3.3 model

## Tech Stack
- **Python**
- **Streamlit** — web interface
- **Groq API** — AI summarization (Llama 3.3 70B)
- **pypdf** — PDF text extraction

## How it works
1. User uploads a PDF
2. The app extracts the text content
3. The text is sent to an LLM with a summarization prompt
4. The summary is displayed instantly in the browser

## Setup
1. Clone this repo
2. Install dependencies: `pip install streamlit groq pypdf python-dotenv`
3. Create a `.env` file with your Groq API key: