# Note: punctuations have to be from 0 to 10
QUESTIONS_ANSWERS = [
# Gender
        ('How many women are now in this meeting? (percentage)', ['10', '30', '50'], {'10': 0, '30': 5, '50': 10}),
        ('Are your bosses men?', ['y', 'n'], {'y': -5, 'n': 10}),
        ('White men?', ['y', 'n'], {'y': -5, 'n': 10}),
        ('Cisgender men?', ['y', 'n'], {'y': -5, 'n': 10}),
# Sexual orientation
        ('Have you ever made or heard a joke about gay people?', ['y', 'n'], {'y': 0, 'n': 5}),
# Age
        ('Is your group made only of 20-40y people?', ['y', 'n'], {'y': 0, 'n': 5}),
        ('Is there anyone conciliating childcare with the activity in the group?', ['y', 'n'], {'y': 10, 'n': 0}),
# Abilities
        ('Do you see people with functional diversity?', ['y', 'n'], {'y': 5, 'n': 0}),
        ('Are you aware of accesibility issues for this meeting?', ['y', 'n'], {'y': 5, 'n': 0}),
# Origin
        ('Do you see people from elsewhere?', ['y', 'n'], {'y': 5, 'n': 0}),
        ('Do you see black people?', ['y', 'n'], {'y': 10, 'n': 0}),
        ('Do you see people from Latin America?', ['y', 'n'], {'y': 10, 'n': 0}),
# Economic status
        ('Are you aware of grants for people with less resources in your group?', ['y', 'n'], {'y': 5, 'n': 0}),
        ('In your office, is there anyone who entered thanks to a recommendation?', ['y', 'n'], {'y': 0, 'n': 10}),
# Access to studies
        ('Do you think that people without university degree have to be better to be respected?', ['y', 'n'], {'y': 0, 'n': 5}),
# Focus inside technology
        ('Do you think in your group developers are more respected than facilitators?', ['y', 'n'], {'y': 0, 'n': 5}),
        ('Do you sometimes take a look at the health of your community?', ['y', 'n'], {'y': 5, 'n': 0}),
# Focus in other interests
        ('Do you sometimes feel inspired by the hobbies of your colleagues?', ['y', 'n'], {'y': 5, 'n': 0}),
        ('Do your group focus the conversation always in the same topics?', ['y', 'n'], {'y': 0, 'n': 5}),
# Focus in technology
        ('Is your group open to different technologies?', ['y', 'n'], {'y': 5, 'n': 0}),
]

def get_answer(qa):
    return input('%(q)s --> %(a)s: ' % {'q': qa[0], 'a': '/'.join(qa[1])})

result = 0
max_point = 0
min_point = 0
for qa in QUESTIONS_ANSWERS:
    max_point += max(qa[2].values())
    answer = get_answer(qa)
    while answer not in qa[1]:
        print('Enter a valid answer for the question.')
        answer = get_answer(qa)

    result += qa[2][answer]

print('\n\n')
print('The punctuation for this community at this moment is: {0:.1f}'.format(result*10/max_point))
print('\n\n')
