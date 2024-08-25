import streamlit as st
import pandas as pd
from openai import AzureOpenAI

# Load the data
df = pd.read_csv(r'E:\chatbot_floodai_iitgn\Untitled spreadsheet - Sheet1 (1).csv')
# Initialize the Azure OpenAI client
openai_api_key = "78a7f8fb40a44e0eb56fac5a142a8ad5"
openai_endpoint = "https://azopenai2024.openai.azure.com/"
client = AzureOpenAI(api_key=openai_api_key, api_version="2024-02-01", azure_endpoint=openai_endpoint)

# Create a Streamlit app
def chatbot():
    st.title("Flood Assistance Chatbot")

    # Get user input
    user_input = st.text_input("Enter your query:")

    # Get column names
    column_names = df.columns.tolist()

    # Define the chatbot response function
    def rag(user_input, column_names):
        data_summary = df.head(100).to_csv(index=False)
        response = client.chat.completions.create(
            model="MSOpenAIModel",
            messages=[
                {"role": "system", "content": "There is a flood. you are here to resolve their queries. tell user about the single city mentioned in query its road and traffic as well as water logging. if a route is asked generate a route from nearest city to goal city through those with less affected areas shortest route possible."},
                {"role": "user", "content": data_summary + ' so now for data column names are ' + 'now give the output from this given data'}
            ]
        )
        return response.choices[0].message.content

    # Display the chatbot response
    if st.button("Get Response"):
        response = rag(user_input, column_names)
        st.write("Chatbot: ", response)

# Run the Streamlit app
if __name__ == "__main__":
    chatbot()