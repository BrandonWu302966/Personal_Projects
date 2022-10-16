function submission_confirmation(e) {
    e.preventDefault();
    // TODO: Fill in the rest 
    var name = document.getElementById("name").value
    var location = document.getElementById("location").value
    var incident = document.getElementById("incident").value

    console.log("name: " + name)
    console.log("location: " + location)
    console.log("incident description: " + incident)

    alert("Yay Spiderman got your message WOO!")

}
