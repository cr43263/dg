import pickle
import random
import operator
import math
import re
from operator import itemgetter

from village_master import *

def menu_main():
    print ('**************************************************************')
    print (' ')
    print ('                 Welcome to the Main Menu')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To:')
    print ('  ======     ----------------------------------')
    print ('   (1)        Start New Village')
    if safe_pick('current_village') != {}:
        print ('   (2)        Select Existing Village')
    mm=str(input())
    if mm == ('1'):
        print ('1')
        return menu_start_new_village()
    elif mm == ('2'):
        print ('2')
        return menu_select_village()
    else:
        print (' Dead End Found, Sorry, Returning to previous menu')
        return menu_main()
        


def find_menu(menu_to_find,previous_menu):
    try:
        print('5')
        return menu_to_find
    except:
        print('6')
        print (' Dead End Found, Sorry, Returning to previous menu')
        return previous_menu
    
def menu_select_village():
    print ('**************************************************************')
    print (' ')
    print ('                 Please Select A Village')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    VL=list(village_list().keys())
    vlcl = []
    for counter, village in enumerate(VL):
        vlcl.append([counter,village])
        print ('   ({})        {}'.format(counter,village))
    rttmm=counter+1
    print ('   ({})        Return To Main Menu'.format(rttmm))    
    msv=int(input())
    if msv == rttmm:
        return menu_main()
    try:
        print (vlcl[msv][1])
        change_current_village(vlcl[msv][1])
        return menu_village(vlcl[msv][1])
    except:
        print (' Dead End Found, Sorry, Returning to previous menu')
        return menu_select_village()

def menu_start_new_village():
    print ('**************************************************************')
    print (' ')
    print ('              Please Select A New Village Type')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    for counter, types in enumerate(list_vtl):
        print ('   ({})        {}'.format(counter,types))
    rttmm=counter+1
    print ('   ({})        Return To Main Menu'.format(rttmm)) 
    snv=input()
    if int(snv) == int(rttmm):
        return menu_main()
    print ('Please Enter A Village Name:')
    snvn=input()
    try:
        start_and_move_to_new_village(str(snvn),int(snv))
        return menu_village(str(snvn))
    except:
        print ('seems like something went wrong')
        return menu_start_new_village()
        
def menu_village(village_name):    
    change_current_village(village_name)
    print ('**************************************************************')
    print (' ')
    print ('                  Welcome to {}'.format(village_name))
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    print ('   (0)         Return To Main Menu') 
    print ('   (1)         Show All Bios')  
    print ('   (2)         Show All Parents')  
    print ('   (3)         Show All Children')   
    print ('   (4)         Show All Siblings')   
    print ('   (5)         Show All Objectives')  
    print ('   (6)         Make Something (Menu)')  
    print ('   (7)         Check Objectives')
    print ('   (8)         Show Sorted List')
    print ('   (9)         Edit Groups')
   
    vmi=input()
    if int(vmi) == 0:
        return menu_main()
    if int(vmi) == 1:
        bc()
        return menu_village(village_name)
    if int(vmi) == 2:
        parents_classed()
        return menu_village(village_name)
    if int(vmi) == 3:
        children_classed()
        return menu_village(village_name)
    if int(vmi) == 4:
        display_siblings()
        return menu_village(village_name)
    if int(vmi) == 5:
        read_objectives()
        return menu_village(village_name)
    if int(vmi) == 6:
        return menu_make_something()
    if int(vmi) == 7:
        print(check_objectives())
        return menu_village(cvs())
    if int(vmi) == 8:
        return menu_sort_select()
    if int(vmi) == 9:
        return menu_edit_groups()
    
def menu_make_something():
    print ('**************************************************************')
    print (' ')
    print ('              Make Something for {}'.format(cvs()))
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    print ('   (0)         Return To Main Menu')
    print ('   (1)         Return To Village Menu')  
    print ('   (2)         Make A Law') 
    print ('   (3)         Make an Objective')
    print ('   (4)         Make A Track')
    print ('   (5)         Make A Kid Plus')
    mms=input()
    if int(mms) == 0:
        return menu_main()
    if int(mms) == 1:
        return menu_village(cvs())
    if int(mms) == 2:
        return menu_make_law()
    if int(mms) == 3:
        print( "How many Parameters (2-5)?")
        nop=input()
        print( "Objective Name?")
        on=input()
        new_objtv=create_objective(int(nop))
        save_objective(str(on),new_objtv)
        return menu_village(cvs())
    if int(mms) == 4:
        print( "How many Sections?")
        ts=int(input())
        print( "Length of each Section?")
        sl=int(input())
        print( "Name?")
        tn=input()
        nt=generate_track(ts,sl)
        add_track(nt,tn)
        return menu_list_by_stuff(list_times,cvl(),tn)
    if int(mms) == 5:
        return menu_kid_plus()
    
def menu_make_kid():
    print ('**************************************************************')
    print (' ')
    print ('             Pick a dad from {}'.format(cvs()))
    print (' ')
    print ('**************************************************************')
    print ('   Enter:                    To Select a Dad:')
    print ('  ========     ----------------------------------')
    for counter, dudes in enumerate(sort_by_gender()[0]):
        print ('   ({})        {}'.format(str(counter).rjust(3,' '),dudes[1]))
        c1=counter+1
        c2=counter+2
    print ('   ({})         Return To Main Menu'.format(str(c1).rjust(3,' ')))
    print ('   ({})         Return To Village Menu'.format(str(c2).rjust(3,' ')))
    idaddy=int(input())
    if int(idaddy) == c1:
        return menu_main()
    if int(idaddy) == c2:
        return menu_village(cvs())
    daddy=sort_by_gender()[0][idaddy][1]
    print (daddy)
    print ('**************************************************************')
    print (' ')
    print ('             Pick a mom from {}'.format(cvs()))
    print ('             to have a kid with {}'.format(daddy))
    print (' ')
    print ('**************************************************************')
    print ('   Enter:                    To Select a Mom:')
    print ('  ========     ----------------------------------')
    for counter, chicks in enumerate(sort_by_gender()[1]):
        print ('   ({})        {}'.format(str(counter).rjust(3,' '),chicks[1]))
        c1=counter+1
        c2=counter+2
    print ('   ({})         Return To Main Menu'.format(str(c1).rjust(3,' ')))
    print ('   ({})         Return To Village Menu'.format(str(c2).rjust(3,' ')))
    imommy=int(input())
    if int(imommy) == c1:
        return menu_main()
    if int(imommy) == c2:
        return menu_village(cvs())
    mommy=sort_by_gender()[1][imommy][1]
    print (mommy)
    nk=conceive_and_add(current_villagers_list()[mommy],current_villagers_list()[daddy])
    print ('Welcome {} to the world!'.format(nk.name))
    Bio(nk.code)
    return menu_village(cvs())


def menu_kid_plus():
    print ('**************************************************************')
    print (' ')
    print ('              Pick An Sorting Type:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    print ('   (0)         Return To Main Menu')
    print ('   (1)         Return To Village Menu')
    print ('   (2)         Height')
    print ('   (3)         Weight')
    print ('   (4)         Hair Color')
    print ('   (5)         Eye Color')
    print ('   (6)         Track Time')   
    mkp=input()
    if int(mkp) == 0:
        return menu_main()
    if int(mkp) == 1:
        return menu_village(cvs())
    if int(mkp) == 2:
        return menu_list_sorted_parents(list_height)
    if int(mkp) == 3:
        return menu_list_sorted_parents(list_weight)
    if int(mkp) == 4:
        return menu_list_sorted_parents(list_hair_color)
    if int(mkp) == 5:
        return menu_list_sorted_parents(list_eye_color)
    if int(mkp) == 6:
        ts=menu_select_from_list(list(all_pick('tracks').keys()),'Track')
        return menu_list_sorted_parents(list_times,ts)
    

def menu_make_objective():
    print ('**************************************************************')
    print (' ')
    print ('              Pick An Objective Type:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    print ('   (0)         Return To Main Menu')
    print ('   (1)         Custom')
    print ('   (2)         Fully Random')
    print ('   (3)         Partial Random')
    mmo=input()
    if int(mmo) == 0:
        return menu_main()
    """
    if int(mmo) == 1:
        return menu_custom_objective()
    if int(mmo) == 2:
        return menu_random_objective()
    if int(mmo) == 2:
        return menu_compound_objective()
    """
    if int(mmo) == 1:
        return menu_main()
    if int(mmo) == 2:
        print( "How many Parameters (2-5)?")
        nop=input()
        print( "Objective Name?")
        on=input()
        new_objtv=create_objective(int(nop))
        save_objective(str(on),new_objtv)
        return menu_village(cvs())
    if int(mmo) == 3:
        return menu_main()


def menu_list_by_stuff(list_type,original_list,args=[]):
    a= list_type.__name__
    print (a)
    b=a[5:]
    wl=sorted_from_list(list_type,original_list,args)
    print ('*****************************************************************************************************')
    print (' ')
    print ('              Sorted by {} '.format(b.title()))
    print (' ')
    print ('*****************************************************************************************************')
    if args==[]:
        print ('  Rank:                   Name:                 Weight   Height    Hair    Eye   Gender   Home Town ')
        print (' ========   --------------------------------------------------------------------------------------------------')
        for counter, being in enumerate(wl):
            print ('  ({})     {} {}lbs {}ft {}in  {}  {} {}   {}'.format(str(counter).rjust(3,' '),being[1].ljust(35,' '),str(weight(being[2].code)).rjust(3,' '),str(height(being[2].code)[0]).rjust(2,' '),str(height(being[2].code)[1]).rjust(2,' '),hair_color(being[2].code).ljust(6,' '),eye_color(being[2].code).ljust(6,' '),check_gender(being[2].code).ljust(6,' '),being[2].village_born_in.ljust(20,' ')))
    else:
        print ('  Rank:                   Name:                 Weight   Height    Hair    Eye   Gender   Home Town             Time')
        print (' ========   ------------------------------------------------------------------------------------------------------- ')
        for counter, being in enumerate(wl):
            print ('  ({})     {} {}lbs {}ft {}in  {}  {} {}  {}   {}'.format(str(counter).rjust(3,' '),being[1].ljust(35,' '),str(weight(being[2].code)).rjust(3,' '),str(height(being[2].code)[0]).rjust(2,' '),str(height(being[2].code)[1]).rjust(2,' '),hair_color(being[2].code).ljust(6,' '),eye_color(being[2].code).ljust(6,' '),check_gender(being[2].code).ljust(6,' '),being[2].village_born_in.ljust(20,' '),int(being[0])))
    return menu_sort_select()


def menu_sort_select():
    print ('**************************************************************')
    print (' ')
    print ('              Pick An Sorting Type:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    print ('   (0)         Return To Main Menu')
    print ('   (1)         Return To Village Menu')
    print ('   (2)         Height')
    print ('   (3)         Weight')
    print ('   (4)         Hair Color')
    print ('   (5)         Eye Color')
    print ('   (6)         Track Time')
    print ('   (7)         Home Town')
    iss=input()
    if int(iss) == 0:
        return menu_main()
    if int(iss) == 1:
        return menu_village(cvs())
    if int(iss) == 2:
        return menu_list_by_stuff(list_height,cvl())
    if int(iss) == 3:
        return menu_list_by_stuff(list_weight,cvl())
    if int(iss) == 4:
        return menu_list_by_stuff(list_hair_color,cvl())
    if int(iss) == 5:
        return menu_list_by_stuff(list_eye_color,cvl())
    if int(iss) == 6:
        ts=menu_select_from_list(list(all_pick('tracks').keys()),'Track')
        return menu_list_by_stuff(list_times,cvl(),ts)
    if int(iss) == 7:
        return menu_list_by_stuff(list_hometown,cvl())
    
    
def menu_list_sorted_parents(list_type,args=[]):
    a= list_type.__name__
    print (a)
    b=a[5:]
    dl=sorted_from_list(list_type,sort_by_gender_being()[0],args)
    ml=sorted_from_list(list_type,sort_by_gender_being()[1],args)
    print ('*****************************************************************************************************')
    print (' ')
    print ('              Pick A Dad:')
    print ('              Sorted by {} '.format(b.title()))
    print (' ')
    print ('*****************************************************************************************************')
    if args==[]:
        print ('  Enter:                   To Select:           Weight   Height    Hair    Eye   Gender')
        print (' ========   ---------------------------------------------------------------------------------')
        for counter, being in enumerate(dl):
            print ('  ({})     {} {}lbs {}ft {}in  {}  {} {}'.format(str(counter).rjust(3,' '),being[1].ljust(35,' '),str(weight(being[2].code)).rjust(3,' '),str(height(being[2].code)[0]).rjust(2,' '),str(height(being[2].code)[1]).rjust(2,' '),hair_color(being[2].code).ljust(6,' '),eye_color(being[2].code).ljust(6,' '),check_gender(being[2].code).ljust(6,' ')))
            c1=counter+1
            c2=counter+2
    else:
        print ('  Enter:                   To Select:           Weight   Height    Hair    Eye   Gender  Time')
        print (' ========   --------------------------------------------------------------------------------- ')
        for counter, being in enumerate(dl):
            print ('  ({})     {} {}lbs {}ft {}in  {}  {} {}  {}'.format(str(counter).rjust(3,' '),being[1].ljust(35,' '),str(weight(being[2].code)).rjust(3,' '),str(height(being[2].code)[0]).rjust(2,' '),str(height(being[2].code)[1]).rjust(2,' '),hair_color(being[2].code).ljust(6,' '),eye_color(being[2].code).ljust(6,' '),check_gender(being[2].code).ljust(6,' '),int(being[0])))
            c1=counter+1
            c2=counter+2
    print ('  ({})      Return To Main Menu'.format(str(c1).rjust(3,' ')))
    print ('  ({})      Return To Village Menu'.format(str(c2).rjust(3,' ')))
    idaddy=int(input())
    if int(idaddy) == c1:
        return menu_main()
    if int(idaddy) == c2:
        return menu_village(cvs())
    daddy=dl[idaddy]
    print ('*****************************************************************************************************')
    print (' ')
    print ('              Pick A Mom:')
    print ('              Sorted by {} '.format(b.title()))
    print (' ')
    print ('*****************************************************************************************************')
    if args==[]:
        print ('  Enter:                   To Select:           Weight   Height    Hair    Eye   Gender')
        print (' ========   ---------------------------------------------------------------------------------')
        for counter, being in enumerate(ml):
            print ('  ({})     {} {}lbs {}ft {}in  {}  {} {}'.format(str(counter).rjust(3,' '),being[1].ljust(35,' '),str(weight(being[2].code)).rjust(3,' '),str(height(being[2].code)[0]).rjust(2,' '),str(height(being[2].code)[1]).rjust(2,' '),hair_color(being[2].code).ljust(6,' '),eye_color(being[2].code).ljust(6,' '),check_gender(being[2].code).ljust(6,' ')))
            c1=counter+1
            c2=counter+2
    else:
        print ('  Enter:                   To Select:           Weight   Height    Hair    Eye   Gender  Time')
        print (' ========   --------------------------------------------------------------------------------- ')
        for counter, being in enumerate(ml):
            print ('  ({})     {} {}lbs {}ft {}in  {}  {} {}  {}'.format(str(counter).rjust(3,' '),being[1].ljust(35,' '),str(weight(being[2].code)).rjust(3,' '),str(height(being[2].code)[0]).rjust(2,' '),str(height(being[2].code)[1]).rjust(2,' '),hair_color(being[2].code).ljust(6,' '),eye_color(being[2].code).ljust(6,' '),check_gender(being[2].code).ljust(6,' '),int(being[0])))
            c1=counter+1
            c2=counter+2
    print ('  ({})      Return To Main Menu'.format(str(c1).rjust(3,' ')))
    print ('  ({})      Return To Village Menu'.format(str(c2).rjust(3,' ')))
    imommy=int(input())
    if int(imommy) == c1:
        return menu_main()
    if int(imommy) == c2:
        return menu_village(cvs())
    mommy=ml[imommy]
    nk=conceive_and_add(mommy[2],daddy[2])
    print ('Welcome {} to the world!'.format(nk.name))
    Bio(nk.code)
    return menu_village(cvs())

def menu_make_law():
    print ('**************************************************************')
    print ('IF subjects {{thing1}} is {{comparer1}} {{value1}},')
    print ('their mates {{thing2}} must be {{comparer2}} {{value2}}')
    print ('EXAMPLE')
    print ('IF subjects hair_color is not blonde,')
    print ('their mates weight must be less than 250 ')
    print (' ')
    print ('              Pick {{thing1}}:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Select:')
    print ('  ======     ----------------------------------')
    print ('  (  1)        Hair Color')
    print ('  (  2)        Eye Color')
    print ('  (  3)        Weight')
    print ('  (  4)        Height')
    print ('  (  5)        Track Time')
    print ('  ({})        Return To Main Menu'.format(str(6).rjust(3,' ')))
    print ('  ({})        Return To Village Menu'.format(str(7).rjust(3,' ')))
    ilaw_t1=int(input())
    
    if int(ilaw_t1) == 6:
        return menu_main()
    if int(ilaw_t1) == 7:
        return menu_village(cvs())
    if int(ilaw_t1) == 1:
        thing1 = 'hair color'
    if int(ilaw_t1) == 2:
        thing1 = 'eye color'
    if int(ilaw_t1) == 3:
        thing1 = 'weight'
    if int(ilaw_t1) == 4:
        thing1 = 'height'
    if int(ilaw_t1) == 5:
        st1=select_track()
        thing1 = 'heat time on {}'.format(st1)
    thing1l = [thing1,ilaw_t1]
    print ('**************************************************************')
    print ('IF subjects {}'.format(thing1),'{{comparer1}} {{value1}}')
    print ('their mates {{thing2}} must be {{comparer2}} {{value2}}')
    print ('EXAMPLE')
    print ('IF subjects hair_color {{is not}} {{blonde}},')
    print ('their mates weight must be less than 250 ')
    print (' ')
    print ('              Pick {{comparer1}}:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Select:')
    print ('  ======     ----------------------------------')
    if int(ilaw_t1) == 1 or int(ilaw_t1) == 2:
        print ('  (  1)        is')
        print ('  (  2)        is not')
    else:
        print ('  (  1)        is')
        print ('  (  2)        is not')
        print ('  (  3)        is less than')
        print ('  (  4)        is less than or equal to')
        print ('  (  5)        is greater than')
        print ('  (  6)        is greater than or equal to')
    ilaw_c1=int(input())
    if int(ilaw_c1) == 1:
        comparer1 = 'is'
    if int(ilaw_c1) == 2:
        comparer1 = 'is not'
    if int(ilaw_c1) == 3:
        comparer1 = 'is less than'
    if int(ilaw_c1) == 4:
        comparer1 = 'is less than or equal to'
    if int(ilaw_c1) == 5:
        comparer1 = 'is greater than'
    if int(ilaw_c1) == 6:
        comparer1 = 'is greater than or equal to'
    comparer1l=[comparer1,ilaw_c1]
    print ('**************************************************************')
    print ('IF subjects {} {}'.format(thing1,comparer1),' {{value1}}')
    print ('their mates {{thing2}} must be {{comparer2}} {{value2}}')
    print ('EXAMPLE')
    print ('IF subjects hair_color... {{is not}} {{blonde}},')
    print ('their mates weight must be less than 250 ')
    print (' ')
    if int(ilaw_t1) == 1 or int(ilaw_t1) == 2:
        print ('              Pick {{value1}}:')
        print (' ')
        print ('**************************************************************')
        print ('  Enter:                    To Select:')
        print ('  ======     ----------------------------------')
        if int(ilaw_t1) == 1:
            clist=hcs
        else:
            clist=ecs
        for counter, color in enumerate(clist):
            print ('   ({})        {}'.format(str(counter).rjust(3,' '),color))
        ilaw_v1=int(input())        
        value1=clist[ilaw_v1]
    elif int(ilaw_t1) == 4:
        print ('Feet:')
        ilaw_v1f=int(input())
        print ('Inches:')
        ilaw_v1i=int(input())
        ilaw_v1=(12*ilaw_v1f)+ilaw_v1i
        value1='{} foot {} inches'.format(ilaw_v1f,ilaw_v1i)
    elif int(ilaw_t1) == 5:
        print ('              Enter {{value1}}:')
        print (' ')
        print ('**************************************************************')
        ilaw_v1=int(input())
        value1=ilaw_v1
    else:
        print ('              Enter {{value1}}:')
        print (' ')
        print ('**************************************************************')
        ilaw_v1=int(input())
        value1='{} lbs'.format(ilaw_v1)
    value1l=[value1,ilaw_v1]
    print ('**************************************************************')
    print ('IF subjects {} {} {}'.format(thing1,comparer1,value1))
    print ('their mates {{thing2}} must be {{comparer2}} {{value2}}')
    print ('EXAMPLE')
    print ('IF subjects hair_color... {{is not}} {{blonde}},')
    print ('their mates weight must be less than 250 ')
    print (' ')
    print ('              Pick {{thing2}}:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Select:')
    print ('  ======     ----------------------------------')
    print ('  (  1)        Hair Color')
    print ('  (  2)        Eye Color')
    print ('  (  3)        Weight')
    print ('  (  4)        Height')
    print ('  (  5)        Track Time')
    print ('  ({})        Return To Main Menu'.format(str(6).rjust(3,' ')))
    print ('  ({})        Return To Village Menu'.format(str(7).rjust(3,' ')))
    ilaw_t2=int(input())    
    if int(ilaw_t2) == 6:
        return menu_main()
    if int(ilaw_t2) == 7:
        return menu_village(cvs())
    if int(ilaw_t2) == 1:
        thing2 = 'hair color'
    if int(ilaw_t2) == 2:
        thing2 = 'eye color'
    if int(ilaw_t2) == 3:
        thing2 = 'weight'
    if int(ilaw_t2) == 4:
        thing2 = 'height'
    if int(ilaw_t2) == 5:
        st2=select_track()
        thing2 = 'heat time on {}'.format(st2)
    thing2l=[thing2,ilaw_t2]
    """
    print ('**************************************************************')
    print ('IF subjects {} {} {}'.format(thing1,comparer1,value1))
    print ('their mates {}'.format(thing2), '{{cant/must}} be {{comparer2}} {{value2}}')
    print ('EXAMPLE')
    print ('IF subjects hair_color {{is not}} {{blonde}},')
    print ('their mates weight must be less than 250 ')
    print (' ')
    print ('              Pick {{cant/must}}:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Select:')
    print ('  ======     ----------------------------------')
    print ('  (  1)        cant')
    print ('  (  2)        must')
    icm=int(input())
    if int(icm) == 1:
        xcm = 'cant'
    if int(icm) == 2:
        xcm = 'must'
    """
    print ('**************************************************************')
    print ('IF subjects {} {} {}'.format(thing1,comparer1,value1))
    print ('their mates {} must'.format(thing2),' be {{comparer2}} {{value2}}')
    print ('EXAMPLE')
    print ('IF subjects hair_color {{is not}} {{blonde}},')
    print ('their mates weight must be less than 250 ')
    print (' ')
    print ('              Pick {{comparer2}}:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Select:')
    print ('  ======     ----------------------------------')
    if int(ilaw_t2) == 1 or int(ilaw_t2) == 2:
        print ('  (  1)        be')
        print ('  (  2)        not be')
    else:
        print ('  (  1)        be')
        print ('  (  2)        not be')
        print ('  (  3)        be less than')
        print ('  (  4)        be less than or equal to')
        print ('  (  5)        be greater than')
        print ('  (  6)        be greater than or equal to')
    ilaw_c2=int(input())
    if int(ilaw_c2) == 1:
        comparer2 = 'be'
    if int(ilaw_c2) == 2:
        comparer2 = 'not be'
    if int(ilaw_c2) == 3:
        comparer2 = 'be less than'
    if int(ilaw_c2) == 4:
        comparer2 = 'be less than or equal to'
    if int(ilaw_c2) == 5:
        comparer2 = 'be greater than'
    if int(ilaw_c2) == 6:
        comparer2 = 'be greater than or equal to'
    comparer2l=[comparer2,ilaw_c2]
    print ('**************************************************************')
    print ('IF subjects {} {} {}'.format(thing1,comparer1,value1))
    print ('their mates {} must {}'.format(thing2,comparer2),' {{value2}}')
    print ('EXAMPLE')
    print ('IF subjects hair_color... {{is not}} {{blonde}},')
    print ('their mates weight must be less than 250 ')
    print (' ')
    if int(ilaw_t2) == 1 or int(ilaw_t2) == 2:
        print ('              Pick {{value2}}:')
        print (' ')
        print ('**************************************************************')
        print ('  Enter:                    To Select:')
        print ('  ======     ----------------------------------')
        if int(ilaw_t2) == 1:
            clist=hcs
        else:
            clist=ecs
        for counter, color in enumerate(clist):
            print ('   ({})        {}'.format(str(counter).rjust(3,' '),color))
        ilaw_v2=int(input())        
        value2=clist[ilaw_v2]
    elif int(ilaw_t2) == 4:
        print ('Feet:')
        ilaw_v2f=int(input())
        print ('Inches:')
        ilaw_v2i=int(input())
        ilaw_v2=(12*(ilaw_v2f))+ilaw_v2i
        value2='{} foot {} inches'.format(ilaw_v2f,ilaw_v2i)
    elif int(ilaw_t2) == 5:
        print ('              Enter {{value2}}:')
        print (' ')
        print ('**************************************************************')
        ilaw_v2=int(input())
        value1=ilaw_v2
    else:
        print ('              Enter {{value2}}:')
        print (' ')
        print ('**************************************************************')
        ilaw_v2=int(input())
        value2='{} lbs'.format(ilaw_v2)
    value2l=[value2,ilaw_v2]
    print ('**************************************************************')
    print (' ')
    print ('              Pick a name for this law:')
    print (' ')
    print ('**************************************************************')
    print ('IF subjects {} {} {}'.format(thing1,comparer1,value1))
    print ('their mates {} must {} {}'.format(thing2,comparer2,value2))
    law_name=str(input())
    saave([thing1l,comparer1l,value1l,thing2l,comparer2l,value2l],law_name,'laws{}'.format(cvs()))
    return menu_village(cvs())
           
        
               
               
def menu_select_from_list(alist,listname='Thing'):
    print ('**************************************************************')
    print (' ')
    print ('              Pick A {}:'.format(listname))
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Select:')
    print ('  ======     ----------------------------------')
    nl=[]
    for counter, thing in enumerate(alist):
        nl.append(thing)
        print ('   ({})        {}'.format(str(counter).rjust(3,' '),thing))
    iselect=int(input())
    try:
        selection=alist[iselect]
    except:
        selection=alist[nl[iselect]]
    return selection
    
    
def select_track():
    print ('**************************************************************')
    print (' ')
    print ('              Pick A Track:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Select:')
    print ('  ======     ----------------------------------')
    tl=[]
    tl = list(all_pick('tracks').keys())
    for counter, track in enumerate(tl):
        print ('   ({})        {}'.format(str(counter).rjust(3,' '),track))
    ilaw_tl=int(input())
    return tl[ilaw_tl]
    
def menu_edit_groups():
    print ('**************************************************************')
    print (' ')
    print ('              Pick A Group:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Select:')
    print ('  ======     ----------------------------------')
    gs=[]
    gs = list(safe_pick('groups_{}'.format(cvs())).keys())
    if gs == []:
        c1=0
        c2=1
        c3=2
    for counter, group in enumerate(gs):
        print ('  ({})      {}'.format(str(counter).rjust(3,' '),group))
        c1=counter+1
        c2=counter+2
        c3=counter+3
        c4=counter+4
    print ('  ({})      Create New Group'.format(str(c1).rjust(3,' ')))
    print ('  ({})      Return To Main Menu'.format(str(c2).rjust(3,' ')))
    print ('  ({})      Return To Village Menu'.format(str(c3).rjust(3,' ')))
    print ('  ({})      Move Group to a Different Village'.format(str(c4).rjust(3,' ')))
    igs=int(input())
    if int(igs) == c1:
        print ('Enter a name for this Group:')
        group_name=str(input())
        selected_group=[]
        srt_styl=menu_choose_sort_style()
        try:
            return menu_edit_one_group(srt_styl[0],selected_group,group_name,srt_styl[1])
        except:
            return menu_edit_one_group(srt_styl,selected_group,group_name)
    if int(igs) == c2:
        return menu_main()
    if int(igs) == c3:
        return menu_village(cvs())
    if int(igs) == c4:
        return menu_move_group()
    selected_group=[]
    selected_group=safe_pick('groups_{}'.format(cvs()))[gs[igs]]
    srt_styl=menu_choose_sort_style()
    print(srt_styl)
    try:
        return menu_edit_one_group(srt_styl[0],selected_group,gs[igs],srt_styl[1])
    except:
        return menu_edit_one_group(srt_styl,selected_group,gs[igs])
    
    
        
def menu_create_group():
    print ('Enter a name for this Group:')
    group_name=str(input())
    return None

def menu_edit_one_group(list_type,selected_group,group_name,args=[]):
    a= list_type.__name__
    print (a)
    b=a[5:]
    wl=sorted_from_list(list_type,cvl(),args)
    print ('*****************************************************************************************************')
    print (' ')
    print ('              Sorted by {} '.format(b.title()))
    print (' ')
    print ('*****************************************************************************************************')
    if args==[]:
        print ('  Rank:                   Name:                 Weight   Height    Hair    Eye   Gender   Status')
        print (' ========   ------------------------------------------------------------------------------------')
        for counter, being in enumerate(wl):
            status=' ADD  '
            if being[1] in selected_group:
                status='REMOVE'
            print ('  ({})     {} {}lbs {}ft {}in  {}  {} {}  {}'.format(str(counter).rjust(3,' '),being[1].ljust(35,' '),str(weight(being[2].code)).rjust(3,' '),str(height(being[2].code)[0]).rjust(2,' '),str(height(being[2].code)[1]).rjust(2,' '),hair_color(being[2].code).ljust(6,' '),eye_color(being[2].code).ljust(6,' '),check_gender(being[2].code).ljust(6,' '),'[{}]'.format(status)))
            c1=counter+1
            c2=counter+2
            c3=counter+3
    else:
        print ('  Rank:                   Name:                 Weight   Height    Hair    Eye   Gender  Time    Status')
        print (' ========   -------------------------------------------------------------------------------------------')
        for counter, being in enumerate(wl):
            status=' ADD  '
            if being[1] in selected_group:
                status='REMOVE'
            print ('  ({})     {} {}lbs {}ft {}in  {}  {} {}  {}  {}'.format(str(counter).rjust(3,' '),being[1].ljust(35,' '),str(weight(being[2].code)).rjust(3,' '),str(height(being[2].code)[0]).rjust(2,' '),str(height(being[2].code)[1]).rjust(2,' '),hair_color(being[2].code).ljust(6,' '),eye_color(being[2].code).ljust(6,' '),check_gender(being[2].code).ljust(6,' '),str(int(being[0])).ljust(6,' '),'[{}]'.format(status))) 
            c1=counter+1
            c2=counter+2
            c3=counter+3
    print ('  ({})      Return To Main Menu'.format(str(c1).rjust(3,' ')))
    print ('  ({})      Return To Village Menu'.format(str(c2).rjust(3,' ')))
    print ('  ({})      Return To Edit Groups Menu'.format(str(c3).rjust(3,' ')))
    bs=int(input())
    if int(bs) == c1:
        return menu_main()
    if int(bs) == c2:
        return menu_village(cvs())
    if int(bs) == c3:
        return menu_edit_groups()
    edit_group(group_name,wl[bs][1])
    return menu_edit_one_group(list_type,safe_pick('groups_{}'.format(cvs()))[group_name],group_name,args=[])

def menu_choose_sort_style():
    print ('**************************************************************')
    print (' ')
    print ('              Pick An Sorting Type:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    print ('   (0)         Return To Main Menu')
    print ('   (1)         Return To Village Menu')
    print ('   (2)         Height')
    print ('   (3)         Weight')
    print ('   (4)         Hair Color')
    print ('   (5)         Eye Color')
    print ('   (6)         Track Time')
    iss=input()
    if int(iss) == 0:
        return menu_main()
    if int(iss) == 1:
        return menu_village(cvs())
    if int(iss) == 2:
        return list_height
    if int(iss) == 3:
        return list_weight
    if int(iss) == 4:
        return list_hair_color
    if int(iss) == 5:
        return list_eye_color
    if int(iss) == 6:
        ts=menu_select_from_list(list(all_pick('tracks').keys()),'Track')
        return list_times,ts    

def menu_move_group():
    gl=list(all_pick('groups_{}'.format(cvs())).keys())
    print ('**************************************************************')
    print (' ')
    print ('              Pick A Group:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    for counter, group in enumerate(gl):
        print ('  ({})      {}'.format(str(counter).rjust(3,' '),group))
        c1=counter+1
        c2=counter+2
    print ('  ({})      Return To Main Menu'.format(str(c1).rjust(3,' ')))
    print ('  ({})      Return To Village Menu'.format(str(c2).rjust(3,' ')))
    iss=input()
    if int(iss) == c1:
        return menu_main()
    if int(iss) == c2:
        return menu_village(cvs())
    selected_group=gl[int(iss)]
    other_villages_list=list(village_list().keys())
    other_villages_list.remove(cvs())
    print ('**************************************************************')
    print (' ')
    print ('              Pick A Village To Move To:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    print ('   (0)         Return To Main Menu')
    print ('   (1)         Return To Village Menu')
    for counter, group in enumerate(other_villages_list):
        print ('  ({})      {}'.format(str(counter).rjust(3,' '),group))
        c21=counter+1
        c22=counter+2
    iss2=input()
    if int(iss2) == c21:
        return menu_main()
    if int(iss2) == c22:
        return menu_village(cvs())
    selected_village=other_villages_list[int(iss2)]
    log_tran_group(selected_group,selected_village)
    return menu_village(cvs())
    

 
def menu_show_family_tree(being):
    print ('**************************************************************')
    print (' ')
    print ('              Family Tree for {}:'.format(display_name(being.name)))
    print (' ')
    print ('**************************************************************')
    print ('  Parents:')
    print ('  Mom  =======>  {}'.format(display_name(being.mom[0])))
    print ('  Dad  =======>  {}'.format(display_name(being.dad[0])))
    print (' ')
    print ('  Children:')
    for kid in being.children:
        print (display_name(kid[0]))
    print (' ')
    print ('  Aunts And Uncles:')
    for anu in loop_list_siblings(loop_list_parents([display_name(being.name)])):
        print (anu)
    print (' ')
    print (' Full Siblings:')
    for fsib in loop_list_siblings([display_name(being.name)])[0]:
        print (fsib)
    print (' ')
    print (' Half Siblings:')
    for hsib in loop_list_siblings([display_name(being.name)])[1]:
        print (hsib)
    
    
           
    
"""
def sorted_from_list(sort_type,og_list,args=[]):
    if args==[]:
        rl=sort_type(og_list)
    else:
        rl=sort_type(og_list,args)
    return rl
    

def menu_list_by_stuff(list_type,original_list,args=[]):
    a= list_type.__name__
    print (a)
    b=a[5:]
    wl=sorted_from_list(list_type,original_list,args)
    print ('*****************************************************************************************************')
    print (' ')
    print ('              Sorted by {} '.format(b.title()))
    print (' ')
    print ('*****************************************************************************************************')
    if args==[]:
        print ('  Rank:                   Name:                 Weight   Height    Hair    Eye   Gender')
        print (' ========   ---------------------------------------------------------------------------------')
        for counter, being in enumerate(wl):
            print ('  ({})     {} {}lbs {}ft {}in  {}  {} {}'.format(str(counter).rjust(3,' '),being[1].ljust(35,' '),str(weight(being[2].code)).rjust(3,' '),str(height(being[2].code)[0]).rjust(2,' '),str(height(being[2].code)[1]).rjust(2,' '),hair_color(being[2].code).ljust(6,' '),eye_color(being[2].code).ljust(6,' '),check_gender(being[2].code).ljust(6,' ')))
    else:
        print ('  Rank:                   Name:                 Weight   Height    Hair    Eye   Gender  Time')
        print (' ========   --------------------------------------------------------------------------------- ')
        for counter, being in enumerate(wl):
            print ('  ({})     {} {}lbs {}ft {}in  {}  {} {}  {}'.format(str(counter).rjust(3,' '),being[1].ljust(35,' '),str(weight(being[2].code)).rjust(3,' '),str(height(being[2].code)[0]).rjust(2,' '),str(height(being[2].code)[1]).rjust(2,' '),hair_color(being[2].code).ljust(6,' '),eye_color(being[2].code).ljust(6,' '),check_gender(being[2].code).ljust(6,' '),int(being[0])))
    return menu_sort_select()


def menu_sort_select():
    print ('**************************************************************')
    print (' ')
    print ('              Pick An Sorting Type:')
    print (' ')
    print ('**************************************************************')
    print ('  Enter:                    To Go To:')
    print ('  ======     ----------------------------------')
    print ('   (0)         Return To Main Menu')
    print ('   (1)         Return To Village Menu')
    print ('   (2)         Height')
    print ('   (3)         Weight')
    print ('   (4)         Hair Color')
    print ('   (5)         Eye Color')
    print ('   (6)         Track Time')
    iss=input()
    if int(iss) == 0:
        return menu_main()
    if int(iss) == 1:
        return menu_village(cvs())
    if int(iss) == 2:
        return menu_list_by_stuff(list_height,cvl())
    if int(iss) == 3:
        return menu_list_by_stuff(list_weight,cvl())
    if int(iss) == 4:
        return menu_list_by_stuff(list_hair_color,cvl())
    if int(iss) == 5:
        return menu_list_by_stuff(list_eye_color,cvl())
    if int(iss) == 6:
        ts=menu_select_from_list(list(all_pick('tracks').keys()),'Track')
        return menu_list_by_stuff(list_times,cvl(),ts)
"""
