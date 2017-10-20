

# Class Features:
#    Objective: Creates a corpus of all the concepts used in all the documents and reduce the number of dimensions

#    ===>       Class Constructor  ====> input: multiple dictionaries each containing all unique nouns in each of the documents
#                                  ====> self.n_corpus      ==> List containing all unique nouns from all doucments.

#    ===>       reduced_corpus     ====> clusters similar nouns together in different lists 

#    ===>       max_similarity     ====> Calculates the maximum semantic similarity between two words using WordNet's library.




import itertools
from nltk.corpus import wordnet as wn
class Concept_Corpus:
    def __init__(self,*nfile):
        n_corpus = []
        for file in nfile:
            n_corpus+=file.keys()
        #Extract keys from each of the dictionaries and add them to a single list
        self.n_corpus = list(set(n_corpus))  
        #Removes repeated terms
    
    def reduced_corpus(self):
        corpus = []
        for i in range(len(self.n_corpus)-1):
            if i ==0:
                corpus.append([self.n_corpus[i]])
                primary = 0
            else:
                for c in range(len(corpus)):
                    if self.n_corpus[i] in corpus[c]:
                        primary = c
                        break
                    elif c == len(corpus)-1:
                        corpus.append([self.n_corpus[i]])
                        primary = len(corpus)-1
            
            for j in range(i+1,len(self.n_corpus)):
                if self.max_similarity(self.n_corpus[i],self.n_corpus[j]) >= 0.5:
                    if self.n_corpus[j] not in corpus[primary]:
                        corpus[primary].append(self.n_corpus[j])
        #Iterate through all possible combinations of nouns and checks for similarity to cluster similar nouns together
        return(corpus)
    
    def max_similarity(self,word1,word2):
        term1 = wn.synsets(word1,pos='n')
        term2 = wn.synsets(word2,pos='n')
        #Each of the above terms contain various synsets each representing one of the many senses of a word.
        maxsim = 0
        for syn1 in term1:
            for syn2 in term2:
                sim = wn.path_similarity(syn1,syn2)
                if sim == None:
                    sim =0
                if sim > maxsim:
                    maxsim = sim
        return(maxsim)
   


#Uncomment the below region for testing code integrity
#Raw_Text = "As St.Francis high school dropout myself and now a mother of six children, one kid being a recent high school graduate, one just entering high school, and another soon to enter high school in a year with three others trailing behind, I often find myself reflecting on my high school years. Why was I so unmotivated to finish high school? What made me want to go back to school? The question it all comes down to is, what can be done to prevent high school students from losing motivation, detouring them from dropping out and not becoming just another statistic? Motivating high school students may seem like a daunting task; however, it is easier than we think by encouraging them, helping them acquire their own aspirations, and making school interesting. Students will not only meet graduation requirements, but they will feel a sense of accomplishment while doing it."
#
#text1 = tokenizer.Tokenizer(Raw_Text)
#print(text1.nounset)
#x = Concept_Corpus(text1.nounset,text1.nounset)
#print(x.n_corpus)
#print(x.reduced_corpus())
