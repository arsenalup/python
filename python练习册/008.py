from bs4 import BeautifulSoup


def find_content(path):
    with open(path) as f:
        soup = BeautifulSoup(f, 'lxml')
        content = soup.get_text().strip('\n')
        return content

if __name__ == '__main__':
    find_content()
