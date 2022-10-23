'''
This problem was asked by Amazon.

The stable marriage problem is defined as follows:

Suppose you have N men and N women, and each person has ranked their prospective opposite-sex partners in order of preference.

[Hard]

For example, if N = 3, the input could be something like this:

guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
Write an algorithm that pairs the men and women together in such a way that no two people of opposite sex would both rather be with each other than with their current partners.
'''

def stableMarriges(guy_prefs, gal_prefs):
    # Free woman who will get to choose (choosing is an advantage)
    free_woman = []
    for woman in gal_prefs.keys():
        free_woman.append(woman)


    tentative_marriges = []
    while len(free_woman) > 0:
        for woman in free_woman:
            for man in gal_prefs[woman]:
                taken_match = [couple for couple in tentative_marriges if man in couple]

                if len(taken_match) == 0:
                    tentative_marriges.append([woman, man])
                    free_woman.remove(woman)
                    break
                else:
                    # Current woman rank for the man 
                    current_woman = guy_prefs[man].index(taken_match[0][0])
                    # Potential woman rank for the man
                    potential_woman = guy_prefs[man].index(woman)

                    if potential_woman < current_woman:
                        free_woman.remove(woman)
                        free_woman.append(taken_match[0][0])
                        taken_match[0][0] = woman
                        break
    return tentative_marriges




# guy_preferences = {
#     'andrew': ['caroline', 'abigail', 'betty'],
#     'bill': ['caroline', 'betty', 'abigail'],
#     'chester': ['betty', 'caroline', 'abigail'],
# }

# gal_preferences = {
#     'abigail': ['andrew', 'bill', 'chester'],
#     'betty': ['bill', 'andrew', 'chester'],
#     'caroline': ['bill', 'chester', 'andrew']
# }

# print(stableMarriges(guy_preferences, gal_preferences))

preferred_rankings_men = {
	'ryan': 	['lizzy', 'sarah', 'zoey', 'daniella'],
	'josh': 	['sarah', 'lizzy', 'daniella', 'zoey'],
	'blake': 	['sarah', 'daniella', 'zoey', 'lizzy'],
	'connor': 	['lizzy', 'sarah', 'zoey', 'daniella']
}

#The men that the women prefer
preferred_rankings_women = {
	'lizzy': 	['ryan', 'blake', 'josh', 'connor'],
	'sarah': 	['ryan', 'blake', 'connor', 'josh'],
	'zoey':  	['connor', 'josh', 'ryan', 'blake'],
	'daniella':	['ryan', 'josh', 'connor', 'blake'] 
}

print(stableMarriges(preferred_rankings_men, preferred_rankings_women))