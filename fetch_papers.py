import requests
import argparse

def fetch_arxiv_papers(query, max_results):
    params = {
        'search_query': query,
        'max_results': max_results
    }
    # print(f"params = {params}")
    response = requests.get('http://export.arxiv.org/api/query', params=params)
    # print(f"response.url = {response.url}")
    return response.text

import xml.etree.ElementTree as ET

def parse_arxiv_xml(xml_data):
    # Parse the XML data
    root = ET.fromstring(xml_data)

    # List to store parsed data
    parsed_data = []

    # Iterate over each entry in the XML
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        # Extract title
        title = entry.find('{http://www.w3.org/2005/Atom}title').text

        # Extract all authors
        authors = [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')]

        # Extract abstract
        abstract = entry.find('{http://www.w3.org/2005/Atom}summary').text

        # Append the extracted information to the list
        parsed_data.append({
            'title': title,
            'authors': authors,
            'abstract': abstract
        })

    return parsed_data


def main():
    parser = argparse.ArgumentParser(description='Fetch papers from arXiv.')
    parser.add_argument('query', type=str, help='Search query for arXiv papers')
    args = parser.parse_args()

    results = fetch_arxiv_papers(args.query)
    print(results)

if __name__ == "__main__":
    main()
