from django.shortcuts import render, redirect


# Simulated data dictionary
data = {
    'name': 'Ram',
    'age': 20,
    'city': 'Delhi',
}

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        city = request.POST['city']
        
        # Update the dictionary (simulated storage)
        data['name'] = name
        data['age'] = age
        data['city'] = city
        
        return redirect('read')
    
    return render(request, 'create.html')

def read(request):
    # Retrieve data from the dictionary (simulated retrieval)
    return render(request, 'read.html', {'data': data})

def update(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        
        # Update the dictionary (simulated update)
        data[key] = value
        return redirect('read')
    
    return render(request, 'update.html')

def delete(request):
    if request.method == 'POST':
        key_to_delete = request.POST['key_to_delete']
        
        # Delete from the dictionary (simulated deletion)
        if key_to_delete in data:
            del data[key_to_delete]
        return redirect('read')
    
    return render(request, 'delete.html')
