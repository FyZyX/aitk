import requests
import streamlit as st
from bs4 import BeautifulSoup


@st.cache_data
def get_links(url):
    with st.spinner():
        res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    submissions_div = soup.find('div', {'id': 'submissions'})
    grid_div = submissions_div.find('div', {'class': 'grid'})

    links = grid_div.find_all('a')
    return [link['href'] for link in links]


def main():
    st.title('Project Submissions URL Finder')
    hackathon_url = "https://lablab.ai"
    endpoint = "/event/anthropic-ai-hackathon"

    # url = st.text_input('Enter URL:', hackathon_url + endpoint)
    # if url:
    #     endpoints = get_links(url)
    #     st.metric("Number of Submissions", len(endpoints))
    #     links = [f"- {hackathon_url + endpoint}" for endpoint in endpoints]
    #     st.markdown("\n".join(links))


if __name__ == '__main__':
    main()
