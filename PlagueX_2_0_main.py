import os
import glob
import PlagueX_2_0_tokenizer
import PlagueX_2_0_concept_corpus
import PlagueX_2_0_mini_corpus
import PlagueX_2_0_sem_eval
import itertools
raw_text = []
filenames = []
for infile in glob.glob( os.path.join('Test Cases/', '*.txt') ):
    f=open(infile, 'r')
    filenames.append(infile)
    raw_text.append(f.read())

file_combs =            list(itertools.combinations(range(len(raw_text)), 2))
tokenized_objects =     list(map(lambda text: PlagueX_2_0_tokenizer.Tokenizer(text),raw_text))
token_data =            list(map(lambda token_object: token_object.tokenized_text, tokenized_objects ))
nounset_list =          list(map(lambda token_object: token_object.nounset, tokenized_objects ))
noun_indices =          list(map(lambda token_object: token_object.noun_index, tokenized_objects ))
primary_corpus = PlagueX_2_0_concept_corpus.Concept_Corpus(nounset_list)
secodary_corpus = PlagueX_2_0_mini_corpus.Mini_Corpus(primary_corpus.doc_data,noun_indices)
semantic_evaluation = PlagueX_2_0_sem_eval.Sem_Eval(secodary_corpus.query_data,token_data)
final_scores = semantic_evaluation.score_data






for index, comb in enumerate(file_combs):
    print("="*100)
    print("Detections between '%s' and '%s':" % (filenames[comb[0]],filenames[comb[1]]))
    print("="*100)
    print("\n")
    if final_scores[index] == []:
        print("\t\tNo Detections")
    for match in final_scores[index]:
        print("\tA: \t'%s'" % match[0])
        print("\tB: \t'%s'" % match[1])
        print("\tScore:\t%r" % match[2])
        print("\n")
    print("\n")






    
    
    
    
