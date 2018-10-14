import re
import process

# return list of [h, date, subject, author, email, file, insertions, deletions]
def gitNumstat():
    numstat = list()
    lines = process.execute("git log --pretty=tformat:'%h,%aI,%s,%aN,%ae' --numstat --no-merges").split("\n")
    
    for line in lines:
        match = re.match(r"(\w+),([0-9\-T:\+]+),(.*),(.*),([a-zA-Z0-9_\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+)", line)
        if match: 
            (file, insertions, deletions) = ("", 0, 0)
            h = match.group(1)
            date = match.group(2)
            subject = match.group(3)
            author = match.group(4).title()
            email = match.group(5)
        
        elif re.match(r"\d+\t+\d+\t+.+", line):
            (insertions, deletions, file) = line.split("\t")
            numstat.append([h, date, subject, author, email, file, int(insertions), int(deletions)])
    
    return numstat


# return list of [file, author, email, content]
def gitBlame():
    blame = list()
    files = process.execute("git ls-files").split("\n")[0:-1]
    
    for file in files:
        try:
            lines = process.execute("git blame --line-porcelain %s" % file).split("\n")
            for line in lines:
                authorMatch = re.match(r"author (.+)", line)
                emailMatch = re.match(r"author-mail <(.+)>", line)
                if authorMatch:
                    author = authorMatch.group(1).title()
                    email = ""
                
                elif emailMatch:
                    email = emailMatch.group(1)
                
                elif line.startswith("\t"):
                    content = line[1:]
                    blame.append([file, author, email, content])
        
        except process.ProcessException:
            continue
    
    return blame
