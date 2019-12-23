import requests
from bs4 import BeautifulSoup


def clean_links(links):
    results = []
    for link in links:
        hashIndex = link.find('#')
        if hashIndex > -1:
            link = link[:hashIndex]
        queryStringIndex = link.find('?')
        if queryStringIndex > -1:
            link = link[:queryStringIndex]
        if len(link) > 0 and link != '/':
            results.append(link)
    return sorted(list(set(results)))


def get_links(a_elements):
    links = [link.get('href')
             for link in a_elements if link.get('href') != None and link.get('href') != '']
    links_internal = clean_links([l for l in links if l[0] != 'h'])
    links_external = clean_links([l for l in links if l[0] == 'h'])
    return links_internal, links_external


def print_links(links):
    for link in links:
        print(link)


def run(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    a_elements = soup.find_all('a')
    links_internal, links_external = get_links(a_elements)

    print('-' * 100)
    print(f'URL: {url}')
    print()
    print(f'INTERNAL: {len(links_internal)}')
    print_links(links_internal)
    print()
    print(f'EXTERNAL: {len(links_external)}')
    print_links(links_external)
    print()
    print()


if __name__ == "__main__":
    urls = [
        'https://www.python.org/',
        'https://www.datacamp.com/',
        'https://realpython.com/',
        'https://reactjs.org',
        'https://graphql.org',
        'https://apollographql.com',
        'https://principledgraphql.com',
        'https://twitter.com',
        'https://www.instagram.com/',
        'https://facebook.com',
    ]
    for url in urls:
        run(url)
