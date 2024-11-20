# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from datetime import datetime
# from myApp.models import Article, Publication, Reporter
# from datetime import datetime
# import json

# # Create your views here.

# # def index(request):
# #     if request.method == 'GET':
# #         return render(request, "index.html")
    
# # def tmp(request):
# #     if request.method == 'GET':
# #         items = ['apple', 'kiwi', 'grape', 'blueberry']
# #         context = {
# #             'user_name': 'Alice',  # 사용자 이름
# #             'is_logged_in': True,  # 로그인 상태
# #             'items': items,  # 리스트 데이터
# #             'today': datetime.now()  # 현재 날짜
# #         }
# #         return render(request, "tmp.html", context)
    
# # def create(request):
# #     if request.method == 'POST':
# #         headline = request.POST.get('headline')
# #         Article.objects.create(pub_date=datetime.now(),
# #                                headline=headline, 
# #                                reporter_id=2)

# #         return HttpResponse('successfully created', status=201)
# #     else:
# #         return HttpResponse('error', status=400)

# # def read(request):
# #     if request.method == 'GET':
# #         data = Article.objects.all()

# #         article_data = []
# #         for a in data:
# #             article_data.append({
# #                 'id': a.id,
# #                 'headline': a.headline,
# #                 'reporter_id' : a.reporter.id ,
# #                 'date': a.pub_date,
# #             })

# #         return JsonResponse(article_data, safe=False)
# #     else:
# #         return HttpResponse('error', status=400)

# # def update(request, article_id):
# #     if request.method == 'PUT':
# #         try:
# #             a = Article.objects.get(id=article_id)
# #             # PUT 요청에서 JSON 데이터를 처리할 때는 request.body를 사용하여 데이터를 가져온 뒤 json.loads()로 파싱
# #             # request.body 는 바이너리 형태(byte) 로 전달되기 때문에 이를 처리하기 위해서는 json 으로 바꿔주는 작업을 거쳐야 함
# #             a.headline = json.loads(request.body).get('headline')
# #             a.save()
            
# #             return HttpResponse("successfully updated", status=200)
# #         except Article.DoesNotExist:
# #             return HttpResponse('article does not exist', status=400)
    
# #     elif request.method == 'POST':
# #         try:
# #             a = Article.objects.get(id=article_id)
# #             a.headline = request.POST.get('headline')
# #             a.save()
            
# #             return HttpResponse('successfully updated', status=200)
# #         except Article.DoesNotExist:
# #             return HttpResponse('article does not exist', status=400)
        
# #     else:
# #         return HttpResponse('incorrect approach', status=400)

# # def delete(request, article_id):
# #     if request.method == 'DELETE':
# #         Article.objects.get(id=article_id).delete()
# #         return HttpResponse('Successfully deleted', status=200)
# #     else:
# #         return HttpResponse('error', status=400)
        