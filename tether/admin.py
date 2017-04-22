from django.contrib import admin
from tether.models import UserProfile1, League #RecentMatches


class LeagueAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('league_name',)}

admin.site.register(UserProfile1)
admin.site.register(League, LeagueAdmin)
#admin.site.register(RecentMatches)
