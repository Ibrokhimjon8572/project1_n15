from django.shortcuts import render
from .models import Profile

# olma, OlMa,olMA
def profiles(request):
    print(request)
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    profiles = Profile.objects.filter(name__icontains=search_query)
    context = {'profiles':profiles, 'search_query':search_query}
    return render(request, 'profile/profiles.html', context)


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skill = profile.skill_set.exclude(description__exact="")
    another_skill = profile.skill_set.filter(description__exact="")
    context = {'profile':profile, 'top_skill':top_skill, 'another_skill':another_skill}
    return render(request, 'profile/profile.html', context)
