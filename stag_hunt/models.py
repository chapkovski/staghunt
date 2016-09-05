# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
import random
from otree.common import Currency as c, currency_range
# </standard imports>
import django.forms.extras.widgets

#to delete block below
from jsonfield import JSONField
from otree.db import models
import otree.models
import otree.constants
from otree import widgets
from otree import forms
from otree.common import Currency as c, currency_range
import random
from django.core.validators import MaxLengthValidator
#end of deleting block


doc = """
This is a 2-player 2-strategy coordination game. The original story was from
<a href="https://en.wikipedia.org/wiki/Jean-Jacques_Rousseau" target="_blank">
    Jean-Jacques Rousseau
</a>.
"""

bibliography = (
    (
        'Skyrms, Brian. "The stag hunt." Proceedings and Addresses of the '
        'American Philosophical Association. American Philosophical '
        'Association, 2001.'
    ),
    (
        'Battalio, Raymond, Larry Samuelson, and John Van Huyck. '
        '"Optimization incentives and coordination failure in laboratory stag '
        'hunt games."Econometrica 69.3 (2001): 749-764.'
    )
)


from otree.db import models


class Constants(BaseConstants):
    #dont' forget to delete below
    priming_time, hunting_time = 15,15
    #dont forget to delete above
    name_in_url = 'stag_hunt'
    players_per_group = None
    num_rounds = 1
    waiting_partner=2

#first is the payoff of a player, second - a payoff of another
    stag_stag_amount = c(3)
    stag_hare_amount = c(0)
    hare_stag_amount = c(0.5)
    hare_hare_amount = c(0.5)

    n_questions=10 #for welcome page: number of questions that a player will have to answer in the preselection questinnaire
    lb_earnings=c(10) #lower bound of earnings that they can get int the game
    ub_earnings=c(20) #upper bound of earnings that they can get int the game



class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.treatment = random.choice([True, False])


class Group(BaseGroup):
    pass
#for time experimenting
from django.utils import timezone
#dont forget to delete above later

class Player(BasePlayer):

    #########experimenting with own timer
    hunting_start_time = models.DateTimeField()

    def hunting_time_left(self):
        start = self.hunting_start_time
        now = timezone.now()
        time_left = Constants.round_1_seconds - (now - start).seconds
        return time_left if time_left > 0 else 0
    #end of exper with timer

    treatment=models.BooleanField()
    age = models.IntegerField(
        verbose_name="How old are you?",
    )
    gender = models.CharField(
        verbose_name="Please indicate your sex",
        choices=['Male', 'Female'],
    )

    education = models.IntegerField(
        verbose_name="How many years have you spent in full-time education (school, college, university)",
    )
    income = models.CharField(
        verbose_name="What is currently your annual household income before tax?",
        choices=[   "Currently have no income",
                    "0-10,000$/year",
                    "10,000-20,000$/year",
                    "20,000-30,000$/year",
                    "30,000-40,000$/year",
                    "40,000-60,000$/year",
                    "60,000-100,000$/year" ,
                    "over 100,000$/year",
                ],
    )


    poverty = models.BooleanField(
        verbose_name="During the last month, did you experience any difficulties in paying your regular bills?",
        # choices=['Yes', 'No'],
    )

    race = models.CharField(
        verbose_name="Which categories describe you best? Select all boxes that may apply.",
        choices =  ["White",
                    "Hispanic",
                    "Black or African American",
                    "Asian",
                    "American Indian or Alaska Native",
                    "Middle Eastern or North African" ,
                    "Native Hawaiian or Other Pacific Islander",
                    "Some other race, ethnicity, or origin",
                     ],
        # # widget = forms.CheckboxSelectMultiple,

    )
    childen = models.CharField(
        verbose_name="Do you have children?",
        choices=["no",
                 "yes, 1 child",
                 "yes, 2 children",
                 "yes, 3 children",
                 "yes, 4 children",
                 "yes, 5 children",
                 "yes, 6 children",
                 "yes, 7 children or more",
        ]
    )
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    STATE_CHOICE=[]
    temp = []
    for key, value in states.items():
        temp = [key, value]
        STATE_CHOICE.append(temp)
    state = models.CharField(
        verbose_name="Which state do you currently live in?",
        choices=STATE_CHOICE,

    )
    # passed_the_test=models.BooleanField()
    remember_sum = models.CharField(
        verbose_name="Do you remember the sum required for the treatment?",
        choices=["25$", "100$", "250$", "750$", "1250$", "2000$", "2500$", "3000$"]
    )
    stress_sum = models.CharField(
        verbose_name="The decision would cause me severe financial stress.",
        choices=["Agree fully", "Agree somewhat", "Neither agree nor disagree", "Disagree somewhat", "Fully disagree"]
    )
    touch= models.BooleanField( verbose_name="The decision would require me to touch my savings.")
    loan = models.BooleanField(verbose_name="The decision would require me to take out a loan.")
    friends = models.BooleanField(verbose_name="I would ask my friends or family for financial support.")


    risks = models.CharField(
        verbose_name="How much do you like to take risks?",
        choices=[
            "I like to take risks",
            "I don’t mind taking risks",
            "I am careful not to take too many risks",
            "I do not like to take risks",

        ]
    )


    paid_tomorrow = models.CharField(
        verbose_name="Imagine you could choose to be paid 15$ today, or you could choose to be paid 30$ in two weeks. Which of the following describes best what you feel:",
        choices=[
            "I much prefer to be paid 15$ today",
            "I slightly prefer to be paid 15$ today",
            "I am indifferent whether I am paid 15$ today, or 30$ in two weeks",
            "I slightly prefer to be paid 30$ in two weeks",
            "I much prefer to be paid 30$ in two weeks",
        ]
    )

    while_waiting=   models.CharField(
            verbose_name="In Task 2, what did you do while waiting?",
            choices=[
                "I did something else",
                "I was just waiting",
            ]
        )


    understand=   models.TextField(
        verbose_name="Were there any parts of this study that you found hard to understand?",
        blank=True
    )

    letknow=   models.TextField(
        verbose_name="Is there anything else that you want to let us know?",
        blank=True)

    decision=models.CharField(choices=["Stag","Hare"])


    def set_payoff(self):
        self.payoff = c(1)

