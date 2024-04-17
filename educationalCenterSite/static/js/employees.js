let arrayChanges = new Set();
let addEmployeesList = []
thALL = document.querySelectorAll("th");
thALL.forEach(function(th) {th.addEventListener("input",
    function () {
        arrayChanges.add(this.getAttribute("name"))
    },
    false);});
function postDate() {
    addEmployeesList.forEach(function(idAdd) {
        let tr = document.getElementById(idAdd)
        let fullName = tr.getElementsByClassName("fullName")[0]
        let position = tr.getElementsByClassName('position')[0]
        let json = JSON.stringify({
            idEmployees: idAdd,
            fullName: fullName.innerText,
            position: position.innerText
         })
        fetch('/api/add-employees/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: json
    }).then(response=>response.json())
        .then(response1 => {
            console.log(response1);
        })
    })
    addEmployeesList = []
    arrayChanges.forEach(function(id) {
        let tr = document.getElementById(id)
        let fullName = tr.getElementsByClassName("fullName")[0]
        let position = tr.getElementsByClassName('position')[0]
        let json = JSON.stringify({
            idEmployees: id,
            fullName: fullName.innerText,
            position: position.innerText
         })
        fetch('/api/update-employees/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: json
    }).then(response=>response.json())
        .then(response1 => {
            console.log(response1);
        })
    })
    arrayChanges = []
}

function add() {
    let table = document.getElementsByTagName('table')[0]
    let id = document.getElementsByTagName('tr').length - 1
    table.innerHTML += `<tr id="${id}">\n
                   <th class="id" name="${id}">${id}</th>\n
                   <th contenteditable="true" class="fullName" name="${id}"> </th>\n
                   <th contenteditable="true" class="position" name="${id}"> </th>\n
                   </tr>`
    addEmployeesList.push(id)
}