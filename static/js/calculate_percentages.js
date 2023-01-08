 window.onload = function () {
     let total_capital = document.getElementById("total_capital")
     let rows_capital = document.getElementsByClassName("capital")
     let rows_share = document.getElementsByClassName("share_percent")
     for (let i = 0; i < rows_capital.length; i++) {
        rows_share[i].innerHTML = ((parseFloat(rows_capital[i].textContent) / parseFloat(total_capital.textContent))
                    * 100).toFixed(2).toString() +"%";}
        }
        console.log();