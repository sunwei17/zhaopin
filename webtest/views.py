from django.shortcuts import render,HttpResponse
from django.shortcuts import render

# Create your views here.
from . models import listtwot
def get(request):
    #Student.objects.create(name='哈哈',age=20, _id='哈哈')
    # john = listtwo(name="John Fourkas",age=20, _id='哈哈')
    # john.save()
    xitongjicheng = listtwot.objects.filter()[0:4]
    guanli = listtwot.objects.filter(jobType='IT质量管理/测试/配置管理')[0:4]
    keyan = listtwot.objects.filter(jobType='公务员/事业单位/科研机构')[0:4]
    return render(request, 'zhilian/index.html', {'xitongjicheng': xitongjicheng,'guanli':guanli,'keyan':keyan})
    #return HttpResponse('hello word'+istr)
def getType(request):
    if len(request.GET)>0:
        typename = request.GET['jobtype']
        cc = listtwot.objects.filter(jobTypeName=typename)
    else:
        cc = listtwot.objects.filter()
    #cc = listtwot.objects.filter()
    return render(request, 'zhilian/list.html',{'citydetail_list':cc,'jobtype':typename})
def getList(request):
    jobtype = ''
    if len(request.GET)>1:
        cityname = request.GET['city']
        jobtype = request.GET['jobtype']
        cc = listtwot.objects.filter(city=cityname,jobTypeName=jobtype)
    else:
        cc = listtwot.objects.filter()
    #cc = listtwot.objects.filter()
    return render(request, 'zhilian/list.html',{'citydetail_list':cc,'jobtype':jobtype})