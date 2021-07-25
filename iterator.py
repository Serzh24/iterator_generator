import json

class Wiki:

    url = 'https://en.wikipedia.org/wiki/'

    def __init__(self, path, path_link=None):
        self.path = path
        self.path_link = path_link

    def __iter__(self):
        with open(self.path, encoding='utf-8') as file:
            self.countries = json.load(file)
        return self

    def __next__(self):
        if not self.countries:
            raise StopIteration

        country = self.countries.pop()['name']['common']

        if self.path_link is not None:
            with open(self.path_link, "a", encoding="utf-8") as file:
                file.write(country+' - ' + self.get_link(country) + '\n')

        return country

    def get_link(self, country):
        return self.url + country.replace(' ', '_')


if __name__ == '__main__':
    for el in Wiki('countries.json', 'countries_links.txt'):
        print(el)

