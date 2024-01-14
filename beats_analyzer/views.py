import librosa
from madmom.features.key import CNNKeyRecognitionProcessor, key_prediction_to_label
from django.shortcuts import render
from .forms import BeatUploadForm


# Create your views here.
def home(request):
    form = BeatUploadForm()
    return render(request, 'index.html', {'form': form})

def upload_beat(request):
    if request.method == 'POST':
        form = BeatUploadForm(request.POST, request.FILES)
        if form.is_valid():    
            uploaded_file = request.FILES['file']
            y, sr = librosa.load(uploaded_file, sr=None)
            tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
            duration = librosa.get_duration(y=y, sr=sr)
            key_processor = CNNKeyRecognitionProcessor()
            key_prediction = key_processor(uploaded_file.temporary_file_path())
            key = key_prediction_to_label(key_prediction)

            analysis_results = {
                'tempo': tempo,
                'duration': duration,
                'key': key,
            }

            return render(request, 'upload_beat.html', analysis_results)
        else:
            form = BeatUploadForm()
    else:
        form = BeatUploadForm()

    return render(request, 'upload_beat.html', {'form': form})