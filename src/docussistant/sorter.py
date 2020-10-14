from strsimpy.jaro_winkler import JaroWinkler
import numpy as np

def check_for_text_match(self,str1,strlist):
    jarowinkler = JaroWinkler()
    similarities=[]
    for str2 in strlist:
        similarities.append(jarowinkler.similarity(str1, str2))
    index_max = np.argmax(similarities)
    if index_max >= .70:
        return strlist[index_max]
    similarities=[]
    for str2 in strlist:
        similarities.append(jarowinkler.similarity(str1.lower(), str2.lower())) 
    index_max = np.argmax(similarities) 
    if index_max >= .70:
        return strlist[index_max]  
    else:
        return None
    
