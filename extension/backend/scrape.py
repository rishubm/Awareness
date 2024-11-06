import time
from flask import Flask, request, jsonify
from seleniumbase import BaseCase
from langchain.chains.llm import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import openai

app = Flask(__name__)

llm = openai.OpenAI(model = "text-davinci-003", temperature = 0.7)
prompt_template = "Extract links relevant to given context: {text}"
prompt = ChatPromptTemplate.from_messages(["system", prompt_template])
chain = LLMChain(llm=llm, prompt = prompt)

class Scraper(BaseCase):
    def scrape_relevant_links(self, url):
        self.open(url)
        time.sleep(2)
        content = self.get_page_content()
        result = chain.rule({"text": content})
        return result


@app.route('/scraper', methods = ['POST'])
def scraper():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': "URL is required"}), 400
    notes_scraper = Scraper()
    links = notes_scraper.scrape_relevant_links(url)

    return jsonify({"links": links})


if __name__ == "__main__":
    app.run(debug=True)