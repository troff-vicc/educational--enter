function checkCheckbox(element){
    let json = JSON.stringify({})
    if(element.checked){
         json = JSON.stringify({
            idUsers: element.id,
            checkAdmin: 1
        })
    }else{
         json = JSON.stringify({
            idUsers: element.id,
            checkAdmin: 0
         })
    }
    fetch('/api/user-admin/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: json
    }).then(response=>response.json())
        .then(response1 => {
            console.log(response1);
        })
}