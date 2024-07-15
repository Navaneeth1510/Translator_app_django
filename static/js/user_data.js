user_data = {
}


function signin() {
    var email = document.getElementById('Mail').value;
    var password = document.getElementById('Pass').value;

    if (user_data.hasOwnProperty(email) && user_data[email] === password) {
        alert('Login successful!');
        window.location.href = 'http://127.0.0.1:8000/translator.html/'; 
    } else {
        alert('Login failed. Please check your credentials.');
    }
};


function auth(){
    var email = document.getElementById('Email').value;
    var password = document.getElementById('Password').value;
    var cpassword = document.getElementById('CPassword').value;

    if (cpassword === password) {
        user_data[email] = password;  
        alert('Account created successfully!');
        window.location.href = 'http://127.0.0.1:8000/loginpage.html';  
    } else {
        alert('Please enter the same password');
    }
}