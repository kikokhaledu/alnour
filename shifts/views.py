from django.shortcuts import render
from .models import shift_types_table
from products.models import products_table
from inventory.models import finished_products
from suppliers.models import suppliers_table
# Create your views here.

def daily_shift_report(request):
	shift_types = shift_types_table.objects.all()
	all_suppliers = suppliers_table.objects.all()
	products = products_table.objects.all()
	if request.method == 'POST':
		try:
			day = request.POST.get('day')
			date = request.POST.get('date')
			shift_type = request.POST.get('shift_type')
			shift_types_table.objects.create(day = day, date = date, shift_type = shift_type)
		except:
			pass
		###############  add finished porducts #####################
		try:
			for product in products:
				try:
					unit_name = product.name+'number_of_units'
					ton_name = product.name+'tons'
					comment_name = product.name+'comments'
					units = request.POST.get(unit_name)
					tons = request.POST.get(ton_name)
					comments = request.POST.get(comment_name)
					try:
						finished_product_obj = finished_products.objects.get(id = product.id)
						finished_product_obj.number_of_units += units
						finished_product_obj.weight += tons
						finished_product_obj.comment = comments
						finished_product_obj.save()
					except:
						finished_products.objects.create(number_of_units = units ,weight=tons,comment =comments)
				except:
					pass
		except:
			pass
		############################################################
		# try:
		# 	supplier = request.POST.get('supplier')
		# 	batch = request.POST.get('batch')
		# 	loader_expense = request.POST.get('loader_expense')
		# 	paied_ammount = request.POST.get('paied_ammount')
		# 	pending_ammount = request.POST.get('pending_ammount')
		# 	comment = request.POST.get('comments')
		# 	try:
		# 		supplied_product=supplier.raw_material.name
				

	context = {
	'shift_types':shift_types,
	'products':products,
	'all_suppliers':all_suppliers,
	}
	return render (request,'shifts/daily_shift_report.html',context)



