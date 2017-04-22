import django_tables2 as tables
from tether import models
from tether.models import League
from django_tables2.utils import A
from django.db.models import Count

class LeagueTable(tables.Table):
    league_name = tables.Column()
    region = tables.Column()
    skill_level = tables.Column()
    password_status = tables.Column()
    players = tables.Column()
    submit_column = tables.LinkColumn('public_league', verbose_name='Join', args=[A('slug')], empty_values=(), text='View', orderable=False)

    class Meta:
        attrs = {'class': 'table table-bordered table-hover'}

class ResultsTable(tables.Table):
    league_name = tables.Column(attrs={'tr': {'bgcolor': 'black'}})
    region = tables.Column()
    skill_level = tables.Column()
    password_status = tables.Column()
    players = tables.Column()
    submit_column = tables.LinkColumn('public_league', verbose_name='Join', args=[A('slug')], empty_values=(), text='View', orderable=False)

    class Meta:
        attrs = {'class': 'table table-bordered table-hover'}

class MatchesTable(tables.Table):
    name = tables.Column()
    player1 = tables.Column()
    player2 = tables.Column()
    player3 = tables.Column()
    player4 = tables.Column()
    player5 = tables.Column()
    player6 = tables.Column()
    player7 = tables.Column()
    player8 = tables.Column()
    player9 = tables.Column()
    player10 = tables.Column()
    winner = tables.Column()

    class Meta:
        attrs = {'class': 'table table-bordered table-hover'}

class MatchTable(tables.Table):
    id_match0 = tables.Column(verbose_name='Match 1')
    id_match1 = tables.Column(verbose_name='Match 2')
    id_match2 = tables.Column(verbose_name='Match 3')
    id_match3 = tables.Column(verbose_name='Match 4')
    id_match4 = tables.Column(verbose_name='Match 5')
    class Meta:
        model = models.NewRecentMatches1
        attrs = {'class': 'table table-bordered table-hover'}
        exclude = ('id',)

class PlayerTable(tables.Table):
    player0_id = tables.Column(verbose_name="Player 1's ID")
    player1_id = tables.Column(verbose_name="Player 2's ID")
    player2_id = tables.Column(verbose_name="Player 3's ID")
    player3_id = tables.Column(verbose_name="Player 4's ID")
    player4_id = tables.Column(verbose_name="Player 5's ID")
    player5_id = tables.Column(verbose_name="Player 6's ID")
    player6_id = tables.Column(verbose_name="Player 7's ID")
    player7_id = tables.Column(verbose_name="Player 8's ID")
    player8_id = tables.Column(verbose_name="Player 9's ID")
    player9_id = tables.Column(verbose_name="Player 10s ID")

    class Meta:
        model = models.MatchPlayers
        attrs = {'class': 'table table-bordered table-hover'}
        exclude = ('id', )


class PlayerData(tables.Table):

    item_0_name = tables.Column(verbose_name='Item 1')
    item_1_name = tables.Column(verbose_name='Item 2')
    item_2_name = tables.Column(verbose_name='Item 3')
    item_3_name = tables.Column(verbose_name='Item 4')
    item_4_name = tables.Column(verbose_name='Item 5')
    item_5_name = tables.Column(verbose_name='Item 6')
    class Meta:
        model = models.MatchData
        attrs = {'class': 'table table-bordered table-hover'}
        exclude = ('id', 'hero_id', 'item_0', 'item_1', 'item_2', 'item_3',
                   'item_4', 'item_5', 'item_6', 'leaver_status', 'hero_id',
                   'scaled_tower_damage', 'leaver_status_name', 'player_slot',
                   'scaled_hero_healing', 'scaled_hero_damage', 'backpack_0',
                   'backpack_1', 'backpack_2', )

        sequence = ('hero_name', 'level', 'kills', 'deaths', 'assists', 'last_hits',
                    'denies', 'gold', 'xp_per_min', 'gold_per_min', 'item_0_name', 'item_1_name',
                    'item_2_name', 'item_3_name', 'item_4_name', 'item_5_name', )