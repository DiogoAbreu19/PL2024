import re

def handleTitle(line: str):
    aux = re.match(r'^#+', line)
    n = len(aux.group())
    title = re.sub(r'^[#+\s]+', "", line)

    html = f"<h{n}>{title}</h{n}>\n\n"

    with open("index.html", "a", encoding='utf-8') as f:
        f.write(html)
    
    f.close()

def handleBoldItalic(line: str):
    aux = re.match(r'^\*+', line)
    n = len(aux.group())
    text = re.sub(r'\*+', "", line)

    if n == 1:
        html = f"<i>{text}</i>\n\n"
    if n == 2:
        html = f"<b>{text}</b>\n\n"

    with open("index.html", "a", encoding='utf-8') as f:
        f.write(html)

    f.close()

def handleNumericalList(line: str):
    aux = re.match(r'^\d', line)
    n = aux.group()

    text = re.sub(r'\d+\.\s+', "", line)

    html = ""

    if n == "1":
        html = ("<ol>\n")
        html += (f"\t<li>{text}</li>\n")

    if n == "2":
        html = (f"\t<li>{text}</li>\n")

    if n == "3":
        html = (f"\t<li>{text}</li>\n")
        html += ("</ol>\n\n")

    with open("index.html", "a", encoding='utf-8') as f:
        f.write(html)
    
    f.close()

def handleLinkImage(line: str):
    if line.__contains__("!["):
        text = re.match(r'(.+)\!\[', line)
        link = re.match(r'.+\((.+)\)', line)
        caption = re.match(r'.+\[(.+)\]', line)

        html = f"{text.group(1)} <img src= \"{link.group(1)}\" alt= \"{caption.group(1)}\"\n\n"
        
        with open("index.html", "a", encoding='utf-8') as f:
            f.write(html)
    
    elif line.__contains__("["):
        text = re.match(r'(.+)\[', line)
        link = re.match(r'.+\((.+)\)', line)
        caption = re.match(r'.+\[(.+)\]', line)

        html = f"{text.group(1)} <a href= \"{link.group(1)}\">{caption.group(1)}</a>\n\n"
        
        with open("index.html", "a", encoding='utf-8') as f:
            f.write(html)
            

def parseLine(line: str):
    if line.startswith("#"):
        handleTitle(line)
    if line.startswith("*"):
        handleBoldItalic(line)
    if line[0].isdigit():
        handleNumericalList(line)
    else:
        handleLinkImage(line)
    
def main():
    
    with open('test.md', 'r', encoding='utf-8') as md:
        for line in md:
            if (not line.isspace()):
                line = line.replace("\n", "")
                parseLine(line)

def clearFile():
    with open("index.html", "w"):
        pass

if __name__ == "__main__":
    clearFile()
    main()