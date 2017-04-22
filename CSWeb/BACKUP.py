# BACKUP FOR MANUAL MERGE. OLD CONTENTS HERE #

import dota2api
import django
from nested_lookup import nested_lookup
django.setup()
from CSWeb import settings
from django.db import models

import tether

#settings.configure()

# END API INIT IMPORTS

# BEGIN SERIALIZATION IMPORTS (EXP. 2-6)


api = dota2api.Initialise("BFF23F667B3B31FD01663D230DF11C25")
#hist = api.get_match_history(account_id=tether.models.UserProfile.objects.values('steam_id')) #steam id queryset
summary = api.get_player_summaries(90453354)
#match_ini = api.get_match_details(match_id=2550699169)
#ini2 = api.get_match_details(match_id=2550699169)  # copying the match_ini dictionary does not work, for unknown reason.
#pool = api.get_tournament_prize_pool(leagueid=4664)
#match_ini['radiant_win']

#----- Save pool to DB -----#
#p = leagues.models.PrizePool(**pool)
#p.save()
#----- End pool save -----#



#print(match_ini)
'''
print (summary)
print(hist)
'''

'''
#----- remove extraneous data -----#
if 'picks_bans' in match_ini:
    del match_ini['picks_bans']
    del ini2['picks_bans']


if 'ability_upgrades' in hist:
    del match_ini['ability_upgrades']
    del ini2['ability_upgrades']

if 'ability_upgrades' in match_ini:
    del match_ini['ability_upgrades']
    del ini2['ability_upgrades']
#----- end remove -----#
'''
'''
#----- Grab all match ids for hist call -----#
def get_match_hist():
    api = dota2api.Initialise("BFF23F667B3B31FD01663D230DF11C25")
    hist = api.get_match_history(account_id=tether.models.UserProfile.objects.values('steam_id'))  # steam id queryset
    #match_list = {}
    match_list = hist

    #nested_lookup('match_id', recent_matches)
    ids = nested_lookup('match_id', match_list) #return in list all ids and dates
    s_time = nested_lookup('start_time', match_list)


    match_list = dict(zip(s_time, ids)) #zip ids and dates into dict

    num_matches = range(100)
    match_incre = []
    for i in num_matches:
        match_incre.append('Match ' + str(i))

    recent_matches = dict(zip(ids, match_incre))
    print(recent_matches)

    for k, v in recent_matches.items():
        kv = {k, v}
        k = [str(k)]
        v = [str(v)]
        matches = dict(zip(k, v))
        new_entry = tether.models.RecentMatches(match_id=k, match_num=v)
        new_entry.save()
    print(matches)
    # ----- End match hist -----#
get_match_hist()
'''
#--- New recent matches attempt ---#
class History():
    '''
    def get_profile_match_hist(self):
        api = dota2api.Initialise("BFF23F667B3B31FD01663D230DF11C25")
        hist = api.get_match_history(account_id=tether.models.UserProfile.objects.values('steam_id'))  # steam id queryset
        match_list2 = hist

        # nested_lookup('match_id', recent_matches)
        ids = nested_lookup('match_id', match_list2)  # return in list all ids and dates
        s_time = nested_lookup('start_time', match_list2)

        match_list = dict(zip(s_time, ids))  # zip ids and dates into dict
        num_ids = range(4)
        num_matches2 = range(5)
        match_incre2 = []

        for i in num_matches2:
            match_incre2.append('id_match' + str(i))
        match_ids = ids[:5]
        recent_matches2 = dict(zip(match_incre2, match_ids))


        matches = {str(k): str(v) for k, v in recent_matches2.items()}

        print(matches)
        new_entry = tether.models.NewRecentMatches1(**matches)
        new_entry.save()
    #get_profile_match_hist()
    #--- end ---#
    '''
class PlayersAndData(History):
    #----- Set up for match players -----#
    #def get_match_players(self):
    def get_match_players(self):
        api = dota2api.Initialise("BFF23F667B3B31FD01663D230DF11C25")
        match_ini = api.get_match_details(match_id=3043374938)#tether.models.NewRecentMatches.objects.values.id_match0(3037647418))
        ini2 = api.get_match_details(match_id=3043374938)  #tether.models.NewRecentMatches.objects.values.id_match0(3037647418))
        hist = api.get_match_history(account_id=tether.models.UserProfile1.objects.values('steam_id'))  # steam id queryset

        # ----- remove extraneous data -----#
        if 'picks_bans' in match_ini:
            del match_ini['picks_bans']
            del ini2['picks_bans']

        if 'ability_upgrades' in hist:
            del match_ini['ability_upgrades']
            del ini2['ability_upgrades']

        if 'ability_upgrades' in match_ini:
            del match_ini['ability_upgrades']
            del ini2['ability_upgrades']
        # ----- end remove -----#

        self.match_plrs = {}
        self.match_plrs = match_ini.pop("players")

        match_plrs_id = {}
        temp = {}

    #----- End set up -----#

    #*****CONVERT TO LOOP
        temp = self.match_plrs[0]
        temp = temp.pop("account_id")
        match_plrs_id['player0_id'] = temp

        temp = self.match_plrs[1]
        temp = temp.pop("account_id")
        match_plrs_id['p1ayer1_id'] = temp

        temp = self.match_plrs[2]
        temp = temp.pop("account_id")
        match_plrs_id['p1ayer2_id'] = temp

        temp = self.match_plrs[3]
        temp = temp.pop("account_id")
        match_plrs_id['p1ayer3_id'] = temp

        temp = self.match_plrs[4]
        temp = temp.pop("account_id")
        match_plrs_id['p1ayer4_id'] = temp

        temp = self.match_plrs[5]
        temp = temp.pop("account_id")
        match_plrs_id['p1ayer5_id'] = temp

        temp = self.match_plrs[6]
        temp = temp.pop("account_id")
        match_plrs_id['p1ayer6_id'] = temp

        temp = self.match_plrs[7]
        temp = temp.pop("account_id")
        match_plrs_id['p1ayer7_id'] = temp

        temp = self.match_plrs[8]
        temp = temp.pop("account_id")
        match_plrs_id['p1ayer8_id'] = temp

        temp = self.match_plrs[9]
        temp = temp.pop("account_id")
        match_plrs_id['p1ayer9_id'] = temp

    #*************** END "LOOP" *******************************

        p_entry = tether.models.MatchPlayers(**match_plrs_id)
        p_entry.save()

        #p_entry.players.add(self.new_entry)
        #return self.match_plrs
        return p_entry
    #get_match_players()
    #----- Save match details / separate players and player details to sep table -----#

    def get_profile_match_hist(self):

        api = dota2api.Initialise("BFF23F667B3B31FD01663D230DF11C25")
        hist = api.get_match_history(account_id=tether.models.UserProfile1.objects.values('steam_id'))  # steam id queryset
        match_list2 = hist

        # nested_lookup('match_id', recent_matches)
        ids = nested_lookup('match_id', match_list2)  # return in list all ids and dates
        s_time = nested_lookup('start_time', match_list2)

        match_list = dict(zip(s_time, ids))  # zip ids and dates into dict
        num_ids = range(4)
        num_matches2 = range(5)
        match_incre2 = []

        for i in num_matches2:
            match_incre2.append('id_match' + str(i))
        match_ids = ids[:5]
        recent_matches2 = dict(zip(match_incre2, match_ids))


        matches = {str(k): str(v) for k, v in recent_matches2.items()}

        print(matches)
        new_entry = tether.models.NewRecentMatches1(**matches)
        #new_entry = p_entry.players.create(tether.models.NewRecentMatches(**matches))
        new_entry.save()
        '''
        prof = tether.models.UserProfile.objects.values_list('steam_id', flat=True).get(pk=1)
        prof.save()

        prof.recent_matches.add(new_entry)
        '''
        prof_id = tether.models.UserProfile1.objects.get(steam_id='101869174')
        prof_id.save()
        prof = tether.models.Profiles_Matches(profile_id=prof_id, match_id=new_entry)
        prof.save()
        plrs = self.get_match_players()

        PIM = tether.models.PlayersInMatch(players_id=plrs, match_id=new_entry)
        PIM.save()
        #new_entry.players.add(plrs)
        #plrs.p_entry.players.add(new_entry)


    #get_profile_match_hist()

    #--- end ---#

    def get_all_data(self):

        plrs_match_data = {}

        for account_id in self.match_plrs:
            if account_id in self.match_plrs and self.match_plrs != 0:
                plrs_match_data = self.match_plrs[1]   # grabs the account id from the player data at the top of the stack
                del self.match_plrs[1]               # define function to loop through all players,


                                         # OR define function to find the current users steam ID, and pull his data.

        if 'ability_upgrades' in plrs_match_data:
            del plrs_match_data['ability_upgrades']
        print(self.match_plrs)
        print(plrs_match_data)
        match_data_entry = tether.models.MatchData(**plrs_match_data)
        match_data_entry.save()

    #----- End match details -----#
    #get_all_data()


#----- Split common GD -----#

    def get_common_d(self):
        match_ini = api.get_match_details(match_id=3043374938)
        wanted = set(match_ini) - {'game_mode_name', 'human_players', 'match_id', 'game_mode', 'duration', 'lobby_type', 'lobby_name', 'engine', 'start_time', 'cluster'}
        common_gd = match_ini
        for unwanted_key in wanted:
            del common_gd[unwanted_key]

        {'match_id': str(k) for k, v in common_gd.items()}
        cd = tether.models.CommonData(**common_gd)
        cd.save()
        print(common_gd)
    #get_common_d()

    def get_dota_d(self):
        ini2 = api.get_match_details(match_id=3043374938) #tether.models.NewRecentMatches.objects.values('id_match0'))  # copying the match_ini dictionary does not work, for unknown reason.
        wanted2 = set(ini2) - {'match_id', 'leagueid', 'tower_status_radiant', 'first_blood_time', 'positive_votes', 'radiant_win', 'tower_status_dire', 'dire_score', 'pre_game_duration', 'flags', 'cluster_name', 'radiant_score', 'barracks_status_radiant', 'match_seq_num', 'barracks_status_dire', 'negative_votes'}
        dota2gd = ini2
        for unwanted_key in wanted2:
            del dota2gd[unwanted_key]

        {'match_id': str(k) for k, v in dota2gd.items()}


        dotad = tether.models.DotaData(**dota2gd)
        dotad.save()

        print(dota2gd)
    #get_dota_d()
r = PlayersAndData()
r.get_match_players()
r.get_profile_match_hist()
r.get_all_data()
r.get_common_d()
r.get_dota_d()


#print(match_ini)

#print(match_plrs)

#print(temp)

#print(match_plrs_id)

#print(plrs_match_data)

# **TO DO:
#   MAKE NEW DICTIONARY MODEL TABLES
#   ADD DICT.SAVES
#   MAKE THIS THING A PRESENTABLE SET OF FUNCTIONS
#   PUT THE PLAYER ID FUNCTION IN A LOOP
#   CRY


'''
picks_bans = match.get('picks_bans', None)
print(picks_bans)
'''
##############################################################
