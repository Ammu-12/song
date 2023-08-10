from django.shortcuts import render,redirect
from .models import Song
from .forms import SongForm
# Create your views here.
def index(request):
    song = Song.objects.all()
    context={
        'song_list':song
    }
    return render(request,'index.html', context)
def detail(request,song_id):
    songs=Song.objects.get(id=song_id)
    return render(request,"details.html",{'song':songs})
def add_song(request):
    if request.method=='POST':
        sname=request.POST.get('sname')
        flyric=request.POST.get('flyric')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        song=Song(sname=sname,flyric=flyric,desc=desc,year=year,img=img)
        song.save()
    return render(request,'add.html')

def update(request,id):
    song=Song.objects.get(id=id)
    form=SongForm(request.POST or None,request.FILES,instance=song)
    if form. is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'song':song})
def delete(request,id):
    if request.method=='POST':
        song = Song.objects.get(id=id)
        song.delete()
        return redirect('/')
    return render(request, 'delete.html')