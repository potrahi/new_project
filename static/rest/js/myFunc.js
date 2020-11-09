function myFunc() {
    if (!(document.getElementById("id").value)) {
        var index = "{% url 'index' %}";
        window.reload(index);
    } else document.getElementById("thisForm").action = "rest-api/folder/" + document.getElementById("id").value;
}