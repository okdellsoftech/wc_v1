from django.shortcuts import render

# Create your views here.
from enum import unique
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View,ListView
from django.shortcuts import render, redirect
from .models import *
import re
from collections import Counter
from django.db.models import Avg
from django.contrib import messages
from langdetect import detect


def clean_word(str):
        regex = r"(\w+-\w+)|-+"
        punctuation = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        txt_clean = re.sub(r"[¬]+\ *", "", str).lower()
        w_clean = re.sub(r"[–—‒−]+\ *", "-", txt_clean).lower()
        result = re.sub(r"[,.;@#?!&$»«+=…“”•●■]+\ *", " ", w_clean).lower()
        f_result = re.sub(regex, r"\1", result)
        
        final_string = ''
        for ch in f_result:
            if ch not in punctuation:
                final_string = final_string + ch

        return final_string.split()

def clean_sentences(str):  # sourcery skip: list-comprehension, remove-pass-body  # sourcery skip: list-comprehension, remove-pass-body
    
        str_result = re.sub(r"([0-9]+[,.]+| [,.]+)", "", str)
        clean_str = str_result.strip()
        sentences = re.split(r'[//.|//!|//?]+|(?<!\.)\.(?!\.)', clean_str.replace('\n',''))
        long_s = []
        for word in sentences:
            if word.isdigit() and len(word)<=2:
                pass
            else:
                long_s.append(word)
        
        return long_s[:-1]



def count_syllables_russian(word):
    vowels = "аеёиоуыэюя"
    syllable_count = 0
    is_vowel = False

    for letter in word:
        if letter in vowels:
            if not is_vowel:
                syllable_count += 1
                is_vowel = True
        else:
            is_vowel = False
    
    return syllable_count

def total_syllable_count(text):
    words = text
    total_count = sum(count_syllables_russian(word) for word in words)
    return total_count

class IndexView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'ru/index.html')
    

    def post(self, request, *args, **kwargs):
        title = request.POST['title_name']
        author = request.POST['author']
        message = request.POST['message']

        # Claning & calculating words 
        all_words = clean_word(message)
        words_q=len(all_words)
        level_result=""

        if words_q >3 and detect(message) !='en':

            
            # Calculating quantity of polysyllabic words

            punctuation = '''аеёиоуэюяыөү'''
            def count_syllables_based_on_vowels(word):
                return sum(1 for letter in word if letter in punctuation)

            def is_polysyllabic(word, syllable_threshold):
                syllable_count = count_syllables_based_on_vowels(word)
                return syllable_count >= syllable_threshold


            longw = []
    
            for word in all_words:
                word_without_hyphen = word.replace('-', '')  # Убираем тире для подсчета слогов и анализа длины
                if len(word_without_hyphen) >= 10 and is_polysyllabic(word_without_hyphen, 3):
                    longw.append((word, len(word_without_hyphen)))

            multisyllabic_wq =len(longw)
            
            # Calculating frequencies of polysyllabic words
            longw_frequencies={}
            for words in longw:
                if words in longw_frequencies: 
                    longw_frequencies[words] += 1
                else: 
                    longw_frequencies[words] = 1


            # Calculating %  of polysyllabic words in text
            lword_p = round(((100/words_q) * multisyllabic_wq ),1)
            

            # Cleaning & calculating sentences
            sentence_q = len(clean_sentences(message))

            # Calculsting average numbers of sentences for  text 
            sentence_avg = round((words_q/sentence_q),1)

            # Calculating syllables
            syllables = total_syllable_count(all_words)


            # Calculating syllables average
            syllables_avg = round((syllables / words_q),1)


            # Calculating unique words
            unique_words = []
            for words in all_words:
                if words not in unique_words:
                    unique_words.append(words)
            
            unique_words.sort()
            
            uniquew_q = len(unique_words)

            # Calculation of lexical diversity
            lexical_d = round((uniquew_q / words_q),2)
            

            # Calculating frequencies of words in uploaded text
            w_frequencies={}
            for words in all_words:
                if words in w_frequencies: 
                    w_frequencies[words] += 1
                else: 
                    w_frequencies[words] = 1

            # Start -->    Get list of long & compound words from database
            get_lcwords = LCWord.objects.values_list('lc_words', flat=True). get(id=1)
            clean_lcwords = clean_word(get_lcwords)
            



            # Comparing uploaded text with database of long and compound words
            lcwords_compare=list(set(clean_lcwords) & set(all_words))
            
            

            lcword_list = []
            for clean_lcwords in all_words:
                     if clean_lcwords in lcwords_compare:
                         lcword_list.append(clean_lcwords)
            
            
            

            # Calculation os hyphenated words

            hyphenated_w = re.findall(r'\w+-\w+[-\w+]*', str(all_words))
            for words in hyphenated_w:
                     if len(words) > 6:
                            lcword_list.append(words)
                
             
            

            #  Frequencies long & compound words
            lcword_frequencies={}
            for word in lcword_list:
                 if word in lcword_frequencies: 
                    lcword_frequencies[word] += 1
                 else:
                    lcword_frequencies[word] = 1
            
            lcwords_q=len(lcword_list)
            lcwors_p = round(((100/len(all_words)) * lcwords_q), 1)

           
            #### END ####

            # Start --> Get list of rare words from database

            get_rarewords = RareWord.objects.values_list('rare_words', flat=True). get(id=1)
            clean_rarewords = clean_word(get_rarewords)

            # Comparing uploaded text with database of long and compound words
            rarewords_compare=list(set(clean_rarewords) & set(all_words))

            rareword_list = []
            for clean_rarewords in all_words:
                 if clean_rarewords in rarewords_compare:
                         rareword_list.append(clean_rarewords)

            
            #  frequencies of words
            rareword_frequencies={}
            for word in rareword_list:
                 if word in rareword_frequencies: 
                      rareword_frequencies[word] += 1
                 else:
                      rareword_frequencies[word] = 1

            
            
            rareword_q = len(rareword_list)
            rareword_p = round(((100/len(all_words)) * rareword_q), 1)
            ######### END ###################

            ### Start --> # Get list of frequent words from database

            get_frequent_words = FreqWord.objects.values_list('freq_words', flat=True). get(id=1)
            
            clean_frequent_words = re.sub(r'[^\w\s]', '', get_frequent_words).lower().split()
            
            # Comparing uploaded text with database of frequent words
            freq_words_compare=list(set(clean_frequent_words) & set(all_words))
            
            freqword_list = []
            for clean_frequent_words in all_words:
                     if clean_frequent_words in freq_words_compare:
                         freqword_list.append(clean_frequent_words)

            #  frequencies of words
            fw_frequencies={}
            for word in freqword_list:
                if word in fw_frequencies: 
                    fw_frequencies[word] += 1
                else:
                    fw_frequencies[word] = 1
                    

            fw_q = len(freqword_list)
            fw_p = round(((100/len(all_words)) * fw_q), 1)
            ###END###

            fre_oborneva = round((206.835 - 1.3 * sentence_avg - 60.11 * syllables_avg),2)

            gunning_fog_index = round((0.4*((0.78*sentence_avg)+100*(syllables/words_q))),2)



            ###Levels for Grade1
            g1_word_q_l1 = g1Level.objects.values_list('g1_word_q_l1', flat=True). get(id=1)
            g1_word_q_l2 = g1Level.objects.values_list('g1_word_q_l2', flat=True). get(id=1)
            g1_word_q_l3 = g1Level.objects.values_list('g1_word_q_l3', flat=True). get(id=1)
            g1_sentence_q_l1 = g1Level.objects.values_list('g1_sentence_q_l1', flat=True). get(id=1)
            g1_sentence_q_l2 = g1Level.objects.values_list('g1_sentence_q_l2', flat=True). get(id=1)
            g1_sentence_q_l3 = g1Level.objects.values_list('g1_sentence_q_l3', flat=True). get(id=1)
            g1_avgwl_insyllables_l1 = g1Level.objects.values_list('g1_avgwl_insyllables_l1', flat=True). get(id=1)
            g1_avgwl_insyllables_l2 = g1Level.objects.values_list('g1_avgwl_insyllables_l2', flat=True). get(id=1)
            g1_avgwl_insyllables_l3 = g1Level.objects.values_list('g1_avgwl_insyllables_l3', flat=True). get(id=1)
            g1_avgl_sentences_inw_l1 = g1Level.objects.values_list('g1_avgl_sentences_inw_l1', flat=True). get(id=1)
            g1_avgl_sentences_inw_l2 = g1Level.objects.values_list('g1_avgl_sentences_inw_l2', flat=True). get(id=1)
            g1_avgl_sentences_inw_l3 = g1Level.objects.values_list('g1_avgl_sentences_inw_l3', flat=True). get(id=1)
            g1_longw_q_l1 = g1Level.objects.values_list('g1_longw_q_l1', flat=True). get(id=1)
            g1_longw_q_l2 = g1Level.objects.values_list('g1_longw_q_l2', flat=True). get(id=1)
            g1_longw_q_l3 = g1Level.objects.values_list('g1_longw_q_l3', flat=True). get(id=1)
            g1_compw_q_l1 = g1Level.objects.values_list('g1_compw_q_l1', flat=True). get(id=1)
            g1_compw_q_l2 = g1Level.objects.values_list('g1_compw_q_l2', flat=True). get(id=1)
            g1_compw_q_l3 = g1Level.objects.values_list('g1_compw_q_l3', flat=True). get(id=1)
            g1_rarew_q_l1 = g1Level.objects.values_list('g1_rarew_q_l1', flat=True). get(id=1)
            g1_rarew_q_l2 = g1Level.objects.values_list('g1_rarew_q_l2', flat=True). get(id=1)
            g1_rarew_q_l3 = g1Level.objects.values_list('g1_rarew_q_l3', flat=True). get(id=1)



            ###Levels for Grade2 ###
            g2_word_q_l1 = g2Level.objects.values_list('g2_word_q_l1', flat=True). get(id=1)
            g2_word_q_l2 = g2Level.objects.values_list('g2_word_q_l2', flat=True). get(id=1)
            g2_sentence_q_l1 = g2Level.objects.values_list('g2_sentence_q_l1', flat=True). get(id=1)
            g2_sentence_q_l2 = g2Level.objects.values_list('g2_sentence_q_l2', flat=True). get(id=1)
            g2_avgwl_insyllables_l1 = g2Level.objects.values_list('g2_avgwl_insyllables_l1', flat=True). get(id=1)
            g2_avgwl_insyllables_l2 = g2Level.objects.values_list('g2_avgwl_insyllables_l2', flat=True). get(id=1)
            g2_avgl_sentences_inw_l1 = g2Level.objects.values_list('g2_avgl_sentences_inw_l1', flat=True). get(id=1)
            g2_avgl_sentences_inw_l2 = g2Level.objects.values_list('g2_avgl_sentences_inw_l2', flat=True). get(id=1)
            g2_longw_q_l1 = g2Level.objects.values_list('g2_longw_q_l1', flat=True). get(id=1)
            g2_longw_q_l2 = g2Level.objects.values_list('g2_longw_q_l2', flat=True). get(id=1)
            g2_compw_q_l1 = g2Level.objects.values_list('g2_compw_q_l1', flat=True). get(id=1)
            g2_compw_q_l2 = g2Level.objects.values_list('g2_compw_q_l2', flat=True). get(id=1)
            g2_rarew_q_l1 = g2Level.objects.values_list('g2_rarew_q_l1', flat=True). get(id=1)
            g2_rarew_q_l2 = g2Level.objects.values_list('g2_rarew_q_l2', flat=True). get(id=1)


            ###Levels for Grade3
            g3_word_q_l1 = g3Level.objects.values_list('g3_word_q_l1', flat=True). get(id=1)
            g3_word_q_l2 = g3Level.objects.values_list('g3_word_q_l2', flat=True). get(id=1)
            g3_sentence_q_l1 = g3Level.objects.values_list('g3_sentence_q_l1', flat=True). get(id=1)
            g3_sentence_q_l2 = g3Level.objects.values_list('g3_sentence_q_l2', flat=True). get(id=1)
            g3_avgwl_insyllables_l1 = g3Level.objects.values_list('g3_avgwl_insyllables_l1', flat=True). get(id=1)
            g3_avgwl_insyllables_l2 = g3Level.objects.values_list('g3_avgwl_insyllables_l2', flat=True). get(id=1)
            g3_avgl_sentences_inw_l1 = g3Level.objects.values_list('g3_avgl_sentences_inw_l1', flat=True). get(id=1)
            g3_avgl_sentences_inw_l2 = g3Level.objects.values_list('g3_avgl_sentences_inw_l2', flat=True). get(id=1)
            g3_longw_q_l1 = g3Level.objects.values_list('g3_longw_q_l1', flat=True). get(id=1)
            g3_longw_q_l2 = g3Level.objects.values_list('g3_longw_q_l2', flat=True). get(id=1)
            g3_compw_q_l1 = g3Level.objects.values_list('g3_compw_q_l1', flat=True). get(id=1)
            g3_compw_q_l2 = g3Level.objects.values_list('g3_compw_q_l2', flat=True). get(id=1)
            g3_rarew_q_l1 = g3Level.objects.values_list('g3_rarew_q_l1', flat=True). get(id=1)
            g3_rarew_q_l2 = g3Level.objects.values_list('g3_rarew_q_l2', flat=True). get(id=1)



            ###Levels for Grade4
            g4_word_q_l1 = g4Level.objects.values_list('g4_word_q_l1', flat=True). get(id=1)
            g4_word_q_l2 = g4Level.objects.values_list('g4_word_q_l2', flat=True). get(id=1)
            g4_sentence_q_l1 = g4Level.objects.values_list('g4_sentence_q_l1', flat=True). get(id=1)
            g4_sentence_q_l2 = g4Level.objects.values_list('g4_sentence_q_l2', flat=True). get(id=1)
            g4_avgwl_insyllables_l1 = g4Level.objects.values_list('g4_avgwl_insyllables_l1', flat=True). get(id=1)
            g4_avgwl_insyllables_l2 = g4Level.objects.values_list('g4_avgwl_insyllables_l2', flat=True). get(id=1)
            g4_avgl_sentences_inw_l1 = g4Level.objects.values_list('g4_avgl_sentences_inw_l1', flat=True). get(id=1)
            g4_avgl_sentences_inw_l2 = g4Level.objects.values_list('g4_avgl_sentences_inw_l2', flat=True). get(id=1)
            g4_longw_q_l1 = g4Level.objects.values_list('g4_longw_q_l1', flat=True). get(id=1)
            g4_longw_q_l2 = g4Level.objects.values_list('g4_longw_q_l2', flat=True). get(id=1)
            g4_compw_q_l1 = g4Level.objects.values_list('g4_compw_q_l1', flat=True). get(id=1)
            g4_compw_q_l2 = g4Level.objects.values_list('g4_compw_q_l2', flat=True). get(id=1)
            g4_rarew_q_l1 = g4Level.objects.values_list('g4_rarew_q_l1', flat=True). get(id=1)
            g4_rarew_q_l2 = g4Level.objects.values_list('g4_rarew_q_l2', flat=True). get(id=1)



            if (words_q <= g1_word_q_l3 and  sentence_q <= g1_sentence_q_l3 and syllables_avg <= g1_avgwl_insyllables_l3 and sentence_avg <= g1_avgl_sentences_inw_l3 ) or (words_q <= g1_word_q_l3 and  sentence_q > g1_sentence_q_l3 and syllables_avg <= g1_avgwl_insyllables_l3 and sentence_avg <= g1_avgl_sentences_inw_l3 ) or (words_q <= g2_word_q_l2 and  sentence_q < g1_sentence_q_l3 and syllables_avg <= g1_avgwl_insyllables_l3 and sentence_avg <= g1_avgl_sentences_inw_l3 and multisyllabic_wq  <= g1_longw_q_l3 and lcwords_q <= g1_compw_q_l3):
                    
                    level_result = "1 класс"
                    book = ruText( book_title=title, book_author=author,book_text=message, sentence_q=sentence_q, words_q=words_q, syllables_avg=syllables_avg, sentence_avg=sentence_avg, multisyllabic_wq=multisyllabic_wq, lcwords_q=lcwords_q, lcwords_p=lcwors_p,
                                rareword_q=rareword_q, rareword_p=rareword_p, fw_q=fw_q, fw_p=fw_p, uniq_w=uniquew_q, lexical_div=lexical_d, level_result=level_result, fre_oborneva = fre_oborneva, gunning_fog_index=gunning_fog_index)
                    book.save()
                    messages.info(request, 'загружен')
            
            elif (words_q <= g1_word_q_l3 and  sentence_q <= g1_sentence_q_l3 and syllables_avg >= g1_avgwl_insyllables_l3 and sentence_avg <= g1_avgl_sentences_inw_l3) or (words_q > g1_word_q_l3 and words_q <= g2_word_q_l2 and  sentence_q <= g1_sentence_q_l3 and syllables_avg >= g1_avgwl_insyllables_l3 and sentence_avg > g1_avgl_sentences_inw_l3 and multisyllabic_wq  <= g1_longw_q_l3 and lcwords_q <= g1_compw_q_l3) or (words_q > g1_word_q_l3 and words_q <= g2_word_q_l2 and  sentence_q > g1_sentence_q_l3 and syllables_avg <= g1_avgwl_insyllables_l3 and sentence_avg <= g1_avgl_sentences_inw_l3 and multisyllabic_wq <= g1_longw_q_l3 and lcwords_q <= g1_compw_q_l3) or (words_q <= g1_word_q_l3  and  sentence_q <= g1_sentence_q_l3 and syllables_avg <= g2_avgwl_insyllables_l2 and sentence_avg > g1_avgl_sentences_inw_l3 and multisyllabic_wq <= g1_longw_q_l3 and lcwords_q <= g1_compw_q_l3):
                 
                    level_result = "1 класс: текст нужно проверить"
                    book = ruText( book_title=title, book_author=author,book_text=message, sentence_q=sentence_q, words_q=words_q, syllables_avg=syllables_avg, sentence_avg=sentence_avg, multisyllabic_wq=multisyllabic_wq, lcwords_q=lcwords_q, lcwords_p=lcwors_p,
                                rareword_q=rareword_q, rareword_p=rareword_p, fw_q=fw_q, fw_p=fw_p, uniq_w=uniquew_q, lexical_div=lexical_d, level_result=level_result, fre_oborneva = fre_oborneva, gunning_fog_index=gunning_fog_index)
                    book.save()
                    messages.error(request, 'загружен')
            
            elif (words_q <= g1_word_q_l3 and  sentence_q <= g1_sentence_q_l3 and syllables_avg <= g1_avgwl_insyllables_l3 and sentence_avg > g1_avgl_sentences_inw_l3):
                 
                    level_result = "1 класс: нужно проверить. Средняя длина предложений в словах  " + str(sentence_avg)
                    book = ruText( book_title=title, book_author=author,book_text=message, sentence_q=sentence_q, words_q=words_q, syllables_avg=syllables_avg, sentence_avg=sentence_avg, multisyllabic_wq=multisyllabic_wq, lcwords_q=lcwords_q, lcwords_p=lcwors_p,
                                rareword_q=rareword_q, rareword_p=rareword_p, fw_q=fw_q, fw_p=fw_p, uniq_w=uniquew_q, lexical_div=lexical_d, level_result=level_result, fre_oborneva = fre_oborneva, gunning_fog_index=gunning_fog_index)
                    book.save()
                    messages.info(request, 'загружен')
            

           
            elif (words_q > g1_word_q_l3 and words_q <= g2_word_q_l2 and  sentence_q > g1_sentence_q_l3 and sentence_q <= g2_sentence_q_l2  and sentence_avg > g1_avgl_sentences_inw_l3  and sentence_avg <= g2_avgl_sentences_inw_l2) or (words_q < g2_word_q_l1 and  sentence_q < g2_sentence_q_l1  and syllables_avg > g1_avgwl_insyllables_l3 and syllables_avg <= g2_avgwl_insyllables_l2 and  sentence_avg > g1_avgl_sentences_inw_l3  and sentence_avg <= g2_avgl_sentences_inw_l2 and multisyllabic_wq > g1_longw_q_l3 and multisyllabic_wq<=g2_longw_q_l2) or (words_q < g2_word_q_l1 and  sentence_q < g2_sentence_q_l1  and syllables_avg > g1_avgwl_insyllables_l3 and syllables_avg <= g2_avgwl_insyllables_l2 and  sentence_avg > g1_avgl_sentences_inw_l3  and sentence_avg <= g2_avgl_sentences_inw_l2 and multisyllabic_wq < g2_longw_q_l2 and rareword_q > g1_rarew_q_l3 and rareword_q <= g2_rarew_q_l2 ) or (words_q < g2_word_q_l1 and  sentence_q < g2_sentence_q_l1  and syllables_avg > g1_avgwl_insyllables_l3 and syllables_avg <= g2_avgwl_insyllables_l2 and  sentence_avg > g1_avgl_sentences_inw_l3  and sentence_avg <= g2_avgl_sentences_inw_l2) or (words_q > g1_word_q_l3 and words_q <= g2_word_q_l2 and  sentence_q < g2_sentence_q_l1  and  sentence_avg > g1_avgl_sentences_inw_l3  and sentence_avg <= g2_avgl_sentences_inw_l2 and rareword_q > g1_rarew_q_l3 and rareword_q <= g2_rarew_q_l2) or (words_q > g1_word_q_l3 and words_q <= g2_word_q_l2 and  sentence_q > g1_sentence_q_l3 and sentence_q <= g2_sentence_q_l2 and syllables_avg > g1_avgwl_insyllables_l3 and syllables_avg <= g2_avgwl_insyllables_l2  and  sentence_avg > g2_avgl_sentences_inw_l2):
                    
                    level_result = "2 класс"
                    book = ruText( book_title=title, book_author=author,book_text=message, sentence_q=sentence_q, words_q=words_q, syllables_avg=syllables_avg, sentence_avg=sentence_avg, multisyllabic_wq=multisyllabic_wq, lcwords_q=lcwords_q, lcwords_p=lcwors_p,
                                rareword_q=rareword_q, rareword_p=rareword_p, fw_q=fw_q, fw_p=fw_p, uniq_w=uniquew_q, lexical_div=lexical_d, level_result=level_result, fre_oborneva = fre_oborneva, gunning_fog_index=gunning_fog_index)
                    book.save()
                    messages.info(request, 'загружен')

            
            elif (words_q < g2_word_q_l2  and  sentence_q < g2_sentence_q_l2 and syllables_avg > g1_avgwl_insyllables_l3 and syllables_avg <= g2_avgwl_insyllables_l2 and sentence_avg > g1_avgl_sentences_inw_l3 and sentence_avg <= g2_avgl_sentences_inw_l2 and lcwords_q > g1_compw_q_l3 and lcwords_q <= g2_compw_q_l2 ) or (words_q > g1_word_q_l3 and words_q <= g2_word_q_l2  and  sentence_q >= g2_sentence_q_l2 and syllables_avg > g1_avgwl_insyllables_l3 and syllables_avg <= g2_avgwl_insyllables_l2 and sentence_avg <= g2_avgl_sentences_inw_l2 and lcwords_q <= g2_compw_q_l2 ) or (words_q > g2_word_q_l2  and  sentence_q > g2_sentence_q_l2 and syllables_avg > g1_avgwl_insyllables_l3 and syllables_avg <= g2_avgwl_insyllables_l2 and sentence_avg <= g2_avgl_sentences_inw_l2 and lcwords_q <= g2_compw_q_l2 ) or (words_q > g1_word_q_l3 and words_q <= g2_word_q_l2  and  sentence_q > g2_sentence_q_l2 and syllables_avg > g1_avgwl_insyllables_l3 and syllables_avg <= g2_avgwl_insyllables_l2 and sentence_avg > g1_avgl_sentences_inw_l3 and sentence_avg <= g2_avgl_sentences_inw_l2 and multisyllabic_wq > g1_longw_q_l3 and multisyllabic_wq <= g2_longw_q_l2 ):
                    
                    level_result = "2 класс: текст нужно проверить"
                    book = ruText( book_title=title, book_author=author,book_text=message, sentence_q=sentence_q, words_q=words_q, syllables_avg=syllables_avg, sentence_avg=sentence_avg, multisyllabic_wq=multisyllabic_wq, lcwords_q=lcwords_q, lcwords_p=lcwors_p,
                                rareword_q=rareword_q, rareword_p=rareword_p, fw_q=fw_q, fw_p=fw_p, uniq_w=uniquew_q, lexical_div=lexical_d, level_result=level_result, fre_oborneva = fre_oborneva, gunning_fog_index=gunning_fog_index)
                    book.save()
                    messages.info(request, 'загружен')


            elif (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q > g2_sentence_q_l2 and sentence_q <= g3_sentence_q_l2  and sentence_avg > g2_avgl_sentences_inw_l2  and sentence_avg <= g3_avgl_sentences_inw_l2 and lcwords_q > g2_compw_q_l2 and lcwords_q <= g3_compw_q_l2) or (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q > g2_sentence_q_l2 and sentence_q <= g3_sentence_q_l2  and syllables_avg > g2_avgwl_insyllables_l2 and syllables_avg <= g3_avgwl_insyllables_l2 and sentence_avg > g2_avgl_sentences_inw_l2  and sentence_avg <= g3_avgl_sentences_inw_l2) or (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q > g2_sentence_q_l2 and sentence_q <= g3_sentence_q_l2 and syllables_avg > g2_avgwl_insyllables_l2 and syllables_avg <= g3_avgwl_insyllables_l2 and multisyllabic_wq  > g2_longw_q_l2 and multisyllabic_wq  <= g3_longw_q_l2 and rareword_q > g2_rarew_q_l2 and rareword_q <= g3_rarew_q_l2) or (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q > g2_sentence_q_l2 and sentence_q <= g3_sentence_q_l2 and syllables_avg > g2_avgwl_insyllables_l2 and syllables_avg <= g3_avgwl_insyllables_l2 and multisyllabic_wq > g2_longw_q_l2 and multisyllabic_wq <= g3_longw_q_l2) or (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q > g2_sentence_q_l2 and sentence_q <= g3_sentence_q_l2 and syllables_avg > g2_avgwl_insyllables_l2 and syllables_avg <= g3_avgwl_insyllables_l2 and rareword_q > g2_rarew_q_l2 and rareword_q <= g3_rarew_q_l2) or (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q > g2_sentence_q_l2 and sentence_q <= g3_sentence_q_l2 and  syllables_avg < g3_avgwl_insyllables_l1 and sentence_avg > g3_avgl_sentences_inw_l2 and multisyllabic_wq > g2_longw_q_l2 and multisyllabic_wq<= g3_longw_q_l2 and lcwords_q > g2_compw_q_l2 and lcwords_q <= g3_compw_q_l2) or (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q > g2_sentence_q_l2 and sentence_q <= g3_sentence_q_l2 and  syllables_avg < g3_avgwl_insyllables_l1 and sentence_avg > g2_avgl_sentences_inw_l2 and sentence_avg <= g3_avgl_sentences_inw_l2   and multisyllabic_wq > g2_longw_q_l2 and multisyllabic_wq <= g3_longw_q_l2) or (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q > g2_sentence_q_l2 and sentence_q <= g3_sentence_q_l2 and  syllables_avg > g2_avgwl_insyllables_l2 and syllables_avg <= g3_avgwl_insyllables_l2 and lcwords_q > g2_compw_q_l2 and lcwords_q <= g3_compw_q_l2):
                    
                    level_result = "3 класс"
                    book = ruText( book_title=title, book_author=author,book_text=message, sentence_q=sentence_q, words_q=words_q, syllables_avg=syllables_avg, sentence_avg=sentence_avg, multisyllabic_wq=multisyllabic_wq, lcwords_q=lcwords_q, lcwords_p=lcwors_p,
                                rareword_q=rareword_q, rareword_p=rareword_p, fw_q=fw_q, fw_p=fw_p, uniq_w=uniquew_q, lexical_div=lexical_d, level_result=level_result, fre_oborneva = fre_oborneva, gunning_fog_index=gunning_fog_index)
                    book.save()
                    messages.info(request, 'загружен')
            
            elif (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q > g2_sentence_q_l2 and sentence_q <= g3_sentence_q_l2  and sentence_avg > g2_avgl_sentences_inw_l2  and sentence_avg <= g3_avgl_sentences_inw_l2 and lcwords_q > g2_compw_q_l2 and lcwords_q > g3_compw_q_l2) or (words_q < g2_word_q_l2  and  sentence_q < g2_sentence_q_l2  and sentence_avg > g2_avgl_sentences_inw_l2  and sentence_avg <= g3_avgl_sentences_inw_l2 and multisyllabic_wq > g2_longw_q_l2 and multisyllabic_wq <= g3_longw_q_l2 ) or (words_q > g3_word_q_l2 and  sentence_q > g3_sentence_q_l2  and sentence_avg > g2_avgl_sentences_inw_l2 and syllables_avg > g2_avgwl_insyllables_l2 and syllables_avg <= g3_avgwl_insyllables_l2 and sentence_avg <= g3_avgl_sentences_inw_l2 and multisyllabic_wq > g2_longw_q_l2 and multisyllabic_wq  <= g3_longw_q_l2 and lcwords_q > g2_compw_q_l2 and lcwords_q <= g3_compw_q_l2) or (words_q < g3_word_q_l1 and  sentence_q < g3_sentence_q_l1  and sentence_avg > g2_avgl_sentences_inw_l2 and sentence_avg <= g3_avgl_sentences_inw_l2 and syllables_avg > g2_avgwl_insyllables_l2 and syllables_avg <= g3_avgwl_insyllables_l2 and lcwords_q > g2_compw_q_l2 and lcwords_q <= g3_compw_q_l2) or (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q < g3_sentence_q_l1 and syllables_avg > g2_avgwl_insyllables_l2 and syllables_avg <= g3_avgwl_insyllables_l2  and sentence_avg > g3_avgl_sentences_inw_l2  and multisyllabic_wq > g2_longw_q_l2 and multisyllabic_wq <= g3_longw_q_l2) or (words_q > g2_word_q_l2 and words_q <= g3_word_q_l2 and  sentence_q > g3_sentence_q_l2 and syllables_avg > g2_avgwl_insyllables_l2 and syllables_avg <= g3_avgwl_insyllables_l2  and multisyllabic_wq > g2_longw_q_l2 and multisyllabic_wq <= g3_longw_q_l2):
                    
                    level_result = "3 класс: текст нужно проверить"
                    book = ruText( book_title=title, book_author=author,book_text=message, sentence_q=sentence_q, words_q=words_q, syllables_avg=syllables_avg, sentence_avg=sentence_avg, multisyllabic_wq=multisyllabic_wq, lcwords_q=lcwords_q, lcwords_p=lcwors_p,
                                rareword_q=rareword_q, rareword_p=rareword_p, fw_q=fw_q, fw_p=fw_p, uniq_w=uniquew_q, lexical_div=lexical_d, level_result=level_result, fre_oborneva = fre_oborneva, gunning_fog_index=gunning_fog_index)
                    book.save()
                    messages.info(request, 'загружен')
            
            elif (words_q > g3_word_q_l2 and words_q >= g4_word_q_l2 and  sentence_q > g3_sentence_q_l2 and sentence_q >= g4_sentence_q_l2) or ( lcwords_q > g3_compw_q_l2 and lcwords_q >= g4_compw_q_l2 and rareword_q > g3_rarew_q_l2 and rareword_q >= g4_rarew_q_l2) or (words_q > g3_word_q_l2 and  sentence_q > g3_sentence_q_l2 and multisyllabic_wq > g3_longw_q_l2 and rareword_q >= g3_rarew_q_l2) or (words_q > g3_word_q_l2 and  sentence_q > g3_sentence_q_l2 and syllables_avg > g3_avgwl_insyllables_l2 and multisyllabic_wq > g3_longw_q_l2) or (words_q > g3_word_q_l2 and  sentence_q > g3_sentence_q_l2 and lcwords_q > g3_compw_q_l2 and rareword_q > g3_rarew_q_l2) or (words_q > g3_word_q_l2 and  sentence_q > g3_sentence_q_l1 and sentence_q < g4_sentence_q_l1 and sentence_avg > g3_avgl_sentences_inw_l2 and lcwords_q > g3_compw_q_l2 and rareword_q > g3_rarew_q_l2) or (words_q < g4_word_q_l1 and  sentence_q < g4_sentence_q_l1 and syllables_avg > g3_avgwl_insyllables_l2 and  sentence_avg > g3_avgl_sentences_inw_l2 and multisyllabic_wq > g3_longw_q_l2 and  lcwords_q > g3_compw_q_l2):
                    
                    level_result = "4 класс"
                    book = ruText( book_title=title, book_author=author,book_text=message, sentence_q=sentence_q, words_q=words_q, syllables_avg=syllables_avg, sentence_avg=sentence_avg, multisyllabic_wq=multisyllabic_wq, lcwords_q=lcwords_q, lcwords_p=lcwors_p,
                                rareword_q=rareword_q, rareword_p=rareword_p, fw_q=fw_q, fw_p=fw_p, uniq_w=uniquew_q, lexical_div=lexical_d, level_result=level_result, fre_oborneva = fre_oborneva, gunning_fog_index=gunning_fog_index)
                    book.save()
                    messages.info(request, 'загружен')

            elif (words_q > g3_word_q_l1  and words_q < g4_word_q_l1 and  sentence_q > g3_sentence_q_l1 and sentence_q < g4_sentence_q_l1 and syllables_avg > g3_avgwl_insyllables_l2 and multisyllabic_wq > g3_longw_q_l2 and rareword_q > g3_rarew_q_l2) or (words_q > g3_word_q_l2  and sentence_q > g3_sentence_q_l2 and multisyllabic_wq > g3_longw_q_l2 and lcwords_q > g3_compw_q_l2 and  rareword_q < g4_rarew_q_l1):
                    
                    level_result = "4 класс: текст нужно проверить"
                    book = ruText( book_title=title, book_author=author,book_text=message, sentence_q=sentence_q, words_q=words_q, syllables_avg=syllables_avg, sentence_avg=sentence_avg, multisyllabic_wq=multisyllabic_wq, lcwords_q=lcwords_q, lcwords_p=lcwors_p,
                                rareword_q=rareword_q, rareword_p=rareword_p, fw_q=fw_q, fw_p=fw_p, uniq_w=uniquew_q, lexical_div=lexical_d, level_result=level_result, fre_oborneva = fre_oborneva, gunning_fog_index=gunning_fog_index)
                    book.save()
                    messages.info(request, 'загружен')

           

            
            else:
                    level_result = "Текст состоит из " + str(words_q) + " слов и нуждается в дополнительной проверке"
                    book = ruText( book_title=title, book_author=author,book_text=message, sentence_q=sentence_q, words_q=words_q, syllables_avg=syllables_avg, sentence_avg=sentence_avg, multisyllabic_wq=multisyllabic_wq, lcwords_q=lcwords_q, lcwords_p=lcwors_p,
                                rareword_q=rareword_q, rareword_p=rareword_p, fw_q=fw_q, fw_p=fw_p, uniq_w=uniquew_q, lexical_div=lexical_d, level_result=level_result, fre_oborneva = fre_oborneva, gunning_fog_index=gunning_fog_index)
                    book.save()
                    
                    messages.error(request, 'Текст нужно проверить')





            

            
            context = {'words_q':words_q, 'sentence_q':sentence_q, 'syllables':syllables, 'syllables_avg':syllables_avg, 'sentence_avg':sentence_avg, 'multisyllabic_wq':multisyllabic_wq, 'longw_frequencies':longw_frequencies, 'lword_p':lword_p, 'uniquew_q':uniquew_q,
                        'w_frequencies': w_frequencies, 'lcwords_q':lcwords_q, 'lcword_frequencies':lcword_frequencies, 'rareword_frequencies':rareword_frequencies, 'lexical_d':lexical_d,
                        'rareword_q':rareword_q, 'fw_frequencies':fw_frequencies,'fw_p':fw_p, 'g1_word_q_l1':g1_word_q_l1, 'g1_word_q_l2':g1_word_q_l2, 'g1_word_q_l3':g1_word_q_l3,
                        'g1_sentence_q_l1':g1_sentence_q_l1, 'g1_sentence_q_l2':g1_sentence_q_l2, 'g1_sentence_q_l3':g1_sentence_q_l3, 'level_result':level_result,
                        'g1_avgwl_insyllables_l1':g1_avgwl_insyllables_l1, 'g1_avgwl_insyllables_l2':g1_avgwl_insyllables_l2, 'g1_avgwl_insyllables_l3':g1_avgwl_insyllables_l3,
                        'g1_avgl_sentences_inw_l1':g1_avgl_sentences_inw_l1, 'g1_avgl_sentences_inw_l2':g1_avgl_sentences_inw_l2, 'g1_avgl_sentences_inw_l3':g1_avgl_sentences_inw_l3,
                        'g1_longw_q_l1':g1_longw_q_l1, 'g1_longw_q_l2':g1_longw_q_l2, 'g1_longw_q_l3':g1_longw_q_l3, 'g1_compw_q_l1':g1_compw_q_l1, 'g1_compw_q_l2':g1_compw_q_l2,
                        'g1_compw_q_l3':g1_compw_q_l3, 'g1_rarew_q_l1':g1_rarew_q_l1, 'g1_rarew_q_l2':g1_rarew_q_l2, 'g1_rarew_q_l3':g1_rarew_q_l3, 'g2_word_q_l1':g2_word_q_l1, 'g2_word_q_l2':g2_word_q_l2,
                        'g2_sentence_q_l1':g2_sentence_q_l1, 'g2_sentence_q_l2':g2_sentence_q_l2, 'g2_avgwl_insyllables_l1':g2_avgwl_insyllables_l1, 'g2_avgwl_insyllables_l2':g2_avgwl_insyllables_l2,
                        'g2_avgl_sentences_inw_l1':g2_avgl_sentences_inw_l1, 'g2_avgl_sentences_inw_l2':g2_avgl_sentences_inw_l2, 'g2_longw_q_l1':g2_longw_q_l1, 'g2_longw_q_l2':g2_longw_q_l2, 'g2_compw_q_l1':g2_compw_q_l1, 'g2_compw_q_l2':g2_compw_q_l2, 'g2_rarew_q_l1':g2_rarew_q_l1, 'g2_rarew_q_l2':g2_rarew_q_l2, 'g3_word_q_l1':g3_word_q_l1, 'g3_word_q_l2':g3_word_q_l2,
                        'g3_sentence_q_l1':g3_sentence_q_l1, 'g3_sentence_q_l2':g3_sentence_q_l2, 'g3_avgwl_insyllables_l1':g3_avgwl_insyllables_l1, 'g3_avgwl_insyllables_l2':g3_avgwl_insyllables_l2, 'g3_avgl_sentences_inw_l1':g3_avgl_sentences_inw_l1, 'g3_avgl_sentences_inw_l2':g3_avgl_sentences_inw_l2, 'g3_longw_q_l1':g3_longw_q_l1, 'g3_longw_q_l2':g3_longw_q_l2, 'g3_compw_q_l1':g3_compw_q_l1, 'g3_compw_q_l2':g3_compw_q_l2, 'g3_rarew_q_l1':g3_rarew_q_l1, 'g3_rarew_q_l2':g3_rarew_q_l2,
                         'g4_word_q_l1':g4_word_q_l1, 'g4_word_q_l2':g4_word_q_l2, 'g4_sentence_q_l1':g4_sentence_q_l1, 'g4_sentence_q_l2':g4_sentence_q_l2, 'g4_avgwl_insyllables_l1':g4_avgwl_insyllables_l1, 'g4_avgwl_insyllables_l2':g4_avgwl_insyllables_l2,'g4_avgl_sentences_inw_l1':g4_avgl_sentences_inw_l1, 'g4_avgl_sentences_inw_l2':g4_avgl_sentences_inw_l2, 'g4_longw_q_l1':g4_longw_q_l1, 'g4_longw_q_l2':g4_longw_q_l2, 'g4_compw_q_l1':g4_compw_q_l1, 'g4_compw_q_l2':g4_compw_q_l2, 'g4_rarew_q_l1':g4_rarew_q_l1, 'g4_rarew_q_l2':g4_rarew_q_l2, 'fre_oborneva':fre_oborneva, 'gunning_fog_index':gunning_fog_index}
            
            return render(request, 'ru/result.html', context)
             
        
        
        
        
        else:
                messages.error(request, 'Ошибка: Вводите текст на русском!!!')
        
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)