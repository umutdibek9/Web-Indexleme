import requests
from bs4 import BeautifulSoup
import operator

#1.Aşama/Frekansları bulmamızı sağlayan döngü yapıları ve fonsiyonlar

def wordfreq(url):
    words=[]

    def symbols(words):
        nonsymbol = []
        symboll = "?1234567890,./;'&-=·›|#!@:`~+[’]$%^*()_{}\"<>"
    
        for word in words:

            #lower metodu büyük olan harfleri küçük olarak yazmamızı sağlamıştır.
            word = word.lower()
            #Sembolü bulup onun yerine replace metodu ile tanımlanan boşluk,yer değiştirme yapar ve aşağıda verilen append metodu ile de yeni kelime eklemeye devam eder.
            for symbol_i in symboll:
                if symbol_i in word:
                    word=word.replace(symbol_i,"")

            if(len(word) > 0):
                nonsymbol.append(word)    

        return nonsymbol            

    a = requests.get(url)

    soup = BeautifulSoup(a.content,"html.parser")


    for word_g in soup.find_all("body"):
        text = word_g.text
        words_i = text.split()
#split() karakter dizilerini bölmek amacıyla kullanıldı.
        for word in words_i:
            words.append(word)
#append() dizinin sonuna karakter eklemek için kullanıldı.

    words = symbols(words)

    copy_i = words.copy()

    def dictCreate(words):
        wordvalue = {}
#sıralama yapılması için kullanılan döngü yapısı
        for word in words:
            if word in wordvalue:
                wordvalue[word] = wordvalue[word] + 1
            else:
                wordvalue[word] = 1

        return wordvalue

    wordvalue = dictCreate(words)

    wordSorted = sorted(wordvalue.items(),key = operator.itemgetter(1),reverse = True)

    return wordSorted

"""------------------------------------------------------------------------------------------------"""
#2.Aşama/Anahtar kelimeleri bulmamızı sağlayan döngü yapıları ve fonsiyonlar


def key_word(dict_1, url):

#sembolleri ayıklamak için kullanıldı.

    def symbols(words):
        nonsymbol = []
        symboll = "?1234567890,./;'&-=·›|#!@:`~+[’]$%^*()_{}\"<>"
    
        for word in words:

            
            word = word.lower()

            for symbol_i in symboll:
                if symbol_i in word:
                    word=word.replace(symbol_i,"")

            if(len(word) > 0):
                nonsymbol.append(word)    

        return nonsymbol


    a = requests.get(url)
    soup = BeautifulSoup(a.content, "html.parser")


    indexStr = soup.title.string.split()
    indexStr = symbols(indexStr)

    copyStr = indexStr.copy()

    counter = 0
    keyDict = []

    for word in dict_1:
        if (counter == 10):
            break
        keyDict .append((word[0], word[1]))
        counter=counter+1
    return keyDict

#3.Aşama/İki URL Arasındaki Benzerlik Skorlamasını bulmamızı sağlayan fonksiyonlar ve döngüler   

def key_word(dict_1, url):

#sembolleri ayıklamak için kullanıldı.

    def symbols(words):
        nonsymbol = []
        symboll = "?1234567890,./;'&-=·›|#!@:`~+[’]$%^*()_{}\"<>"
    
        for word in words:

            
            word = word.lower()

            for symbol_i in symboll:
                if symbol_i in word:
                    word=word.replace(symbol_i,"")

            if(len(word) > 0):
                nonsymbol.append(word)    

        return nonsymbol


    a = requests.get(url)
    soup = BeautifulSoup(a.content, "html.parser")


    indexStr = soup.title.string.split()
    indexStr = symbols(indexStr)

    copyStr = indexStr.copy()


    counter = 0
    keyDict = []

    for word in dict_1:
        if (counter == 10):
            break
        keyDict.append((word[0], word[1]))
        counter=counter+1
        ExList = list()
    for i, j in keyDict :
        ExList.append(i)

    return keyDict

#benzerlik skorlaması için döngü yapıları ve fonksiyonlar
def likeRate(key_word, words):
    counter2 = 0
    wordNum = 0
    for keyy in key_word:
        for word in words:
            if(keyy [0] == word[0]):
                counter2=counter2+(word[1]+keyy [1])

    for word in words:
        wordNum=wordNum+word[1]

    for word in key_word:
        wordNum=wordNum+word[1]
  

    return ((float(counter2 )/float(wordNum))*100.0)    

#4.Aşama/İki URL Arasındaki Benzerlik Skorlamasını bulmamızı sağlayan fonksiyonlar ve döngüler 

def get_url(url):

        
    a = requests.get(url)

    soup = BeautifulSoup(a.content,"html.parser")




   




    