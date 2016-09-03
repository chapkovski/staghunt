# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants


def vars_for_all_templates(self):

    return {'total_q': 1,
            'total_rounds': Constants.num_rounds,
            'round_number': self.subsession.round_number}



class Hunting(Page):
    timeout_seconds = 90
    def is_displayed(self):
        if self.player.decision == 'Stag' and self.player.other_player().decision == 'Stag':
            return True
        else:
            return False

    # form_model = models.Player
    # form_fields = ['decision']


    def vars_for_template(self):
        return {'player_index': self.player.id_in_group,
                'stag_stag': Constants.stag_stag_amount,
                'stag_hare': Constants.stag_hare_amount,
                'hare_stag': Constants.hare_stag_amount,
                'hare_hare': Constants.hare_hare_amount}

    def before_next_page(self):
        if self.timeout_happened:
            self.player.decision = 'Stag'
        else:
            self.player.decision = 'Hare'



class Welcome(Page):
    pass
class PreselectionQuestionnaire(Page):
    pass
class ThankYou(Page):
    pass
class Priming(Page):
    pass
class Instructions1(Page):
    pass
class Instructions2(Page):
    pass
class Waiting1(Page):
    pass
class PartnerJoined(Page):
    pass
class QuestionnaireAnnouncement(Page):
    pass
class PostQuestionnaire1(Page):
    pass
class PostQuestionnaire2(Page):
    pass
class FinalPage(Page):
    pass

page_sequence = [
            Welcome,
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
