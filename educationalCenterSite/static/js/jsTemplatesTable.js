let elements = Array.from(document.querySelectorAll('tr')).slice(1);
elements.forEach(function(el) {
  if (Number(el.getAttribute('id')) % 2 === 1){
      el.style.background = "#F7F8FC"
  }
});