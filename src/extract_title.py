
def extract_title(markdown):
    list_of_lines = markdown.split('\n')
    for line in list_of_lines:
        if len(line)<3:
            continue
        if line[:2] == '# ':
            heading = line[2:]
            heading = heading.strip()
            return heading
    raise Exception('No Heading Found')

