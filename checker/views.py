from django.shortcuts import render
# from pros import do_something
import grammar_check

# Create your views here.
def check(request):
	return render(request, 'index.html')

def output_text(request):
	if request.method == 'GET':
		name= request.GET.get('q')
		tool = grammar_check.LanguageTool('en-GB')
		texts = name
		matches = tool.check(texts)
		name = grammar_check.correct(texts,matches)
		return render(request, 'index2.html', {'result': name})