function Pergjigjia() {
    var score = 0;
    var correct = "lime";
    var incorrect = "red";

    if(document.getElementById("po1").checked == true) {
        score += 1;
        document.getElementById("1").style.color = correct;
    } else {
        document.getElementById("1").style.color = incorrect;
    }

    if(document.getElementById("1706").checked == true) {
        score += 1;
        document.getElementById("2").style.color = correct;
    } else {
        document.getElementById("2").style.color = incorrect;
    }

    if(document.getElementById("po3").checked == true) {
        score += 1;
        document.getElementById("3").style.color = correct;
    } else {
        document.getElementById("3").style.color = incorrect;
    }

    if(document.getElementById("Greqisht").checked == true) {
        score += 1;
        document.getElementById("4").style.color = correct;
    } else {
        document.getElementById("4").style.color = incorrect;
    }

    if(document.getElementById("po5").checked == true) {
        score += 1;
        document.getElementById("5").style.color = correct;
    } else {
        document.getElementById("5").style.color = incorrect;
    }

    if(document.getElementById("Asnje").checked == true) {
        score += 1;
        document.getElementById("6").style.color = correct;
    } else {
        document.getElementById("6").style.color = incorrect;
    }

    if(document.getElementById("jo7").checked == true) {
        score += 1;
        document.getElementById("7").style.color = correct;
    } else {
        document.getElementById("7").style.color = incorrect;
    }

    if(document.getElementById("Math").checked == true) {
        score += 1;
        document.getElementById("8").style.color = correct;
    } else {
        document.getElementById("8").style.color = incorrect;
    }

    if(document.getElementById("po9").checked == true) {
        score += 1;
        document.getElementById("9").style.color = correct;
    } else {
        document.getElementById("9").style.color = incorrect;
    }

    if(document.getElementById("William Shanks").checked == true) {
        score += 1;
        document.getElementById("10").style.color = correct;
    } else {
        document.getElementById("10").style.color = incorrect;
    }

    if(document.getElementById("pie").checked == true) {
        score += 1;
        document.getElementById("11").style.color = correct;
    } else {
        document.getElementById("11").style.color = incorrect;
    }

    if(document.getElementById("kostante").checked == true) {
        score += 1;
        document.getElementById("12").style.color = correct;
    } else {
        document.getElementById("12").style.color = incorrect;
    }

    if(document.getElementById("62.8").checked == true) {
        score += 1;
        document.getElementById("13").style.color = correct;
    } else {
        document.getElementById("13").style.color = incorrect;
    }

    if(document.getElementById(".5").checked == true) {
        score += 1;
        document.getElementById("14").style.color = correct;
    } else {
        document.getElementById("14").style.color = incorrect;
    }

    alert("ju keni gjetur sakte " + score + " nga 14 pyetjet e pyetsorit");
    document.getElementById("buton").disabled = true;
}
