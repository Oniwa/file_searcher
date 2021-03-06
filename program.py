from pathlib import Path
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("We can't search for nothing.")
        return

    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1
        # print(m)
        print('----------MATCH----------')
        print(f'file: {m.file}')
        print(f'line: {m.line:,}')
        print(f'match: {m.text.strip()}')
        print()
    print(f'Found {match_count:,} matches.')


def print_header():
    print('--------------------------------------')
    print('            FILE SEARCH APP')
    print('--------------------------------------')


def get_folder_from_user():
    folder = input("What folder do you want to search? ")
    if not folder or not folder.strip():
        return None
    else:
        folder = Path(folder)

    if not folder.is_dir():
        return None

    return folder.absolute()


def get_search_text_from_user():
    text = input("What are you searching for [single phrases only]? ")
    return text.lower()


def search_folders(folder, text):
    items = Path(folder)

    for item in items.iterdir():
        if item.is_dir():
            yield from search_folders(item, text)
        else:
            yield from search_file(item, text)


def search_file(filename, search_text):
    with open(filename, 'r', encoding='utf-8') as fin:
        for line_num, line in enumerate(fin):
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                yield m


if __name__ == '__main__':
    main()
