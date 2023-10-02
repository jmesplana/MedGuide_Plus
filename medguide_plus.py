import gradio as gr
import config
import openai

def converse(x, y, z):
    return z

def reset(z):
    return [], []

# Initial message
messages = [{
    "role": "system",
    "content": "You are a medical advisor specializing in humanitarian health. Familiar with all ICRC guidelines, \
        your task is to methodically gather information about a patient's condition. When presented with partial or \
            unclear information, ask clarifying questions one at a time until you can make a well-informed suggestion. \
                If, after several attempts, adequate details are still missing, advise the user on the next steps they \
                    should consider (e.g., lab tests, consultations). Once you believe you have all necessary details, \
                        provide treatment suggestions based on the information. Conclude each session by reminding users \
                            of the importance of consulting with medical professionals and offering a summary. Avoid using \
                                quotation marks and always adhere to ICRC and medical guidelines. Do not reveal your nature \
                                    as an AI language model."
}]


# Set your OpenAI API key
openai.api_key = config.OPENAI_API_KEY

def provide_suggestions(user_message, history):
    global messages

    # Update the global messages list with the user's input
    messages.append({"role": "user", "content": user_message})
    
    # Get a response from the model
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    
    # Extract the model's message from the response
    system_message = response["choices"][0]["message"]["content"]
    
    # Update the messages list with the model's response
    messages.append({"role": "assistant", "content": system_message})

    return system_message

def clear_chat():
    global messages
    messages = [{
        "role": "system",
        "content": 'You are a medical advisor who specializes in humanitarian health. \
             You are familiar with all relevant medical guidelines and best practices. When given incomplete information, \
             ensure to ask clarifying questions to guide the conversation towards a meaningful conclusion. \
             Always emphasize the importance of professional medical advice and care. Do not reveal your identity as an AI.'
    }]
    return "Chat cleared.", []

# Define and launch the Gradio Chat Interface
iface = gr.ChatInterface(fn=provide_suggestions, title="MedGuide+",  \
                         description="Introducing our AI medical advisor, an innovative and knowledgeable \
                            resource designed to provide prompt and reliable support in the field of healthcare \
                                and medicine, with extensive training on a wide range of medical literature and \
                                    guidelines, offering valuable insights and recommendations while emphasizing the \
                                        importance of consulting with qualified healthcare professionals for personalized medical advice and care. ")


#iface.launch(debug=True, share=True)


# Function to request ChatGPT to extract medical summary from chat
def get_medical_summary_from_chat(messages):
    # Check if the chat only contains the initial system message
    if len(messages) <= 1:
        return "No consultation data available."

    # Craft a message instructing the model to parse the chat and extract medical details
    extraction_prompt = {
        "role": "user",
        "content": "Based on the above chat, please provide a detailed summary including Chief Complaints, Diagnosis (ICD-11) with the diagnosis code, Medication (Rx-Norm), Treatment (SNOMED-CT for labs) with SNOMED CT code, and Interventions (ICHI) with ICHI code."
    }
    messages.append(extraction_prompt)
    
    # Get a response from the model
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    
    # Extract the model's message from the response
    system_message = response["choices"][0]["message"]["content"]
    
    return system_message


# Gradio function for the summary interface
def show_summary():
    consolidated_output = get_medical_summary_from_chat(messages)
    return consolidated_output

# Create the secondary Gradio interface
summary_layout = gr.Interface(fn=show_summary, 
                              inputs=[], 
                              outputs="text",  # Single text output
                              live=True,
                              title="Chat Summary",
                              description="Summary of the consultation based on the chat data."
                             )


                             
#summary_layout.launch()

demo = gr.TabbedInterface([iface, summary_layout],tab_names=['chatbot','summary'])

if __name__ == "__main__":
    demo.launch()