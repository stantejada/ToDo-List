from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    
    return render_template('login.html', boolean=True)



@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get("password")
        password2 = request.form.get('password2')
        
        if len(email) < 8:
            flash('Email must be greater than 8 characters', category='error')
        elif password != password2:
            flash('Password don\'t match', category='error')
        elif len(password) < 8:
            flash('Password must be greater than 8 character', category='error')
        else:
            flash('Account has been created succesfully!', category='success')
          
        data=request.form  
        print(data)
    
    return render_template('signup.html')