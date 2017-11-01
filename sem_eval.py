from tokenizer import Tokenizer
from nltk.corpus import wordnet as wn

doc1 = Tokenizer("Adit and Kaushik are doing the project")

doc2 = Tokenizer("The work is being done by Adit and Kaushik ")
class Sem_Eval:
    def __init__(self, Rawtext1, Rawtext2):
        self.token_text1 = Tokenizer(Rawtext1)
        self.token_text2 = Tokenizer(Rawtext2)
        self.weightlist = {"NN":1.0, "NNP":1.0, "JJ":0.5, "RB": 0.4, "VB":1.0 }                           
    def compare(self):
        maxmatchlist = []
        maxposlist = []
        for word1 in self.token_text1.tokenized_text:
            matchlist = []
            poslist = []
            syn1 = wn.synsets(word1[0])
            for word2 in self.token_text2.tokenized_text:
                syn2 = wn.synsets(word2[0])
                interlist = list(set(syn1) & set(syn2))
                if(word1[0]==word2[0]):
                    matchlist.append(1)
                elif(len(interlist)>0):
                    matchlist.append(1)
                else:
                    matchlist.append(0)

                if(word1[1]==word2[1]):
                    poslist.append(1)
                elif(word1[1][:2] == "VB" and word2[1][:2] == "VB"):
                    poslist.append(0.7)
                elif(word1[1][:2] == "NN" and word2[1][:2] == "NN"):
                    poslist.append(0.7)
                elif(word1[1][:2] == "JJ" and word2[1][:2] == "JJ"):
                    poslist.append(0.7)
                elif(word1[1][:2] == "RB" and word2[1][:2] == "RB"):
                    poslist.append(0.7)
                else:
                    poslist.append(0)
            print(word1[0])        
            print(matchlist)
            print(poslist)
            input()
            maxmatchlist.append(max(matchlist))
            maxposlist.append(max(poslist))
            
        print(maxmatchlist)
        print("\n\n")
        print(maxposlist)
            
comp1 = Sem_Eval("Adit and Kaushik are doing the project", "The work is being done by Adit and Kaushik ")
print(doc1.tokenized_text)
print("\n\n")
print(doc2.tokenized_text)
comp1.compare()
