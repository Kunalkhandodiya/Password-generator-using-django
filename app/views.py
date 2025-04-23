from django.shortcuts import render
import string
import random

def password_generator(request):
    result = None
    
    if request.method == "POST":
        # Get the desired length of the password
        password_length = int(request.POST.get("password_num", 4))  # default to 8 if not provided
        
        # Check which character sets to include
        use_numbers = request.POST.get("num")
        use_chars = request.POST.get("char")
        use_punctuation = request.POST.get("punctuation")

        character_pool = ""

        if use_chars:
            character_pool += string.ascii_letters  # a-zA-Z
        if use_numbers:
            character_pool += string.digits  # 0-9
        if use_punctuation:
            character_pool += string.punctuation  # !@#$%^&*(), etc.

        # Fallback if no character type is selected
        if not character_pool:
            character_pool = string.ascii_letters + string.digits

        # Generate the password
        result = "".join(random.choice(character_pool) for _ in range(password_length))

    return render(request, "index.html", {"result": result})
