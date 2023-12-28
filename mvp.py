from fetch_papers import fetch_arxiv_papers, parse_arxiv_xml
from summarize import summarize_text

def mvp_arxiv_summarizer(user_query, max_results):
    # Fetch papers related to the query
    xml_data = fetch_arxiv_papers(user_query, max_results)
    # print(f"xml_dat = {xml_data}")
    parsed_data = parse_arxiv_xml(xml_data)
    # print(f"parse_data = {parsed_data}")
    abstracts = [paper['abstract'] for paper in parsed_data]

    summaries = []
    for abstract in abstracts:
        summary = summarize_text(abstract)
        summaries.append(summary)

    return summaries

import argparse

def main():
    parser = argparse.ArgumentParser(description='Fetch papers from arXiv.')
    parser.add_argument('query', type=str, help='Search query for arXiv papers')
    args = parser.parse_args()
    user_query = args.query
    summaries = mvp_arxiv_summarizer(user_query)
    for summary in summaries:
        print(summary)

if __name__ == "__main__":
    main()
