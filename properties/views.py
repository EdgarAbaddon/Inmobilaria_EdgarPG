from django.shortcuts import render, get_object_or_404, redirect
from .forms import PropertyForm
from .models import Property
from django.contrib import messages

#Alumno : Edgar Perez Gomez S4C

# List and Create Properties
def property_list_create(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property created successfully!')
            return redirect('property_list_create')
    else:
        form = PropertyForm()
    
    properties = Property.objects.all()
    context = {
        "properties": properties,
        "form": form
    }
    return render(request, "properties/property_list.html", context=context)

# View Property Details
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    context = {
        "property": property
    }
    return render(request, "properties/property_detail.html", context=context)

# Update Property
def property_update(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property updated successfully!')
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm(instance=property)
    
    context = {
        "form": form
    }
    return render(request, "properties/property_form.html", context=context)

# Delete Property
def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        property.delete()
        messages.success(request, 'Property deleted successfully!')
        return redirect('property_list_create')
    
    context = {
        "property": property
    }
    return render(request, "properties/property_confirm_delete.html", context=context)
