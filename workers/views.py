from django.shortcuts import render
from . models import workers,drivers
from django.http import HttpResponse

########################################weekly employment form##############################################
def weekly_employment_form(request):
	all_workers = workers.objects.all()

	if request.method == 'POST':
		print('===============================')
		print(request.data)
		print('===============================')
	context = {
	'all_workers':all_workers,
	}
	return render (request,'workers/weekly_employment_form.html',context)


def get_worker_pay_value(request,id):
	woker = workers.objects.get(id = id )
	pay_value = woker.pay_ammount_per_shift
	return HttpResponse (pay_value)