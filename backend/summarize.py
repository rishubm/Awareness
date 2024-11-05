import json
import logging
from langchain_groq import ChatGroq
from langchain_community.document_loaders import SeleniumURLLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate

# Setup logging
logging.basicConfig(level=logging.INFO)

# Initialize Groq LLM
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

loader = SeleniumURLLoader(['https://utexas.campuslabs.com/engage/organization/texasconvergent'])
docs = loader.load()


# Define prompt
prompt = ChatPromptTemplate.from_messages(
    [("system", "Write a concise summary of the following:\\n\\n{context}")]
)

# Instantiate chain
chain = create_stuff_documents_chain(llm, prompt)

# Invoke chain
# result = chain.invoke({"context": docs})

# 1. Function to extract data from a URL
def extract_data_website(url):
    """Extracts data from a given URL."""
    loader = SeleniumURLLoader([url])
    docs = loader.load()
    return docs


# Main function to process URLs from JSON and generate summaries
def process_urls_from_json(json_file_path):
    """Loads URLs from a JSON file, extracts content, and generates summaries."""
    try:
        with open(json_file_path, 'r') as file:
            url_data = json.load(file)
        
        summaries = {}
        
        for entry in url_data:
            url = entry.get('url')
            if url:

                # Extract data from the URL
                docs = extract_data_website(url)

                # Generate summary
                summary = chain.invoke({"context": docs})
                
                # Store summary in the dictionary
                summaries[url] = summary
        
        # Save summaries to JSON
        with open("./json/summaries.json", "w", encoding="utf-8") as outfile:
            json.dump(summaries, outfile, ensure_ascii=False, indent=4)
        
        logging.info("Summaries saved to summaries.json")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Run the process
if __name__ == "__main__":
    json_file_path = "./json/selenium_search_results.json"
    process_urls_from_json(json_file_path)
