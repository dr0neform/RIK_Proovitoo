    function validate_update() {
        let capital_p = 0;
        let capital_j = 0;
        let capital_u_p = 0;
        let capital_u_j = 0;

        for (let i = 0; i < parseInt(document.getElementById('physical').getAttribute('value')); i++) {

            capital_p += parseInt(document.getElementById('id_create_p-' + i + '-capital').value)
        }

        capital_p = capital_p || 0

        for (let i = 0; i < parseInt(document.getElementById('juridical').getAttribute('value')); i++) {

            capital_j += parseInt(document.getElementById('id_create_j-' + i + '-capital').value)
        }

        capital_j = capital_j || 0

        let update_p_forms = document.getElementsByClassName("update_p")
            for (let i = 0; i < update_p_forms.length; i++) {

            capital_u_p += parseInt(document.getElementById('id_update_p-' + i + '-capital').value)

        }

            capital_u_p = capital_u_p || 0

        let update_j_forms = document.getElementsByClassName("update_j")
            for (let i = 0; i < update_j_forms.length; i++) {

            capital_u_j += parseInt(document.getElementById('id_update_j-' + i + '-capital').value)

        }

            capital_u_p = capital_u_p || 0

        let capital = capital_j + capital_p + capital_u_p + capital_u_j

        if (capital < 2500) {
            Swal.fire({
                icon: 'error',
                title: 'Tähelepanu! Osakapital peab olema vähemalt 2500 EUR',
                text: 'Puudu on ' + (2500 - capital).toString() + ' EUR'
            })
        } else {
            try {
            let p_forms = document.getElementsByClassName("detail-form-p")
            p_forms = Array.from(p_forms);
            for (let i = 0; i < 5; i++) {
                if (p_forms[i].getAttribute('style') == "display: none;") {
                    p_forms[i].remove()}
            }

            let j_forms = document.getElementsByClassName("detail-form-j")
            j_forms = Array.from(j_forms);
            for (let i = 0; i < 5; i++) {
                if (j_forms[i].getAttribute('style') == "display: none;") {
                    j_forms[i].remove()}
            }}
            catch {}
            document.getElementById('submitButton').click();
        }
    }