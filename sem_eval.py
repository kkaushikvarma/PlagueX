from tokenizer import Tokenizer

from nltk.corpus import wordnet as wn
import itertools

class Sem_Eval:
    def __init__(self, query_data, token_data):
        
        self.score_data = []
        
        self.doc_combs = list(itertools.combinations(range(len(token_data)), 2))
        for index, comb  in enumerate(query_data):
            comb_scores = []
            for match in comb:
                text1 = token_data[self.doc_combs[index][0]][match[0][0]:match[0][1]]
                text2 = token_data[self.doc_combs[index][1]][match[1][0]:match[1][1]]
                if len(text1) > len(text2):
                    text1,text2 = text2,text1
                score = self.getscore(text1,text2)
                if score > 0:
                    comb_scores.append((self.get_rawtext(text1),self.get_rawtext(text2),self.getscore(text1,text2)))
            self.score_data.append(comb_scores)
    def get_rawtext(self,text):
        return(" ".join(list(map(lambda token: token[0],text))))
    def getscore(self,text1,text2):
        if len(text1) < 4 or len(text2) < 4:
            return(0)
        score_data = self.compare(text1,text2)
        raw_scores = list(map(lambda score: (score[0]*0.6)+(score[1]*0.4)*score[2],score_data))
        normalization = list(map(lambda score:score[2],score_data))
        
        return(sum(raw_scores)/sum(normalization))
        
    def compare(self,text1,text2):
        weightlist = {"NN":1.0, "JJ":0.8, "RB": 0.8, "VB":0.7 } 
        score_data = []
        for word1 in text1:
            try:
                pos_priority = weightlist[word1[1][:2]]
            except:
                pos_priority = 0.4
            matchlist = []
            poslist = []
            syn1 = wn.synsets(word1[0])
            for word2 in text2:
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
                    poslist.append(0.0)
            score_data.append((max(matchlist),max(poslist), pos_priority ))
        return(score_data)


