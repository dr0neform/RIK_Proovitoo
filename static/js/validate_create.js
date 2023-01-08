function validate_create() {

            let rc = document.getElementById("id_reg_code").value

            if (rc.toString() == ""){

            }
            else if (cl.includes(rc.toString())) {
                Swal.fire({
                    icon: 'error',
                    title: 'Valitud registrikood on juba kasutusel',
                    text: 'Palun sisesta uus registrikood'
                });
                return;
            }



        let capital_p = 0;
        let capital_j = 0;

        for (let i = 0; i < parseInt(document.getElementById('physical').getAttribute('value')); i++) {

            capital_p += parseInt(document.getElementById('id_create_p-' + i + '-capital').value)
        }

        capital_p = capital_p || 0

        for (let i = 0; i < parseInt(document.getElementById('juridical').getAttribute('value')); i++) {

            capital_j += parseInt(document.getElementById('id_create_j-' + i + '-capital').value)
        }

        capital_j = capital_j || 0

        let capital = capital_j + capital_p

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
            console.log()
        }
    }