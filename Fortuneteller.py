#А эта программа вам погадает и даст ответ на вопрос, для неё надо использовать текстовый файл book.txt

def listen_question():
    quest = input("Введите вопрос, заканчивающийся вопросительным знаком: ")

    if quest[len(quest)-1]=='?':
        quest=quest[:-1]
        slovo=quest.split(' ')
        return len(slovo[len(slovo)-1])
    else:
        while quest[len(quest)-1]!='?':
            print ("Вы не забыли вопросительный знак?")
            quest = input("Здравствуй, путник, введи интересующий тебя вопрос, заканчивающийся вопросительным знаком: ")
        quest=quest[:-1]
        slovo=quest.split(' ')
        slovo = len(slovo[len(slovo)-1])
        return slovo

def read_book():
    with open("book.txt", encoding='utf-8') as f:
        text=f.read()
    
    return text


def answer():
    
    a=listen_question()
    b=read_book()

    b=b.split('\n')

    i=1
    for i in range (len(b)):
        b[i-1]=list(b[i-1])


    i=0
    x=0
    for i in range (len(b)-1):
        if b[i][0]== '"':
            x+=1



    i=0
    y=0
    for i in range(len(b)-1):
        if b[i][0]=='"':
            y+=1
            if y==(a%x+1):
                line=b[i]
           

    answer=''.join(line)
        
            
    return answer


def print_answer():
    
    key=answer()
    print("Моя книга никогда не лжёт, и сейчас она отвечает: ", key)

def main():
    
    a=print_answer()
    print(a)

if __name__ == '__main__':
    main()
