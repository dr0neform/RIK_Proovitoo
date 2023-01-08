        let addButton_p = document.querySelector("#add-form_p")
        let totalForms = document.querySelector("#id_create_p-TOTAL_FORMS")
        let removeButton_p = document.getElementById("remove_p")
        let addButton_j = document.querySelector("#add-form_j")
        let totalForms_j = document.querySelector("#id_create_j-TOTAL_FORMS")
        let removeButton_j = document.getElementById("remove_j")

        addButton_p.addEventListener('click', addForm_p)
        removeButton_p.addEventListener('click', removeForm_p)

        addButton_j.addEventListener('click', addForm_j)
        removeButton_j.addEventListener('click', removeForm_j)

        function addForm_p(e){
            let pf = parseInt(document.getElementById('physical').getAttribute('value'))
            document.getElementsByClassName("detail-form-p")[pf].style.display = "block"
            removeButton_p.style.display = "initial"
            pf++
            totalForms.setAttribute('value', pf.toString())
            document.getElementById('physical').setAttribute('value', pf.toString())
        }

        function removeForm_p(e){
            let pf = parseInt(document.getElementById('physical').getAttribute('value'))
            document.getElementsByClassName("detail-form-p")[pf -1].style.display = "none"
            if (pf == 1) {
            removeButton_p.style.display = "none"}
            pf = pf-1
            totalForms.setAttribute('value', pf.toString())
            document.getElementById('physical').setAttribute('value', pf.toString())
        }

        function removeForm_j(e){
            let pj = parseInt(document.getElementById('juridical').getAttribute('value'))
            document.getElementsByClassName("detail-form-j")[pj -1].style.display = "none"
            if (pj == 1) {
            removeButton_j.style.display = "none"}
            pj = pj-1
            totalForms_j.setAttribute('value', pj.toString())
            document.getElementById('juridical').setAttribute('value', pj.toString())
        }

        function addForm_j(e){

            let jf = parseInt(document.getElementById('juridical').getAttribute('value'))
            document.getElementsByClassName("detail-form-j")[jf].style.display = "block"
            document.getElementById("remove_j").style.display = "initial"
            jf++
            totalForms_j.setAttribute('value', jf.toString())
            document.getElementById('juridical').setAttribute('value', jf.toString())

        }