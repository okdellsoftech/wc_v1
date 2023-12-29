
if(!Array.prototype.filter){

    Array.prototype.filter= function(fun, scope){
        var T= this, A= [], i= 0, itm, L= T.length;
        if(typeof fun=== 'function'){
            while(i<L){
                if(i in T){
                    itm= T[i];
                    if(fun.call(scope, itm, i, T)) A[A.length]= itm;
                }
                ++i;
            }
        }
        return A;
    };
}

if(!Array.prototype.diff){
    Array.prototype.diff = function(a) {
        return this.filter(function(i) {return !(a.indexOf(i) > -1);});
    };
}

if (!('indexOf' in Array.prototype)) {
    Array.prototype.indexOf= function(find, i /*opt*/) {
        if (i===undefined) i= 0;
        if (i<0) i+= this.length;
        if (i<0) i= 0;
        for (var n= this.length; i<n; i++)
            if (i in this && this[i]===find)
                return i;
        return -1;
    };
}

if (!Array.prototype.unique){
    Array.prototype.unique=function(a) {
        return this.filter(function(itm,i,a) {
            return i===a.indexOf(itm);
        });
    };
}

if (!Array.prototype.remove) {
    Array.prototype.remove = function(from, to) {
      var rest = this.slice((to || from) + 1 || this.length);
      this.length = from < 0 ? this.length + from : from;
      return this.push.apply(this, rest);
    };
}

var cleartext = function(text) {
    return text
            .replace(/[\.,\/#!$%\^&\*;:{}=\_`~()\"\'…©▼•—–\\\[\]<>»×?\|0-9¿˘¯˜ı◊˛¸`»ˆ¨ˇ‰´⁄€‹›‡°·‚—~±√∞»”’„†“\@♦\+«®]/g, ' ')
            .replace(/^\-|\s-{1}/g,' ')
            .replace(/\s+/g, ' ')
            .replace(/^\s+|\s+$/g, '')
            
    ;
};

var numwords = function(text) {
    return cleartext(text).split(' ').length;
};
        


// sort the uniques array in descending order by frequency
function compareFrequency(a, b) {
    return b[1] - a[1];
}

var freqwords = function(words, minfreq, onlyval) {
    var frequency = {}, value;
    if (!minfreq) minfreq = 1;

    // compute frequencies of each value
    for(var i = 0; i < words.length; i++) {
        value = words[i];
        if(value in frequency) {
            frequency[value]++;
        }
        else {
            frequency[value] = 1;
        }
    }

    if (onlyval) {
        var uniques = [];
        for(value in frequency) {
            if (frequency[value] >= minfreq)
                uniques.push(value);
        }

        // sort the uniques array in descending order by frequency
        function compareFrequency(a, b) {
            return frequency[b] - frequency[a];
        }
    } else {

        // make array from the frequency object to de-duplicate
        var uniques = [];
        for(value in frequency) {
            if (frequency[value] >= minfreq)
                uniques.push([value, frequency[value]]);
        }
    }
    

    return uniques.sort(compareFrequency);
};

function fill_multi_matrix(words, n) {
    var result = [];
    
    if (n > words.length) 
        return result;
    
    for (var i = 0; i < words.length-n+1; i++) {
        var m_word = [];
        for (var j=0; j < n; j++) {
            m_word[j] = words[i+j];
        }
        result[i] = m_word.join(' ');
    }

    result = $.grep(result, function(el, ind){
        if (el.split(' ').diff(stopwords).length === 0)
            return false;

        return true;
    });

    return result;
}

 function longestWord(sen) {
  big_word = ""
  var long_word = "";
  words = sen.split(" ")
  words.forEach(function(word){
    if (word.length >= 10){
        big_word ++;

    };
  });
return big_word

};
        
    
//var long_words_list =[];
//function longWords(text){
//    var long_words_list =[];
//    
//    for (i=0;i<text.length;i++){
//            if (text[i].length >= 8){
//              
//                long_words_list.push(text[i])
//    };
//    }
//    return long_words_list;
//}

 
var all_words;
        
        
        
// start
var db_stat = {};

$(document).ready(function() {


    $('input#analyze').click(function(){
        console.log(document.frm1.textbox1.value)
        var source = $('textarea#text').val(), ///////////////////////////////// #  1
            stat = {};
        // var source = result,
        // stat = {};
        stat.length = source.length;
        stat.length_clear = source.replace(/"'"[\s\t\-_!,.:+=?)(]/g, '').length;
	     

        
		
        var inline = source.split(/[\r\n]+/).join('. ').toLowerCase();
        var clear = cleartext(inline);
        all_words = clear
        console.log(clear)
        var words = clear.split(' ');
//        var words = inline.match(/[^\s.,\/\\()]+/g);
	
		
		var fname = document.getElementById('textarea1').value;////////////????#   2
       
		//var fname1 = document.getElementById('text').value;
        var fname1 = document.getElementById('text').value;  ////////////// # 3 = 1
        
		stat.text_result = fname1;
		var text1 = fname.replace(/\-/gi,",");
	    
		stat.t_slog = text1.match(/[аеёиоуэюяыөү]/g).length;
		
		if (fname1.match(/вств|здн|ндск|нтск|стл|стн|лнц|рдц|стск/gi)){
		var comb_s = fname1.replace(/вств|здн|ндск|нтск|стл|стн|лнц|рдц|стск/gi,"sog1");
		stat.comb_p = comb_s.match(/sog1/gi).length;
		}
	 
		
        stat.words = words.length;
        stat.words_uniq = words.unique().length;
        var words_clear = words.diff(stopwords);
       
        stat.words_stopwords = $(words).filter(stopwords).length;
		stat.m_slog = Math.round(stat.t_slog/stat.words*10)/10;
        // stat.long_words1 = longestWord(fname1);
       
//		stat.long_words2 = longWords(words);// для списка длинных слов
        
		stat.long_wordsP = Math.round((stat.long_words1 / stat.words)*100);
        
        if (stat.words) {
            stat.words_water = Math.round(stat.words_stopwords/stat.words*1000)/10;
        } else {
            stat.words_water = 0;
        }
        
        var word_len_avg = 0;
        $.each(words, function(){
       word_len_avg += this.length;
        });
    
        if (stat.words) {
            word_len_avg /= stat.words;
        } else {
            word_len_avg = 0;
        }
    
     
		stat.word_len = Math.round(word_len_avg);
	
        //Main1 var sentences = inline.split(/[\.\?\!][\s\t]/);
		//Main2 var sentences = inline.match( /[^\.!\?]+[\.!\?]+/g );
		
		
		var sentences = inline.match(/([^ \r\n][^!?\.\r\n]+[\w!?\.]+)/g);
        stat.sentences = sentences.length;
		
		stat.words_sentences = Math.round(stat.words/stat.sentences*10)/10;
		stat.p_slog = Math.round((stat.sentences/stat.t_slog)*100);
        
        var min = numwords(sentences[0]),
            max = numwords(sentences[0]),
            avg = 0;
        $.each(sentences, function(){
            var wc = numwords(this);
            if (wc < min)
                min = wc;
            if (wc > max)
                max = wc;
            avg += wc;
        });
    
        if (stat.sentences) {
            avg /= stat.sentences;
        } else {
            avg = 0;
        }
        
        stat.sentence_min = min;
        stat.sentence_max = max;
        stat.sentence_avg = Math.round(avg*10)/10;
        stat.commas = inline.length - inline.replace(/,/g, '').length;
        stat.commas_avg = stat.sentences ? Math.round(10*stat.commas/stat.sentences)/10 : 0;
		
		//Vowels
		stat.res_a = inline.length - inline.replace(/а/g, '').length;
        if (stat.res_a <= 0) 
		{
		var t_a = 0;
		}
		else
		{
		var t_a = 1;
		}
		stat.res_e = inline.length - inline.replace(/е/g, '').length;
        if (stat.res_e <= 0)
		{
		var t_e = 0;
		}
		else
		{
		var t_e = 1;
		}
		stat.res_e1 = inline.length - inline.replace(/ё/g, '').length;
        if (stat.res_e1 <= 0)
		{
		var t_e1 = 0;
		}
		else
		{
		var t_e1 = 1;
		}
		stat.res_i = inline.length - inline.replace(/и/g, '').length;
        if (stat.res_i <= 0)
		{
		var t_i = 0;
		}
		else
		{
		var t_i = 1;
		}
		stat.res_o = inline.length - inline.replace(/о/g, '').length;
        if (stat.res_o <= 0)
		{
		var t_o = 0;
		}
		else
		{
		var t_o = 1;
		}
		stat.res_y = inline.length - inline.replace(/у/g, '').length;
        if (stat.res_y <= 0)
		{
		var t_y = 0;
		}
		else
		{
		var t_y = 1;
		}
		stat.res_e2 = inline.length - inline.replace(/э/g, '').length;
        if (stat.res_e2 <= 0)
		{
		var t_e2 = 0;
		}
		else
		{
		var t_e2 = 1;
		}
		stat.res_u = inline.length - inline.replace(/ю/g, '').length;
        if (stat.res_u <= 0)
		{
		var t_u = 0;
		}
		else
		{
		var t_u = 1;
		}
		stat.res_ia = inline.length - inline.replace(/я/g, '').length;
        if (stat.res_ia <= 0)
		{
		var t_ia = 0;
		}
		else
		{
		var t_ia = 1;
		}
	    stat.res_iy = inline.length - inline.replace(/ы/g, '').length;
        if (stat.res_iy <= 0)
		{
		var t_iy = 0;
		}
		else
		{
		var t_iy = 1;
		}
		
		stat.res_o1 = inline.length - inline.replace(/ө|ѳ/g, '').length;
        if (stat.res_o1 <= 0)
		{
		var t_o1 = 0;
		}
		else
		{
		var t_o1 = 1;
		}
		stat.res_u1 = inline.length - inline.replace(/ү/g, '').length;
        if (stat.res_u1 <= 0)
		{
		var t_u1 = 0;
		}
		else
		{
		var t_u1 = 1;
		}
		
		
		
		
		// Consonants
		stat.res_b = inline.length - inline.replace(/б/g, '').length;
        if (stat.res_b <= 0)
		{
		var t_b = 0;
		}
		else
		{
		var t_b = 1;
		}
		stat.res_v = inline.length - inline.replace(/в/g, '').length;
        if (stat.res_v <= 0)
		{
		var t_v = 0;
		}
		else
		{
		var t_v = 1;
		}
		stat.res_g = inline.length - inline.replace(/г/g, '').length;
        if (stat.res_g <= 0)
		{
		var t_g = 0;
		}
		else
		{
		var t_g = 1;
		}
		stat.res_d = inline.length - inline.replace(/д/g, '').length;
        if (stat.res_d <= 0)
		{
		var t_d = 0;
		}
		else
		{
		var t_d = 1;
		}
		stat.res_j = inline.length - inline.replace(/ж/g, '').length;
        if (stat.res_j <= 0)
		{
		var t_j = 0;
		}
		else
		{
		var t_j = 1;
		}
		stat.res_z = inline.length - inline.replace(/з/g, '').length;
        if (stat.res_z <= 0)
		{
		var t_z = 0;
		}
		else
		{
		var t_z = 1;
		}
		stat.res_i1 = inline.length - inline.replace(/й/g, '').length;
        if (stat.res_i1 <= 0)
		{
		var t_i1 = 0;
		}
		else
		{
		var t_i1 = 1;
		}
		stat.res_k = inline.length - inline.replace(/к/g, '').length;
        if (stat.res_k <= 0)
		{
		var t_k = 0;
		}
		else
		{
		var t_k = 1;
		}
		stat.res_l = inline.length - inline.replace(/л/g, '').length;
        if (stat.res_l <= 0)
		{
		var t_l = 0;
		}
		else
		{
		var t_l = 1;
		}
		stat.res_m = inline.length - inline.replace(/м/g, '').length;
        if (stat.res_m <= 0)
		{
		var t_m = 0;
		}
		else
		{
		var t_m = 1;
		}
		stat.res_n = inline.length - inline.replace(/н/g, '').length;
        if (stat.res_n <= 0)
		{
		var t_n = 0;
		}
		else
		{
		var t_n = 1;
		}
		stat.res_p = inline.length - inline.replace(/п/g, '').length;
        if (stat.res_p <= 0)
		{
		var t_p = 0;
		}
		else
		{
		var t_p = 1;
		}
		stat.res_r = inline.length - inline.replace(/р/g, '').length;
        if (stat.res_r <= 0)
		{
		var t_r = 0;
		}
		else
		{
		var t_r = 1;
		}
		stat.res_s = inline.length - inline.replace(/с/g, '').length;
        if (stat.res_s <= 0)
		{
		var t_s = 0;
		}
		else
		{
		var t_s = 1;
		}
		stat.res_t = inline.length - inline.replace(/т/g, '').length;
        if (stat.res_t <= 0)
		{
		var t_t = 0;
		}
		else
		{
		var t_t = 1;
		}
		stat.res_f = inline.length - inline.replace(/ф/g, '').length;
        if (stat.res_f <= 0)
		{
		var t_f = 0;
		}
		else
		{
		var t_f = 1;
		}
		stat.res_h = inline.length - inline.replace(/х/g, '').length;
        if (stat.res_h <= 0)
		{
		var t_h = 0;
		}
		else
		{
		var t_h = 1;
		}
		stat.res_ts = inline.length - inline.replace(/ц/g, '').length;
        if (stat.res_ts <= 0)
		{
		var t_ts = 0;
		}
		else
		{
		var t_ts = 1;
		}
		stat.res_ch = inline.length - inline.replace(/ч/g, '').length;
        if (stat.res_ch <= 0)
		{
		var t_ch = 0;
		}
		else
		{
		var t_ch = 1;
		}
		stat.res_sh = inline.length - inline.replace(/ш/g, '').length;
        if (stat.res_sh <= 0)
		{
		var t_sh = 0;
		}
		else
		{
		var t_sh = 1;
		}
		stat.res_sh1 = inline.length - inline.replace(/щ/g, '').length;
        if (stat.res_sh1 <= 0)
		{
		var t_sh1 = 0;
		}
		else
		{
		var t_sh1 = 1;
		}
		
		stat.res_n1 = inline.length - inline.replace(/ң/g, '').length;
        if (stat.res_n1 <= 0)
		{
		var t_n1 = 0;
		}
		else
		{
		var t_n1 = 1;
		}
		
		
		// Miagkiy i tverdiy znak
		
		stat.res_mm1 = inline.length - inline.replace(/ь/g, '').length;
        if (stat.res_mm1 <= 0)
		{
		var t_mm1 = 0;
		}
		else
		{
		var t_mm1 = 1;
		}
		stat.res_tt1 = inline.length - inline.replace(/ъ/g, '').length;
        if (stat.res_tt1 <= 0)
		{
		var t_tt1 = 0;
		}
		else
		{
		var t_tt1 = 1;
		}
		
		stat.total = t_a + t_e + t_e1 + t_i + t_o + t_y + t_e2 + t_u + t_ia + t_iy + t_b + t_v + t_g + t_d + t_j + t_z + t_i1 + t_k + t_l + t_m + t_n + t_p + t_r + t_s + t_t + t_f + t_h + t_ts + t_ch + t_sh + t_sh1 + t_mm1 + t_tt1;
        // вычисление последовательностей
        /*
        var two_words = [], three_words = [];
        
        for (i = 0; i < words.length-1; i++) {
            two_words[i] = [words[i], words[i+1]].join(' ');
            
            if (i < words.length-2)
                three_words[i] = [words[i], words[i+1], words[i+2]].join(' ');
        }
        */
       var multi_words_matrix = [], multi_words, multi_words_dic = [];
       
       var mx_max = 6;
       for(var n_mx = mx_max; n_mx > 1; n_mx--) {
            multi_words = fill_multi_matrix(words, n_mx);
            
            var freq = freqwords(multi_words, 2);

            
            if (n_mx !== mx_max) {
                freq = $.grep(freq, function(el, ind){
                    for(var i = 0; i < multi_words_dic.length; i++) {
                        if (multi_words_dic[i][0].indexOf(el[0]) !== -1) {
                            return (multi_words_dic[i][1] < el[1]);
                        }
                    }

                    return true;
                });

            }
        
            multi_words_dic = $.merge(multi_words_dic, freq);
       }
   
       multi_words_dic = multi_words_dic.sort(compareFrequency);
       
//    two_words = ['после того', 'создание сайтов', 'того как', 'того как', 'после того'];
//    three_words = ['после того как', 'после того как'];
//    
    
                
        // заполнение частотного словаря
        var freq = freqwords(words_clear, 2),
            freq = freq.sort(compareFrequency);
           
            cont = '';
    
        for(var i = 0; i < Math.min(20, freq.length); i++) {
            cont += '<tr><th><span>'+ freq[i][0] +'</span></th><td><span>'+ freq[i][1] +'</span></td></tr>';
        }
    
        $('table#wordfreq tbody').html(cont);

        
     
var freq2 = freqwords(words_clear, 1)

var longList= []; //массив с длинными словами больше 10
   
    for (i=0;i<freq2.length;i++){
        if(freq2[i][0].length>=10){
            longList.push([freq2[i][0],freq2[i][1],freq2[i][0].length]);
        }
    }

//Сортировка     
longList = longList.sort(function(a,b) {
 return b[2]-a[2];
 });
console.log(longList)
////////     
var sum_f=0;   
for (i=0;i<longList.length;i++){sum_f+=longList[i][1]}
stat.long_words1 = sum_f;
stat.long_wordsP = Math.round((stat.long_words1 / stat.words)*100);
//for(i=0;i<longList.length;i++){
//console.log("Слово "+longList[i][0]+" Частота "+longList[i][1]+" Длина "+longList[i][2])
//};
        
////// зополнение Html  
longListHtml = '';

var num_=1;
for(i=0;i<longList.length;i++) {
	
longListHtml += '<tr><th><span>'+ num_ +'</span></th><th><span>'+ longList[i][0] +'</span></th><td><span>'+ longList[i][2] +'</span></td><td><span>'+ longList[i][1] +'</span></td></tr>';
num_++;
}
          
$('table#longwordfreq tbody').html(longListHtml);
/////////////////////////////
uniqueListHtml = '';
/////////////// заполнение для списка уникальных слов
for(i=0;i<words.unique().length;i++) {

uniqueListHtml += '<tr><th><span>'+ words.unique()[i] +'</span></th></tr>';
}

        
$('#words_unique_list tbody').html(uniqueListHtml);
        // for(i=0;i<freqwords(words_clear, 1).length;i++){console.log(freqwords(words_clear, 1)[i][0])}
// console.log(freqwords(words_clear, 1))
		

        /*
        var freq_two_words = freqwords(two_words, 2);
        var freq_three_words = freqwords(three_words, 2);
        
        // удаление двойных последовательностей, которые есть в тройных
        freq_two_words = $.grep(freq_two_words, function(el, ind){
            
            if (el[0].split(' ').diff(stopwords.py).length === 0)
                return false;
            
            for(var i = 0; i < freq_three_words.length; i++) {
                if (freq_three_words[i][0].indexOf(el[0]) !== -1)
                    return false;
            }
        
            return true;
        });
    
        freq_three_words = $.grep(freq_three_words, function(el, ind){
            if (el[0].split(' ').diff(stopwords.py).length === 0)
                return false;
            
            return true;
        });


        // заполнение таблицы частых связок
        var freq = freq_two_words.concat(freq_three_words),
            cont = '';
        */

        var freq = multi_words_dic;
            cont = '';
    
        for(var i = 0; i < Math.min(20, freq.length); i++) {
            cont += '<tr><th><span>'+ freq[i][0] +'</span></th><td><span>'+ freq[i][1] +'</span></td></tr>';
        }
    
        $('table#seqfreq tbody').html(cont);
        
        for (i in stat) {
            $('span#' + i).html(stat[i]);
        }
///////////////////////////////////////////////////    
        // $('html, body').animate({
        //     scrollTop: $("#results").offset().top
        // }, 500);
/////////////////////////////////////////////////////    
//        ga('send', 'event', 'button', 'click', 'analyze', stat.words);
     var hightlightColor = "rgb(212,75,56)";
        
        if (stat.m_slog >0 && stat.m_slog <= 2.1){ 
          $("#average_syllables > td:eq( 2 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.m_slog > 2.1 && stat.m_slog <= 2.2){ 
          $("#average_syllables > td:eq( 3 )").css({"font-weight": "900","background-color": hightlightColor});
        }
                else if(stat.m_slog > 2.2 && stat.m_slog <= 2.3){ 
          $("#average_syllables > td:eq( 4 )").css({"font-weight": "900","background-color": hightlightColor});
        }
                else if(stat.m_slog > 2.3 && stat.m_slog <= 2.4){ 
  
          $("#average_syllables > td:eq( 5 )").css({"font-weight": "900","background-color": hightlightColor});
       }
                else if(stat.m_slog > 2.4 && stat.m_slog <= 2.5){ 
          $("#average_syllables > td:eq( 6 )").css({"font-weight": "900","background-color": hightlightColor});
        }
       else if(stat.m_slog > 2.5 && stat.m_slog <= 2.6){ 
          $("#average_syllables > td:eq( 7 )").css({"font-weight": "900","background-color": hightlightColor});
            }
         else if(stat.m_slog > 2.6 && stat.m_slog <= 2.7){ 
          $("#average_syllables > td:eq( 8 )").css({"font-weight": "900","background-color": hightlightColor});
        }
              else if(stat.m_slog > 2.7 && stat.m_slog <= 2.8){ 
          $("#average_syllables > td:eq( 9 )").css({"font-weight": "900","background-color": hightlightColor});
            }
         else if(stat.m_slog > 2.8){ 
          $("#average_syllables > td:eq( 10 )").css({"font-weight": "900","background-color": hightlightColor});
        }


        
        //////////////////////////////////////////////////////////////
        if (stat.words > 0 && stat.words <= 50){  
          $("#NumberOfWords > td:eq( 2 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 50 && stat.words <= 100){ 
        console.log(stat.words);
          $("#NumberOfWords > td:eq( 3 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 100 && stat.words <= 150){ 
        console.log(stat.words);
          $("#NumberOfWords > td:eq( 4 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 150 && stat.words <= 200){  
        console.log(stat.words);
          $("#NumberOfWords > td:eq( 5 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 200 && stat.words <= 350){
        console.log(stat.words);
          $("#NumberOfWords > td:eq( 6 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 350 && stat.words <= 450){ 
        console.log(stat.words);
          $("#NumberOfWords > td:eq( 7 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 450 && stat.words <= 600){ 
        console.log(stat.words);
          $("#NumberOfWords > td:eq( 8 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 600 && stat.words <= 700){  
        console.log(stat.words);
          $("#NumberOfWords > td:eq( 9 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 700 && stat.words <= 1000){  
        console.log(stat.words);
          $("#NumberOfWords > td:eq( 10 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 1000){  
        console.log(stat.words);
          $("#NumberOfWords > td:eq( 10 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        //////////////////////////////////////////////////////////////////////////////////////////////////////

        if (stat.words >=0 && stat.long_words1 < 1){  
        $("#NumberOfLongWords > td:eq( 1 )");
        }
        else if(stat.words >= 1 && stat.long_words1 <= 4){
        $("#NumberOfLongWords > td:eq( 2 )").css({"font-weight": "900","background-color": hightlightColor});
        }
         else if(stat.words > 4 && stat.long_words1 <= 6){
        $("#NumberOfLongWords > td:eq( 3 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 6 && stat.long_words1 <= 8){ 
        $("#NumberOfLongWords > td:eq( 4 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 8 && stat.long_words1 <= 12){ 
        $("#NumberOfLongWords > td:eq( 5 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 12 && stat.long_words1 <= 16){ 
        $("#NumberOfLongWords > td:eq( 6 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 16 && stat.long_words1 <= 20){ 
        $("#NumberOfLongWords > td:eq( 7 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 20 && stat.long_words1 <= 24){ 
        $("#NumberOfLongWords > td:eq( 8 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 24 && stat.long_words1 <= 28){ 
        $("#NumberOfLongWords > td:eq( 9 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 28 && stat.long_words1 <= 32){ 
        $("#NumberOfLongWords > td:eq( 10 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words > 32){ 
        $("#NumberOfLongWords > td:eq( 10 )").css({"font-weight": "900","background-color": hightlightColor});
                }
        
        /////////////////////////////////////////////////////////////////////////////////////////////////////////
        if (stat.long_wordsP >= 0 && stat.long_wordsP <= 10){  
        $("#LongWordsPercentage > td:eq( 2 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.long_wordsP > 10 && stat.long_wordsP <= 15){ 
        $("#LongWordsPercentage > td:eq( 3 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.long_wordsP > 15 && stat.long_wordsP <= 20.5){ 
        $("#LongWordsPercentage > td:eq( 4 )").css({"font-weight": "900","background-color": hightlightColor});
        } 
        else if(stat.long_wordsP > 20.5&& stat.long_wordsP <= 22.5){ 
        $("#LongWordsPercentage > td:eq( 5 )").css({"font-weight": "900","background-color": hightlightColor});
        } 
        else if(stat.long_wordsP > 22.5 && stat.long_wordsP <= 27.5){ 
        $("#LongWordsPercentage > td:eq( 6 )").css({"font-weight": "900","background-color": hightlightColor});
        }        
        else if(stat.long_wordsP > 27.5 && stat.long_wordsP <= 30){ 
        $("#LongWordsPercentage > td:eq( 7 )").css({"font-weight": "900","background-color": hightlightColor});
        }        
        else if(stat.long_wordsP > 30 && stat.long_wordsP <= 35){ 
        $("#LongWordsPercentage > td:eq( 8 )").css({"font-weight": "900","background-color": hightlightColor});
        }        
        else if(stat.long_wordsP > 35 && stat.long_wordsP <= 39.5){ 
        $("#LongWordsPercentage > td:eq( 9 )").css({"font-weight": "900","background-color": hightlightColor});
        }            
        else if(stat.long_wordsP > 39.5 ){ 
        $("#LongWordsPercentage > td:eq( 10 )").css({"font-weight": "900","background-color": hightlightColor});
        }


        /////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        if (stat.word_len > 1 && stat.word_len <= 5){  
        $("#AverageNumberOfLetters > td:eq( 2 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.word_len > 5 && stat.word_len <= 6){ 
        $("#AverageNumberOfLetters > td:eq( 3 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.word_len > 6 && stat.word_len <= 7){ 
        $("#AverageNumberOfLetters > td:eq( 4 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.word_len > 7 && stat.word_len <= 8){ 
        $("#AverageNumberOfLetters > td:eq( 5 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.word_len > 8 && stat.word_len <= 9){ 
        $("#AverageNumberOfLetters > td:eq( 6 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.word_len > 9 && stat.word_len <= 10){ 
        $("#AverageNumberOfLetters > td:eq( 7 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.word_len > 10 && stat.word_len <= 11){ 
        $("#AverageNumberOfLetters > td:eq( 8 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.word_len > 11 && stat.word_len <= 12){ 
        $("#AverageNumberOfLetters > td:eq( 9 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.word_len > 12){ 
        $("#AverageNumberOfLetters > td:eq( 10 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        if (stat.sentences >= 1 && stat.sentences <= 10){  
        $("#NumberOfSentences > td:eq( 2 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.sentences > 10 && stat.sentences <= 15){ 
        $("#NumberOfSentences > td:eq( 3 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.sentences > 15 && stat.sentences <= 25){ 
        $("#NumberOfSentences > td:eq( 4 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.sentences > 25 && stat.sentences <= 50){ 
        $("#NumberOfSentences > td:eq( 5 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.sentences > 50 && stat.sentences <= 100){ 
        $("#NumberOfSentences > td:eq( 6 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.sentences > 100 && stat.sentences <= 200){ 
        $("#NumberOfSentences > td:eq( 7 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.sentences > 200 && stat.sentences <= 250){ 
        $("#NumberOfSentences > td:eq( 8 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.sentences > 250&& stat.sentences <= 300){ 
        $("#NumberOfSentences > td:eq( 9 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.sentences > 350){ 
        $("#NumberOfSentences > td:eq( 10 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        //////////////////////////////////////////////////////////////////////////////////////////////////////
        if (stat.words_sentences > 1 && stat.words_sentences <= 5){  
        $("#AverageNumberOfSent > td:eq( 2 )").css({"font-weight": "900","background-color": hightlightColor});
        }
        else if(stat.words_sentences > 5 && stat.words_sentences <= 5.5){ 
        $("#AverageNumberOfSent > td:eq( 3 )").css({"font-weight": "900","background-color": hightlightColor});
        }       
        else if(stat.words_sentences > 5.5 && stat.words_sentences <= 6){ 
        $("#AverageNumberOfSent > td:eq( 4 )").css({"font-weight": "900","background-color": hightlightColor});
        }  
        else if(stat.words_sentences > 6 && stat.words_sentences <= 6.5){ 
        $("#AverageNumberOfSent > td:eq( 5 )").css({"font-weight": "900","background-color": hightlightColor});
        }  
        else if(stat.words_sentences > 6.5 && stat.words_sentences <= 7){ 
        $("#AverageNumberOfSent > td:eq( 6 )").css({"font-weight": "900","background-color": hightlightColor});
        }  
        else if(stat.words_sentences > 7 && stat.words_sentences <= 7.5){ 
        $("#AverageNumberOfSent > td:eq( 7 )").css({"font-weight": "900","background-color": hightlightColor});
        }  
        else if(stat.words_sentences > 7.5 && stat.words_sentences <= 8){ 
        $("#AverageNumberOfSent > td:eq( 8 )").css({"font-weight": "900","background-color": hightlightColor});
        } 
        else if(stat.words_sentences > 8 && stat.words_sentences <= 8.5){ 
        $("#AverageNumberOfSent > td:eq( 9 )").css({"font-weight": "900","background-color": hightlightColor});
        }        
        else if(stat.words_sentences > 8.5 ){ 
        $("#AverageNumberOfSent > td:eq( 10 )").css({"font-weight": "900","background-color": hightlightColor});
        } 
        
		db_stat=stat;




    });




});





$('#list > tbody > tr > td:first-child').css('background', '#b4bfaa');
$('#list > tbody > tr > td:nth-child(2)').css('background', '#abbab3');
$('#head').css('background', 'white');


$(document).ready(function() {
    $("#analyze").click(function(e) {
        $(".progressbar").animate({
            width: "100%"},
           {duration: 1500,
            step: function (now) 
            {
                $(".progressbar").text('Анализ: '+Math.round(now)+'%');
                
            }	
        });
    
        
        setTimeout(function(){ document.getElementById('results').style.display = "block"; }, 1600);
        setTimeout(function(){  $('html, body').animate({scrollTop: $("#results").offset().top}, 500);}, 1700);
        return false;

    })
})
////////////////////////////////////////////////////////////////////////////////////////

 $('#save_db').click(function (event) {
 	event.preventDefault();
	console.log(all_words)

      $.ajax({
        url: 'save_db/',
        method:'post',
        data: {
          	'text_result': db_stat.text_result,
			'words': db_stat.words,
			'words_sentences': db_stat.words_sentences,
			't_slog': db_stat.t_slog,
			'word_len': db_stat.word_len,
			'long_words1': db_stat.long_words1,
			'm_slog': db_stat.m_slog,
			'sentences': db_stat.sentences,
			'all_words':all_words,


        },
        success: function (response) {
          console.log(response)
        }
      });




});
function refreshApp(newHtml) {
        document.open();
        document.write(newHtml);
        document.close();
      }

// $.ajax({
// 	url:url,
// 	method:'get',
// 	data:{
// 		id: parseInt(e.currentTarget.attributes[0].nodeValue),
// 	},
// 	success:function (response) {
// 	console.log(response);
//
// }
//
// });



