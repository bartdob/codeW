def domain_name(url):
    newUrl = ""
    if url[0] == 'w' or url[0] == 'h':
        for j, i in enumerate(url):
            if j+1 < len(url):
                if url[j] == "/" and url[j+1] == "/" or url[j] == "w" and url[j+1] == ".":
                    newUrl = url[j+2]
                    for s in range(j+3, len(url)):
                        newUrl = newUrl + url[s]
                        if url[s+1] == ".":
                            break
    else: 
        for s, m in enumerate(url): 
            if s+2<len(url):
                newUrl = newUrl + url[s]
                if url[s+1] == ".":
                    break

    return (newUrl)
