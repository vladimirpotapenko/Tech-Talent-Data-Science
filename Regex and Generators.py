# Q1

import re

regex_sub_dict = {
    re.compile(r'[ ]&&[ ]') : ' and ',
    re.compile(r'[ ]\|\|[ ]') : ' or '
    }

string = '''There was once &&&& that had !!!! yet&& was ||s 
nose never worked && was often missing. 
This is the story of good || something else. | 12& can't try|| 
recognize need more effort.
To learn regex && python in general&|
This is 
a
python && || & &&& $&& | |||| as|| as&& &&ss ||ss _&& _&&&

exercise && '''


def mult_regex_sub_func(dictionary, string):
    '''This function performs multiple regex substitutions for on a string
    based on regex keywords in a translation dictionary'''
    
    
    if len(string.splitlines()) >= 100 or len(string.splitlines()) < 1:
        print("At least one line; no more than 99")
    for regex, repl in dictionary.items():
        string = regex.sub(repl, string)
    return string


print(mult_regex_sub_func(regex_sub_dict, string))

# Q2


import re

list_of_names_and_emails = ["dexter <dexter@hotmail.com>",
"VIRUS <virus!@variable.:p>"]

pattern = re.compile(r'(?P<name>[a-zA-z]+) <(?P<entire>(?P<username>[a-zA-z][\w\-\.]*)@(?P<domain>[a-zA-z]+)\.(?P<extension>[a-zA-z]{1,3}))>')

if len(list_of_names_and_emails) < 100 and len(list_of_names_and_emails) > 0:
    for pair in list_of_names_and_emails:
        match = pattern.search(pair)
        if match:
            print(match.group(1).upper(), match.group("entire") )

