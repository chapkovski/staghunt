# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants
from django.utils import timezone

def preselection(player):
    if player.poverty!=None:
        return player.poverty
    else:
        return True

def vars_for_all_templates(self):

    return {'eligible': preselection(self.player)}



class Hunting(Page):
    form_model=models.Player
    def get_form_fields(self):
        return ["decision"]

    def is_displayed(self):
        # self.player.hunting_start_time = timezone.now()
        return preselection(self.player) and self.player.hunting_time_left()
    #


    def vars_for_template(self):

        return {'player_index': self.player.id_in_group,
                'stag_stag': Constants.stag_stag_amount,
                'stag_hare': Constants.stag_hare_amount,
                'hare_stag': Constants.hare_stag_amount,
                'hare_hare': Constants.hare_hare_amount,
                "time_left": self.player.hunting_time_left(),
                }

class Welcome(Page):
    def vars_for_template(self):
        return {'nq': 10,
                'lb': c(1),
                'ub': c(2),
                # "time_limit": int(Constants.round_1_seconds / 60),
               }



class PreselectionQuestionnaire(Page):
    form_model=models.Player
    def get_form_fields(self):
        return ["age",
                "gender",
                "education",
                "income",
                "poverty",
                "race",
                "childen",
                "state",
                ]

class ThankYou(Page):
    def before_next_page(self):
        self.player.priming_start_time= timezone.now()


class Priming(Page):
    def is_displayed(self):
        return preselection(self.player) and self.player.priming_time_left()

    def vars_for_template(self):
        self.player.priming_start_time = timezone.now()
        if self.player.treatment:
            tr_text=["$2.500","$230","$2.800"]
        else:
            tr_text=["$150","$15","$180"]
        return {'tr_text': tr_text, "time_left": self.player.priming_time_left(),}


class Instructions1(Page):
    def is_displayed(self):
        return preselection(self.player)
class Instructions2(Page):
    def is_displayed(self):
        return preselection(self.player)


class Waiting1(Page):
    template_name = 'stag_hunt/WaitingPage.html'
    timeout_seconds = Constants.waiting_partner_time
    text="Please wait until the other MTurker has joined the hunting task…."
    def vars_for_template(self):
        return {'text': self.text}
    def is_displayed(self):
        return preselection(self.player)


class PartnerJoined(Page):
    def is_displayed(self):
        return preselection(self.player)
    def before_next_page(self):
        self.player.hunting_start_time= timezone.now()

class QuestionnaireAnnouncement(Page):
    def is_displayed(self):
        return preselection(self.player)
    def vars_for_template(self):

        return {'nq': 5,
                'bonus_earnings':c(2),
                'stag':True if self.player.decision=="Stag" else False}
class PostQuestionnaire1(Page):
    form_model = models.Player
    def get_form_fields(self):
        return ["remember_sum",
                "stress_sum",
                "touch",
                "loan",
                "friends",
                ]

    def vars_for_template(self):
        return {'nq_remaining':2,}

    def is_displayed(self):
        return preselection(self.player)

class PostQuestionnaire2(Page):
    form_model = models.Player
    def get_form_fields(self):
        return [
                "risks",
                "paid_tomorrow",
                ]
    def is_displayed(self):
        return preselection(self.player)
class FinalPage(Page):
    def is_displayed(self):
        return preselection(self.player)
    form_model = models.Player
    def get_form_fields(self):
        return [
                "while_waiting",
                "understand",
                "letknow",
                ]


page_sequence = [Welcome,
                PreselectionQuestionnaire,
                ThankYou,
                Priming,
                Instructions1,
                Instructions2,
                Waiting1,
                PartnerJoined,
                Hunting,
                QuestionnaireAnnouncement,
                PostQuestionnaire1,
                PostQuestionnaire2,
                FinalPage,
            ]
