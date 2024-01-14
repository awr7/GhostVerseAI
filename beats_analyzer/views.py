import librosa
from django.shortcuts import render
from .forms import BeatUploadForm
from .models import Beat

# Create your views here.
def home(request):
    form = BeatUploadForm()
    return render(request, 'index.html', {'form': form})

def upload_beat(request):
    if request.method == 'POST':
        form = BeatUploadForm(request.POST, request.FILES)
        if form.is_valid():
            beat_instance = Beat(file=request.FILES['file'])
            beat_instance.save()

            y, sr = librosa.load(beat_instance.file.path, sr=None)
            tempo,_ = librosa.beat.beat_track(y=y, sr=sr)
            form.fields['is_submitted'].initial = True
            return render(request, 'upload_beat.html', {'tempo': tempo})
        else:
            form = BeatUploadForm()
        return render(request, 'upload_beat.html',{'form': form})