from django.db import models

# Create your models here.

class kgText(models.Model):
    book_title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Чыгарманын аты')
    book_author = models.CharField(max_length=255, null=True, blank=True, verbose_name='Автору')
    book_text = models.TextField(null=True, blank=True,verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True)
    words_q = models.IntegerField( null=True, blank=True, verbose_name="Сөздөрдүн саны")
    syllables_avg = models.FloatField( null=True, blank=True, verbose_name="Сөздөрдүн орточо узундугу муундар менен")
    sentence_q = models.IntegerField( null=True, blank=True, verbose_name="Сүйлөмдөрдүн жалпы саны")
    sentence_avg = models.FloatField( null=True, blank=True, verbose_name="Сүйлөмдүрдүн орточо узундугу сөздөр менен")
    multisyllabic_wq = models.FloatField( null=True, blank=True, verbose_name="Көп муунду сөздөрдүн саны")
    compound_w_q = models.FloatField( null=True, blank=True, verbose_name="Татаал жана кош сөздөрдүн саны")
    rareword_q = models.FloatField( null=True, blank=True, verbose_name="Сейрек сөздөрдүн саны")
    rareword_p = models.FloatField( null=True, blank=True, verbose_name="Сейрек сөздөрдүн %")
    complex_w_q = models.FloatField(null=True, blank=True,verbose_name='Кошмок сөздөрдүн саны')
    all_compound_words_p =  models.FloatField(null=True, blank=True,verbose_name='Татаал сөздөрдүн % ')
    fw_q =  models.FloatField(null=True, blank=True,verbose_name='Көп колдонулган сөздөр')
    fw_p =  models.FloatField(null=True, blank=True,verbose_name='Көп колдонулган сөздөрдүн %')
    uniq_w = models.IntegerField( null=True, blank=True, verbose_name="Уникалдуу сөздөрдүн саны")
    lexical_div = models.FloatField( null=True, blank=True, verbose_name="Коэф. лекс-го разн-ия")
    level_result =  models.CharField(max_length=255, null=True, blank=True, verbose_name='Сунушталган класс')
    

    def __str__(self):
        return "{}".format(self.book_title)
    
    class Meta:
        verbose_name = "Кыргызча текст"
        verbose_name_plural = "Кыргызча тексттер"

class FreqWord(models.Model):
    freq_words = models.TextField(null=True, blank=True,verbose_name='Көп колдонулган сөздөр')

    def __str__(self):
        return self.freq_words  
    
    class Meta:
        verbose_name = "Көп колдонулган сөздөр"
        verbose_name_plural = "Көп колдонулган сөздөр"

class LCWord(models.Model):
    lc_words = models.TextField(null=True, blank=True,verbose_name='Татаал сөздөр')

    def __str__(self):
        return self.lc_words  
    
    class Meta:
        verbose_name = "Татаал сөздөр"
        verbose_name_plural = "Татаал сөздөр"

class RareWord(models.Model):
    rare_words = models.TextField(null=True, blank=True,verbose_name='Сейрек сөздөр')

    def __str__(self):
        return self.rare_words  
    
    class Meta:
        verbose_name = "Сейрек сөздөр"
        verbose_name_plural = "Сейрек сөздөр"

class CompoundWord(models.Model):
    compound_words = models.TextField(null=True, blank=True,verbose_name='Кошмок сөздөр')

    def __str__(self):
        return self.compound_words  
    
    class Meta:
        verbose_name = "Кошмок сөздөр"
        verbose_name_plural = "Кошмок сөздөр"





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
        verbose_name = "Уровень для 4-го класса"
        verbose_name_plural = "Уровни для 4-го класса"