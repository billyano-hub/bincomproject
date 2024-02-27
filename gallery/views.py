from django.http import HttpResponse,Http404
from django.shortcuts import render, get_list_or_404
from . models import Pictures,Track,Video,Genre
# Create your views here.
def index(request):
    pictures=Pictures.objects.all()
    tracks=Track.objects.all()
    videos=Video.objects.all()
    return render(request,'gallery/index.html',{'Pictures':pictures,'Tracks':tracks,'Videos':videos})

def detail(request, picture_id):
    try:
        picture = Pictures.objects.get(pk=picture_id)
        
        return render(request, 'gallery/picture_detail.html', {'picture': picture})
    except Pictures.DoesNotExist:
        raise Http404("Picture not found")

def detailone(request,track_id):
    try:
        track = Track.objects.get(pk=track_id)
        return render(request, 'gallery/track_detail.html', {'track':track})
    except Track.DoesNotExist:
        raise Http404("Track not found")
    
def detailtwo(request, video_id):
    try:
        video=Video.objects.get(pk=video_id)
        return render(request, 'gallery/video_detail.html', {'video':video})
    except Video.DoesNotExist:
        raise Http404("Video not found")


