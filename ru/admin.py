from django.contrib import admin
from .models import *
from django.http import HttpResponse
import xlwt
import re
from import_export.admin import ExportActionMixin
import xlsxwriter
import io



def clean_word(text):
    # Чистим текст от пунктуации
    regex = r"(\w+-\w+)|-+"
    punctuation = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
    txt_clean = re.sub(r"[¬]+\ *", "", text).lower()
    w_clean = re.sub(r"[–—‒−]+\ *", "-", txt_clean).lower()
    result = re.sub(r"[,.;@#?!&$»«+=…“”•●■]+\ *", " ", w_clean).lower()
    f_result = re.sub(regex, r"\1", result)

    # Удаляем пунктуацию из очищенного текста
    final_string = ''.join(ch for ch in f_result if ch not in punctuation)

    # Разделяем обратно на слова
    words_cleaned = final_string.split()

    return words_cleaned


def find_compound_words(text, compound_words):
    compound_words_found = []
    non_compound_words = []

    words = text  # <-- Замените это на words = text

    i = 0
    while i < len(words):
        word = words[i]
        compound = " ".join(words[i:i+2])
        if compound in compound_words:
            compound_words_found.append(compound)
            i += 2  # пропускаем второе слово составного слова
        else:
            non_compound_words.append(word)
            i += 1

    # Если нет составных слов, просто считаем слова как обычно
    if not compound_words_found:
        non_compound_words = words

    return compound_words_found, non_compound_words

def getDuplicatesWithInfo(listOfElems):
    dictOfElems = dict()
    # Iterate over each element in list and keep track of index
    for elem in listOfElems:
        # If element exists in dict then keep its index in lisr & increment its frequency
        if elem in dictOfElems:
            dictOfElems[elem][0] += 1
        else:
        # Add a new entry in dictionary 
            dictOfElems[elem] = [1, len(elem)]  
    # dictOfElems = { key:value for key, value in dictOfElems.items() if value[0] > 1}
    return dictOfElems




def excel(modelAdmin, request, queryset):
    output = io.BytesIO()
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=report_kg.xlsx'
    wb = xlsxwriter.Workbook(output)
    ws = wb.add_worksheet('all_words')
    row_num = 0
    bold = wb.add_format({'bold': True})
    columns = ['Word', 'count', 'len']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], bold)

    words_array_low = []

    get_compoundwords = CompoundWord.objects.values_list('compound_words', flat=True). get(id=1)
    compound_words = get_compoundwords.lower()
    for book in queryset:
        cleaned_text = re.sub(r'[a-zA-Z0-9_]', '', book.book_text).lower()
        hyphenated_w = re.findall(r'\w+-\w+', cleaned_text)
        clean = re.sub(r'\w+-\w+', ' ', cleaned_text).split()


        words_array = clean_word(" ".join(clean))  # Очищаем слова от пунктуации и дубликатов

        # Поиск составных слов
        compound_words_found, non_compound_words = find_compound_words(words_array, compound_words)
        words_array_low += compound_words_found + non_compound_words + hyphenated_w
    
    
    
    word_freq_len = getDuplicatesWithInfo(words_array_low)

    array_r = []
    for key, value in word_freq_len.items():
        temp = [key, value[0], len(key.replace('-', ''))]
        array_r.append(temp)

    for row in array_r:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num])	
    
    wb.close()
    response.write(output.getvalue())
    return response

excel.short_description = 'Excel'


class ruTextAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['pub_date', 'level_result']
    list_display  = ( 'book_title', 'book_author', 'pub_date', 'words_q', 'sentence_q', 'level_result')
    actions = [excel]

admin.site.register(ruText, ruTextAdmin)

class FreqWordAdmin(admin.ModelAdmin):
    
    list_display  = ['freq_words']


admin.site.register(FreqWord, FreqWordAdmin)

class LCWordAdmin(admin.ModelAdmin):
    
    list_display  = ['lc_words']
admin.site.register(LCWord, LCWordAdmin)

class RareWordAdmin(admin.ModelAdmin):
    
    list_display  = ['rare_words']
admin.site.register(RareWord, RareWordAdmin)


class CompoundWordAdmin(admin.ModelAdmin):
    
    list_display  = ['compound_words']
admin.site.register(CompoundWord, CompoundWordAdmin)

class g1LevelAdmin(admin.ModelAdmin):
    
    list_display  = ['g1_word_q_l1', 'g1_word_q_l2', 'g1_word_q_l3', 'g1_sentence_q_l1', 'g1_sentence_q_l2', 'g1_sentence_q_l3' ]
admin.site.register(g1Level, g1LevelAdmin)

class g2LevelAdmin(admin.ModelAdmin):
    
    list_display  = ['g2_word_q_l1', 'g2_word_q_l2', 'g2_sentence_q_l1', 'g2_sentence_q_l2']
admin.site.register(g2Level, g2LevelAdmin)



class g3LevelAdmin(admin.ModelAdmin):
    
    list_display  = ['g3_word_q_l1', 'g3_word_q_l2', 'g3_sentence_q_l1', 'g3_sentence_q_l2']
admin.site.register(g3Level, g3LevelAdmin)


class g4LevelAdmin(admin.ModelAdmin):
    
    list_display  = ['g4_word_q_l1', 'g4_word_q_l2', 'g4_sentence_q_l1', 'g4_sentence_q_l2']
admin.site.register(g4Level, g4LevelAdmin)




admin.site.site_header = "Okuu keremet!" 
admin.site.site_title = "WC"
admin.site.index_title = "Okuu keremet!"  