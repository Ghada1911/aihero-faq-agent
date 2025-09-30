import re

text = 'Visit https://example.com. Also check https://test.org!'
url_pattern = r'(?<!\[)(?<!\()(?<!<)(https?://[^\s<>\)]+)(?!\])(?!\))(?!>)'
matches = re.findall(url_pattern, text)
print('Matches found:', repr(matches))

def replace_url(match):
    full_url = match.group(1)
    print('Original URL:', repr(full_url))
    # Extract trailing punctuation
    trailing_punct = ''
    url = full_url
    while url and url[-1] in '.,;:!?':
        trailing_punct = url[-1] + trailing_punct
        url = url[:-1]
    print('Stripped URL:', repr(url))
    return f'[{url}]({url})'

result = re.sub(url_pattern, replace_url, text)
print('Final result:', repr(result))