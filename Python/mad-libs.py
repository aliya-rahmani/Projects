from random import randint
import copy

story = (
    "One day my {} friend and I decided to go to the {} game in {}. "+
    "We really wanted to see the {} play the {}. "+
    "So, we {} our {} down to the {} and bought some {}s. "+
    "We got into the game and it was a lot of fun. "+
    "We ate some {} and drank some {}. "+
    "We had a great time! We plan to go ahead next year! "
)

#create a dictionary to lookup the words by type

word_dict = {
    'adjective':['greedy','abrasive','grubby','rich','harsh','tasty'],
    'city name':['Trivandrum','Kochi','Kollam','Thrissur','Alappuzha'],
    'noun':['people','map','dog','hamster','ball','shwarma','salad'],
    'action verb':['run','fall','crawl','scurry','cry','watch','swim','jump','bounce'],
    'sport noun':['ball','bat','puck','player','helmet','uniform','team'],
    'place':['park','forest','desert','store','restaurant','waterfall']
}

def get_word(type,local_dict):#local dict is the main dict itself, local in this func
    words = local_dict[type] #will get the list of that type in the dict
    count = len(words)-1
    index = randint(0,count)
    return local_dict[type].pop(index)#removing the already use word.

def create_story():
    local_dict = copy.deepcopy(word_dict)#making a replication of the word dict, we cannot use =
    return story.format(
        get_word('adjective', local_dict),
        get_word('sport noun',local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun',local_dict),
        get_word('action verb', local_dict),
        get_word('noun', local_dict),
        get_word('place',local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun',local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
    )
print("STORY 1:")
print(create_story())
print()
print("STORY 2:")
print(create_story())

