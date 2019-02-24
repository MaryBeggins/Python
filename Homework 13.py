def read_text():
    with open('text.txt', encoding='utf-8-sig') as f:
        text = f.read()
        text = text.replace(' ', '\n')
        text = text.replace('.', '')
        text = text.replace(',', '')
        text = text.replace('?', '')
        text = text.replace(':', '')
        text = text.replace(';', '')
        text = text.replace('!', '')
        text = text.replace('"', '')
        text = text.replace('(', '')
        text = text.replace(')', '')
            
    return text

def liaste():
    a = read_text()
    words = a.split()

    return words

def word_hood():
    b = liaste()
    hod = []

    for i in range (len(b)):
        if b[i][-4:] == 'hood':
            hod.append(b[i])

    return hod

def slov_hood():
    c = word_hood()
    hood = {}
    for word in c:
       if word in hood: 
           hood[word] += 1 / len(c)
       else:
           hood[word] = 1 / len(c)
    return hood


def min_freq():
    d = slov_hood()
    min_freq = 1
    for key in sorted(d):
        if (d[key] < min_freq):
            min_freq = d[key]
            slovo = key
            
    return slovo

def kolichestvo():
    d = slov_hood()
    keys = list(d.keys())
    kol = len(keys)

    return kol

def nachalo():
    d = slov_hood()
    keys = list(d.keys())

    for i in range(len(keys)):
        keys[i]=keys[i][:-4]

    return keys

def main():
    
    b=min_freq()
    c=kolichestvo()
    d=nachalo()

    print("Слов с данным суффиксом: ", c)
    print("Слово с минимальной частотностью: ", b)
    print("Слова, от которых образованы: ", d)

if __name__ == '__main__':
    main()

