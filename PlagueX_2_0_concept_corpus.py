

# Class Features:
#    Objective: Creates a corpus of all the concepts used in all the documents and reduce the number of dimensions

#    ===>       Class Constructor     ====> input: multiple dictionaries each containing all unique nouns in each of the documents
#                                     ====> self.n_corpus      ==> List containing all unique nouns from all doucments.

#    ===>       reduced_corpus        ====> clusters similar nouns together in different lists 

#    ===>       doc_datagen           ====> generates a variant of each document containing only its concepts



import itertools
import random
from nltk.corpus import wordnet as wn
class Concept_Corpus:
    def __init__(self,nfile):
        self.nfiles = nfile
        n_corpus = []
        for file in nfile:
            n_corpus+=file
        #Extract keys from each of the dictionaries and add them to a single list
        
        self.n_corpus = list(set(n_corpus))
        self.y_corpus = []
        self.x_corpus = {}
        for term in self.n_corpus:
            synset = wn.synsets(term)
            if synset == []:
                self.y_corpus.append([term])
            else:
                self.x_corpus[term]=synset
        #Removes repeated terms
        self.n_reduced = self.reduced_corpus()
        self.con_code = list(range(len(self.n_reduced)))
        self.doc_data = self.doc_datagen()
    def reduced_corpus(self):
        n_reduced = list()
        for key1 in self.x_corpus:
            wordlist = list()
            for key2 in self.x_corpus:
                interlist =  list(set(self.x_corpus[key1]) & set(self.x_corpus[key2]))
                if(len(interlist)>0):
                    wordlist.append(key2)
            if(wordlist not in n_reduced):
                n_reduced.append(wordlist)
        return(n_reduced+self.y_corpus)
    def doc_datagen(self):
        doc_data = []
        for file in self.nfiles:
            noun_order = []
            for term in file:
                for i in range(len(self.n_reduced)):
                    if term in self.n_reduced[i]:
                        noun_order.append(self.con_code[i])
                        continue
            doc_data.append(noun_order)
        return(doc_data)
                    
                    
            
        
                        

#Raw_Text = "As St.Francis high school dropout myself and now a mother of six children, one kid being a recent high school graduate, one just entering high school, and another soon to enter high school in a year with three others trailing behind, I often find myself reflecting on my high school years. Why was I so unmotivated to finish high school? What made me want to go back to school? The question it all comes down to is, what can be done to prevent high school students from losing motivation, detouring them from dropping out and not becoming just another statistic? Motivating high school students may seem like a daunting task; however, it is easier than we think by encouraging them, helping them acquire their own aspirations, and making school interesting. Students will not only meet graduation requirements, but they will feel a sense of accomplishment while doing it."
#text1 = tokenizer.Tokenizer(Raw_Text)
#x = Concept_Corpus(text1.nounset,text1.nounset)
#print(x.n_reduced)
#print(x.con_code)
#print(x.doc_data)
#

