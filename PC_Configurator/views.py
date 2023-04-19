from django.shortcuts import render, get_object_or_404, redirect
from .models import Processor, add_processor, Motherboard, add_motherboard, Videocard, add_videocard, RAM, add_RAM, HDD, \
    add_HDD, PowerBlock, add_PowerBlock, add_Cooler, Cooler, Case, add_Case
from django import forms
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    p2 = add_processor.objects.all()
    m2 = add_motherboard.objects.all()
    v2 = add_videocard.objects.all()
    r2 = add_RAM.objects.all()
    h2 = add_HDD.objects.all()
    po2 = add_PowerBlock.objects.all()
    co2 = add_Cooler.objects.all()
    ca2 = add_Case.objects.all()
    if request.method == 'POST':
        processor_id = request.POST.get('processor_id')
        add_processor.objects.filter(id=processor_id).delete()
    if request.method == 'POST':
        motherboard_id = request.POST.get('motherboard_id')
        add_motherboard.objects.filter(id=motherboard_id).delete()
    if request.method == 'POST':
        videocard_id = request.POST.get('videocard_id')
        add_videocard.objects.filter(id=videocard_id).delete()
    if request.method == 'POST':
        RAM_id = request.POST.get('RAM_id')
        add_RAM.objects.filter(id=RAM_id).delete()
    if request.method == 'POST':
        HDD_id = request.POST.get('HDD_id')
        add_HDD.objects.filter(id=HDD_id).delete()
    if request.method == 'POST':
        powerblock_id = request.POST.get('powerblock_id')
        add_PowerBlock.objects.filter(id=powerblock_id).delete()
    if request.method == 'POST':
        cooler_id = request.POST.get('cooler_id')
        add_Cooler.objects.filter(id=cooler_id).delete()
    if request.method == 'POST':
        case_id = request.POST.get('case_id')
        add_Case.objects.filter(id=case_id).delete()
    return render(request, 'PC_Configurator/Configurator.html', {
        'product1': p2,
        'product2': m2,
        'product3': v2,
        'product4': r2,
        'product5': h2,
        'product6': po2,
        'product7': co2,
        'product8' : ca2
    })


def show_processors(request):
    p = Processor.objects.order_by('Price')
    if request.method == 'POST':
        processor_id = request.POST.get('processor_id')
        selected_processor = Processor.objects.get(id=processor_id)
        add_processor.objects.create(Name=selected_processor.Name, Socket=selected_processor.Socket,
                                     Memory_type=selected_processor.Memory_type, Photo=selected_processor.Photo,
                                     Price=selected_processor.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Processors.html', {
        'processors': p
    })


def show_one_processor(request, name_processor: str):
    dir = get_object_or_404(Processor, Name=name_processor)
    return render(request, 'PC_Configurator/One_processor.html', {
        'processor': dir
    })


def show_motherboards(request):
    m = Motherboard.objects.order_by('Price')
    if request.method == 'POST':
        motherboard_id = request.POST.get('motherboard_id')
        selected_motherboard = Motherboard.objects.get(id=motherboard_id)
        add_motherboard.objects.create(Name=selected_motherboard.Name, Socket=selected_motherboard.Socket,
                                       Memory_type=selected_motherboard.Memory_type, Photo=selected_motherboard.Photo,
                                       Price=selected_motherboard.Price, Size=selected_motherboard.Size,
                                       PCI_slot=selected_motherboard.PCI_slot)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Motherboards.html', {
        'motherboards': m
    })


def show_one_motherboard(request, name_motherboard: str):
    dir = get_object_or_404(Motherboard, Name=name_motherboard)
    return render(request, 'PC_Configurator/One_motherboard.html', {
        'motherboard': dir
    })


def show_videocards(request):
    v = Videocard.objects.order_by('Price')
    if request.method == 'POST':
        videocard_id = request.POST.get('videocard_id')
        selected_videocard = Videocard.objects.get(id=videocard_id)
        add_videocard.objects.create(Name=selected_videocard.Name, PCI_slot=selected_videocard.PCI_slot,
                                     Photo=selected_videocard.Photo,
                                     Price=selected_videocard.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Videocards.html', {
        'videocards': v
    })


def show_one_videocard(request, name_videocard: str):
    dir = get_object_or_404(Videocard, Name=name_videocard)
    return render(request, 'PC_Configurator/One_videocard.html', {
        'videocard': dir
    })


def show_RAMS(request):
    r = RAM.objects.order_by('Price')
    if request.method == 'POST':
        RAM_id = request.POST.get('RAM_id')
        selected_RAM = RAM.objects.get(id=RAM_id)
        add_RAM.objects.create(Name=selected_RAM.Name, Memory_type=selected_RAM.Memory_type, Photo=selected_RAM.Photo,
                               Price=selected_RAM.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/RAMS.html', {
        'RAMS': r
    })


def show_one_RAM(request, name_ram: str):
    dir = get_object_or_404(RAM, Name=name_ram)
    return render(request, 'PC_Configurator/One_ram.html', {
        'ram': dir
    })


def show_HDD(request):
    h = HDD.objects.order_by('Price')
    if request.method == 'POST':
        HDD_id = request.POST.get('hdd_id')
        selected_HDD = HDD.objects.get(id=HDD_id)
        add_HDD.objects.create(Name=selected_HDD.Name, Photo=selected_HDD.Photo, Price=selected_HDD.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/HDD.html', {
        'HDDS': h
    })


def show_one_HDD(request, name_hdd: str):
    dir = get_object_or_404(HDD, Name=name_hdd)
    return render(request, 'PC_Configurator/One_hdd.html', {
        'hdd': dir
    })


def show_powerblocks(request):
    po = PowerBlock.objects.order_by('Price')
    if request.method == 'POST':
        powerblock_id = request.POST.get('powerblock_id')
        selected_powerblock = PowerBlock.objects.get(id=powerblock_id)
        add_PowerBlock.objects.create(Name=selected_powerblock.Name, Photo=selected_powerblock.Photo,
                                      Price=selected_powerblock.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Powerblocks.html', {
        'pows': po
    })


def show_one_powerblock(request, name_powerblock: str):
    dir = get_object_or_404(PowerBlock, Name=name_powerblock)
    return render(request, 'PC_Configurator/One_powerblock.html', {
        'pow': dir
    })


def show_coolers(request):
    co = Cooler.objects.order_by('Price')
    if request.method == 'POST':
        cooler_id = request.POST.get('cooler_id')
        selected_cooler = Cooler.objects.get(id=cooler_id)
        add_Cooler.objects.create(Name=selected_cooler.Name, Photo=selected_cooler.Photo, Price=selected_cooler.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Coolers.html', {
        'coolers': co
    })


def show_one_cooler(request, name_cooler: str):
    dir = get_object_or_404(Cooler, Name=name_cooler)
    return render(request, 'PC_Configurator/One_cooler.html', {
        'cooler': dir
    })


def show_cases(request):
    Ca = Case.objects.order_by('Price')
    if request.method == 'POST':
        case_id = request.POST.get('case_id')
        selected_case = Case.objects.get(id=case_id)
        add_Case.objects.create(Name=selected_case.Name, Photo=selected_case.Photo, Price=selected_case.Price, Form=selected_case.Form)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Cases.html', {
        'cases': Ca
    })

def show_one_case(request, name_case: str):
    dir = get_object_or_404(Case, Name=name_case)
    return render(request, 'PC_Configurator/One_case.html', {
        'case': dir
    })