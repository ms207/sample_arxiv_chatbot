from mvp import mvp_arxiv_summarizer
from langchain.llms import OpenAI
import argparse

import os

def create_llm_object():
    # Retrieve API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables")

    llm = OpenAI(api_key=api_key)
    return llm

def answer_question(llm, question, context):
    prompt = f"{context}\n\nQuestion: {question}\nAnswer:"
    response = llm.generate([prompt], max_tokens=100)
    return response

def main():
    parser = argparse.ArgumentParser(description='Fetch papers from arXiv.')
    parser.add_argument('query', type=str, help='Search query for arXiv papers')
    args = parser.parse_args()
    user_query = args.query
    summaries: list = mvp_arxiv_summarizer(user_query, max_results=5)
    llm = create_llm_object()
    context:str = " ".join(summaries)  # Combine all summaries into a string
    # Start of chatbot
    while True:
        user_question = input("Ask a question (or type 'exit' to quit): ")
        if user_question.lower() == 'exit':
            break
        response = answer_question(llm, user_question, context)
        print("Answer:", response)

if __name__ == "__main__":
    main()
