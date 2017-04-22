from tether.models import UserProfile1, League
from django.contrib.auth.models import User
from django import forms


# The form for user profiles


class UserForm(forms.ModelForm):
    # Keeps the password hidden while typing
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-md'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-md'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-md'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


# Additional form for more attributes to user profile.
class UserProfileForm(forms.ModelForm):
    region = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-md'}))
    steam_id = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-md'}))

    class Meta:
        model = UserProfile1
        fields = ('region', 'steam_id')


class LeagueForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = League
        fields = ('league_name', 'region', 'skill_level', 'password', 'slug')


class MatchPlayersForm(forms.Form):
    PlayersChoices = (
        ('MATCH0', 'Get Players for Match 0'),
        ('MATCH1', 'Get Players for Match 1'),
        ('MATCH2', 'Get Players for Match 2'),
        ('MATCH3', 'Get Players for Match 3'),
        ('MATCH4', 'Get Players for Match 4'),
    )
    DataChoices = (
        ('PLAYER0', 'Get Data for Player 0'),
        ('PLAYER1', 'Get Data for Player 1'),
        ('PLAYER2', 'Get Data for Player 2'),
        ('PLAYER3', 'Get Data for Player 3'),
        ('PLAYER4', 'Get Data for Player 4'),
        ('PLAYER5', 'Get Data for Player 5'),
        ('PLAYER6', 'Get Data for Player 6'),
        ('PLAYER7', 'Get Data for Player 7'),
        ('PLAYER8', 'Get Data for Player 8'),
        ('PLAYER9', 'Get Data for Player 9'),
    )
    Players = forms.ChoiceField(initial='MATCH0', choices=PlayersChoices, required=False)
    Data = forms.ChoiceField(initial='PLAYER0', choices=DataChoices, required=False)

class PlayerDataForm(forms.Form):

    #DataChoices = (
        ('PLAYER0', 'Get Data for Player 0'),
        ('PLAYER1', 'Get Data for Player 1'),
        ('PLAYER2', 'Get Data for Player 2'),
        ('PLAYER3', 'Get Data for Player 3'),
        ('PLAYER4', 'Get Data for Player 4'),
        ('PLAYER5', 'Get Data for Player 5'),
        ('PLAYER6', 'Get Data for Player 6'),
        ('PLAYER7', 'Get Data for Player 7'),
        ('PLAYER8', 'Get Data for Player 8'),
        ('PLAYER9', 'Get Data for Player 9'),
    #)
    #playerdata = forms.ChoiceField(initial='PLAYER0', choices=DataChoices, required=False)

