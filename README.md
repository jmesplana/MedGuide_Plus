# MedGuide+ Chatbot

The MedGuide+ chatbot is an AI-powered medical advisor that specializes in humanitarian health. It is designed to provide prompt, reliable support in the field of healthcare and medicine. The chatbot offers valuable insights and recommendations while emphasizing the importance of consulting with qualified healthcare professionals for personalized medical advice and care.

## Features

- **Guided Consultation**: The chatbot methodically gathers information about a patient's condition. When presented with partial or unclear information, it will ask clarifying questions until it can provide a well-informed suggestion.
- **Treatment Recommendations**: Once all necessary details are acquired, the chatbot provides treatment suggestions based on the collected information.
- **Summary Extraction**: At the end of each session, users can request a detailed summary of the consultation, which includes Chief Complaints, Diagnosis, Medication, Treatment, and Interventions.
  
## Setup

1. Ensure you have `gradio`, `config`, and `openai` libraries installed.
2. Set your OpenAI API key in the `config.py` file.
3. Run the main script to launch the chatbot.

## Usage

Run the main script:

```bash
python medguide_plus.py
```

This will launch the MedGuide+ chatbot. Engage with the chatbot by providing medical details or asking questions. At the end of the consultation, you can request a summary of the chat for a consolidated view of the advice provided.

## Note

Always remember that while the chatbot provides valuable medical insights, it is crucial to consult with medical professionals for any health-related concerns.

---

This `README.md` file provides an overview of the MedGuide+ chatbot, its features, setup instructions, and usage guidelines. You can place this in the root directory of your GitHub repository. Make sure to replace `medguide_plus.py` with the actual name of your script if it's different.
