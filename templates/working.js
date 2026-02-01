document.getElementById("emailForm").addEventListener("submit", async function(e){
    e.preventDefault();

    let emailValue = document.getElementById("email").value;

    let response = await fetch("http://127.0.0.1:5000/verify", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "email=" + encodeURIComponent(emailValue)
    });

    let result = await response.json();
    
    let resultTag = document.getElementById("result");
    resultTag.innerText = result.message;

    if(result.status === "success"){
        resultTag.style.color = "lime";
    } else {
        resultTag.style.color = "yellow";
    }
});
