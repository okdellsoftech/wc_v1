from django.db import models

# Create your models here.

class uzText(models.Model):
    grade = models.IntegerField( null=True, blank=True, verbose_name="Класс")
    book_title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название произведения')
    book_author = models.CharField(max_length=255, null=True, blank=True, verbose_name='Автор')
    book_text = models.TextField(null=True, blank=True,verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True)
    words_q = models.IntegerField( null=True, blank=True, verbose_name="Количество слов")
    syllables_avg = models.FloatField( null=True, blank=True, verbose_name="Средняя длина слов в слога")
    sentence_q = models.IntegerField( null=True, blank=True, verbose_name="Сүйлөмдөрдүн жалпы саны")
    sentence_avg = models.FloatField( null=True, blank=True, verbose_name="Сүйлөмдүрдүн орточо узундугу сөздөр менен")
    multisyllabic_wq = models.FloatField( null=True, blank=True, verbose_name="Многосложные слова")
    compound_w_q = models.FloatField( null=True, blank=True, verbose_name="Количество сложных и с тире слов ")
    rareword_q = models.FloatField( null=True, blank=True, verbose_name="Количество редких слов")
    rareword_p = models.FloatField( null=True, blank=True, verbose_name="% Редких слов")
    complex_w_q = models.FloatField(null=True, blank=True,verbose_name='Количество составных слов')
    all_compound_words_p =  models.FloatField(null=True, blank=True,verbose_name='% Сложных слов ')
    fw_q =  models.FloatField(null=True, blank=True,verbose_name='Часто используемые слова')
    fw_p =  models.FloatField(null=True, blank=True,verbose_name='% Часто используемых слов')
    uniq_w = models.IntegerField( null=True, blank=True, verbose_name="Количество уникальных слов")
    lexical_div = models.FloatField( null=True, blank=True, verbose_name="Коэф. лекс-го разн-ия")
    level_result =  models.CharField(max_length=255, null=True, blank=True, verbose_name='Рекомендуемый класс')
    

    def __str__(self):
        return "{}".format(self.book_title)
    
    class Meta:
        verbose_name = "Ўзбек тилидаги матнлар"
        verbose_name_plural = "Ўзбек тилидаги матнлар"

class FreqWord(models.Model):
    freq_words = models.TextField(null=True, blank=True,verbose_name='Кўп ишлатиладиган сўзларин')

    def __str__(self):
        return self.freq_words  
    
    class Meta:
        verbose_name = "Кўп ишлатиладиган сўзларин"
        verbose_name_plural = "Кўп ишлатиладиган сўзларин"

class LCWord(models.Model):
    lc_words = models.TextField(null=True, blank=True,verbose_name='Қийин сўзлар')

    def __str__(self):
        return self.lc_words  
    
    class Meta:
        verbose_name = "Қийин сўзлар"
        verbose_name_plural = "Қийин сўзлар"

class RareWord(models.Model):
    rare_words = models.TextField(null=True, blank=True,verbose_name='Ноёб сўзлар')

    def __str__(self):
        return self.rare_words  
    
    class Meta:
        verbose_name = "Ноёб сўзлар"
        verbose_name_plural = "Ноёб сўзлар"

class CompoundWord(models.Model):
    compound_words = models.TextField(null=True, blank=True,verbose_name='Кўшма сўзлар')

    def __str__(self):
        return self.compound_words  
    
    class Meta:
        verbose_name = "Кўшма сўзлар"
        verbose_name_plural = "Кўшма сўзлар"





class g1Level(models.Model):
    
    g1_word_q_l1 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 1.1")
    g1_word_q_l2 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 1.2")
    g1_word_q_l3 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 1.3")
    g1_sentence_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 1.1")
    g1_sentence_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 1.2")
    g1_sentence_q_l3 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 1.3")
    g1_avgwl_insyllables_l1 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 1.1")
    g1_avgwl_insyllables_l2 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 1.2")
    g1_avgwl_insyllables_l3 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 1.3")
    g1_avgl_sentences_inw_l1 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 1.1")
    g1_avgl_sentences_inw_l2 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 1.2")
    g1_avgl_sentences_inw_l3 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 1.3")
    g1_multisyllabic_wq_l1 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 1.1")
    g1_multisyllabic_wq_l2 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 1.2")
    g1_multisyllabic_wq_l3 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 1.3")
    g1_compw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 1.1")
    g1_compw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 1.2")
    g1_compw_q_l3 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 1.3")
    g1_rarew_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 1.1")
    g1_rarew_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 1.2")
    g1_rarew_q_l3 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 1.3")
    g1_complexw_q_l1 = models.FloatField(null=True, blank=True,verbose_name='Кошмок сөздөрдүн саны 1.1')
    g1_complexw_q_l2 = models.FloatField(null=True, blank=True,verbose_name='Кошмок сөздөрдүн саны 1.2')
    g1_complexw_q_l3 = models.FloatField(null=True, blank=True,verbose_name='Кошмок сөздөрдүн саны 1.3')



    def __str__(self):
        return "{}".format(self.g1_word_q_l1)

    class Meta:
        verbose_name = "1-синф учун даража"
        verbose_name_plural = "1-синф учун даража"



class g2Level(models.Model):
    
    g2_word_q_l1 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 2.1")
    g2_word_q_l2 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 2.2")
    g2_sentence_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 2.1")
    g2_sentence_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 2.2")
    g2_avgwl_insyllables_l1 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 2.1")
    g2_avgwl_insyllables_l2 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 2.2")
    g2_avgl_sentences_inw_l1 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 2.1")
    g2_avgl_sentences_inw_l2 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 2.2")
    g2_multisyllabic_wq_l1 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 2.1")
    g2_multisyllabic_wq_l2 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 2.2")
    g2_compw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 2.1")
    g2_compw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 2.2")
    g2_rarew_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 2.1")
    g2_rarew_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 2.2")
    g2_complexw_q_l1 = models.FloatField(null=True, blank=True,verbose_name='Кошмок сөздөрдүн саны 2.1')
    g2_complexw_q_l2 = models.FloatField(null=True, blank=True,verbose_name='Кошмок сөздөрдүн саны 2.2')



    def __str__(self):
        return "{}".format(self.g2_word_q_l1)

    class Meta:
        verbose_name = "2-синф учун даража"
        verbose_name_plural = "2-синф учун даража"


class g3Level(models.Model):
    
    g3_word_q_l1 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 3.1")
    g3_word_q_l2 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 3.2")
    g3_sentence_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 3.1")
    g3_sentence_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 3.2")
    g3_avgwl_insyllables_l1 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 3.1")
    g3_avgwl_insyllables_l2 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 3.2")
    g3_avgl_sentences_inw_l1 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 3.1")
    g3_avgl_sentences_inw_l2 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 3.2")
    g3_multisyllabic_wq_l1 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 3.1")
    g3_multisyllabic_wq_l2 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 3.2")
    g3_compw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 3.1")
    g3_compw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 3.2")
    g3_rarew_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 3.1")
    g3_rarew_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 3.2")
    g3_complexw_q_l1 = models.FloatField(null=True, blank=True,verbose_name='Кошмок сөздөрдүн саны 3.1')
    g3_complexw_q_l2 = models.FloatField(null=True, blank=True,verbose_name='Кошмок сөздөрдүн саны 3.2')




    def __str__(self):
        return "{}".format(self.g3_word_q_l1)

    class Meta:
        verbose_name = "3-синф учун даража"
        verbose_name_plural = "3-синф учун даража"


class g4Level(models.Model):
    
    g4_word_q_l1 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 4.1")
    g4_word_q_l2 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 4.2")
    g4_sentence_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 4.1")
    g4_sentence_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 4.2")
    g4_avgwl_insyllables_l1 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 4.1")
    g4_avgwl_insyllables_l2 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 4.2")
    g4_avgl_sentences_inw_l1 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 4.1")
    g4_avgl_sentences_inw_l2 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 4.2")
    g4_multisyllabic_wq_l1 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 4.1")
    g4_multisyllabic_wq_l2 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 4.2")
    g4_compw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 4.1")
    g4_compw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 4.2")
    g4_rarew_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 4.1")
    g4_rarew_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 4.2")
    g4_complexw_q_l1 = models.FloatField(null=True, blank=True,verbose_name='Кошмок сөздөрдүн саны 4.1')
    g4_complexw_q_l2 = models.FloatField(null=True, blank=True,verbose_name='Кошмок сөздөрдүн саны 4.2')



    def __str__(self):
        return "{}".format(self.g4_word_q_l1)

    class Meta:
        verbose_name = "4-синф учун даража"
        verbose_name_plural = "4-синф учун даража"