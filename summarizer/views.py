from django.shortcuts import render,redirect
from .forms import SummaryForm
def test(request):
    return render(request,'summarizer/home.html')

from django.conf import settings
from huggingface_hub import InferenceClient
from .forms import SummaryForm

def summary_view(request):
    if request.method == "POST":
        form = SummaryForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']

            client = InferenceClient(api_key=settings.HUGGINGFACE_API_KEY)
            result = client.summarization(text, model="facebook/bart-large-cnn")
            summary = result["summary_text"]

            request.session["summary"] = summary   # store temporarily
            return redirect("sum")  

    else:
        summary = request.session.pop("summary", None)
        form = SummaryForm(initial={'text': summary} if summary else None)

    return render(request, "summarizer/home.html", {"form": form})

                 