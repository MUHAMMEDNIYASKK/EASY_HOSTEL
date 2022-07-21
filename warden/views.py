from student.models import Login, Hreg,Sreg
from django.template import loader
from django.http import HttpResponse
from .models import book,attendance
from student.models import room
from _datetime import datetime
from django.shortcuts import render
# Create your views here.
def warden_home(request):
    template=loader.get_template("warden_home.html")
    context={}
    return HttpResponse(template.render(context,request))
def w_home(request):
    template=loader.get_template("w_home.html")
    context={}
    return HttpResponse(template.render(context,request))
def addatt(request):
    uname = request.session['uname']
    data = Hreg.objects.get(uname=uname)
    p = data.id
    r = book.objects.raw(
        "select warden_book.id,student_sreg.sfname,student_sreg.sfname,warden_book.Sid,warden_book.bdate,student_hreg.rent from student_sreg,warden_book,student_hreg where student_sreg.id=warden_book.Sid and student_Hreg.id=warden_book.Hid and warden_book.status='approve' and warden_book.Hid=" + str(
            request.session['lid']))
    template = loader.get_template("addatt.html")
    context = {'k': r}
    return HttpResponse(template.render(context, request))


def addatt1(request):
    uname = request.session['uname']
    data = Hreg.objects.get(uname=uname)
    p = data.id
    r = book.objects.raw(
        "select warden_book.id,student_sreg.sfname,student_sreg.sfname,warden_book.Sid,warden_book.bdate,student_hreg.rent from student_sreg,warden_book,student_hreg where student_sreg.id=warden_book.Sid and student_Hreg.id=warden_book.Hid and warden_book.status='approve' and warden_book.Hid=" + str(
            request.session['lid']))
    date=request.POST['d']
    att=request.POST.getlist('att')
    print("======================================")
    print(att)
    for i in r:
        ob=attendance()
        ob.date=date
        ob.stid=i.Sid
        ob.status="0"
        print(i.Sid,type(i.Sid))
        if str(i.Sid) in att:
            ob.status="1"
        ob.save()
    template = loader.get_template("addatt.html")
    context = {'k': r}
    return HttpResponse(template.render(context, request))



def hreg(request):
    if (request.method == "POST"):
        r = Hreg()
        r.hname = request.POST.get("hname")
        r.build_no = request.POST.get("bnumber")
        r.location = request.POST.get("location")
        r.email = request.POST.get("Email")
        r.con = request.POST.get("cnumber")
        r.wname = request.POST.get("wname")
        r.rno = request.POST.get("rooms")
        r.fno = request.POST.get("floors")
        r.rent = request.POST.get("rent")
        r.img = request.FILES['img']
        r.uname = request.POST.get("uname")
        r.type = request.POST.get("ht")
        r.status = 'pending'
        r.save()

        l = Login()
        l.username = request.POST.get("uname")
        l.password = request.POST.get("pass")
        l.utype = 'warden'
        l.save()
        return HttpResponse("<script>alert('registration successfull');window.location='/log'</script>")
    template=loader.get_template("hreg.html")
    context={}
    return HttpResponse(template.render(context,request))
def b_pending(request):
    uname = request.session['uname']
    data = Hreg.objects.get(uname= uname)
    p=data.id
    r=book.objects.raw("select warden_book.id,student_sreg.sfname,warden_book.bdate,student_hreg.rent from student_sreg,warden_book,student_hreg where student_sreg.id=warden_book.Sid and student_Hreg.id=warden_book.Hid and warden_book.status='pending' and warden_book.Hid="+str(request.session['lid']))
    template = loader.get_template("b_pending.html")
    context = {'k': r}
    return HttpResponse(template.render(context, request))
def approve_booking(request,id):
    r = book.objects.get(id=id)
    r.status ='approve'
    r.save()
    r = book.objects.raw(
        "select warden_book.id,student_sreg.sfname,warden_book.bdate,student_hreg.rent from student_sreg,warden_book,student_hreg where student_sreg.id=warden_book.Sid and student_Hreg.id=warden_book.Hid and warden_book.status='pending' and warden_book.Hid=" + str(
            request.session['lid']))
    template = loader.get_template("b_pending.html")
    context = {'k': r}
    return HttpResponse(template.render(context, request))

def markattendance(request,id):
    r = book.objects.get(id=id)
    r.status ='approve'
    r.save()
    r = book.objects.raw(
        "select warden_book.id,student_sreg.sfname,warden_book.bdate,student_hreg.rent from student_sreg,warden_book,student_hreg where student_sreg.id=warden_book.Sid and student_Hreg.id=warden_book.Hid and warden_book.status='pending' and warden_book.Hid=" + str(
            request.session['lid']))
    template = loader.get_template("b_pending.html")
    context = {'k': r}
    return HttpResponse(template.render(context, request))


def reject_booking(request,id):
    r = book.objects.get(id=id)
    r.status='reject'
    r.save()
    r = book.objects.raw("select * from warden_book where status = 'pending' ")
    template = loader.get_template("b_pending.html")
    context = {'k': r}
    return HttpResponse(template.render(context, request))
def approve_list_booking(request):
    r = book.objects.raw("select * from warden_book where status = 'approve' and  Hid='"+str(request.session['lid'])+"'")
    template = loader.get_template("booking_approve.html")
    context = {'k': r}
    return HttpResponse(template.render(context, request))

def w_room(request):
    r = room.objects.raw("select student_room.id,student_room.rno,warden_book.* from warden_book,student_room where warden_book.Sid=student_room.stid and warden_book.status = 'approve' and  warden_book.Hid='"+str(request.session['lid'])+"'")
    template = loader.get_template("room.html")
    context = {'k': r}
    return HttpResponse(template.render(context, request))
def w_rooma(request):
    r = book.objects.raw("select * from warden_book where warden_book.status = 'approve' and  warden_book.Hid='"+str(request.session['lid'])+"' and warden_book.Sid not in(select stid from student_room) ")
    template = loader.get_template("room_allo.html")
    context = {'k': r}
    return HttpResponse(template.render(context, request))
def w_rooma1(request,id):
    r = book.objects.raw("select * from warden_book where id="+str(id))
    template = loader.get_template("room_allo1.html")
    context = {'k': r[0]}
    return HttpResponse(template.render(context, request))
def w_rooma2(request):

    rno=request.POST['rno']
    sid=request.POST['sid']
    wid=request.session['lid']

    ob=room()
    ob.stid=sid
    ob.htid=wid
    ob.rno=rno
    ob.save()

    template = loader.get_template("warden_home.html")
    context = {}
    return HttpResponse(template.render(context, request))


def vacate(request,id):
    r=book.objects.get(id=id)
    r.status='vacate'
    r.save()
    template = loader.get_template("s_home.html")
    context={}
    return HttpResponse(template.render(context, request))






