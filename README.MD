# 🛟 Disaster Response & Relief Explainer Bot
**[🔗 View Live Demo](http://localhost:8501/)**
## Summary

**Disaster Response & Relief Explainer Bot** is a responsible Gen-AI application designed to help citizens understand disaster management processes in simple, clear language.

### Key Features

✅ **Explains disaster response & relief workflows** in simple language  
✅ **Helps citizens understand** evacuation, relief distribution, and safety steps  
✅ **Answers are short, polite, and easy to understand**  
✅ **Designed only for awareness** (no alerts, no predictions)  
✅ **Does not coordinate rescue** or give live emergency instructions  
✅ **Reduces panic** and repetitive emergency helpline queries  

### Technology Stack

- **Built using Gemini Flash + Streamlit**
- **System prompt ensures safe and restricted responses**
- **Demonstrates responsible Gen-AI for disaster management**

## How It Works

The bot uses a carefully crafted system prompt to ensure it:
- Only explains disaster-related processes
- Provides calm, summarized responses (2-6 sentences)
- Avoids giving alerts, predictions, or rescue coordination
- Redirects unrelated questions politely

## Getting Started

### Prerequisites
- Python 3.8+
- Streamlit
- Google Generative AI SDK

### Installation

```bash
pip install streamlit google-genai
```

### Running the Application

```bash
streamlit run user.py
```

### Environment Variables

Set your Google API key:
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

## Usage

Simply ask questions about disaster response processes, such as:
- "How does relief distribution work after floods?"
- "What are the evacuation procedures during earthquakes?"
- "How is emergency shelter allocated?"

The bot will provide clear, calm explanations to help you understand the processes.

## Responsible AI

This application demonstrates responsible use of generative AI by:
- Limiting scope to educational explanations only
- Avoiding emergency coordination or predictions
- Providing clear disclaimers about its limitations
- Encouraging users to follow official government guidance

## License

This project is open source and available for educational and disaster awareness purposes.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the bot's educational value.



