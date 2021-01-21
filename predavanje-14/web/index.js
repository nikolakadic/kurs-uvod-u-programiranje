const xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       const parsedResponse = JSON.parse(xhttp.responseText);
       const name = parsedResponse['name'];
       const imgUrl = parsedResponse['avatar_url']
       document.getElementById("info").innerHTML = name;
       document.getElementById("profilePicture").src = imgUrl;
    }
};

xhttp.open("GET", 'https://api.github.com/users/nikolakadic', true);
xhttp.send();
