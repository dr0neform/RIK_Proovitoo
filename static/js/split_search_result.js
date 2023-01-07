function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}
        $(async function() {
        $("#id_create_p-0-id_code").on('change', async function(e) {
            await delay(150);
  	    let text = document.getElementById('id_create_p-0-id_code').value
        const myArray = text.split(" ");
        document.getElementById('id_create_p-0-id_code').value = myArray[0].trim();
        document.getElementById('id_create_p-0-shareholder_first_name').value = myArray[2].trim();
        document.getElementById('id_create_p-0-shareholder_last_name').value = myArray[3].trim();
    })
        })
             $(async function() {
        $("#id_create_p-1-id_code").on('change', async function(e) {
            await delay(150);
  	    let text = document.getElementById('id_create_p-1-id_code').value
        const myArray = text.split(" ");
        document.getElementById('id_create_p-1-id_code').value = myArray[0].trim();
        document.getElementById('id_create_p-1-shareholder_first_name').value = myArray[2].trim();
        document.getElementById('id_create_p-1-shareholder_last_name').value = myArray[3].trim();
    })
        })
             $(async function() {
        $("#id_create_p-2-id_code").on('change', async function(e) {
            await delay(150);
  	    let text = document.getElementById('id_create_p-2-id_code').value
        const myArray = text.split(" ");
        document.getElementById('id_create_p-2-id_code').value = myArray[0].trim();
        document.getElementById('id_create_p-2-shareholder_first_name').value = myArray[2].trim();
        document.getElementById('id_create_p-2-shareholder_last_name').value = myArray[3].trim();
    })
        })
            $(async function() {
        $("#id_create_p-3-id_code").on('change', async function(e) {
            await delay(150);
  	    let text = document.getElementById('id_create_p-3-id_code').value
        const myArray = text.split(" ");
        document.getElementById('id_create_p-3-id_code').value = myArray[0].trim();
        document.getElementById('id_create_p-3-shareholder_first_name').value = myArray[2].trim();
        document.getElementById('id_create_p-3-shareholder_last_name').value = myArray[3].trim();
    })
        })
            $(async function() {
        $("#id_create_p-4-id_code").on('change', async function(e) {
            await delay(150);
  	    let text = document.getElementById('id_create_p-4-id_code').value
        const myArray = text.split(" ");
        document.getElementById('id_create_p-4-id_code').value = myArray[0].trim();
        document.getElementById('id_create_p-4-shareholder_first_name').value = myArray[2].trim();
        document.getElementById('id_create_p-4-shareholder_last_name').value = myArray[3].trim();
    })
        })
     $(async function() {
        $("#id_create_j-0-shareholder_company_reg_code").on('change', async function(e) {
            await delay(150);
  	    let text = document.getElementById('id_create_j-0-shareholder_company_reg_code').value
        const myArray = text.split(" ",);
        document.getElementById('id_create_j-0-shareholder_company_reg_code').value = myArray[0].trim();
        let c_string= '';
        for (let i = 2; i < myArray.length; i++) {
        c_string = (c_string + " " + myArray[i]).trim() }
        document.getElementById('id_create_j-0-shareholder_company_name').value = c_string


    })
        })
          $(async function() {
        $("#id_create_j-1-shareholder_company_reg_code").on('change', async function(e) {
            await delay(150);
  	    let text = document.getElementById('id_create_j-1-shareholder_company_reg_code').value
        const myArray = text.split(" ",);
        document.getElementById('id_create_j-1-shareholder_company_reg_code').value = myArray[0].trim();
        document.getElementById('id_create_j-1-shareholder_company_name').value = myArray[2].trim() + " " + myArray[3].trim();
    })
        })
          $(async function() {
        $("#id_create_j-2-shareholder_company_reg_code").on('change', async function(e) {
            await delay(150);
  	    let text = document.getElementById('id_create_j-2-shareholder_company_reg_code').value
        const myArray = text.split(" ",);
        document.getElementById('id_create_j-2-shareholder_company_reg_code').value = myArray[0].trim();
        document.getElementById('id_create_j-2-shareholder_company_name').value = myArray[2].trim() + " " + myArray[3].trim();
    })
        })
     $(async function() {
        $("#id_create_j-3-shareholder_company_reg_code").on('change', async function(e) {
            await delay(150);
  	    let text = document.getElementById('id_create_j-3-shareholder_company_reg_code').value
        const myArray = text.split(" ",);
        document.getElementById('id_create_j-3-shareholder_company_reg_code').value = myArray[0].trim();
        document.getElementById('id_create_j-3-shareholder_company_name').value = myArray[2].trim() + " " + myArray[3].trim();
    })
        })
          $(async function() {
        $("#id_create_j-4-shareholder_company_reg_code").on('change', async function(e) {
            await delay(150);
  	    let text = document.getElementById('id_create_j-4-shareholder_company_reg_code').value
        const myArray = text.split(" ",);
        document.getElementById('id_create_j-4-shareholder_company_reg_code').value = myArray[0].trim();
        document.getElementById('id_create_j-4-shareholder_company_name').value = myArray[2].trim() + " " + myArray[3].trim();
    })
        })