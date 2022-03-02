system main inputs 

the system will work on 12  hour bases  for shifts 

each shift will have the following at the end 

##############################################shift report##############################################

# inputs
Date time filed   Auto by default  but still can be edited 
#################################################################

##############################################5 sections############################################## 

 section 1 

 prduction details:

 product type select feild (TDF,1-4mm,)



 ############## products table#######
 name : char
 unit : select ( pack  ,  cart )
 weight : float
 min ammount 
#####################################


############### suppliers############

name: char 
acc_deliveries in kg  < tons
pending_payments
paied_ammounts
deducted ammonunts
number of rejected deliverie
datetime filed  for each time they delvier a shipment
phone number 
extra information text 
######################################

######################### clients table  ##################
name 
ammountin tons since i started working with him 
address of HQ
address of shipment default but can be edited




oreder_id for PO unique forigen key




####################### PO ########################

name 
client  forign key
client address value from key
shipment address value from key
invoice number  auto generated  (there will be no po number an in that case it will  not  be subjecct to taxes )
invoice date : current date no time 
PO  number Char
invoice period 
due date  date field  will alert me when there is a payment this week  in the upcoming payments tab
invoice period    two dates  from a date picker  start and end 


###################invoice################# 
ITEM
DESCRIPTION
unit price 
quantity
subtotal 
item total float
VAT default 14% edit 
CIT default -1% edit 
total null unitl populated
tax Reg No : default 618-665-959
CR No : default 160612 
po as a forign key 


bank info: text field defailts to 
"
National Bank OF EGYPT 
account number 6433171331027301011
account branch : Merag City Branch 
IBAN : EG 250003064331713310273010110"


footer of the invoice 

info@alnourrrubber.com
+0201100671510
+0201000380435

address
###################### users ####################
level 2
name
email 
phone number 
is admin
is auditor will only see the inventory and can fill the daily shift  form 
##################### 

####################### drivers #############################
name 
licence number
number of shipments auto
phone nubmer 
######################################### 
##########################orders table #####################
client name
order number auto client name + number
date placed
total capacity  for ex 20 tons  in total 
pending ammount 
product check in inventory  if not in in ventory  we will take the available ammount and will add the rest in pending ammount  
price_per_ton
status (pending,completed) boolean
########################shipments###############################
date
issuer name  defaults to company name 
client key  can be null 
additional_product (optional) to Null
order forigen key  can be null 
ammount_kg_to_tons  threshold is the order total cap ammount 
driver
car plates number
notes: text null
attestment: text notnull dfault = text sent from omar
text for client not null  default = text sent from omar
#################################################################



								################### TDF ###########################
same as the rubber but it will not be based on orders so make the ammendments 
########################shipments###############################
date
issuer name  defaults to company name 
client key  can be null 
courrier name 
ammount_kg_to_tons 
notes: text null
attestment: text notnull dfault = text sent from omar
text for client not null  default = text sent from omar
invoice  same  no order 
po same no order 
oncreate  will add a record  in loaders   ton  =20 

###################################################

###################wire############################
every  1 ton   produces  220 KG wire 
########################shipments###############################
date
issuer name  defaults to company name 
client key  can be null 
courrier name 
ammount_kg_to_tons 
notes: text null
attestment: text notnull dfault = text sent from omar
text for client not null  default = text sent from omar
invoice  same  no order 
po same no order 
oncreate  will add a record  in loaders   for 250 egp 

###################################################



section 2 : 
inventory

raw materials :
#####################batch#########################
penalty  float  default = 0 
weight float 
price per ton 
total price  float 
supplier  fk 
date 
shift 
checkbox loader or not  default  True 
comment 
###################################################
total raw material will be deducted from when we make a product 
name 
weight
##########################inventory of finished products:###############################3
name fk
number of packs  or carts 
weight
###################################################


############################# items################
item  which are all products in the products table created with the product 
all null  and will be updated when i submit the daily shift report 
ammount in stock
###################################################
##########################################workers##################
id number 
phone number 
name 
hire date auto today
how many shifts 
pay ammount per shift default 150 
bouns 
down payments solfa  
deductions 
net 
shift type fk 
function shift report for workers 


will have a list of all available workers and you can choose from them who worked on that day you will do that every
day so that at the end of the week you can tell how much they will get 
tab will have all the employee names and how much will they get paid per week 
########################################worker payments #############################################
worker 
payment ammount
date  auto  
###################################shifts type #######################
name  day or night 
############################

##################################expenses category 
name 
update per number of days 
alrm on  ammount 
################################ expenses  over heads ####################
category fk
ammount
description
function 
threshhold expenses limit will send an email  and show a notfication  
################################ loader  expenses ####################  
pay_ammount 
type  load  or unload  true false 
date time  auto 
######################################################################

##############################shift reports archive###################
date time 
products  many = True 
ammount  
#############################factory production total################
per shift   ,  day or night 
ammount  
total ammount for both shifts 

