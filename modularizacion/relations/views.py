from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction, IntegrityError
from .models import Article, Reporter, Page, Publication

# Create your views here.
def create(request):
	reporter = Reporter(first_name="Hector", last_name="Valdez", email="hector@gmail.com")
	reporter.save()

	article1 = Article(headline="Noticia del año", reporter=reporter)
	article2 = Article(headline="Apalapapa 2023", reporter=reporter)
	article3 = Article(headline="Todo lo bueno del 2023", reporter=reporter)

	article1.save()
	article2.save()
	article3.save()

	result = article1.reporter.email
	return HttpResponse(result)


def reporter(request):
	reporter = Reporter.objects.get(id=1)
	result = reporter.article_set.count()
	print(result)
	return HttpResponse(result)

@transaction.atomic()
def createmany(request):
    try:
        publication1 = Publication(title='La mejor publicación')
        publication2 = Publication(title='Otra publicacion')
        publication3 = Publication(title='God of wardo')
        publication4 = Publication(title='Nasheee')

        publication1.save()
        publication2.save()
        publication3.save()
        publication4.save()

        page1 = Page(headline="Pagina de momos")
        page2 = Page(headline="Pagina de kokos")
        
        page1.save()
        page2.save()
        
        # Relacionar
        page1.publications.add(publication1)
        page1.publications.add(publication3)
        page1.publications.add(publication4)

        page2.publications.add(publication2)
        page2.publications.add(publication4)
        result = page1.publications.all()
        return HttpResponse(result)
    except IntegrityError:
        return HttpResponse('Error al crear')

def page(request):
	# publication = Publication.objects.get(id=1)
	# result = publication.page_set.all()
	
	pageinfo = Page.objects.get(id=2)
	result = pageinfo.publications.all()
	pageinfo.publications.remove(result[0])
	return HttpResponse(pageinfo.publications.all())