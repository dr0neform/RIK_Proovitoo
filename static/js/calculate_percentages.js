 window.onload = function () {
     let total_capital = document.getElementById("total_capital")
     let rows_capital = document.getElementsByClassName("capital")
     let rows_share = document.getElementsByClassName("share_percent")
     for (let i = 0; i < rows_capital.length; i++) {
        rows_share[i].innerHTML = Math.floor((rows_capital[i].textContent / parseInt(total_capital.textContent)
                    * 100)).toString() +"%";}
        }
