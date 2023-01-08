    window.onload = function () {

        let physical_forms = document.getElementById('physical').getAttribute('value')
        let juridical_forms = document.getElementById('juridical').getAttribute('value')
        let totalForms_p = document.querySelector("#id_create_p-TOTAL_FORMS")
        let totalForms_j = document.querySelector("#id_create_j-TOTAL_FORMS")
        totalForms_p.setAttribute('value', physical_forms)
        totalForms_j.setAttribute('value', juridical_forms)
        let physical_elements = document.getElementsByClassName("detail-form-p")
        let juridical_elements = document.getElementsByClassName("detail-form-j")
            document.getElementById("remove_p").style.display = "none"
            document.getElementById("remove_j").style.display = "none"
        physical_elements[0].style.display = "none"
        physical_elements[1].style.display = "none"
        physical_elements[2].style.display = "none"
        physical_elements[3].style.display = "none"
        physical_elements[4].style.display = "none"
        juridical_elements[0].style.display = "none"
        juridical_elements[1].style.display = "none"
        juridical_elements[2].style.display = "none"
        juridical_elements[3].style.display = "none"
        juridical_elements[4].style.display = "none"
            console.log();
    };