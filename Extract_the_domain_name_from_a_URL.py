def domain_name(url):
    '''
    Write a function that when given a URL as a string,
    parses out just the domain name and returns it as a string. For example:
    domain_name("http://github.com/carbonfive/raygun") == "github"
    domain_name("http://www.zombie-bites.com") == "zombie-bites"
    domain_name("https://www.cnet.com") == "cnet"

    '''
    if 'www.' in url:
        start = url.find('www.') + 4
        step_1 = url[start:]
    elif '//' in url:
        start = url.find('//') + 2
        step_1 = url[start:]
    else:
        step_1 = url

    if '.' in url:
        finish = step_1.find('.')
        return step_1[:finish]
    else:
        return step_1


print(domain_name("http://github.com/carbonfive/raygun"))