from django.db import models

# Create your models here.

class ruText(models.Model):
    book_title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название произведения')
    book_author = models.CharField(max_length=255, null=True, blank=True, verbose_name='Автор')
    book_text = models.TextField(null=True, blank=True,verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True)
    words_q = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов")
    syllables_avg = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах")
    sentence_q = models.IntegerField( null=True, blank=True, verbose_name="Кол-во предложений")
    sentence_avg = models.FloatField( null=True, blank=True, verbose_name="Сред. кол-во слов в предлож.")
    multisyllabic_wq = models.FloatField( null=True, blank=True, verbose_name="Кол-во многосложных слов")
    lcwords_q = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов для 1-4 кл.")
    lcwords_p = models.FloatField( null=True, blank=True, verbose_name="% Сложных  слов для 1-4 кл.")
    rareword_q = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов для 1-4 кл.")
    rareword_p = models.FloatField( null=True, blank=True, verbose_name="% редких  слов для 1-4 кл.")
    fw_q =  models.FloatField(null=True, blank=True,verbose_name='Часто используемые слова')
    fw_p =  models.FloatField(null=True, blank=True,verbose_name='% часто используемых слов')
    uniq_w = models.IntegerField( null=True, blank=True, verbose_name="Кол-во уник-ых слов")
    lexical_div = models.FloatField( null=True, blank=True, verbose_name="Коэф. лекс-го разн-ия")
    level_result =  models.CharField(max_length=255, null=True, blank=True, verbose_name='Рекемендуемый класс')
    fre_oborneva = models.FloatField( null=True, blank=True, verbose_name="Формула удобочитаемости Флеша (Оборнева 2006 г.)")
    gunning_fog_index = models.FloatField( null=True, blank=True, verbose_name="Показатель Фога (Ганнинга)")


    def __str__(self):
        return "{}".format(self.book_title)
    
    class Meta:
        verbose_name = "Текст на русском"
        verbose_name_plural = "Тексты на русском"

class FreqWord(models.Model):
    freq_words = models.TextField(null=True, blank=True,verbose_name='Часто используемые слова')

    def __str__(self):
        return self.freq_words  
    
    class Meta:
        verbose_name = "Список часто используемых слов"
        verbose_name_plural = "Часто используемые слова"

class LCWord(models.Model):
    lc_words = models.TextField(null=True, blank=True,verbose_name='Длинные и сложные слова для 1-4 класса')

    def __str__(self):
        return self.lc_words  
    
    class Meta:
        verbose_name = "Список сложных слов для 1-4 класса"
        verbose_name_plural = "Сложные слова для 1-4 класса"

class RareWord(models.Model):
    rare_words = models.TextField(null=True, blank=True,verbose_name='Редко используемые  слова')

    def __str__(self):
        return self.rare_words  
    
    class Meta:
        verbose_name = "Список редко используемых слов для 1-4 класса"
        verbose_name_plural = "Редкие слова для 1-4 класса"


class CompoundWord(models.Model):
    compound_words = models.TextField(null=True, blank=True,verbose_name='Кошмок сөздөр')

    def __str__(self):
        return self.compound_words  
    
    class Meta:
        verbose_name = "Составные слова"
        verbose_name_plural = "Составные слова"


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
    g1_longw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 1.1")
    g1_longw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 1.2")
    g1_longw_q_l3 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 1.3")
    g1_compw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 1.1")
    g1_compw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 1.2")
    g1_compw_q_l3 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 1.3")
    g1_rarew_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 1.1")
    g1_rarew_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 1.2")
    g1_rarew_q_l3 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 1.3")

   



    def __str__(self):
        return "{}".format(self.g1_word_q_l1)

    class Meta:
        verbose_name = "Уровень для 1-го класса"
        verbose_name_plural = "Уровни для 1-го класса"



class g2Level(models.Model):
    
    g2_word_q_l1 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 2.1")
    g2_word_q_l2 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 2.2")
    g2_sentence_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 2.1")
    g2_sentence_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 2.2")
    g2_avgwl_insyllables_l1 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 2.1")
    g2_avgwl_insyllables_l2 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 2.2")
    g2_avgl_sentences_inw_l1 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 2.1")
    g2_avgl_sentences_inw_l2 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 2.2")
    g2_longw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 2.1")
    g2_longw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 2.2")
    g2_compw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 2.1")
    g2_compw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 2.2")
    g2_rarew_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 2.1")
    g2_rarew_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 2.2")




    def __str__(self):
        return "{}".format(self.g2_word_q_l1)

    class Meta:
        verbose_name = "Уровень для 2-го класса"
        verbose_name_plural = "Уровни для 2-го класса"


class g3Level(models.Model):
    
    g3_word_q_l1 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 3.1")
    g3_word_q_l2 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 3.2")
    g3_sentence_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 3.1")
    g3_sentence_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 3.2")
    g3_avgwl_insyllables_l1 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 3.1")
    g3_avgwl_insyllables_l2 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 3.2")
    g3_avgl_sentences_inw_l1 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 3.1")
    g3_avgl_sentences_inw_l2 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 3.2")
    g3_longw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 3.1")
    g3_longw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 3.2")
    g3_compw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 3.1")
    g3_compw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 3.2")
    g3_rarew_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 3.1")
    g3_rarew_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 3.2")




    def __str__(self):
        return "{}".format(self.g3_word_q_l1)

    class Meta:
        verbose_name = "Уровень для 3-го класса"
        verbose_name_plural = "Уровни для 3-го класса"


class g4Level(models.Model):
    
    g4_word_q_l1 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 4.1")
    g4_word_q_l2 = models.IntegerField( null=True, blank=True, verbose_name="Кол-во слов для уровня 4.2")
    g4_sentence_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 4.1")
    g4_sentence_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Общее кол. предложений 4.2")
    g4_avgwl_insyllables_l1 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 4.1")
    g4_avgwl_insyllables_l2 = models.FloatField( null=True, blank=True, verbose_name="Ср. длина слова в слогах 4.2")
    g4_avgl_sentences_inw_l1 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 4.1")
    g4_avgl_sentences_inw_l2 = models.FloatField( null=True, blank=True, verbose_name="Сред. дл. предл. в словах 4.2")
    g4_longw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 4.1")
    g4_longw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Многосложные  слова 4.2")
    g4_compw_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 4.1")
    g4_compw_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во сложных  слов 4.2")
    g4_rarew_q_l1 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 4.1")
    g4_rarew_q_l2 = models.FloatField( null=True, blank=True, verbose_name="Кол-во редких  слов 4.2")




    def __str__(self):
        return "{}".format(self.g4_word_q_l1)

    class Meta:
        verbose_name = "Уровень для 4-го класса"
        verbose_name_plural = "Уровни для 4-го класса"