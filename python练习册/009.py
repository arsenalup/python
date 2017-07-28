from bs4 import BeautifulSoup


def find_link(path):
    link = []
    with open(path) as f:
        soup = BeautifulSoup(f, 'lxml')
        for i in soup.find_all('a'):
            link.append(i['href'])
        return link

if __name__ == '__main__':
    find_link(path=path)
