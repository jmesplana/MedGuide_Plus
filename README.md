![alt text](https://github.com/jmesplana/MedGuide_Plus/blob/main/medguide_plus.png?raw=true)
<br>

# MedGuide+ Chatbot

The MedGuide+ chatbot is an AI-powered medical advisor that specializes in humanitarian health. It is designed to provide prompt, reliable support in the field of healthcare and medicine. The chatbot offers valuable insights and recommendations while emphasizing the importance of consulting with qualified healthcare professionals for personalized medical advice and care.

## Features

- **Guided Consultation**: The chatbot methodically gathers information about a patient's condition. When presented with partial or unclear information, it will ask clarifying questions until it can provide a well-informed suggestion.
- **Treatment Recommendations**: Once all necessary details are acquired, the chatbot provides treatment suggestions based on the collected information.
- **Summary Extraction**: At the end of each session, users can request a detailed summary of the consultation, which includes Chief Complaints, Diagnosis, Medication, Treatment, and Interventions.

## Tabbed Functionality
### 1. Chatbot
This is the main interface where users can interact with the AI medical advisor.

**Functionality**:
- Gathers information about a patient's condition, asking clarifying questions if needed.
- Once enough information is obtained, it provides medical advice or recommendations.
- Emphasizes the importance of consulting with qualified healthcare professionals for personalized medical advice and care.

### 2. Summary
Provides a summarized view of the chat's contents, extracting and displaying key medical details.

**Functionality**:
- Based on the conversation in the *chatbot* tab, this interface extracts and presents a detailed summary.
- The summary includes Chief Complaints, Diagnosis (with ICD-11 codes), Medication (Rx-Norm), Treatment (with SNOMED-CT codes for labs), and Interventions (with ICHI codes).
  
Switch between the **chatbot** and **summary** tabs to access the respective features.


## Setup

1. Ensure you have `gradio`, `config`, and `openai` libraries installed.
2. Set your OpenAI API key in the `config.py` file.
3. Run the main script to launch the chatbot.

## Usage

Run the main script:

```bash
python medguide_plus.py
```
## Sharing

In the code, when launching the interface, set the `share` parameter to `True`. For example:
```python
demo.launch(share=True)
```

This will launch the MedGuide+ chatbot. Engage with the chatbot by providing medical details or asking questions. At the end of the consultation, you can request a summary of the chat for a consolidated view of the advice provided.

## Note

Always remember that while the chatbot provides valuable medical insights, it is crucial to consult with medical professionals for any health-related concerns.

---

This `README.md` file provides an overview of the MedGuide+ chatbot, its features, setup instructions, and usage guidelines. You can place this in the root directory of your GitHub repository. Make sure to replace `medguide_plus.py` with the actual name of your script if it's different.
