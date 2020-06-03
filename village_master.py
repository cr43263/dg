import pickle
import random
import operator
import math
import re
from operator import itemgetter



import pdb

import datetime
"""print(datetime.datetime.now().time())"""






def roseta(list_to_interpert,type_to_output,village_name=' '):
    if village_name == ' ':
        village_name=cvs()
        village_beings=safe_pick('classed_beings{}'.format(village_name))
    elif village_name == 'x':
        village_beings=CVA
    else:
        village_beings=safe_pick('classed_beings{}'.format(village_name))       
    
    l_o_names=[]
    if type(list_to_interpert) == dict:
        l_o_names=list(list_to_interpert.keys())
    elif hasattr(list_to_interpert[0],'name') :
        for entry in list_to_interpert:
            l_o_names.append(display_name(entry.name))
    elif type(list_to_interpert[0]) == str:
        l_o_names = list_to_interpert
    elif type(list_to_interpert[0][0]) == str:
        for entry in list_to_interpert:
                l_o_names.append(str(entry[0]))
    elif type(list_to_interpert[1]) == str:
        for entry in list_to_interpert[0]:
            l_o_names.append(entry[1])
    elif type(list_to_interpert[0][1]) == str:
        for entry in list_to_interpert:
            l_o_names.append(entry[1])
    else:
        if type_to_output == 5:
            return list_to_interpert
        else:
            return "can't work up from codes"
               
    if type_to_output == 1:
        return l_o_names
    out_list=[]
    if type_to_output == 2:
        for entry2 in l_o_names:
            out_list.append([entry2])
        return out_list
    if type_to_output == 3:
        out_dict={}
        for entry2 in l_o_names:
            out_dict.update({entry2:village_beings[entry2]})
        return out_dict
    if type_to_output == 4:
        ct=int(0)
        for entry2 in l_o_names:
            ct+=1
            out_list.append([ct,entry2,village_beings[entry2]])
        return out_list
    if type_to_output == 5:
        for entry2 in l_o_names:
            out_list.append(village_beings[entry2].code)
        return out_list
    if type_to_output == 6:
        for entry2 in l_o_names:
            out_list.append(village_beings[entry2])
        return out_list
    if type_to_output == 7:
        ct=int(0)
        for entry2 in l_o_names:
            ct+=1
            out_list.append([ct,entry2,village_beings[entry2]])
        out_list=[out_list,' ']
        return out_list



def cvl_ALL():
    villages= list(safe_pick('village_list').keys())
    alll={}
    for vill in villages:
        cvll=safe_pick('classed_beings{}'.format(vill))
        for name,being in cvll.items():
            alll.update({name:[being,vill]})
    return alll



"""

flat list of names        == [name1,name2,name3]
dimesional list of names  == [[name1],[name2],[name3]]
cvl style                 == {name1:being_obj1 , name2:being_obj2 , name3:being_obj3]
triple set                == [[[sorter_value, name, being_obj] , [extra_value_slot]] , [[sorter_value2, name2, being_obj2] , [extra_value_slot2]] , [[sorter_value3, name3, being_obj3] , [extra_value_slot3]] , 
codes                     == [being1.code , being2.code , being3.code]
beings                    == [being_obj1 , being_obj2 , being_obj3]
_______________________________________

Names

_______________________________________test

"""

xI=['Chi','Di','Fi','Ki','Li','Ni','Qi','Ti','Wi','Zi']

xO=['Bo','Co','Do','Fo','Ho','Jo','Mo','Po','So','Yo']

xU=['Chu','Fu','Gu','Nu','Mu','Qu','Vu','Wu','Yu','Ku']

Color=['Gray','Silver','Black','White','Green','Brown']

Hard=['Stone','Steele','Slate','Ridge','Hammer','Heft']

Boringm=['John','Al','Mike','George','Ryan','Tom']

f2019m=['Chad','Kyle']

f2019f=['Karen','Sharon']

Boringf= ['Ashely','Mary','Heather','Jill','Melissa','Lisa']

why=['y']
consa_m=['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','w','z']
consa_1=['c','k','j','l']
consa_2=['b','d','m','n']
consa_3=['f','g','h']
consa_4=['p','r','s']
consa_5=['v','w','z']
consa_x=['q','x']
cc_1=['ch','ll','ph','th','sh','st']

vowel_m=['a','e','i','o','u']
vowel_1=['a','e']
vowel_2=['i','y']
vowel_3=['o','u']
v_dicts=[vowel_m,vowel_1,vowel_2,vowel_3,why]
c_dicts=[consa_m,consa_1,consa_2,consa_3,consa_4,consa_5,cc_1,consa_x,why]

randon=[xI,xO,xU]
boring=[Color,Hard]
types=[random,boring]
boys=[Boringm,f2019m]
girls=[Boringf,f2019f]
"""
gender:
1 = female
2 = male
"""


def cust_name(c_options,v_options,type_list=[]):
    """
returns a name STRING based on 3 parameters:

c_options = LIST of consonants
V_options = LIST of vowels
type_list = *OPTIONAL* LIST of numbers 1-5 , determines options for name length
    1 = c-v-c (consonant - vowel - consonant)
    2 = v-c-c-v
    3 = c-c-v-c
    4 = c-v-c-v-c
    5 = c-v-c-c
"""
    name=' '
    if type_list==[]:
        type_list=[1,2,3,4,5]
    name_type=random.choice(type_list)
    if name_type == 1:
        name=str(random.choice(c_options)+random.choice(v_options)+random.choice(c_options)).title()
    if name_type == 2:
        name=str(random.choice(v_options)+random.choice(c_options)+random.choice(c_options)+random.choice(v_options)).title()
    if name_type == 3:
        name=str(random.choice(c_options)+random.choice(c_options)+random.choice(v_options)+random.choice(c_options)).title()
    if name_type == 4:
        name=str(random.choice(c_options)+random.choice(v_options)+random.choice(c_options)+random.choice(v_options)+random.choice(c_options)).title()
    if name_type == 5:
        name=str(random.choice(c_options)+random.choice(v_options)+random.choice(c_options)+random.choice(c_options)).title()
    return name


def custom(number_of_c_dicts=int(),number_of_v_dicts=int()):
    """
USES GLOBAL CONSTANTS: * c_dicts * a LIST of LISTs of STRINGs (consonats)
                       * v_dicts * a LIST of LISTs of STRINGs (vowels)

returns a name STRING by selecting #[a number] of preset LISTs of letter (STRING) options from a preset library LIST

inputs are two optional parameters:
the number of lists the function chooses from c_dicts and v_dicts to assemble the letter choices for name assembly

"""

    name=''
    c_options = []
    v_options = []
    name_type = random.randint(1,5)
    if number_of_c_dicts == 0:
        number_of_c_dicts = random.randint(1,4)
    if number_of_v_dicts == 0:
        number_of_v_dicts = random.randint(1,4)
    for options_c in range(number_of_c_dicts):
        c_options.extend(random.choice(c_dicts))
    for options_v in range(number_of_v_dicts):
        v_options.extend(random.choice(v_dicts))
    if name_type == 1:
        name=str(random.choice(c_options)+random.choice(v_options)+random.choice(c_options)).title()
    if name_type == 2:
        name=str(random.choice(v_options)+random.choice(c_options)+random.choice(c_options)+random.choice(v_options)).title()
    if name_type == 3:
        name=str(random.choice(c_options)+random.choice(c_options)+random.choice(v_options)+random.choice(c_options)).title()
    if name_type == 4:
        name=str(random.choice(c_options)+random.choice(v_options)+random.choice(c_options)+random.choice(v_options)+random.choice(c_options)).title()
    if name_type == 5:
        name=str(random.choice(c_options)+random.choice(v_options)+random.choice(c_options)+random.choice(c_options)).title()
    return name


def full_custom(number_of_c_dicts=int(),number_of_v_dicts=int()):
    """
USES GLOBAL CONSTANTS: * c_dicts * a LIST of LISTs of STRINGs (consonats)
                       * v_dicts * a LIST of LISTs of STRINGs (vowels)

returns: (1) a name STRING by selecting #[a number] of preset LISTs of letter (STRING) options from a preset library LIST
         (2) the LIST of letter STRINGs for consonants
         (3) the LIST of letter STRINGs for vowels

inputs are two optional parameters:
the number of lists the function chooses from c_dicts and v_dicts to assemble the letter choices for name assembly

"""
    name=''
    c_options=[]
    v_options=[]
    name_type= random.randint(1,5)
    if number_of_c_dicts == 0:
        number_of_c_dicts = random.randint(2,4)
    if number_of_v_dicts == 0:
        number_of_v_dicts = random.randint(1,4)
    for options_c in range(number_of_c_dicts):
        c_options.extend(random.choice(c_dicts))
    for options_v in range(number_of_v_dicts):
        v_options.extend(random.choice(v_dicts))
    if name_type == 1:
        name=str(random.choice(c_options)+random.choice(v_options)+random.choice(c_options)).title()
    if name_type == 2:
        name=str(random.choice(v_options)+random.choice(c_options)+random.choice(c_options)+random.choice(v_options)).title()
    if name_type == 3:
        name=str(random.choice(c_options)+random.choice(c_options)+random.choice(v_options)+random.choice(c_options)).title()
    if name_type == 4:
        name=str(random.choice(c_options)+random.choice(v_options)+random.choice(c_options)+random.choice(v_options)+random.choice(c_options)).title()
    if name_type == 5:
        name=str(random.choice(c_options)+random.choice(v_options)+random.choice(c_options)+random.choice(c_options)).title()
    return name,c_options,v_options


def names_number_translator():
    """
returns an -RANDOM- INTEGER 1-5 based on a preset assymetric alogorithm

1 = 7%
2 = 73%
3 = 15%
4 = 4%
5 = 1%
"""
    number=random.randint(1, 100)
    if number == 1:
        return 5
    if 1 < number <= 5:
        return 4
    if 5 < number <= 20:
        return 3
    if 20 < number <= 93:
        return 2
    if 93 < number:
        return 1


def inheritted(number_of_names):
    """

"""
    inherit_number=random.randint(1, 100)
    if inheritted_question(number_of_names) == 'No':
        return ['',0,number_of_names]
    else:
        if 0 <= inherit_number <= 15:
            return ['Y',0,number_of_names]
        if 15 < inherit_number <= 30:
            return ['Y',1,number_of_names]
        if 30 < inherit_number <= 45:
            return ['Y',(number_of_names-2),number_of_names]
        if 45 < inherit_number:
            return ['Y',(number_of_names-1),number_of_names]


def inheritted_question(number_of_names):
    if number_of_names == 1:
        return ('No')
    inherited_question=random.randint(1, 100)
    if 0 < inherited_question < 30:
        return ('No')
    else:
        return ('Yes')


def compound_name():
    compound_num=random.randint(1, 100)
    if 0 < compound_num <= 4:
        fumber=4
    if 4 < compound_num <=44:
        fumber=3
    if 44 < compound_num:
        fumber=2
    chunk=str()
    for fname in range(fumber):
        lis=random.randint(0,2)
        nam=random.randint(0,9)
        chunk += randon[lis][nam]
    return chunk


def innie_name():
    typ=random.randint(1, 100)
    if 0 < typ <= 20:
        return compound_name()
    if 20 < typ <= 29:
        end=len(Boringf)-1
        ind=random.randint(0, end)
        lis=random.randint(0,2)
        nam=random.randint(0,9)
        chuk = randon[lis][nam]
        return Boringf[ind]+chuk
    if 29 < typ <= 92:
        return custom()
    if 92 < typ <= 97:
        end=len(Boringf)-1
        ind=random.randint(0, end)
        return Boringf[ind]
    if 97 < typ:
        return f2019f[random.randint(0,1)]


def outtie_name():
    typ=random.randint(1, 100)
    if 0 < typ <= 20:
        return compound_name()
    if 20 < typ <= 29:
        end=len(Boringm)-1
        ind=random.randint(0, end)
        lis=random.randint(0,2)
        nam=random.randint(0,9)
        chuk = randon[lis][nam]
        return Boringm[ind]+chuk
    if 29 < typ <= 92:
        return custom()
    if 92 < typ <= 97:
        end=len(Boringm)-1
        ind=random.randint(0, end)
        return Boringm[ind]
    if 97 < typ:
        return f2019m[random.randint(0,1)]


def family_name():
    fam=random.randint(1, 100)
    lis=random.randint(0,2)
    nam=random.randint(0,9)
    if 0 < fam <= 9:
        return compound_name()
    if 9 < fam <= 19:
        return Color[random.randint(0,5)]+randon[lis][nam]
    if 19 < fam <= 39:
        return Color[random.randint(0,5)]
    if 39 < fam <= 49:
        return Hard[random.randint(0,5)]+randon[lis][nam]
    if 49 < fam <= 69:
        return Hard[random.randint(0,5)]
    if 69 < fam:
        return custom()


def generate_name(gender='',names_no=''):
    name=[]
    stuff=[]
    if gender=='':
        gender=random.randint(1, 2)
    stuff=inheritted(names_number_translator())
    if names_no!='':
           stuff[2]=names_no
    if gender == 1:
        for chunks in range(stuff[2]):
            name.append(innie_name())
    if gender == 2:
        for chunks in range(stuff[2]):
            name.append(outtie_name())
    if stuff[0] == 'Y':
        name[stuff[1]]='!{}!'.format(family_name())
    return name


def girl_childs_name(moms_name,dads_name,m=''):
    name=[]
    if m=='':
        for x in dads_name:
            if '!' in x:
                name.append(x)
            else:
                name.append(innie_name())
    else:
        for x in moms_name:
            if '!' in x:
                name.append(x)
            else:
                name.append(innie_name())
    return name


def boy_childs_name(moms_name,dads_name,m=''):
    name=[]
    if m=='':
        for x in dads_name:
            if '!' in x:
                name.append(x)
            else:
                name.append(outtie_name())
    else:
        for x in moms_name:
            if '!' in x:
                name.append(x)
            else:
                name.append(outtie_name())
    return name


def childs_name(moms_name,dads_name,gender=0,n=''):
    if gender == 0:
        gender = random.randint(1,2)
    if gender == 1:
        return girl_childs_name(moms_name,dads_name,n)
    else:
        return boy_childs_name(moms_name,dads_name,n)

"""
_______________________________________

Tracks

_______________________________________

"""
flat_1s=[(1,3),(1,3),(1,3),(1,3),(1,3)]
flat_2s=[(2,3),(2,3),(2,3),(2,3),(2,3)]
flat_3s=[(3,3),(3,3),(3,3),(3,3),(3,3)]
flat_4s=[(4,3),(4,3),(4,3),(4,3),(4,3)]

chad1=[(2, 2), (2, 3), (2, 2), (2, 1), (2, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 2), (1, 1), (1, 1), (1, 1), (1, 2), (1, 2), (2, 1), (2, 1), (2, 1), (2, 2), (2, 3), (4, 4), (4, 3), (4, 2), (4, 3), (4, 2), (2, 3), (2, 2), (2, 3), (2, 3), (2, 4), (4, 5), (4, 5), (4, 4), (4, 4), (4, 3), (2, 2), (2, 2), (2, 2), (2, 3), (2, 3), (4, 4), (4, 5), (4, 4), (4, 3), (4, 2), (2, 1), (2, 1), (2, 2), (2, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 3), (3, 2), (1, 3), (1, 4), (1, 3), (1, 4), (1, 5), (3, 4), (3, 4), (3, 4), (3, 4), (3, 5), (1, 4), (1, 5), (1, 4), (1, 5), (1, 4), (2, 3), (2, 4), (2, 4), (2, 4), (2, 3), (4, 3), (4, 2), (4, 1), (4, 2), (4, 1), (3, 1), (3, 2), (3, 3), (3, 2), (3, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 2), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 5), (2, 4), (2, 4), (2, 4), (2, 5), (2, 5), (4, 4), (4, 3), (4, 3), (4, 2), (4, 3), (3, 2), (3, 2), (3, 3), (3, 3), (3, 4), (1, 3), (1, 2), (1, 3), (1, 3), (1, 2), (4, 3), (4, 3), (4, 3), (4, 2), (4, 1), (3, 2), (3, 2), (3, 1), (3, 2), (3, 3), (1, 2), (1, 3), (1, 2), (1, 3), (1, 4), (3, 4), (3, 3), (3, 2), (3, 2), (3, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 2), (2, 2), (2, 1), (2, 1), (2, 1), (2, 2), (4, 3), (4, 4), (4, 3), (4, 3), (4, 4), (2, 5), (2, 4), (2, 5), (2, 5), (2, 5), (3, 4), (3, 4), (3, 4), (3, 4), (3, 5), (1, 5), (1, 4), (1, 5), (1, 4), (1, 4), (2, 3), (2, 4), (2, 5), (2, 4), (2, 5), (3, 5), (3, 4), (3, 3), (3, 2), (3, 2), (1, 3), (1, 4), (1, 4), (1, 4), (1, 4), (4, 3), (4, 2), (4, 3), (4, 3), (4, 4), (2, 3), (2, 4), (2, 3), (2, 4), (2, 5), (4, 4), (4, 4), (4, 4), (4, 4), (4, 5), (1, 4), (1, 4), (1, 4), (1, 3), (1, 2)]
chad2=[(2, 5), (2, 4), (2, 3), (2, 2), (2, 2), (4, 3), (4, 2), (4, 3), (4, 2), (4, 3), (1, 2), (1, 1), (1, 2), (1, 3), (1, 3), (3, 4), (3, 5), (3, 4), (3, 4), (3, 4), (2, 5), (2, 5), (2, 4), (2, 3), (2, 2), (3, 1), (3, 2), (3, 3), (3, 3), (3, 4), (2, 3), (2, 2), (2, 1), (2, 1), (2, 1), (4, 2), (4, 1), (4, 1), (4, 1), (4, 2), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (2, 1), (2, 2), (2, 1), (2, 1), (2, 1), (3, 1), (3, 2), (3, 2), (3, 2), (3, 2), (2, 3), (2, 4), (2, 4), (2, 3), (2, 2), (4, 1), (4, 1), (4, 2), (4, 1), (4, 1), (2, 2), (2, 2), (2, 2), (2, 3), (2, 4), (4, 5), (4, 5), (4, 4), (4, 5), (4, 4), (3, 3), (3, 4), (3, 4), (3, 4), (3, 4), (1, 3), (1, 2), (1, 1), (1, 1), (1, 2), (2, 1), (2, 1), (2, 2), (2, 1), (2, 2), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (3, 2), (3, 3), (3, 2), (3, 1), (3, 2), (1, 1), (1, 1), (1, 2), (1, 2), (1, 2), (3, 3), (3, 4), (3, 4), (3, 5), (3, 5), (1, 5), (1, 5), (1, 4), (1, 3), (1, 4), (2, 3), (2, 4), (2, 3), (2, 4), (2, 4), (3, 3), (3, 3), (3, 2), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (2, 4), (2, 4), (3, 5), (3, 4), (3, 5), (3, 4), (3, 4), (2, 5), (2, 5), (2, 4), (2, 4), (2, 5), (3, 4), (3, 3), (3, 4), (3, 5), (3, 4), (1, 5), (1, 4), (1, 5), (1, 5), (1, 4), (4, 4), (4, 5), (4, 4), (4, 3), (4, 4), (2, 3), (2, 3), (2, 4), (2, 4), (2, 5), (3, 4), (3, 4), (3, 5), (3, 4), (3, 5), (1, 5), (1, 5), (1, 4), (1, 3), (1, 4), (3, 3), (3, 4), (3, 4), (3, 4), (3, 4), (1, 3), (1, 2), (1, 1), (1, 2), (1, 3), (3, 3), (3, 3), (3, 2), (3, 2), (3, 2), (1, 2), (1, 2), (1, 1), (1, 2), (1, 2), (3, 3), (3, 2), (3, 1), (3, 1), (3, 1), (1, 1), (1, 2), (1, 2), (1, 2), (1, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 2), (1, 2), (1, 1), (1, 1), (1, 2), (1, 3)]
chad3=[(3, 5), (3, 5), (3, 4), (3, 3), (3, 4), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (2, 5), (2, 5), (2, 5), (2, 4), (2, 3), (4, 3), (4, 3), (4, 3), (4, 4), (4, 3), (3, 4), (3, 3), (3, 3), (3, 4), (3, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 4), (3, 4), (3, 3), (3, 2), (3, 3), (3, 3), (1, 3), (1, 2), (1, 2), (1, 2), (1, 3), (4, 3), (4, 3), (4, 3), (4, 2), (4, 3), (1, 2), (1, 2), (1, 2), (1, 2), (1, 3), (2, 2), (2, 1), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 3), (3, 3), (3, 2), (1, 2), (1, 3), (1, 4), (1, 3), (1, 3), (3, 4), (3, 4), (3, 4), (3, 5), (3, 5), (2, 4), (2, 5), (2, 5), (2, 5), (2, 5), (4, 4), (4, 5), (4, 5), (4, 5), (4, 4), (2, 3), (2, 2), (2, 2), (2, 2), (2, 3), (4, 3), (4, 4), (4, 5), (4, 5), (4, 4), (3, 3), (3, 4), (3, 4), (3, 5), (3, 4), (2, 3), (2, 4), (2, 4), (2, 3), (2, 3), (3, 2), (3, 1), (3, 2), (3, 3), (3, 4), (1, 3), (1, 3), (1, 4), (1, 5), (1, 5), (2, 5), (2, 4), (2, 3), (2, 2), (2, 1), (3, 1), (3, 2), (3, 3), (3, 2), (3, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (4, 4), (4, 4), (4, 3), (4, 4), (4, 4), (2, 5), (2, 5), (2, 5), (2, 4), (2, 5), (3, 4), (3, 3), (3, 3), (3, 2), (3, 1), (1, 2), (1, 2), (1, 3), (1, 2), (1, 2), (3, 2), (3, 2), (3, 2), (3, 1), (3, 2), (1, 2), (1, 3), (1, 3), (1, 4), (1, 4), (3, 3), (3, 2), (3, 3), (3, 4), (3, 3), (2, 2), (2, 2), (2, 1), (2, 2), (2, 2), (3, 1), (3, 2), (3, 1), (3, 1), (3, 2), (1, 3), (1, 2), (1, 3), (1, 4), (1, 3), (3, 3), (3, 4), (3, 3), (3, 2), (3, 1), (2, 1), (2, 1), (2, 1), (2, 2), (2, 2), (3, 2), (3, 1), (3, 1), (3, 2), (3, 3), (2, 4), (2, 4), (2, 3), (2, 2), (2, 3)]

flat_smeet=[flat_1s,flat_2s,flat_3s,flat_4s]
chadprix=[chad1,chad2,chad3]

"""
_______________________________________

Chars

_______________________________________

"""

def master(being):
    master=float()
    sex_num=int()
    for genes in range(12):
        sex_num += int(being[0][0][genes])
    if sex_num > 24:
        master=float()
        threes=1
        non_threes=int()
        for genes in range(12):
            if being[0][0][genes] == 3:
                threes += 3
            else:
                non_threes += being[0][0][genes]
        master = non_threes / threes
        if float(master) == 0:
            master=float(0.1)
        return float(master)
    else:
        master=float()
        ones=1
        non_ones=int()
        for genes in range(12):
            if being[0][0][genes] == 1:
                ones += 1
            else:
                non_ones += being[0][0][genes]
        master = float(non_ones / ones)
        if float(master) == 0:
            master=float(0.1)
        return float(master)


def boy_master(being):
    master=float()
    threes=1
    non_threes=int()
    for genes in range(12):
        if being[0][0][genes] == 3:
            threes += 3
        else:
            non_threes += being[0][0][genes]
    master = non_threes / threes
    print(non_threes,threes,being[0][0],'a',master)
    return float(master)


def girl_master(being):
    master=float()
    ones=1
    non_ones=int()
    for genes in range(12):
        if being[0][0][genes] == 1:
            ones += 1
        else:
            non_ones += being[0][0][genes]
    master = float(non_ones / ones)
    print (non_ones , ones,being[0][0],'b',master)
    return float(master)


def sub_char(a,b,c):
    if a == 1:
        return abs(float(b - c))
    if a == 2:
        return float(b / c)
    if a == 3:
        return float(b * c)
    if a == 4:
        return float(b + c)


def char_1(being):
    a=being[0][0][3]
    b=being[0][0][4]
    c=being[0][0][5]
    d=being[0][1][3]
    e=being[0][1][4]
    f=being[0][1][5]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_2(being):
    a=being[1][0][3]
    b=being[1][0][4]
    c=being[1][0][5]
    d=being[1][1][3]
    e=being[1][1][4]
    f=being[1][1][5]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_3(being):
    a=being[1][0][5]
    b=being[1][0][6]
    c=being[1][0][7]
    d=being[1][1][5]
    e=being[1][1][6]
    f=being[1][1][7]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=1+v1+v2
    return vt


def char_4(being):
    a=being[2][0][1]
    b=being[2][0][2]
    c=being[2][0][3]
    d=being[2][1][1]
    e=being[2][1][2]
    f=being[2][1][3]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_5(being):
    a=being[2][0][3]
    b=being[2][0][4]
    c=being[2][0][5]
    d=being[2][1][3]
    e=being[2][1][4]
    f=being[2][1][5]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_6(being):
    a=being[2][0][7]
    b=being[2][0][8]
    c=being[2][0][9]
    d=being[2][1][7]
    e=being[2][1][8]
    f=being[2][1][9]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_7(being):
    a=being[2][0][9]
    b=being[2][0][10]
    c=being[2][0][11]
    d=being[2][1][9]
    e=being[2][1][10]
    f=being[2][1][11]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_8(being):
    a=being[2][0][5]
    b=being[2][0][6]
    c=being[2][0][7]
    d=being[2][1][5]
    e=being[2][1][6]
    f=being[2][1][7]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_9(being):
    a=being[3][0][0]
    b=being[3][0][1]
    c=being[3][0][2]
    d=being[3][1][0]
    e=being[3][1][1]
    f=being[3][1][2]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_10(being):
    a=being[3][0][9]
    b=being[3][0][10]
    c=being[3][0][11]
    d=being[3][1][9]
    e=being[3][1][10]
    f=being[3][1][11]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt

def char_a(being):
    a=being[1][0][6]
    b=being[1][0][7]
    c=being[1][0][8]
    d=being[1][1][6]
    e=being[1][1][7]
    f=being[1][1][8]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_b(being):
    a=being[0][0][8]
    b=being[0][0][9]
    c=being[0][0][10]
    d=being[0][1][8]
    e=being[0][1][9]
    f=being[0][1][10]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_11(being):
    a=being[3][0][3]
    b=being[3][0][4]
    c=being[3][0][5]
    d=being[3][1][3]
    e=being[3][1][4]
    f=being[3][1][5]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_12(being):
    a=being[3][0][6]
    b=being[3][0][7]
    c=being[3][0][8]
    d=being[3][1][6]
    e=being[3][1][7]
    f=being[3][1][8]
    v1=sub_char(a,b,c)
    v2=sub_char(d,e,f)
    vt=v1+v2
    return vt


def char_dict(being):
    char_dict={
        '1':float(char_1(being)),
        '2':float(char_2(being)),
        '3':float(char_3(being)),
        '4':float(char_4(being)),
        '5':float(char_5(being)),
        '6':float(char_6(being)),
        '7':float(char_7(being)),
        '8':float(char_8(being)),
        '9':float(char_9(being)),
        '10':float(char_10(being)),
        'a':float(char_a(being)),
        'b':float(char_b(being)),
        '11':float(char_11(being)),
        '12':float(char_12(being)),
        'm':float(master(being))
    }
    return char_dict

"""
_______________________________________

Clas

_______________________________________

"""

class Being():
    def __init__(self,name,code,mom,dad,village_born_in):
        self.name=name
        self.code=code
        self.mom=mom
        self.dad=dad
        self.children=[]
        self.village_born_in=village_born_in
        self.name_options=[]

    def add_child(self, being):
        return self.children.append([being.name,being.code])



def check_sex(being):
    sex_mum=int()
    for genes in range(12):
        sex_mum += int(being[0][0][genes])
    if sex_mum > 25:
        return 2
    else:
        return 1


def create_named_being(gender=''):
    if gender=='':
        gender=random.randint(1, 2)
    if gender == 1 :
        return[generate_name(1),generate_innie()]
    if gender == 2 :
        return[generate_name(2),generate_outtie()]


def create_classed_being(vbi=' '):
    if vbi == ' ':
        vbi=cvs()
    mom=create_named_being(1)
    dad=create_named_being(2)
    name=childs_name(mom[0],dad[0])
    code=generate_child(mom[1],dad[1])
    village_born_in=vbi
    instance=variable_name(name)
    instance= Being(name,code,mom,dad,village_born_in)
    return instance


def create_classed_innie(vbi='Somewhere Else...'):
    mom=create_named_being(1)
    dad=create_named_being(2)
    name=childs_name(mom[0],dad[0],1)
    code=generate_child(mom[1],dad[1],1)
    village_born_in=vbi
    instance=variable_name(name)
    instance= Being(name,code,mom,dad,village_born_in)
    return instance


def create_classed_outtie(vbi='Somewhere Else...'):
    mom=create_named_being(1)
    dad=create_named_being(2)
    name=childs_name(mom[0],dad[0],2)
    code=generate_child(mom[1],dad[1],2)
    village_born_in=vbi
    instance=variable_name(name)
    instance= Being(name,code,mom,dad,village_born_in)
    return instance


def create_and_save_being(gender=' ',vbi=' '):
    if vbi == ' ':
        vbi=cvs()
    if gender == ' ':
        return pickle_being(create_classed_being(vbi))
    if gender == 'innie':
        return pickle_being(create_classed_innie(vbi))
    if gender == 'outtie':
        return pickle_being(create_classed_outtie(vbi))


def conceive(mom,dad):
    try:
        name=childs_name(mom[0],dad[0])
        code=generate_child(mom[1],dad[1])
        momo=mom
        dado=dad
    except:
        name=childs_name(mom.name,dad.name)
        code=generate_child(mom.code,dad.code)
        momo=[mom.name,mom.code]
        dado=[dad.name,dad.code]
    village_born_in=cvs()
    instance=variable_name(name)
    instance= Being(name,code,momo,dado,village_born_in)
    return instance


def pickle_being(being):
    return saave(being,display_name(being.name),'classed_beings{}'.format(cvs()))


def bios_classed():
    for name, stuff in all_pick('classed_beings{}'.format(cvs())).items():
        try:
            print('-----------------------------------')
            print (name)
            print('------')
            Bio(stuff.code)
        except:
            print('ERROR')
            continue
    return ''

def has_kids():
    vll=cvl()
    hk={}
    for name, stuff in cvl().items():
        if stuff.children == []:
            continue
        else:
            hk[name]=stuff
    return hk



def children_classed():
    for name, stuff in all_pick('classed_beings{}'.format(cvs())).items():
        print(' ')
        print(' ')
        print (name)
        print('------')
        if stuff.children != []:
            for child in stuff.children:
                print ('---',display_name(child[0]))
        else:
            print('No Kids')
        continue
    return ''


def parents_classed():
    for name, stuff in all_pick('classed_beings{}'.format(cvs())).items():
        try:
            print('@-----------------------------------@')
            print (name)
            print('------')
            print('Mom:',display_name(stuff.mom[0]))
            print ('Dad:',display_name(stuff.dad[0]))
            print('------')
        except:
            print('ERROR')
            continue
    return ''


def pickle_children(being):
    mom=being.mom[0]
    dad=being.dad[0]
    people=all_pick('classed_beings{}'.format(cvs()))
    if display_name(dad) in list(people.keys()):
        people[display_name(dad)].add_child(being)
    if display_name(mom) in list(people.keys()):
        people[display_name(mom)].add_child(being)
    return overwrite(people,'classed_beings{}'.format(cvs()))


def overwrite(obj,file):
    stuff=obj
    db={}
    dbfile=open(file,'wb')
    pickle.dump(db,dbfile)
    dbfile.close()
    for name, instance in stuff.items():
        saave(instance,name,file)
    return file,obj,'4'


def add_track(track,name):
    t=all_pick('tracks')
    t[name]=track
    overwrite(t,'tracks')
    print('-------')
    return all_pick('tracks')


def conceive_and_add(mom,dad):
    gender = random.randint(1,2)
    name=childs_name(mom.name,dad.name,gender)
    code=generate_child(mom.code,dad.code,gender)
    village_born_in=cvs()
    instance=variable_name(name)
    instance= Being(name,code,[mom.name,mom.code],[dad.name,dad.code],village_born_in)
    pickle_being(instance)
    CVA.update({display_name(name):[instance, cvs()]})
    pickle_children(instance)
    return instance


def pickle_family(mom,dad,number=random.randint(1,5)):
    kids = 0
    for conceptions in range(number):
        conceive_and_add(mom,dad)
        kids += 1
    return kids


def create_group(number=random.randint(5,25)):
    for creator in range(number):
        create_and_save_being()
    return ''


def classed_names():
    people=all_pick('classed_beings{}'.format(cvs()))
    names=list(people.keys())
    return names


def find_innie(number=10):
    for finder in range(number):
        she= all_pick('classed_beings{}'.format(cvs()))[random.choice(classed_names())]
        if check_sex(she.code)==1:
            return she
        else:
            continue
    raise Exception('Could not find a mommy :(')


def find_outtie(number=10):
    for finder in range(number):
        he= all_pick('classed_beings{}'.format(cvs()))[random.choice(classed_names())]
        if check_sex(he.code)==2:
            return he
        else:
            continue
    raise Exception('Could not find a dad :(')


def random_baby(number=10):
    mom=find_innie(number)
    dad=find_outtie(number)
    return conceive_and_add(mom,dad)


def random_babies(babies,number=10):
    for babymaker in range(babies):
        random_baby(number)
    return ''

def sort_by_gender():
    dudes=[]
    chicks=[]
    dc=0
    cc=0
    for counter,villager in enumerate(current_villagers_list()):
        if check_sex(current_villagers_list()[villager].code) == 2:
            dudes.append([dc,villager])
            dc+=1
        if check_sex(current_villagers_list()[villager].code) == 1:
            chicks.append([cc,villager])
            cc+=1
    return [dudes,chicks]

def sort_by_gender_being():
    dudes={}
    chicks={}
    for villager in current_villagers_list():
        if check_sex(current_villagers_list()[villager].code) == 2:
            dudes.update({villager:cvl()[villager]})
        if check_sex(current_villagers_list()[villager].code) == 1:
            chicks.update({villager:cvl()[villager]})
    return [dudes,chicks]
"""
all_pick('classed_beings{}'.format(cvs()))[random.choice(classed_names())]
_______________________________________

run_track

_______________________________________

"""


def generate_track(length=int(5),group_length=int(10)):
    track=[]
    piece=()
    terrain=random.randint(1, 4)
    slope=random.randint(1, 5)
    for x in range(length):
        if terrain == 1:
            terrain += random.randint(1, 3)
            for y in range(group_length):
                if slope == 1:
                    slope += random.randint(0, 1)
                    piece=(terrain,slope)
                    track.append(piece)
                elif slope == 5:
                    slope += random.randint(-1, 0)
                    piece=(terrain,slope)
                    track.append(piece)
                else:
                    slope += random.randint(-1, 1)
                    piece=(terrain,slope)
                    track.append(piece)
        if terrain == 2:
            terrain += random.randint(1, 2)
            for y in range(group_length):
                if slope == 1:
                    slope += random.randint(0, 1)
                    piece=(terrain,slope)
                    track.append(piece)
                elif slope == 5:
                    slope += random.randint(-1, 0)
                    piece=(terrain,slope)
                    track.append(piece)
                else:
                    slope += random.randint(-1, 1)
                    piece=(terrain,slope)
                    track.append(piece)
        if terrain == 3:
            terrain += random.randint(-2, -1)
            for y in range(group_length):
                if slope == 1:
                    slope += random.randint(0, 1)
                    piece=(terrain,slope)
                    track.append(piece)
                elif slope == 5:
                    slope += random.randint(-1, 0)
                    piece=(terrain,slope)
                    track.append(piece)
                else:
                    slope += random.randint(-1, 1)
                    piece=(terrain,slope)
                    track.append(piece)
        if terrain == 4:
            terrain += random.randint(-3, -1)
            for y in range(group_length):
                if slope == 1:
                    slope += random.randint(0, 1)
                    piece=(terrain,slope)
                    track.append(piece)
                elif slope == 5:
                    slope += random.randint(-1, 0)
                    piece=(terrain,slope)
                    track.append(piece)
                else:
                    slope += random.randint(-1, 1)
                    piece=(terrain,slope)
                    track.append(piece)
    length=int()
    group_length=int()
    """
    print (len(track),length,group_length)
    """
    return track


def generate_track_piece():
    terrain=random.randint(1, 4)
    slope=random.randint(-2, 2)
    piece=(terrain,slope)
    return piece


def run_track(track,being):
    cd=char_dict(being)
    time=int(0)
    x=int(0)
    for piece in track:
        a=str(3+track[x][0])
        an=int(a)
        b=str(7+track[x][1])
        bn=int(b)
        time+=((cd['3'])*((cd[a]+cd['b'])/((cd['m'])*(an)))+
         (cd['3'])*((cd[b]+cd['1'])/((cd['m'])*(bn))))
        x+=1
    return time


def run_heat(track,runners):
    heat_results={}
    rt={}
    for x,y in runners.items():
        heat_results.update([(x,run_track(track,y))])
    rt=sorted(heat_results.items(), key=operator.itemgetter(1))
    return rt


def run_meet(tracks,runners):
    heat_results=int()
    meet_results={}
    rt={}
    for x,y in runners.items():
        heat_results=int(0)
        for track in tracks:
            heat_results+=run_track(track,y)
        meet_results.update([(x,heat_results)])
    rt=sorted(meet_results.items(), key=operator.itemgetter(1))
    return rt


def run_trial(tracks,runner):
    trial_results=float()
    for track in tracks:
        try:
            trial_results+=run_track(track,runner)
        except :
            trial_results+=run_track(track,runner.code)
    return trial_results


def run_random_from_file():
    track=find_random('tracks')
    runner=find_random('people')
    result=int(run_track(track[1],runner[1]))
    return [result,track[0],runner[0]]

"""
_______________________________________


generators

_______________________________________

"""

children=random.randint(1, 5)

def generate_chromosome():
    chrom = []
    for gene in range(12):
        chrom.append(int(random.randint(1, 4)))
    return chrom


def generate_chrom_set():
    chrom_set = []
    for chromset in range(2):
        chrom_set.append(generate_chromosome())
    return chrom_set


def generate_being():
    being =[]
    sex_gene_1=[]
    sex_gene_2=[]
    for chromset in range(4):
        being.append(generate_chrom_set())
    gender=random.randint(1, 2)
    if gender == 1:
       for gene in range(12):
        sex_gene_1.append(int(random.randint(1, 2)))
        sex_gene_2.append(int(random.randint(1, 2)))
    if gender == 2:
       for gene in range(12):
        sex_gene_1.append(int(random.randint(3, 4)))
        sex_gene_2.append(int(random.randint(1, 2)))
    being[0][0]=sex_gene_1
    being[0][1]=sex_gene_2
    return being


def generate_innie():
    being =[]
    sex_gene_1=[]
    sex_gene_2=[]
    for chromset in range(4):
        being.append(generate_chrom_set())
    for gene in range(12):
        sex_gene_1.append(int(random.randint(1, 2)))
        sex_gene_2.append(int(random.randint(1, 2)))
    being[0][0]=sex_gene_1
    being[0][1]=sex_gene_2
    return being


def generate_outtie():
    being =[]
    sex_gene_1=[]
    sex_gene_2=[]
    for chromset in range(4):
        being.append(generate_chrom_set())
    for gene in range(12):
        sex_gene_1.append(int(random.randint(3, 4)))
        sex_gene_2.append(int(random.randint(1, 2)))
    being[0][0]=sex_gene_1
    being[0][1]=sex_gene_2
    return being


def check_gender(being):
    sex_mum=int()
    for genes in range(12):
        sex_mum += int(being[0][0][genes])
    if sex_mum > 24:
        return 'Outtie'
    else:
        return 'Innie'


def check_parents_gender(mom,dad):
    sex_mum=int()
    for genes in range(12):
        sex_mum += int(mom[0][0][genes])
    if sex_mum > 24:
        return 'shes a dude, dude'
    sex_dum=int()
    for genes in range(12):
        sex_dum += int(dad[0][0][genes])
    if sex_dum < 24:
        return 'hes a lady, lady'


def generate_child(mom,dad,gender=0):
    if gender == 0:
        gender = random.randint(1,2)
    sex_mum=int()
    for genes in range(12):
        sex_mum += int(mom[0][0][genes])
    if sex_mum > 24:
        raise Exception( 'shes a dude, dude')
    sex_dum=int()
    for genes in range(12):
        sex_dum += int(dad[0][0][genes])
    if sex_dum < 24:
        raise Exception( 'hes a lady, lady')
    set_1m_choice=random.randint(0, 1)
    set_2m_choice=random.randint(0, 1)
    set_3m_choice=random.randint(0, 1)
    set_4m_choice=random.randint(0, 1)
    if gender==1:
        set_1d_choice=1
    if gender==2:
        set_1d_choice=0
    set_2d_choice=random.randint(0, 1)
    set_3d_choice=random.randint(0, 1)
    set_4d_choice=random.randint(0, 1)
    """print(set_1m_choice,set_2m_choice,set_3m_choice,set_4m_choice,set_1d_choice,set_2d_choice,set_3d_choice,set_4d_choice)"""
    child=[]
    child=[[dad[0][set_1d_choice],mom[0][set_1m_choice]],
           [dad[1][set_2d_choice],mom[1][set_2m_choice]],
           [dad[2][set_3d_choice],mom[2][set_3m_choice]],
           [dad[3][set_4d_choice],mom[3][set_4m_choice]]]
    mutate(child)
    return child


def q_kid():
    return generate_child(generate_innie(),generate_outtie())


def generate_family(mom,dad,children=children):
    family_dict={}
    kidno=int(0)
    family_dict.update([('mom',mom),('dad',dad)])
    for kids in range(children):
        kidno+=1
        new_kid=[]
        new_kid_name='Child{}'.format(str(kidno))
        new_kid=generate_child(mom,dad)
        family_dict.update([(new_kid_name,new_kid)])
    return family_dict

"""
_______________________________________


Bio

_______________________________________

"""

def hair_color(being):
    codon=char_dict(being)['2']
    hc=str()
    if codon <= 1:
        hc='Green'
    if 1 < codon <= 4:
        hc='Blonde'
    if 4 < codon <= 9:
        hc='Black'
    if 9 < codon <= 19:
        hc='Brown'
    if 19 < codon <31:
        hc='Silver'
    if codon >= 31:
        hc='Flames'
    return hc


def eye_color(being):
    codon=char_dict(being)['a']
    hc=str()
    if codon <= 1:
        hc='Black'
    if 1 < codon <= 4:
        hc='Blue'
    if 4 < codon <= 9:
        hc='Brown'
    if 9 < codon <= 19:
        hc='Green'
    if 19 < codon <31:
        hc='Purple'
    if codon >= 31:
        hc='Flames'
    return hc
    return none

hcs=['Green','Blonde','Black','Brown','Silver','Flames']
ecs=['Green','Blue','Black','Brown','Purple','Flames']

def height(being):
    h=int(35+char_dict(being)['m']*char_dict(being)['8']+char_dict(being)['m']*char_dict(being)['7'])
    f=math.trunc(h/12)
    hf=h-(f*12)
    return f,hf


def weight(being):
    codo=int(25*(char_dict(being)['m'])+(char_dict(being)['8']*char_dict(being)['5']+char_dict(being)['5']*char_dict(being)['8']+char_dict(being)['4']*char_dict(being)['5']+char_dict(being)['6']*char_dict(being)['7'])/2)
    return codo


def Bio(being):
    cd=char_dict(being)
    print('Height', '            || ',height(being)[0],'foot',height(being)[1],'in')
    print('Weight', '            || ',weight(being),'lbs')
    print('Hair Color', '        || ',hair_color(being))
    print('Eye Color', '         || ',eye_color(being))
    print('Biological Gender', ' || ',check_gender(being))
    print('ChadPrix Time','     || ',int(run_trial(chadprix,being)))
    print('Flat Smeet Time','   || ',int(run_trial(flat_smeet,being)))
    return being


def bios(beings):
    for name, code in beings.items():
        print('-----------------------------------')
        print (name)
        print('------')
        Bio(code)
    return ''


def bioc(being):
    print('-----------------------------------')
    print (being.name)
    print('------')
    Bio(being.code)
    print('Mom', '               || ',display_name(being.mom[0]))
    print('Dad', '               || ',display_name(being.dad[0]))
    if being.children != []:
        print('Names of children')
        print('------')
        for child in being.children:
            print ('*',display_name(child[0]))
    return ''

def named_being(gender=''):
    if gender=='':
        gender=random.randint(1, 2)
    if gender == 1 :
        print(generate_name(1))
        print(Bio(generate_innie()))
    if gender == 2 :
        print(generate_name(2))
        print(Bio(generate_outtie()))


def display_name(name_list):
    d_n=''
    for name in name_list:
        d_n+=' '
        d_n+=name.title()
    return d_n


def list_name(name_string):
    ln=[]
    ln=(name_string).split()
    return ln


def variable_name(name_list):
    v_n = ''
    for name in name_list:
        v_n+=name.title()
        v_n+='_'
    return v_n

"""
_______________________________________


savers

def overwrite(obj,file):
    stuff=obj
    db={}
    dbfile=open(file,'wb')
    pickle.dump(db,dbfile)
    dbfile.close()
    for name, instance in stuff.items():
        saave(instance,name,file)
    return file,obj,'4'
_______________________________________

"""

def saave(obj,name,file):
    db={}
    db[name]=obj
    dbfile = open(file,'ab')
    pickle.dump(db,dbfile)
    dbfile.close()
    return obj


def all_pick(file):
    obj = {}
    with open(file,"rb") as fileOpener:
        while True:
            try:
                obj.update(pickle.load(fileOpener))
            except EOFError:
                break        
    return obj


def safe_pick(file):
    obj ={}
    try:
       obj=all_pick(file)
    except:
        pass
    return obj

    
def all_pick_list(file):
    obj = []
    with open(file,"rb") as fileOpener:
        while True:
            try:
                obj.append(pickle.load(fileOpener))
            except EOFError:
                break
    return obj


def find_in_file(file,name):
    obj = {}
    with open(file,"rb") as fileOpener:
        while True:
            try:
                obj.update(pickle.load(fileOpener))
            except EOFError:
                break
    if name in obj:
        print (obj[name])
    else:
        print (':(')


def find_random(file):
    obj = {}
    with open(file,"rb") as fileOpener:
        while True:
            try:
                obj.update(pickle.load(fileOpener))
            except EOFError:
                break
    return random.choice(list(obj.keys())),random.choice(list(obj.values()))


"""
_______________________________________


mutations

_______________________________________

"""


def mutate(being):
    """
    cycle_type=being[1][1][0]
    cycles=being[1][0][0]
    """
    cycle_type=1
    cycles=being[1][0][0]
    if cycle_type==1:
        for mutations in range(cycles):
            spot_change_mutation(being)
            return being
        """
    if cycle_type==2:
        for mutations in range(cycles):
            spot_delete_mutation(being)
            return being
    if cycle_type==3:
        for mutations in range(cycles):
            spot_add_mutation(being)
            return being
    if cycle_type==4:
        for mutations in range(cycles):
            spot_add_mutation(being)
            spot_delete_mutation(being)
            spot_change_mutation(being)
            return being
    if cycle_type>4:
        return being
        """


def spot_change_mutation(being):
    gene_loc = random.randint(0, 11)
    chrom_set_loc = random.randint(0, 3)
    chrom_loc = random.randint(0, 1)
    new_value = random.randint(1, 4)
    old_value = being[chrom_set_loc][chrom_loc][gene_loc]
    if old_value == 1 and  new_value == 1:
        new_value=random.randint(2, 4)
    if old_value == 2 and  new_value == 2:
        new_value=random.randint(3, 4)
    if old_value == 3 and  new_value == 3:
        new_value=random.randint(1, 2)
    if old_value == 4 and  new_value == 4:
        new_value=random.randint(1, 3)
    being[chrom_set_loc][chrom_loc][gene_loc]=new_value
    return being


def spot_delete_mutation(being):
    gene_loc = random.randint(0, 10)
    chrom_set_loc = random.randint(0, 3)
    chrom_loc = random.randint(0, 1)
    new_value = random.randint(1, 4)
    old_value = being[chrom_set_loc][chrom_loc][gene_loc]
    del being[chrom_set_loc][chrom_loc][gene_loc]
    being[chrom_set_loc][chrom_loc].append(new_value)
    return (being)


def spot_add_mutation(being):
    gene_loc = random.randint(0, 10)
    chrom_set_loc = random.randint(0, 3)
    chrom_loc = random.randint(0, 1)
    new_value = random.randint(1, 4)
    old_value = being[chrom_set_loc][chrom_loc][gene_loc]
    being[chrom_set_loc][chrom_loc].insert(gene_loc,new_value)
    del being[chrom_set_loc][chrom_loc][12]
    return (being)
"""
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
"""

def dict_siblings():
    all_siblings={}
    people=all_pick('classed_beings{}'.format(cvs()))
    for name, stuff in people.items():
        all_siblings.update(find_siblings(stuff))
    return all_siblings


def find_siblings(being):
    siblings_dict={}
    mom1=display_name(being.mom[0])
    dad1=display_name(being.dad[0])
    people=all_pick('classed_beings{}'.format(cvs()))
    half_sibling=[]
    full_sibling=[]
    for namex, stuffx in people.items():
        name2=namex
        mom2=display_name(stuffx.mom[0])
        dad2=display_name(stuffx.dad[0])
        if mom1 == mom2:
            if name2 == display_name(being.name):
                continue
            if dad1 == dad2:
                full_sibling.append([namex])
            else:
                if name2 == being.name:
                    continue
                half_sibling.append([namex,'Same Mom'])
        elif dad1 == dad2:
            if name2 == display_name(being.name):
                continue
            half_sibling.append([namex,'Same Dad'])
        else:
            continue
    siblings=(half_sibling,full_sibling,mom1,dad1)
    siblings_dict[display_name(being.name)]=siblings
    return siblings_dict

def find_siblings_ALL(nameloc):
    ca=CVA
    siblings_dict={}
    being=ca[nameloc[0][0]][0]
    """print (ca[nameloc[0][0]])"""
    mom1=display_name(ca[nameloc[0][0]][0].mom[0])
    dad1=display_name(ca[nameloc[0][0]][0].dad[0])
    people=ca
    half_sibling=[]
    full_sibling=[]
    for namex, stuffx in people.items():
        name2=namex
        mom2=display_name(stuffx[0].mom[0])
        dad2=display_name(stuffx[0].dad[0])
        if mom1 == mom2:
            if name2 == display_name(being.name):
                continue
            if dad1 == dad2:
                full_sibling.append(namex)
            else:
                if name2 == being.name:
                    continue
                half_sibling.append([namex,'Same Mom'])
        elif dad1 == dad2:
            if name2 == display_name(being.name):
                continue
            half_sibling.append([namex,'Same Dad'])
        else:
            continue
    siblings=(half_sibling,full_sibling,mom1,dad1)
    siblings_dict[display_name(being.name)]=siblings
    return siblings_dict

def display_siblings():
    s=dict_siblings()
    for name, sibs in s.items():
        print ('____________________________________________________')
        print (' ')
        print (name)
        print ('Mother :{}'.format(sibs[2]))
        print ('Father :{}'.format(sibs[3]))
        print ('------------------------')
        print ('Half Siblings:',sibs[0])
        print ('------')
        print ('Full Siblings:',sibs[1])
        print ('------')
        print ('____________________________________________________')
    return ''


def tp():
        trak=find_random('tracks')
        p1=find_random('classed_beings{}'.format(cvs()))[1].code
        p2=find_random('classed_beings{}'.format(cvs()))[1].code
        r1=run_track(trak[1],p1)
        r2=run_track(trak[1],p2)
        a=(((r1+r2)/2)+350)
        mod=random.randint(1,2)
        if mod == 1:
            result=(0.8)*a
        if mod == 2:
            result=(1.25)*a
        return [trak[0],result,mod]


def pcp():
    pcp_type=random.randint(1,4)
    pcp_modifier=random.randint(1,2)
    if pcp_type == 1:
        return ['Hair Color',random.choice(['Green','Blonde','Black','Brown']),pcp_modifier]
    if pcp_type == 2:
        return ['Eye Color',random.choice(['Green','Blue','Black','Brown']),pcp_modifier]
    if pcp_type == 3:
        return ['Height',random.randint(45,100),pcp_modifier]
    if pcp_type == 4:
        return ['Weight',random.randint(45,350),pcp_modifier]


def create_param():
    p_type=random.randint(1,2)
    if p_type==1:
        return tp()
    if p_type==2:
        return pcp()


def create_objective(p=random.randint(2,5)):
    objective=[]
    x=0
    track_shutoff=''
    while x < p:
        x=len(objective)
        new_param=create_param()
        if any(new_param[0] in sublist for sublist in objective):
            continue
        try:
            f2=float(new_param[1])
            if f2 > float(350):
                if track_shutoff == '':
                    track_shutoff='yes'
                    objective.append(new_param)
                    continue
                else:
                    continue
            objective.append(new_param)
        except:
            objective.append(new_param)
    return objective


def check_objectives():
    goal_reachers=[]
    all_objectives=safe_pick('objectives{}'.format(cvs()))
    all_tracks=safe_pick('tracks')
    all_people=safe_pick('classed_beings{}'.format(cvs()))
    winners=[]
    real_winners=[]
    past_winners=[]
    for objective_name,params in all_objectives.items():
        """print('----------',all_objectives,objective_name)"""
        for idx,param in enumerate(params):
            real_winners=[]
            """print('----1',param,idx)"""
            """print(2,past_winners,'xxxxxxxx',real_winners)"""
            winners=check_one_param(param)
            """print(3,past_winners,'xxxxxxxx',winners)"""
            if not idx == 0:
                """print(6,idx,winners)"""
                for name in winners:
                    if name in past_winners:
                        real_winners+=name
                        """print(7,name)"""
                        continue
                    else:
                        """print(8,name)"""
                        continue

                past_winners=real_winners
                """print(4,real_winners)"""
            else:
                past_winners=winners
                """print(5,past_winners)"""
        goal_reachers.append([objective_name,real_winners])
    return goal_reachers


def check_one_param(ob):
    """print(ob)"""
    all_people=safe_pick('classed_beings{}'.format(cvs()))
    all_tracks=safe_pick('tracks')
    goal_reachers=[]
    param=ob
    """print(display_param(param))"""
    for person,stuff in all_people.items():
        if param[0]== 'Hair Color':
            phc=str(hair_color(stuff.code))
            """print(phc,person)"""
            if param[2] == 1:
                if phc == param[1]:
                    goal_reachers.append([person])
                    continue
            if param[2] == 2:
                if phc != param[1]:
                    goal_reachers.append([person])
                    continue
            continue
        elif param[0]== 'Eye Color':
            pec=str(eye_color(stuff.code))
            """print(pec,person)"""
            if param[2] == 1:
                if pec == param[1]:
                    goal_reachers.append([person])
                    continue
            if param[2] == 2:
                if pec != param[1]:
                    goal_reachers.append([person])
                    continue
            continue
        elif param[0]== 'Weight':
            pw=weight(stuff.code)
            """print(pw,person)"""
            if param[2] == 1:
                if pw >= param[1]:
                    goal_reachers.append([person])
                    continue
            if param[2] == 2:
                if pw <= param[1]:
                    goal_reachers.append([person])
                    continue
            continue
        elif param[0]== 'Height':
            ph=inch_height(stuff.code)
            """print(ph,person)"""
            if param[2] == 1:
                if ph >= param[1]:
                    goal_reachers.append([person])
                    continue
            if param[2] == 2:
                if ph <= param[1]:
                    goal_reachers.append([person])
                    continue
            continue
        else:
            time=run_track(all_tracks[param[0]],stuff.code)
            """print(time,person)"""
            if param[2] == 1:
                if time < param[1]:
                    goal_reachers.append([person])
                    continue
            if param[2] == 2:
                if time > param[1]:
                    goal_reachers.append([person])
                    continue
            continue
    return goal_reachers


def check_one_param_display(ob):
    """print(ob)"""
    all_people=safe_pick('classed_beings{}'.format(cvs()))
    all_tracks=safe_pick('tracks')
    goal_reachers=[]
    param=ob
    print(display_param(param))
    for person,stuff in all_people.items():
        if param[0]== 'Hair Color':
            phc=str(hair_color(stuff.code))
            print(phc,person)
            if param[2] == 1:
                if phc == param[1]:
                    goal_reachers.append([person])
                    continue
            if param[2] == 2:
                if phc != param[1]:
                    goal_reachers.append([person])
                    continue
            continue
        elif param[0]== 'Eye Color':
            pec=str(eye_color(stuff.code))
            print(pec,person)
            if param[2] == 1:
                if pec == param[1]:
                    goal_reachers.append([person])
                    continue
            if param[2] == 2:
                if pec != param[1]:
                    goal_reachers.append([person])
                    continue
            continue
        elif param[0]== 'Weight':
            pw=weight(stuff.code)
            print(pw,person)
            if param[2] == 1:
                if pw >= param[1]:
                    goal_reachers.append([person])
                    continue
            if param[2] == 2:
                if pw <= param[1]:
                    goal_reachers.append([person])
                    continue
            continue
        elif param[0]== 'Height':
            ph=inch_height(stuff.code)
            print(ph,person)
            if param[2] == 1:
                if ph >= param[1]:
                    goal_reachers.append([person])
                    continue
            if param[2] == 2:
                if ph <= param[1]:
                    goal_reachers.append([person])
                    continue
            continue
        else:
            time=run_track(all_tracks[param[0]],stuff.code)
            print(time,person)
            if param[2] == 1:
                if time < param[1]:
                    goal_reachers.append([person])
                    continue
            if param[2] == 2:
                if time > param[1]:
                    goal_reachers.append([person])
                    continue
            continue
    return goal_reachers


def save_objective(name,objectiv):
    dbfile=open('objectives{}'.format(cvs()),'ab')
    db={}
    db[name]=objectiv
    pickle.dump(db,dbfile)
    dbfile.close()
    return read_objective(objectiv)


def read_objective(objective):
    for params in objective:
        print('***')
        print (display_param(params))
    return ''


def read_objectives():
    all_objectives=safe_pick('objectives{}'.format(cvs()))
    for objt,params in all_objectives.items():
        print('***')
        for param in params:
            print (objt,display_param(param))
    return ''


def save_global_objective(name,objectiv):
    dbfile=open('objectives','ab')
    db={}
    db[name]=objectiv
    pickle.dump(db,dbfile)
    dbfile.close()
    return read_objective(objectiv)


def read_global_objectives():
    all_objectives=safe_pick('objectives')
    for objt,params in all_objectives.items():
        print('***')
        for param in params:
            print (objt,display_param(param))
    return ''


def check_global_objectives():
    goal_reachers=[]
    all_objectives=safe_pick('objectives')
    all_tracks=safe_pick('tracks')
    all_people=safe_pick('classed_beings{}'.format(cvs()))
    winners=[]
    real_winners=[]
    past_winners=[]
    for objective_name,params in all_objectives.items():
        """print('----------',all_objectives,objective_name)"""
        for idx,param in enumerate(params):
            real_winners=[]
            """print('----1',param,idx)"""
            """print(2,past_winners,'xxxxxxxx',real_winners)"""
            winners=check_one_param(param)
            """print(3,past_winners,'xxxxxxxx',winners)"""
            if not idx == 0:
                """print(6,idx,winners)"""
                for name in winners:
                    if name in past_winners:
                        real_winners+=name
                        """print(7,name)"""
                        continue
                    else:
                        """print(8,name)"""
                        continue

                past_winners=real_winners
                """print(4,real_winners)"""
            else:
                past_winners=winners
                """print(5,past_winners)"""
        goal_reachers.append([objective_name,real_winners])
    return goal_reachers


def display_param(param):
    if param[0]== 'Hair Color':
        if param[2] == 1:
            return 'Hair color is {}'.format(param[1])
        if param[2] == 2:
            return 'Hair color is not {}'.format(param[1])
    elif param[0]== 'Eye Color':
        if param[2] == 1:
            return 'Eye color is {}'.format(param[1])
        if param[2] == 2:
            return 'Eye color is not {}'.format(param[1])
    elif param[0]== 'Weight':
        if param[2] == 1:
            return 'Weight is greater than or equal to {}lbs'.format(param[1])
        if param[2] == 2:
            return 'Weight is less than or equal to {}lbs'.format(param[1])
    elif param[0]== 'Height':
        if param[2] == 1:
            return 'Height is greater than or equal to {0}ft{1}in'.format(str(convert_inches_to_mixed(param[1])[0]),str(convert_inches_to_mixed(param[1])[1]))
        if param[2] == 2:
            return 'Height is less than or equal to {0}ft{1}in'.format(str(convert_inches_to_mixed(param[1])[0]),str(convert_inches_to_mixed(param[1])[1]))
    else:
        if param[2] == 1:
            return 'Run {0} faster than {1}'.format(param[0],str(param[1]))
        if param[2] == 2:
            return 'Run {0} slower than {1}'.format(param[0],str(param[1]))


def hcp():
    return ['Hair Color is',random.choice(['Green','Blonde','Black','Brown'])]


def inch_height(being):
    h=int(35+char_dict(being)['m']*char_dict(being)['8']+char_dict(being)['m']*char_dict(being)['7'])
    return h


def convert_inches_to_mixed(inches):
    f=math.trunc(inches/12)
    hf=inches-(f*12)
    return f,hf


def bc():
    return bios_classed()

def build_success_list(thing,value,mod=1):
    results=[]
    if thing == 'Eye Color':
        if mod == 1:
            for name, stuff in cvl().items():
                if eye_color(stuff.code) == value:
                    results.append([name,hair_color(stuff.code),eye_color(stuff.code),weight(stuff.code),height(stuff.code)])
        if mod == 2:
            for name, stuff in cvl().items():
                if eye_color(stuff.code) != value:
                    results.append([name,hair_color(stuff.code),eye_color(stuff.code),weight(stuff.code),height(stuff.code)])
    elif thing == 'Hair Color':
        if mod == 1:
            for name, stuff in cvl().items():
                if hair_color(stuff.code) == value:
                    results.append([name,hair_color(stuff.code),eye_color(stuff.code),weight(stuff.code),height(stuff.code)])
        if mod == 2:
            for name, stuff in cvl().items():
                if hair_color(stuff.code) != value:
                    results.append([name,hair_color(stuff.code),eye_color(stuff.code),weight(stuff.code),height(stuff.code)])
    elif thing == 'Weight':
        if mod == 1:
            for name, stuff in cvl().items():
                if weight(stuff.code) >= value:
                    results.append([name,hair_color(stuff.code),eye_color(stuff.code),weight(stuff.code),height(stuff.code)])
        if mod == 2:
            for name, stuff in cvl().items():
                if weight(stuff.code) <= value:
                    results.append([name,hair_color(stuff.code),eye_color(stuff.code),weight(stuff.code),height(stuff.code)])
    elif thing == 'Height':
        if mod == 1:
            for name, stuff in cvl().items():
                if height(stuff.code) >= value:
                    results.append([name,hair_color(stuff.code),eye_color(stuff.code),weight(stuff.code),height(stuff.code)])
        if mod == 2:
            for name, stuff in cvl().items():
                if height(stuff.code) <= value:
                    results.append([name,hair_color(stuff.code),eye_color(stuff.code),weight(stuff.code),height(stuff.code)])
    elif thing in list(safe_pick('tracks').keys()):
        track=all_pick('tracks')[thing]

        if mod == 1:
            for name, stuff in cvl().items():
                track_time=run_track(track,stuff.code)
                if run_track(track,stuff.code) >= value:
                    results.append([name,hair_color(stuff.code),eye_color(stuff.code),weight(stuff.code),height(stuff.code),track_time])
        if mod == 2:
            for name, stuff in cvl().items():
                track_time=run_track(track,stuff.code)
                if run_track(track,stuff.code) <= value:
                    results.append([name,hair_color(stuff.code),eye_color(stuff.code),weight(stuff.code),height(stuff.code),track_time])
    else:
        return 'What?'
    return results


def get_phenotype(being,mod,track=[]):
    if mod == 1:
        return hair_color(being)
    if mod == 2:
        return eye_color(being)
    if mod == 3:
        return weight(being)
    if mod == 4:
        return height(being)
    if mod == 5:
        return run_track(track,being)


def build_superalitives(mod,sec_phenotype=[]):
    resultx=[]
    if mod == 'Hair Color':
        if sec_phenotype == []:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,1)])
        else:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,1),get_phenotype(stuff.code,sec_phenotype[0],sec_phenotype[1])])
    elif mod == 'Eye Color':
        if sec_phenotype == []:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,2)])
        else:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,2),get_phenotype(stuff.code,sec_phenotype[0],sec_phenotype[1])])
    elif mod == 'Weight':
        if sec_phenotype == []:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,3)])
        else:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,3),get_phenotype(stuff.code,sec_phenotype[0],sec_phenotype[1])])
    elif mod == 'Height':
        if sec_phenotype == []:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,4)])
        else:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,4),get_phenotype(stuff.code,sec_phenotype[0],sec_phenotype[1])])
    if mod == 1:
        if sec_phenotype == []:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,1)])
        elif type(sec_phenotype)is list:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,1),get_phenotype(stuff.code,sec_phenotype[0],sec_phenotype[1])])
        else:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,1),get_phenotype(stuff.code,sec_phenotype)])
    elif mod == 2:
        if sec_phenotype == []:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,2)])
        elif type(sec_phenotype)is list:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,2),get_phenotype(stuff.code,sec_phenotype[0],sec_phenotype[1])])
        else:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,2),get_phenotype(stuff.code,sec_phenotype)])
    elif mod == 3:
        if sec_phenotype == []:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,3)])
        elif type(sec_phenotype)is list:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,3),get_phenotype(stuff.code,sec_phenotype[0],sec_phenotype[1])])
        else:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,3),get_phenotype(stuff.code,sec_phenotype)])
    elif mod == 4:
        if sec_phenotype == []:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,4)])
        elif type(sec_phenotype)is list:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,4),get_phenotype(stuff.code,sec_phenotype[0],sec_phenotype[1])])
        else:
            for name, stuff in cvl().items():
                resultx.append([name,get_phenotype(stuff.code,4),get_phenotype(stuff.code,sec_phenotype)])
    elif type(mod)is list:
        if mod[1] in list(safe_pick('tracks').values()):
            if sec_phenotype == []:
                for name, stuff in cvl().items():
                    resultx.append([name,get_phenotype(stuff.code,5,mod[1])])
            elif type(sec_phenotype)is list:
                for name, stuff in cvl().items():
                    resultx.append([name,get_phenotype(stuff.code,5,mod[1]),get_phenotype(stuff.code,sec_phenotype[0],sec_phenotype[1])])
            else:
                for name, stuff in cvl().items():
                    resultx.append([name,get_phenotype(stuff.code,5,mod[1]),get_phenotype(stuff.code,sec_phenotype)])
        else:
            print ('Can not find track')
    else:
        print ('What?')
    return resultx


def display_super(mod,sec_phenotype=[],reverse='',number_of_returns=20):
    if sec_phenotype!=[]:
        rl=build_superalitives(mod,sec_phenotype)
    else:
        rl=build_superalitives(mod)
    a=sorted(rl, key=lambda person: person[1] )
    x=slice(number_of_returns)
    return a[x]


def key_list_track(track):
    try:
        out=safe_pick('tracks')[track]
    except:
        try:
            out=list(track.keys())
        except:
            out=track[1]
    return [5,out]


def sort_results(results_list,sorter_type=random.randint(1,5)):
    """
sorter_type key ===

'Hair Color' === 1
'Eye Color'  === 2
'Weight'     === 3
'Height'     === 4
some track   === 5
"""
    return sorted(results_list,key=itemgetter(sorter_type))
list_vtl=['Eden','Small Family','Large Family','Small Tribe','Medium Tribe','Large Tribe','10-20 families']

def start_and_move_to_new_village(name,mod=4):
    if name in list(village_list().keys()):
        return 'Sorry, a village with that name already exsists'
    if mod == 0:
        if 'Eden' in list(village_list().keys()):
            return 'Eden already exsists, but we are there now',change_current_village('Eden')
        """Adam and Eve only"""
        add_new_village('Eden')
        change_current_village('Eden')
        pickle_being(Being(['Adam'],generate_outtie(),['God','lol'],['God','lol'],'?Heaven?'))
        pickle_being(Being(['Eve'],generate_innie(),['God','lol'],['God','lol'],'?Heaven?'))
        return bios_classed()
    if mod == 1:
        """ single small family"""
        add_new_village(name)
        change_current_village(name)
        mom=create_classed_innie()
        dad=create_classed_outtie()
        pickle_being(Being(mom.name,mom.code,mom.mom,mom.dad,'Somewhere Else...'))
        pickle_being(Being(dad.name,dad.code,dad.mom,dad.dad,'Somewhere Else...'))
        pickle_family(mom,dad,random.randint(2,4))
        return bios_classed()
    if mod == 2:
        """ very large single family"""
        add_new_village(name)
        change_current_village(name)
        mom=create_classed_innie()
        dad=create_classed_outtie()
        pickle_being(Being(mom.name,mom.code,mom.mom,mom.dad,'Somewhere Else...'))
        pickle_being(Being(dad.name,dad.code,dad.mom,dad.dad,'Somewhere Else...'))
        pickle_family(mom,dad,random.randint(8,12))
        return bios_classed()
    if mod == 3:
        """small 10 people +2 random babies"""
        add_new_village(name)
        change_current_village(name)
        for girls in range(5):
            create_and_save_being(gender='innie',vbi='Somewhere Else...')
        for boys in range(5):
            create_and_save_being(gender='outtie',vbi='Somewhere Else...')
        random_babies(2)
        return bios_classed()
    if mod == 4:
        """normal 10-20 people +2-5 random families"""
        add_new_village(name)
        change_current_village(name)
        for family in range(random.randint(2,5)):
            mom=create_classed_innie()
            dad=create_classed_outtie()
            pickle_being(Being(mom.name,mom.code,mom.mom,mom.dad,'Somewhere Else...'))
            pickle_being(Being(dad.name,dad.code,dad.mom,dad.dad,'Somewhere Else...'))
            pickle_family(mom,dad,random.randint(1,5))
        for girls in range(random.randint(5,10)):
            create_and_save_being(gender='innie',vbi='Somewhere Else...')
        for boys in range(random.randint(5,10)):
            create_and_save_being(gender='outtie',vbi='Somewhere Else...')
    if mod == 5:
        """large 80-100 people +3-8 families"""
        add_new_village(name)
        change_current_village(name)
        for family in range(random.randint(3,8)):
            mom=create_classed_innie()
            dad=create_classed_outtie()
            pickle_being(Being(mom.name,mom.code,mom.mom,mom.dad,'Somewhere Else...'))
            pickle_being(Being(dad.name,dad.code,dad.mom,dad.dad,'Somewhere Else...'))
            pickle_family(mom,dad,random.randint(1,5))
        for girls in range(random.randint(15,25)):
            create_and_save_being(gender='innie',vbi='Somewhere Else...')
        for boys in range(random.randint(15,25)):
            create_and_save_being(gender='outtie',vbi='Somewhere Else...')
        return bios_classed()
    if mod == 6:
        """ 10-20 families """
        add_new_village(name)
        change_current_village(name)
        for family in range(random.randint(10,20)):
            mom=create_classed_innie()
            dad=create_classed_outtie()
            pickle_being(Being(mom.name,mom.code,mom.mom,mom.dad,'Somewhere Else...'))
            pickle_being(Being(dad.name,dad.code,dad.mom,dad.dad,'Somewhere Else...'))
            pickle_family(mom,dad,random.randint(1,5))
        return bios_classed()
    if mod == 7:
        """ ~ 500 people from various sources"""
        
"""
create_and_save_being(gender=' ',vbi=' ')
    def pickle_being(being):
    return saave(being,display_name(being.name),'classed_beings{}'.format(cvs()))

    def overwrite(obj,file):
    stuff=obj
    db={}
    dbfile=open(file,'wb')
    pickle.dump(db,dbfile)
    dbfile.close()
    for name, instance in stuff.items():
        saave(instance,name,file)
    return file,obj,'4'

    def saave(obj,name,file):
    db={}
    db[name]=obj
    dbfile = open(file,'ab')
    pickle.dump(db,dbfile)
    dbfile.close()
    return obj
"""    
"""
def set_current_village(name):
    try:
        cvl=all_pick('village_list')
        if name in list(cvl.keys()):
            dbfile=open('current_village','wb')
            db={}
            db[name]=name
            pickle.dump(db,dbfile)
            dbfile.close()
        else:
            print('Add {} to village list first'.format(name))
    except:
        dbfile=open('current_village','wb')
        db={}
        db[name]=name
        pickle.dump(db,dbfile)
        dbfile.close()
    return current_village()
"""

def current_village():
    cv=all_pick('current_village')
    return cv


def change_current_village(new_village):
    old_cv=all_pick('current_village')
    cvl=all_pick('village_list')
    if new_village in list(cvl.keys()):
        new_cv=set_current_village(new_village)
    else:
        new_cv=old_cv
        print('Add {} to village list first'.format(new_village))
    return old_cv,new_cv


def add_new_village(name):
    dbfile=open('village_list','ab')
    db={}
    db[name]=name
    pickle.dump(db,dbfile)
    dbfile.close()
    return village_list()


def village_list():
    try:
        vl=all_pick('village_list')
    except:
        vl={}
    return vl


def random_current_village():
    v1=village_list()
    nv=random.choice(list(v1.values()))
    set_current_village(nv)
    return current_village()


def set_current_village(name):
    try:
        cvl=all_pick('village_list')
        if name in list(cvl.keys()):
            dbfile=open('current_village','wb')
            db={}
            db[name]=name
            pickle.dump(db,dbfile)
            dbfile.close()
        else:
            print('Add {} to village list first'.format(name))
    except:
        dbfile=open('current_village','wb')
        db={}
        db[name]=name
        pickle.dump(db,dbfile)
        dbfile.close()
    return current_village()


def cvs():
    cvs=''.join(list(current_village().keys()))
    return cvs


def current_villagers_list():
    cvl=safe_pick('classed_beings{}'.format(cvs()))
    return cvl


def cvl():
    return current_villagers_list()

def recycle_sorted_list(sorted_menu_set):
    print(sorted_menu_set)
    beings_dict={}
    if sorted_menu_set[1][0] != ' ':
        sorted_menu_set=[sorted_menu_set,' ']
    for entry in sorted_menu_set[0]:
        ed1={entry[1] : entry[2]}
        beings_dict.update(ed1)
    return beings_dict
    

def list_weight(og_list):
    lw=[]
    for name, being in og_list.items():
        lw.append([weight(being.code),name,being])
    return sorted(lw)

def list_height(og_list):
    lh=[]
    for name, being in og_list.items():
        lh.append([height(being.code),name,being])
    return sorted(lh)  

def list_hair_color(og_list):
    lhc=[]
    for name, being in og_list.items():
        lhc.append([hair_color(being.code),name,being])
    return sorted(lhc)

def list_eye_color(og_list):
    lec=[]
    for name, being in og_list.items():
        lec.append([eye_color(being.code),name,being])
    return sorted(lec)

def list_gender(og_list):
    lg=[]
    for name, being in og_list.items():
        lg.append([check_gender(being.code),name,being])
    return sorted(lg)

def list_hometown(og_list):
    lh=[]
    for name, being in og_list.items():
        try:
            lh.append([being.village_born_in,name,being])
        except:
            lh.append(["Unknown",name,being])
    return sorted(lh)

def list_times(og_list,track):
    lm=[]
    for name, being in og_list.items():
        lm.append([int(run_track(safe_pick('tracks')[track],being.code)),name,being])
    return sorted(lm)

def list_order(og_list):
    lo=[]
    cnt=int(0)
    for name, being in og_list.items():
        cnt += 1
        lo.append([cnt,name,being])
    return lo

def sorted_from_list(sort_type,og_list,args=[]):
    if args==[]:
        rl=sort_type(og_list)
    else:
        rl=sort_type(og_list,args)
    return rl

def list_of_dicts_to_flat_dict(list_of_dicts):
    one_dict={}
    for dict_entry in list_of_dicts:
        one_dict.update(dict_entry)
    return one_dict

def save_law(law_name,thing1,comparer1,value1,thing2,cantmust,comparer2,value2):
    """
8 total args

IF subject's {{thing1}} is {{comparer1}} {{value1}},
    their mate's {{thing2}} must be {{comparer2}} {{value2}}

EXAMPLE

IF subject's hair_color is not blonde,
    their mate's weight must be less than 250
    """
    return saave([thing1,comparer1,value1,thing2,cantmust,comparer2,value2],law_name,'laws{}'.format(cvs()))


            
def list_of_names_to_list_of_being_dicts(list_of_names):
    beings_dicts=[]
    not_found_list=[]
    for name in list_of_names:
        if name in list(cvl().keys()):
            dict_for_being={}
            dict_for_being.update({name:cvl()[name]})
            beings_dicts.append(dict_for_being)
        else:
            not_found_list.append(name)
    return[beings_dicts,not_found_list]

        
def n2bd(list_of_names):
    return list_of_names_to_list_of_being_dicts(list_of_names)

    
def name_list_to_cvl_style(list_of_names):
    return list_of_dicts_to_flat_dict(n2bd(list_of_names)[0])


def lz(ugh):
    return name_list_to_cvl_style(ugh)


def file_to_list(name):
    return list(safe_pick(name).keys())


def ftl(name):
    return file_to_list(name)


def remove_duplicates(list_of_names):
    nl=[]
    for name in list_of_names:
        if name not in nl:
            nl.append(name)
    return nl
        

def loop_list_parents(list_of_names):
    pl=[]
    for being in list_of_names:
        try:
            pl.append(display_name(cvl()[being].mom[0]))
            pl.append(display_name(cvl()[being].dad[0]))
        except:
            try:
                pl.append(display_name(cvl()[being].dad[0]))
                pl.append(display_name(cvl()[being].mom[0]))
            except:
                continue
    return remove_duplicates(pl)        


def loop_list_children(list_of_names):
    cl=[]
    for being in list_of_names:
        try:
            pcl=cvl()[being].children       
            for child in pcl:
                cl.append(display_name(child[0]))
        except:
            continue    
    return remove_duplicates(cl)


def loop_list_siblings(list_of_names):
    full=[]
    half=[]
    for name in list_of_names:
        try:
            isl=list(find_siblings(cvl()[name]).values())
            for halfs in isl[0][0]:
                half.append(halfs)
            for fulls in isl[0][1]:
                full.append(fulls)
        except:
            continue
    return [full,half]

def loop_list_halfsiblings(list_of_names):
    out=[]
    for name in list_of_names:
        try:
            isl=list(find_siblings(cvl()[name]).values())
            for halfs in isl[0][0]:
                out.append(halfs[0])
        except:
            continue
    return out

def loop_list_fullsiblings(list_of_names):
    out=[]
    for name in list_of_names:
        try:
            isl=list(find_siblings(cvl()[name]).values())
            for fulls in isl[0][1]:
                out.append(fulls[0])
        except:
            continue
    return out

def loop_list_allsiblings(list_of_names):
    out=[]
    for name in list_of_names:
        try:
            isl=list(find_siblings(cvl()[name]).values())
            for halfs in isl[0][0]:
                out.append(halfs[0])
            for fulls in isl[0][1]:
                out.append(fulls[0])
        except:
            continue
    return out


def quick_local_family_list(name1,name2):
    """ out[0]=Parent 1=Child 2=Half Sibling
        3=Full Sibling 4=Aunt or Uncle
        5=Cousin 6=Niece or Nephew
        7=GrandParent  8=GrandChild """
    out=list('.........')
    if name2 in loop_list_parents([name1]):
        out[0]='P'
    if name2 in loop_list_children([name1]):
        out[1]='C'
    if name2 in loop_list_halfsiblings([name1]):
        out[2]='H'
    if name2 in loop_list_fullsiblings([name1]):
        out[3]='S'
    if name2 in loop_list_allsiblings(loop_list_parents([name1])):
        out[4]='A'
    if name2 in loop_list_children(loop_list_allsiblings(loop_list_parents([name1]))):
        out[5]='N'
    if name2 in loop_list_children(loop_list_allsiblings([name1])):
        out[6]='E'
    if name2 in loop_list_parents(loop_list_parents([name1])):
        out[7]='G'
    if name2 in loop_list_children(loop_list_children([name1])):
        out[8]='K'   
    return ''.join(out)

def quick_family_list_ALL(prename1,prename2):
    """ out[0]=Parent 1=Child 2=Half Sibling
        3=Full Sibling 4=Aunt or Uncle
        5=Cousin 6=Niece or Nephew
        7=GrandParent  8=GrandChild """
    out=list('.........')
    name1=cnn(prename1)
    name2=cnn(prename2)
    """print (name1)"""
    if name2[0] in loop_list_parents_ALL(name1):
        out[0]='P'
    if name2[0] in loop_list_children_ALL(name1):
        out[1]='C'
    if name2[0] in loop_list_halfsiblings_ALL(name1):
        out[2]='H'
    if name2[0] in loop_list_fullsiblings_ALL(name1):
        out[3]='S'
    if name2[0] in loop_list_allsiblings_ALL(loop_list_parents_ALL(name1)):
        out[4]='A'
    if name2[0] in loop_list_children_ALL(loop_list_allsiblings_ALL(loop_list_parents_ALL(name1))):
        out[5]='N'
    if name2[0] in loop_list_children_ALL(loop_list_allsiblings_ALL(name1)):
        out[6]='E'
    if name2[0] in loop_list_parents_ALL(loop_list_parents_ALL(name1)):
        out[7]='G'
    if name2[0] in loop_list_children_ALL(loop_list_children_ALL(name1)):
        out[8]='K'   
    return ''.join(out)

def change_name_to_namelocs(name):
    nba(name)
    try:
        ca=CVA
        return [[name,ca[name][1],ca[name][0].village_born_in]]
    except:
        ca=cvl_ALL()
        return [[name,ca[name][1],ca[name][0].village_born_in]]


def cnn(name):
    return change_name_to_namelocs(name)

def name_to_village_born_in(name):
    nba(name)
    ca=CVA
    if name not in list(ca.keys()):
        return "Far Away"
    else:
        return ca[name][0].village_born_in

def c():
    return cvl_ALL()


def nto(name):
    return name_to_village_born_in(name)

def name_to_current_village(name):
    nba(name)
    ca=CVA
    if name not in list(ca.keys()):
        return "Unknown"
    else:
        return ca[name][1]

def ntv(name):
    return name_to_current_village(name)

def remove_ancestors_that_arent_here(listofnames):
    ca=CVA
    here=[]
    for name in listofnames:
        if name in list(ca.keys()):
            here.append(name)
        else:
            continue
    return here

def ra(listofnames):
    return remove_ancestors_that_arent_here(listofnames)

def loop_list_parents_ALL(list_of_namelocs):
    """print(datetime.datetime.now().time())"""
    list_of_all_names=[]
    for names in list_of_namelocs:
        list_of_all_names.append(names[0])
    list_of_names=ra(list_of_all_names)
    ca=CVA
    pl=[]
    for being in list_of_names:
        try:
            pl.append([display_name(ca[being][0].mom[0]),ntv(display_name(ca[being][0].mom[0])),nto(display_name(ca[being][0].mom[0]))])
            pl.append([display_name(ca[being][0].dad[0]),ntv(display_name(ca[being][0].dad[0])),nto(display_name(ca[being][0].dad[0]))])
        except:
            try:
                pl.append([display_name(ca[being][0].dad[0]),ntv(display_name(ca[being][0].dad[0])),nto(display_name(ca[being][0].dad[0]))])
                pl.append([display_name(ca[being][0].mom[0]),ntv(display_name(ca[being][0].mom[0])),nto(display_name(ca[being][0].mom[0]))])
            except:
                continue
    """print(datetime.datetime.now().time())"""
    return remove_duplicates(pl)        


def loop_list_children_ALL(list_of_namelocs):
    """print(datetime.datetime.now().time())"""
    list_of_all_names=[]
    """print(list_of_namelocs)"""
    for names in list_of_namelocs:
        """print (names)"""
        list_of_all_names.append(names[0])
    list_of_names=ra(list_of_all_names)
    """print(list_of_names)"""
    """list_of_names=list_of_all_names"""
    ca=CVA
    cl=[]
    for being in list_of_names:
        """print (being)"""
        pcl=ca[being][0].children
        for child in pcl:
            cl.append([display_name(child[0]),ca[display_name(child[0])][1],ca[display_name(child[0])][0].village_born_in])
    """print(datetime.datetime.now().time())"""    
    return remove_duplicates(cl)


def loop_list_fullsiblings_ALL(list_of_namelocs):
    """print(datetime.datetime.now().time())"""
    list_of_all_names=[]
    for names in list_of_namelocs:
        list_of_all_names.append(names[0])
    """list_of_names=ra(list_of_all_names)"""
    list_of_names=list_of_all_names
    out=[]
    ca=CVA
    for name in list_of_names:
        try:
            isl=list(find_siblings_ALL(cnn(name)).values())
            for fulls in isl[0][1]:
                out.append([fulls,ca[fulls][1],ca[fulls][0].village_born_in])
        except:
            continue
    """print(datetime.datetime.now().time())"""
    return remove_duplicates(out)


def loop_list_halfsiblings_ALL(list_of_namelocs):
    """print(datetime.datetime.now().time())"""
    list_of_all_names=[]
    for names in list_of_namelocs:
        list_of_all_names.append(names[0])
    """list_of_names=ra(list_of_all_names)"""
    list_of_names=list_of_all_names
    out=[]
    ca=CVA
    for name in list_of_names:
        try:
            isl=list(find_siblings_ALL(cnn(name)).values())
            for halfs in isl[0][0]:
                out.append([halfs[0],ca[halfs[0]][1],ca[halfs[0]][0].village_born_in])
        except:
            continue
    """print(datetime.datetime.now().time())"""
    return remove_duplicates(out)

def loop_list_allsiblings_ALL(list_of_namelocs):
    """print (list_of_namelocs)"""
    """print(datetime.datetime.now().time())"""
    list_of_all_names=[]
    for names in list_of_namelocs:
        list_of_all_names.append(names[0])
    """list_of_names=ra(list_of_all_names)"""
    list_of_names=list_of_all_names
    out=[]
    ca=CVA
    for name in list_of_names:
        """print (name)"""
        isl=list(find_siblings_ALL(cnn(name)).values())
        for halfs in isl[0][0]:
            out.append([halfs[0],ca[halfs[0]][1],ca[halfs[0]][0].village_born_in])
        for fulls in isl[0][1]:
            out.append([fulls,ca[fulls][1],ca[fulls][0].village_born_in])
    """print(datetime.datetime.now().time())"""
    return remove_duplicates(out)
"""
    return [remove_duplicates(sl)[0],remove_duplicates(sl)[1]]
"""
def residents(list_of_names):
    rl=[]
    for name in list_of_names:
        if name in list(cvl().keys()):
            rl.append(name)
    return remove_duplicates(rl)

           
def edit_group(group_name,person_name):
    gees={}
    try:
        gees=all_pick('groups_{}'.format(cvs()))
        if group_name in list(gees.keys()):
            if person_name in gees[group_name]:    
                gees[group_name].remove(person_name)                
            else:    
                gees[group_name].append(person_name)
        else:
            gees.update({group_name:[person_name]})
        overwrite(gees,'groups_{}'.format(cvs()))       
    except:
        saave([person_name],group_name,'groups_{}'.format(cvs()))
        gees=all_pick('groups_{}'.format(cvs()))
    return all_pick('groups_{}'.format(cvs()))


def emmigrate_beings(list_of_beings,new_village):
    cvll=cvl()
    ncvl=all_pick('classed_beings{}'.format(new_village))
    for being in list_of_beings:
        cvll.pop(display_name(being.name),'Not in list?')
        ncvl.update({display_name(being.name):being})
    overwrite(cvll,'classed_beings{}'.format(cvs()))
    overwrite(ncvl,'classed_beings{}'.format(new_village))
    return [cvl(),not_current_village_list(new_village)]


def emmigrate_beings_test(list_of_beings,new_village):
    cvll=cvl()
    ncvl=all_pick('classed_beings{}'.format(new_village))
    for being in list_of_beings:
        print(being)
        cvll.pop(display_name(being.name),'Not in list?')
        ncvl.update({display_name(being.name):being})
        """
    overwrite(cvll,'classed_beings{}'.format(cvs()))
    overwrite(ncvl,'classed_beings{}'.format(new_village))
    """
    return [cvll,ncvl]

   
def emmigrate_names(list_of_names,new_village):
    cvll=cvl()
    cvl_names=list(cvl().keys())
    ncvl=safe_pick('classed_beings{}'.format(new_village))
    list_of_beings=[]
    for name in list_of_names:
        if name in cvl_names:
            list_of_beings.append(cvl()[name])
    for being in list_of_beings:
        cvll.pop(display_name(being.name),'Not in list?')
        ncvl.update({display_name(being.name):being})
    overwrite(cvll,'classed_beings{}'.format(cvs()))
    overwrite(ncvl,'classed_beings{}'.format(new_village))
    return [cvl(),not_current_village_list(new_village)]


def emmigrate_names_test(list_of_names,new_village):
    cvll=cvl()
    ncvl=all_pick('classed_beings{}'.format(new_village))
    list_of_beings=[]
    for name in list_of_names:
        list_of_beings.append(cvl()[name])
    for being in list_of_beings:
        cvll.pop(display_name(being.name),'Not in list?')
        ncvl.update({display_name(being.name):being})
        """                      
    overwrite(cvll,'classed_beings{}'.format(cvs()))
    overwrite(ncvl,'classed_beings{}'.format(new_village))
    """
    return [cvll,ncvl]


def not_current_village_list(village):
    ncvl=all_pick('classed_beings{}'.format(village))
    return ncvl


def cvg(selected_village=cvs()):
    return safe_pick('groups_{}'.format(selected_village))


def log_tran_group_test(selected_group,new_village,current_village=cvs()):
    a=emmigrate_names_test(all_pick('groups_{}'.format(current_village))[selected_group],new_village)
    """
    print (a)
    """
    new_village_groups=safe_pick('groups_{}'.format(new_village))
    full_group={selected_group:cvg(current_village)[selected_group]}
    d=new_village_groups
    new_village_groups.update({list(full_group.keys())[0]:list(full_group.values())[0]})   
    """
    c=pop_test(selected_group,all_pick('groups_{}'.format(current_village)))
    """
    c=remove_villagers_from_other_groups(selected_group,current_village)
    """
    overwrite(c,'groups_{}'.format(current_village))
    overwrite(d,'groups_{}'.format(new_village))
    """
    return a, 'xxxxxxxxxx' ,d,'yyyyyyyyy',c, '?????????'


def log_tran_group(selected_group,new_village,current_village=cvs()):
    a=emmigrate_names(all_pick('groups_{}'.format(current_village))[selected_group],new_village)
    new_village_groups=safe_pick('groups_{}'.format(new_village))
    full_group={selected_group:cvg(current_village)[selected_group]}
    d=new_village_groups
    new_village_groups.update({list(full_group.keys())[0]:list(full_group.values())[0]})   
    c=pop_test(selected_group,all_pick('groups_{}'.format(current_village)))
    overwrite(c,'groups_{}'.format(current_village))
    overwrite(d,'groups_{}'.format(new_village))
    return a,d,c


def clean_log_tran_group(selected_group,new_village,current_village=cvs()):
    a=emmigrate_names(all_pick('groups_{}'.format(current_village))[selected_group],new_village)
    new_village_groups=safe_pick('groups_{}'.format(new_village))
    full_group={selected_group:cvg(current_village)[selected_group]}
    d=new_village_groups
    new_village_groups.update({list(full_group.keys())[0]:list(full_group.values())[0]})   
    c=remove_villagers_from_other_groups(selected_group,current_village)
    overwrite(c,'groups_{}'.format(current_village))
    overwrite(d,'groups_{}'.format(new_village))
    return a,d,c


def pop_test(popped_entry,dictionary):
    dictionary.pop(popped_entry,None)
    return dictionary

def fix_village_list():
    villist=safe_pick('village_list')
    for vill in list(villist.keys()):
        if safe_pick('classed_beings{}'.format(vill)) == {}:
            del villist[vill]
            
    overwrite(villist,'village_list')
    return safe_pick('village_list')

def fix_group(group_name,village_name=cvs()):
    a=cvg()
    b=cvg()[group_name][0]
    c=pop_test(group_name,cvg())
    d={group_name:b}
    c.update({list(d.keys())[0]:list(d.values())[0]})
    overwrite(c,'groups_{}'.format(village_name))
    return c
    

def update_test(exs_dic, new_entry):
    exs_dic.update({list(new_entry.keys())[0]:list(new_entry.values())})
    return exs_dic


def remove_villagers_from_other_groups(selected_group, selected_village=cvs()):
    other_groups=cvg(selected_village)
    other_groups.pop(selected_group)
    selected_villagers=cvg(selected_village)[selected_group]
    for group in other_groups.values():
        for name in selected_villagers:
            group.remove(name)
    return other_groups


def add_villagers_to_new_village(cvs,selected_village,selected_group):
    return None


def add_group_to_new_village(cvs,selected_village,selected_group):
    return None


def cvs():
    cvs=''.join(list(current_village().keys()))
    return cvs


def four_for_you(being):
    you=being.code
    dadc=being.dad[1]
    momc=being.mom[1]
    d=[[[],[],[],[]],[[],[],[],[]]]
    d2=[]
    d3=[]
    d4=[]
    m=[[[],[],[],[]],[[],[],[],[]]]
    m2=[]
    m3=[]
    m4=[]
    for counter1, chromo in enumerate(you):
        for counter2, pair in enumerate(you[counter1]):
            for counter3, gene in enumerate(you[counter1][counter2]):
                print(counter1,counter2,counter3)
                dd=dadc[counter3]
                md=momc[counter1][counter2][counter3]
                yg=you[counter1][counter2][counter3]
                d[counter1][counter2].append(int(yg-dd))
                m[counter1][counter2].append(int(yg-md))
    return d,m
dftest=[[[1],[2],[3],[4]],[[5],[6],[7],[8]]]


def poppp():
    print (dftest)
    c=dftest[0][0].append(str(6))
    return print(c)


def sbl():
    laws=safe_pick('laws{}'.format(cvs()))
    effected=[]
    if laws == {}:
        return effected
    a=int(0)
    b=int(1)
    c=int(2)
    law_counter=int(1)
    villagers=cvl()
    for law, parameter_list in laws.items():
        for name, being in villagers.items():
            pert_value=''
            if parameter_list[a][1] == 1:
                pert_value=hair_color(being.code)
                comparer_value = parameter_list[c][0]
            elif parameter_list[a][1] == 2:
                pert_value=eye_color(being.code)
                comparer_value = parameter_list[c][0]
            elif parameter_list[a][1] == 3:
                pert_value=weight(being.code)
                comparer_value = parameter_list[c][1]
            elif parameter_list[a][1] == 4:
                pert_value=inch_height(being.code)
                comparer_value = parameter_list[c][1]
            elif parameter_list[a][1] == 5:
                track_name=parameter_list[a][0][13:]
                pert_value=run_track(safe_pick('tracks')[track_name],being.code)
                comparer_value = parameter_list[c][0]
                """
    """
            if parameter_list[b][1] == 1:
                if comparer_value == pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 2:
                if comparer_value != pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 3:
                if comparer_value > pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 4:
                if comparer_value >= pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 5:
                if comparer_value < pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 6:
                if comparer_value <= pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
        law_counter += 1            
    return effected


def tbl():
    laws=safe_pick('laws{}'.format(cvs()))
    effected=[]
    if laws == {}:
        return effected
    a=int(3)
    b=int(4)
    c=int(5)
    law_counter=int(1)
    villagers=cvl()
    for law, parameter_list in laws.items():
        for name, being in villagers.items():
            pert_value=''
            if parameter_list[a][1] == 1:
                pert_value=hair_color(being.code)
                comparer_value = parameter_list[c][0]
            elif parameter_list[a][1] == 2:
                pert_value=eye_color(being.code)
                comparer_value = parameter_list[c][0]
            elif parameter_list[a][1] == 3:
                pert_value=weight(being.code)
                comparer_value = parameter_list[c][1]
            elif parameter_list[a][1] == 4:
                pert_value=inch_height(being.code)
                comparer_value = parameter_list[c][1]
            elif parameter_list[a][1] == 5:
                track_name=parameter_list[a][0][13:]
                pert_value=run_track(safe_pick('tracks')[track_name],being.code)
                comparer_value = parameter_list[c][0]
                """
    """
            if parameter_list[b][1] == 1:
                if comparer_value != pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 2:
                if comparer_value == pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 3:
                if comparer_value <= pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 4:
                if comparer_value < pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 5:
                if comparer_value >= pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 6:
                if comparer_value > pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
        law_counter += 1            
    return effected


def iml(being):
    """pdb.set_trace()"""
    tblx=tbl()
    sblx=sbl()
    noped=[]
    for entry in tblx:
        if entry[0] == display_name(being.name):
            for entry2 in sblx:
                if entry2[2] == entry[2]:
                    if entry2[3] != entry[3]:
                        noped.append(entry2)
    for entry3 in sblx:
        if entry3[0] == display_name(being.name):
            for entry4 in tblx:
                if entry4[2] == entry3[2]:
                    if entry4[3] != entry3[3]:
                        if entry4 not in noped:
                            noped.append(entry4)
    return noped


def create_full_list_of_opposite_gender(being):
    potential_mates=[]
    if check_gender(being) == 'Innie':
        for name, beings in cvl().items():
            if check_gender(beings.code) == 'Outtie':
                potential_mates.append(beings)
    if check_gender(being) == 'Outtie':
        for name, beings in cvl().items():
            if check_gender(beings.code) == 'Innie':
                potential_mates.append(beings)
    return potential_mates


def create_full_list_of_opposite_gender_names(being):
    potential_mates=[]
    if check_gender(being) == 'Innie':
        for name, beings in cvl().items():
            if check_gender(beings.code) == 'Outtie':
                potential_mates.append(name)
    if check_gender(being) == 'Outtie':
        for name, beings in cvl().items():
            if check_gender(beings.code) == 'Innie':
                potential_mates.append(name)
    return potential_mates


def valid_mates_list(being):
    potentials=create_full_list_of_opposite_gender_names(being.code)
    excluded=noped_names(iml(being))
    """print(excluded,potentials)"""
    for name in excluded:
        """print(name)"""
        potentials.remove(name)
    return potentials                    

def noped_names(imlx):
    namess = []
    for entry in imlx:
        namess.append(entry[0])
    return remove_duplicates(namess)
"""
def invalid_mates_list(being):
    law_counter=int(0)
    invalid_mates=[]
    laws=safe_pick('laws{}'.format(cvs()))
    if laws == {}:
        return invalid_mates
    for law, parameter_list in laws.items():
        pert_value=''
        if parameter_list[0][1] == 1:
            pert_value=hair_color(being.code)
            comparer_value = parameter_list[2][0]
        elif parameter_list[0][1] == 2:
            pert_value=eye_color(being.code)
            comparer_value = parameter_list[2][0]
        elif parameter_list[0][1] == 3:
            pert_value=weight(being.code)
            comparer_value = parameter_list[2][1]
        elif parameter_list[0][1] == 4:
            pert_value=inch_height(being.code)
            comparer_value = parameter_list[2][1]
        elif parameter_list[0][1] == 5:
            track_name=parameter_list[0][0][13:]
            pert_value=run_track(safe_pick('tracks')[track_name],being.code)
            comparer_value = parameter_list[2][0]
            """
"""
        if parameter_list[1][1] == 1:
            if comparer_value == pert_value:
                invalid_mates.extend(find_illegal_mates(parameter_list,being))
        elif parameter_list[1][1] == 2:
            if comparer_value != pert_value:
                invalid_mates.extend(find_illegal_mates(parameter_list,being))
        elif parameter_list[1][1] == 3:
            if comparer_value > pert_value:
                invalid_mates.extend(find_illegal_mates(parameter_list,being))
        elif parameter_list[1][1] == 4:
            if comparer_value >= pert_value:
                invalid_mates.extend(find_illegal_mates(parameter_list,being))
        elif parameter_list[1][1] == 5:
            if comparer_value < pert_value:
                invalid_mates.extend(find_illegal_mates(parameter_list,being))
        elif parameter_list[1][1] == 6:
            if comparer_value <= pert_value:
                invalid_mates.extend(find_illegal_mates(parameter_list,being))
        law_counter += 1            
    return remove_duplicates(invalid_mates)

def invalid_mates_tripleset(being):
    pdb.set_trace()
    law_counter=int(1)
    invalid_mates=[]
    laws=safe_pick('laws{}'.format(cvs()))
    if laws == {}:
        return invalid_mates
    for law, parameter_list in laws.items():
        pert_value=''
        if parameter_list[0][1] == 1:
            pert_value=hair_color(being.code)
            comparer_value = parameter_list[2][0]
        if parameter_list[0][1] == 2:
            pert_value=eye_color(being.code)
            comparer_value = parameter_list[2][0]
        if parameter_list[0][1] == 3:
            pert_value=weight(being.code)
            comparer_value = parameter_list[2][1]
        if parameter_list[0][1] == 4:
            pert_value=inch_height(being.code)
            comparer_value = parameter_list[2][1]
        if parameter_list[0][1] == 5:
            track_name=parameter_list[0][0][13:]
            pert_value=run_track(safe_pick('tracks')[track_name],being.code)
            comparer_value = parameter_list[2][0]
            """
"""
        if parameter_list[1][1] == 1:
            if comparer_value == pert_value:
                for restr in find_illegal_mates(parameter_list,being):
                    invalid_mates.append([restr,law,law_counter])
        if parameter_list[1][1] == 2:
            if comparer_value != pert_value:
                for restr in find_illegal_mates(parameter_list,being):
                    invalid_mates.append([restr,law,law_counter])
        if parameter_list[1][1] == 3:
            if comparer_value > pert_value:
                for restr in find_illegal_mates(parameter_list,being):
                    invalid_mates.append([restr,law,law_counter])
        if parameter_list[1][1] == 4:
            if comparer_value >= pert_value:
                for restr in find_illegal_mates(parameter_list,being):
                    invalid_mates.append([restr,law,law_counter])
        if parameter_list[1][1] == 5:
            if comparer_value < pert_value:
                for restr in find_illegal_mates(parameter_list,being):
                    invalid_mates.append([restr,law,law_counter])
        if parameter_list[1][1] == 6:
            if comparer_value <= pert_value:
                for restr in find_illegal_mates(parameter_list,being):
                    invalid_mates.append([restr,law,law_counter])
        law_counter += 1            
    return invalid_mates

def tbl():
    pdb.set_trace()
    laws=safe_pick('laws{}'.format(cvs()))
    effected=[]
    if laws == {}:
        return effected
    a=int(3)
    b=int(4)
    c=int(5)
    print(a,b,c)
    law_counter=int(1)
    villagers=cvl()
    for law, parameter_list in laws.items():
        for name, being in villagers.items():
            pert_value=''
            if parameter_list[a][1] == 1:
                pert_value=hair_color(being.code)
                comparer_value = parameter_list[c][0]
            elif parameter_list[a][1] == 2:
                pert_value=eye_color(being.code)
                comparer_value = parameter_list[c][0]
            elif parameter_list[a][1] == 3:
                pert_value=weight(being.code)
                comparer_value = parameter_list[c][1]
            elif parameter_list[a][1] == 4:
                pert_value=inch_height(being.code)
                comparer_value = parameter_list[c][1]
            elif parameter_list[a][1] == 5:
                track_name=parameter_list[a][0][13:]
                pert_value=run_track(safe_pick('tracks')[track_name],being.code)
                comparer_value = parameter_list[c][0]
                """"""
            if parameter_list[b][1] == 1:
                if comparer_value != pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 2:
                if comparer_value == pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 3:
                if comparer_value <= pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 4:
                if comparer_value < pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 5:
                if comparer_value >= pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
            elif parameter_list[b][1] == 6:
                if comparer_value > pert_value:
                    effected.append([name,law,law_counter,check_gender(being.code)])
        law_counter += 1            
    return effected

def find_illegal_mates(parameter_list,being):
    pdb.set_trace()
    invalid_mates2= []
    biological_mates=create_full_list_of_opposite_gender(being.code)
    for mate in biological_mates:
        pert_value=''
        if parameter_list[3][1] == 1:
            pert_value2=hair_color(mate.code)
            comparer_value = parameter_list[5][0]
        if parameter_list[3][1] == 2:
            pert_value2=eye_color(mate.code)
            comparer_value = parameter_list[5][0]
        if parameter_list[3][1] == 3:
            pert_value2=weight(mate.code)
            comparer_value = parameter_list[5][1]
        if parameter_list[3][1] == 4:
            pert_value2=inch_height(mate.code)
            comparer_value = parameter_list[5][1]
        if parameter_list[3][1] == 5:
            track_name=parameter_list[3][0][13:]
            pert_value2=run_track(safe_pick('tracks')[track_name],mate.code)
            comparer_value = parameter_list[5][0]
        """
"""
        if parameter_list[4][1] == 1:
            if comparer_value != pert_value2:
                invalid_mates2.append(display_name(mate.name))
        if parameter_list[4][1] == 2:
            if comparer_value == pert_value2:
                invalid_mates2.append(display_name(mate.name))
        if parameter_list[4][1] == 3:
            if comparer_value <= pert_value2:
                invalid_mates2.append(display_name(mate.name))
        if parameter_list[4][1] == 4:
            if comparer_value < pert_value2:
                invalid_mates2.append(display_name(mate.name))
        if parameter_list[4][1] == 5:
            if comparer_value >= pert_value2:
                invalid_mates2.append(display_name(mate.name))
        if parameter_list[4][1] == 6:
            if comparer_value > pert_value2:
                invalid_mates2.append(display_name(mate.name))
    return invalid_mates2


def effected_names_list(ebl_instance):
    listonames=[]
    for entry in ebl_instance:
        listonames.append(entry[0])
    return listonames
    

            
def people_effected_by_laws():
    villagers=cvl()
    laws=safe_pick('laws{}'.format(cvs()))
    effected=[]
    for name, being in villagers.items():
        for law, parameter_list in laws.items():
            pert_value=' '
            if parameter_list[0][1] == 1:
                pert_value=hair_color(being.code)
            elif parameter_list[0][1] == 2:
                pert_value=eye_color(being.code)
            elif parameter_list[0][1] == 3:
                pert_value=weight(being.code)
            elif parameter_list[0][1] == 4:
                pert_value=inch_height(being.code)
            elif parameter_list[0][1] == 5:
                track_name=parameter_list[0][0][13:]
                pert_value=run_track(safe_pick('tracks')[track_name],being.code)
            print(pert_value)
            """
"""
            if parameter_list[1][1] == 1:
                if parameter_list[2][1] != pert_value:
                    effected.append([name,law])
            elif parameter_list[1][1] == 2:
                if parameter_list[2][1] == pert_value:
                    effected.append([name,law])
            elif parameter_list[1][1] == 3:
                if parameter_list[2][1] > pert_value:
                    effected.append([name,law])
            elif parameter_list[1][1] == 4:
                if parameter_list[2][1] >= pert_value:
                    effected.append([name,law])
            elif parameter_list[1][1] == 5:
                if parameter_list[2][1] < pert_value:
                    effected.append([name,law])
            elif parameter_list[1][1] == 6:
                if parameter_list[2][1] <= pert_value:
                    effected.append([name,law])
    return effected
            
def people_effected_by_laws_subject():
    villagers=cvl()
    laws=safe_pick('laws{}'.format(cvs()))
    effected=[]
    for name, being in villagers.items():
        for law, parameter_list in laws.items():
            pert_value=' '
            if parameter_list[0][1] == 1:
                pert_value=hair_color(being.code)
            if parameter_list[0][1] == 2:
                pert_value=eye_color(being.code)
            if parameter_list[0][1] == 3:
                pert_value=weight(being.code)
            if parameter_list[0][1] == 4:
                pert_value=inch_height(being.code)
            if parameter_list[0][1] == 5:
                track_name=parameter_list[0][0][13:]
                pert_value=run_track(safe_pick('tracks')[track_name],being.code)
            print(pert_value)
            """
"""
            if parameter_list[1][1] == 1:
                if parameter_list[2][1] != pert_value:
                    effected.append([name,law])
            if parameter_list[1][1] == 2:
                if parameter_list[2][1] == pert_value:
                    effected.append([name,law])
            if parameter_list[1][1] == 3:
                if parameter_list[2][1] > pert_value:
                    effected.append([name,law])
            if parameter_list[1][1] == 4:
                if parameter_list[2][1] >= pert_value:
                    effected.append([name,law])
            if parameter_list[1][1] == 5:
                if parameter_list[2][1] < pert_value:
                    effected.append([name,law])
            if parameter_list[1][1] == 6:
                if parameter_list[2][1] <= pert_value:
                    effected.append([name,law])
    return effected

def people_effected_by_laws_target():
    villagers=cvl()
    laws=safe_pick('laws{}'.format(cvs()))
    effected=[]
    for law, parameter_list in laws.items():
        for name, being in villagers.items():
            pert_value=' '
            if parameter_list[3][1] == 1:
                pert_value=hair_color(being.code)
            if parameter_list[3][1] == 2:
                pert_value=eye_color(being.code)
            if parameter_list[3][1] == 3:
                pert_value=weight(being.code)
            if parameter_list[3][1] == 4:
                pert_value=inch_height(being.code)
            if parameter_list[3][1] == 5:
                track_name=parameter_list[0][0][13:]
                pert_value=run_track(safe_pick('tracks')[track_name],being.code)
            print(pert_value)
            """
"""
            if parameter_list[4][1] == 1:
                if parameter_list[5][1] != pert_value:
                    effected.append([name,law])
            if parameter_list[4][1] == 2:
                if parameter_list[5][1] == pert_value:
                    effected.append([name,law])
            if parameter_list[4][1] == 3:
                if parameter_list[5][1] > pert_value:
                    effected.append([name,law])
            if parameter_list[4][1] == 4:
                if parameter_list[5][1] >= pert_value:
                    effected.append([name,law])
            if parameter_list[4][1] == 5:
                if parameter_list[5][1] < pert_value:
                    effected.append([name,law])
            if parameter_list[4][1] == 6:
                if parameter_list[5][1] <= pert_value:
                    effected.append([name,law])
    return effected

def effected_dict_law(s_or_t='s'):
    op={}
    if s_or_t == 't':
        efectd_list = people_effected_by_laws_target()
    else:
        efectd_list = people_effected_by_laws_subject()
    for entry in efectd_list:
        law=entry[1]
        name=entry[0]
        if law in op:
            op[law].append(name)
        else:
            op[law]= [name]
    return op

def deepdive_laws():
    ddlo=[]
    laws=safe_pick('laws{}'.format(cvs()))
    for name,being in cvl().items():
        ddl=[]
        for law, parm_list in laws.items():
            ddl.append([subjected(being,parm_list),targeted(being,parm_list),law])
        ddlo.append([name,ddl])
    return ddlo
        
        
def subjected(being,parameter_list):
    switch=0            
    pert_value=' '
    if parameter_list[0][1] == 1:
        pert_value=hair_color(being.code)
    if parameter_list[0][1] == 2:
        pert_value=eye_color(being.code)
    if parameter_list[0][1] == 3:
        pert_value=weight(being.code)
    if parameter_list[0][1] == 4:
        pert_value=inch_height(being.code)
    if parameter_list[0][1] == 5:
        track_name=parameter_list[0][0][13:]
        pert_value=run_track(safe_pick('tracks')[track_name],being.code)
        """"""
    if parameter_list[1][1] == 1:
        if parameter_list[2][1] != pert_value:
            switch=1
    if parameter_list[1][1] == 2:
        if parameter_list[2][1] == pert_value:
            switch=1
    if parameter_list[1][1] == 3:
        if parameter_list[2][1] > pert_value:
            switch=1
    if parameter_list[1][1] == 4:
        if parameter_list[2][1] >= pert_value:
            switch=1
    if parameter_list[1][1] == 5:
        if parameter_list[2][1] < pert_value:
            switch=1
    if parameter_list[1][1] == 6:
        if parameter_list[2][1] <= pert_value:
            switch=1 
    return switch

def targeted(being,parameter_list):
    switch=0            
    pert_value=' '
    if parameter_list[3][1] == 1:
        pert_value=hair_color(being.code)
    if parameter_list[3][1] == 2:
        pert_value=eye_color(being.code)
    if parameter_list[3][1] == 3:
        pert_value=weight(being.code)
    if parameter_list[3][1] == 4:
        pert_value=inch_height(being.code)
    if parameter_list[3][1] == 5:
        track_name=parameter_list[0][0][13:]
        pert_value=run_track(safe_pick('tracks')[track_name],being.code)
        """"""
    if parameter_list[4][1] == 1:
        if parameter_list[5][1] != pert_value:
            switch=1
    if parameter_list[4][1] == 2:
        if parameter_list[5][1] == pert_value:
            switch=1
    if parameter_list[4][1] == 3:
        if parameter_list[5][1] > pert_value:
            switch=1
    if parameter_list[4][1] == 4:
        if parameter_list[5][1] >= pert_value:
            switch=1
    if parameter_list[4][1] == 5:
        if parameter_list[5][1] < pert_value:
            switch=1
    if parameter_list[4][1] == 6:
        if parameter_list[5][1] <= pert_value:
            switch=1 
    return switch

def ddlaws_subject():
    villagers=cvl()
    laws=safe_pick('laws{}'.format(cvs()))
    effected=[]
    for name, being in villagers.items():
        for law, parameter_list in laws.items():
            switch=0            
            pert_value=' '
            if parameter_list[0][1] == 1:
                pert_value=hair_color(being.code)
            if parameter_list[0][1] == 2:
                pert_value=eye_color(being.code)
            if parameter_list[0][1] == 3:
                pert_value=weight(being.code)
            if parameter_list[0][1] == 4:
                pert_value=inch_height(being.code)
            if parameter_list[0][1] == 5:
                track_name=parameter_list[0][0][13:]
                pert_value=run_track(safe_pick('tracks')[track_name],being.code)
            print(pert_value)
            """
"""
            if parameter_list[1][1] == 1:
                if parameter_list[2][1] != pert_value:
                    switch=1
            if parameter_list[1][1] == 2:
                if parameter_list[2][1] == pert_value:
                    switch=1
            if parameter_list[1][1] == 3:
                if parameter_list[2][1] > pert_value:
                    switch=1
            if parameter_list[1][1] == 4:
                if parameter_list[2][1] >= pert_value:
                    switch=1
            if parameter_list[1][1] == 5:
                if parameter_list[2][1] < pert_value:
                    switch=1
            if parameter_list[1][1] == 6:
                if parameter_list[2][1] <= pert_value:
                    switch=1
            if law in effected:
                effected[law].append([name,switch])
            else:
                effected[law] = [name,switch]  
    return effected

def ddlaws_target():
    villagers=cvl()
    laws=safe_pick('laws{}'.format(cvs()))
    effected={}
    for law, parameter_list in laws.items():
        print ([law,'x', parameter_list])
        for name, being in villagers.items():
            switch=0
            pert_value=' '
            if parameter_list[3][1] == 1:
                pert_value=hair_color(being.code)
            if parameter_list[3][1] == 2:
                pert_value=eye_color(being.code)
            if parameter_list[3][1] == 3:
                pert_value=weight(being.code)
            if parameter_list[3][1] == 4:
                pert_value=inch_height(being.code)
            if parameter_list[3][1] == 5:
                track_name=parameter_list[0][0][13:]
                pert_value=run_track(safe_pick('tracks')[track_name],being.code)
            print(switch,pert_value, name, parameter_list[4][1] ,parameter_list[5][1] )
            """
"""
            if parameter_list[4][1] == 1:
                if parameter_list[5][1] != pert_value:
                    switch=1
                    print('a',switch)
            if parameter_list[4][1] == 2:
                if parameter_list[5][1] == pert_value:
                    switch=1
                    print('b',switch)
            if parameter_list[4][1] == 3:
                if parameter_list[5][1] > pert_value:
                    switch=1
                    print('c',switch)
            if parameter_list[4][1] == 4:
                if parameter_list[5][1] >= pert_value:
                    switch=1
                    print('d',switch)
            if parameter_list[4][1] == 5:
                if parameter_list[5][1] < pert_value:
                    switch=1
            if parameter_list[4][1] == 6:
                if parameter_list[5][1] <= pert_value:
                    switch=1
                    print('e',switch)
            if law in effected:
                effected[law].append([name,switch])
            else:
                effected[law] = [name,switch]
            
    return effected    
"""
def name_to_being_ALL(name):
    out=''
    try:
        out[name]
    except:
        CVA=cvl_ALL()
        out=CVA[name]
    return out

def nba(name):
    return name_to_being_ALL(name)
        
CVA=cvl_ALL()
